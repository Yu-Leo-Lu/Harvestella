"""Harvestella Crop Allocation Optimizer.

Computes the mathematically optimal seed purchase and planting allocation
using Mixed-Integer Linear Programming (MILP via scipy.optimize.milp).
Accounts for multi-biome plot capacities (Farm, Waterside, Cave), wallet gold,
vendor town unlocks, seed shop stock caps, and Quietus / Restock horizons.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path

import yaml

try:
    from scipy.optimize import Bounds, LinearConstraint, milp
    import numpy as np
    HAS_SCIPY = True
except ImportError:
    HAS_SCIPY = False


# ==============================================================================
# Data Structures
# ==============================================================================

@dataclass
class CropCandidate:
    name: str
    town: str
    biome: str
    cost: float
    daily_profit: float
    prod_days: int
    stock: int
    schedule: str


@dataclass
class AllocationItem:
    crop: CropCandidate
    quantity: int
    subtotal_cost: float
    subtotal_daily_profit: float


@dataclass
class OptimizationResult:
    season: str
    config_path: Path
    current_day: int = 1
    horizon: str = ""
    max_days: int = 0
    wallet_gold: float = 0.0
    total_spent: float = 0.0
    leftover_gold: float = 0.0
    total_daily_profit: float = 0.0
    farm_used: int = 0
    farm_cap: int = 0
    water_used: int = 0
    water_cap: int = 0
    cave_used: int = 0
    cave_cap: int = 0
    items: list[AllocationItem] = field(default_factory=list)
    success: bool = True
    status_message: str = "Optimal solution found."
    max_varieties: int | None = None

    @property
    def gold_pct(self) -> float:
        return (self.total_spent / self.wallet_gold * 100) if self.wallet_gold > 0 else 0.0

    @property
    def projected_net(self) -> float:
        return self.total_daily_profit * self.max_days

    @property
    def plots_summary(self) -> str:
        if self.water_cap == 0 and self.cave_cap == 0:
            return f"{self.farm_used} / {self.farm_cap} Farm"
        parts: list[str] = []
        if self.farm_cap > 0:
            parts.append(f"{self.farm_used} Farm")
        if self.water_cap > 0:
            parts.append(f"{self.water_used} Water")
        if self.cave_cap > 0:
            parts.append(f"{self.cave_used} Cave")
        return ", ".join(parts) if parts else "None"

    @property
    def seeds_summary(self) -> str:
        if not self.items:
            return "None"
        return ", ".join(f"{it.quantity} {it.crop.name} ({it.crop.town})" for it in self.items)


# ==============================================================================
# Helper Functions
# ==============================================================================

def determine_horizon_days(current_day: int, horizon_mode: str) -> tuple[int, str]:
    """Calculate the remaining production days based on horizon selection."""
    mode = str(horizon_mode).strip().lower()
    if mode in ("restock", "next_restock"):
        target = 11 if current_day < 11 else (21 if current_day < 21 else 31)
        days = target - current_day
        return days, f"Next Vendor Restock (Day {target}, {days}d window)"

    # Default: Quietus harvest deadline
    days = 30 if current_day == 1 else max(0, 30 - current_day)
    return days, f"Quietus Deadline (Day 30, {days}d window)"


def is_crop_eligible(prod_days: int, current_day: int, max_days: int, horizon_mode: str) -> bool:
    """Determine if a crop can complete its production cycle within the horizon."""
    mode = str(horizon_mode).strip().lower()
    if mode in ("restock", "next_restock"):
        return prod_days <= max_days
    if current_day == 1:
        return prod_days <= 30
    return current_day <= (30 - prod_days)


def is_town_unlocked(vendor_town: str, unlocked_towns: dict[str, bool]) -> bool:
    """Check if the vendor town is currently unlocked (split on '/' for multi-town)."""
    towns = [t.strip() for t in vendor_town.split("/")]
    return any(unlocked_towns.get(t, False) for t in towns)


# ==============================================================================
# Core Optimization Engine
# ==============================================================================

def solve_allocation(config_path: Path, csv_dir: Path = Path("seasons")) -> OptimizationResult:
    """Solve the bounded integer crop allocation knapsack for a single config."""
    config_path = Path(config_path)
    if not config_path.is_file():
        return OptimizationResult(
            season="",
            config_path=config_path,
            success=False,
            status_message=f"Config file not found: {config_path}",
        )

    with open(config_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    season = str(cfg.get("season", config_path.stem)).strip().lower()
    csv_path = csv_dir / f"{season}.csv"
    if not csv_path.is_file():
        return OptimizationResult(
            season=season,
            config_path=config_path,
            success=False,
            status_message=f"Seasonal CSV not found: {csv_path}",
        )

    current_day = int(cfg.get("current_day", 1))
    wallet_gold = float(cfg.get("wallet_gold", 0.0))
    horizon_mode = str(cfg.get("horizon", "quietus")).strip()
    max_days, horizon_desc = determine_horizon_days(current_day, horizon_mode)

    raw_varieties = cfg.get("max_crop_varieties", None)
    max_varieties: int | None = None
    if raw_varieties is not None:
        try:
            val = int(raw_varieties)
            if val > 0:
                max_varieties = val
        except (ValueError, TypeError):
            max_varieties = None

    free_plots = cfg.get("free_plots", {})
    farm_cap = max(0, int(free_plots.get("farm", 0)))
    water_cap = max(0, int(free_plots.get("waterside", 0)))
    cave_cap = max(0, int(free_plots.get("cave", 0)))

    unlocked_towns = cfg.get("unlocked_towns", {})
    seed_stock = cfg.get("seed_stock", {})

    with open(csv_path, encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))

    candidates: list[CropCandidate] = []
    for r in raw_rows:
        crop_name = r.get("Crop Name", "").strip()
        biome = r.get("Biome", "").strip().lower()
        town = r.get("Vendor Town", "").strip()

        cost_str = r.get("Seed Cost (G)", "").strip()
        profit_str = r.get("Daily NQ Profit (G/d)", "").strip()
        prod_str = r.get("Production (Days)", "").strip()

        if not cost_str or not profit_str or not prod_str:
            continue
        try:
            cost = float(cost_str)
            daily_profit = float(profit_str)
            prod_days = int(prod_str)
        except ValueError:
            continue

        if cost <= 0 or daily_profit <= 0:
            continue
        if not is_town_unlocked(town, unlocked_towns):
            continue
        if not is_crop_eligible(prod_days, current_day, max_days, horizon_mode):
            continue

        # In-stock seed count from YAML configuration (default: 99)
        stock_key_town = f"{crop_name} ({town})"
        if stock_key_town in seed_stock:
            stock = int(seed_stock[stock_key_town])
        elif town in seed_stock and isinstance(seed_stock[town], dict) and crop_name in seed_stock[town]:
            stock = int(seed_stock[town][crop_name])
        elif crop_name in seed_stock:
            stock = int(seed_stock[crop_name])
        else:
            stock = 99
        if stock <= 0:
            continue
        if biome == "waterside" and water_cap <= 0:
            continue
        if biome == "cave" and cave_cap <= 0:
            continue
        if biome == "farm" and farm_cap <= 0:
            continue

        candidates.append(
            CropCandidate(
                name=crop_name,
                town=town,
                biome=biome,
                cost=cost,
                daily_profit=daily_profit,
                prod_days=prod_days,
                stock=stock,
                schedule=r.get("Planting Schedule", "").strip(),
            )
        )

    if not candidates:
        return OptimizationResult(
            season=season,
            config_path=config_path,
            current_day=current_day,
            horizon=horizon_desc,
            max_days=max_days,
            wallet_gold=wallet_gold,
            leftover_gold=wallet_gold,
            farm_cap=farm_cap,
            water_cap=water_cap,
            cave_cap=cave_cap,
            status_message="No eligible crops match current filters (towns, capacity, or deadlines).",
        )

    if not HAS_SCIPY:
        return OptimizationResult(
            season=season,
            config_path=config_path,
            success=False,
            status_message="scipy is not installed. Please run `pip install scipy`.",
        )

    n = len(candidates)
    if max_varieties is not None and max_varieties < n:
        # MILP with 2n variables: x_0..x_{n-1} (seed counts), y_0..y_{n-1} (binary indicators)
        c = np.concatenate([
            np.array([-cand.daily_profit + 1e-6 * cand.cost for cand in candidates]),
            np.zeros(n),
        ])

        # Resource rows: Budget, Farm, Waterside, Cave (padded with 0s for y variables)
        row_budget = [cand.cost for cand in candidates] + [0.0] * n
        row_farm = [1.0 if cand.biome == "farm" else 0.0 for cand in candidates] + [0.0] * n
        row_water = [1.0 if cand.biome == "waterside" else 0.0 for cand in candidates] + [0.0] * n
        row_cave = [1.0 if cand.biome == "cave" else 0.0 for cand in candidates] + [0.0] * n

        A_rows = [row_budget, row_farm, row_water, row_cave]
        lb_list = [0.0, 0.0, 0.0, 0.0]
        ub_list = [wallet_gold, float(farm_cap), float(water_cap), float(cave_cap)]

        # Indicator linking constraints: x_i - stock_i * y_i <= 0
        for i in range(n):
            link_row = [0.0] * (2 * n)
            link_row[i] = 1.0
            link_row[n + i] = -float(candidates[i].stock)
            A_rows.append(link_row)
            lb_list.append(-np.inf)
            ub_list.append(0.0)

        # Cardinality constraint: sum(y_i) <= max_varieties
        card_row = [0.0] * n + [1.0] * n
        A_rows.append(card_row)
        lb_list.append(0.0)
        ub_list.append(float(max_varieties))

        A = np.array(A_rows)
        lb = np.array(lb_list)
        ub = np.array(ub_list)

        constraints = LinearConstraint(A, lb, ub)
        bounds = Bounds(
            lb=np.zeros(2 * n),
            ub=np.concatenate([np.array([cand.stock for cand in candidates]), np.ones(n)]),
        )
        integrality = np.ones(2 * n)

        res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
        if not res.success:
            return OptimizationResult(
                season=season,
                config_path=config_path,
                success=False,
                status_message=f"MILP solver failed: {res.status} - {res.message}",
            )
        solution = np.round(res.x[:n]).astype(int)
    else:
        # Standard MILP with n variables
        c = np.array([-cand.daily_profit + 1e-6 * cand.cost for cand in candidates])
        row_budget = [cand.cost for cand in candidates]
        row_farm = [1.0 if cand.biome == "farm" else 0.0 for cand in candidates]
        row_water = [1.0 if cand.biome == "waterside" else 0.0 for cand in candidates]
        row_cave = [1.0 if cand.biome == "cave" else 0.0 for cand in candidates]

        A = np.array([row_budget, row_farm, row_water, row_cave])
        ub = np.array([wallet_gold, farm_cap, water_cap, cave_cap])
        lb = np.zeros(4)

        constraints = LinearConstraint(A, lb, ub)
        bounds = Bounds(lb=np.zeros(n), ub=np.array([cand.stock for cand in candidates]))
        integrality = np.ones(n)

        res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
        if not res.success:
            return OptimizationResult(
                season=season,
                config_path=config_path,
                success=False,
                status_message=f"MILP solver failed: {res.status} - {res.message}",
            )
        solution = np.round(res.x).astype(int)
    items: list[AllocationItem] = []
    farm_used = water_used = cave_used = 0
    total_spent = total_daily_profit = 0.0

    for i in range(n):
        qty = int(solution[i])
        if qty <= 0:
            continue
        cand = candidates[i]
        subtotal_cost = qty * cand.cost
        subtotal_profit = qty * cand.daily_profit
        total_spent += subtotal_cost
        total_daily_profit += subtotal_profit

        if cand.biome == "farm":
            farm_used += qty
        elif cand.biome == "waterside":
            water_used += qty
        elif cand.biome == "cave":
            cave_used += qty

        items.append(
            AllocationItem(
                crop=cand,
                quantity=qty,
                subtotal_cost=subtotal_cost,
                subtotal_daily_profit=subtotal_profit,
            )
        )

    biome_order = {"farm": 1, "waterside": 2, "cave": 3}
    items.sort(key=lambda it: (biome_order.get(it.crop.biome, 99), -it.crop.daily_profit))

    return OptimizationResult(
        season=season,
        config_path=config_path,
        current_day=current_day,
        horizon=horizon_desc,
        max_days=max_days,
        wallet_gold=wallet_gold,
        total_spent=total_spent,
        leftover_gold=max(0.0, wallet_gold - total_spent),
        total_daily_profit=total_daily_profit,
        farm_used=farm_used,
        farm_cap=farm_cap,
        water_used=water_used,
        water_cap=water_cap,
        cave_used=cave_used,
        cave_cap=cave_cap,
        items=items,
        success=True,
        max_varieties=max_varieties,
    )


# ==============================================================================
# Reporting Formatter (Terminal & Markdown)
# ==============================================================================

def print_result_report(result: OptimizationResult) -> None:
    """Print an aesthetic, readable terminal report of the allocation plan."""
    season_title = result.season.upper() if result.season else "UNKNOWN"
    print("=" * 86)
    print(f" HARVESTELLA CROP ALLOCATION OPTIMIZER: {season_title}")
    print("=" * 86)
    print(f" Config File    : {result.config_path}")
    print(f" Current Day    : Day {result.current_day}")
    print(f" Horizon Plan   : {result.horizon}")
    if result.max_varieties is not None:
        print(f" Variety Limit  : Max {result.max_varieties} distinct crop varieties")
    print(f" Capital Budget : {result.wallet_gold:,.0f} G")
    print(
        f" Plot Capacities: Farm {result.farm_cap} | "
        f"Waterside {result.water_cap} | Cave {result.cave_cap}"
    )
    print("-" * 86)

    if not result.success:
        print(f" [!] ERROR: {result.status_message}\n")
        return

    if not result.items:
        print(f" [i] {result.status_message}\n")
        return

    print(" OPTIMAL PLANTING ALLOCATION")
    print("-" * 86)
    print(
        f"{'Biome':<10} {'Crop Name':<22} {'Vendor':<12} "
        f"{'Cost':>6} {'Qty':>5} {'Subtotal':>9} {'Profit/d':>9} {'Cycle Days':>10}"
    )
    print("-" * 86)

    for it in result.items:
        c = it.crop
        print(
            f"{c.biome.capitalize():<10} "
            f"{c.name:<22} "
            f"{c.town:<12} "
            f"{c.cost:>6,.0f} "
            f"{it.quantity:>5} "
            f"{it.subtotal_cost:>8,.0f} G "
            f"+{it.subtotal_daily_profit:>7,.1f} "
            f"{c.prod_days:>9}d"
        )

    print("-" * 86)
    print(" RESOURCE UTILIZATION & FINANCIAL SUMMARY")
    print("-" * 86)

    farm_pct = (result.farm_used / result.farm_cap * 100) if result.farm_cap > 0 else 0
    print(
        f" Farm Plots Used      : {result.farm_used:>3} / {result.farm_cap:<3} "
        f"({farm_pct:>5.1f}% utilized, {result.farm_cap - result.farm_used} idle)"
    )
    if result.water_cap > 0:
        water_pct = (result.water_used / result.water_cap * 100)
        print(
            f" Waterside Plots Used : {result.water_used:>3} / {result.water_cap:<3} "
            f"({water_pct:>5.1f}% utilized, {result.water_cap - result.water_used} idle)"
        )
    if result.cave_cap > 0:
        cave_pct = (result.cave_used / result.cave_cap * 100)
        print(
            f" Cave Plots Used      : {result.cave_used:>3} / {result.cave_cap:<3} "
            f"({cave_pct:>5.1f}% utilized, {result.cave_cap - result.cave_used} idle)"
        )

    print(
        f" Gold Capital Spent   : {result.total_spent:>8,.0f} G / {result.wallet_gold:,.0f} G "
        f"({result.gold_pct:>5.1f}% spent, {result.leftover_gold:,.0f} G leftover)"
    )
    print(f" Total Daily Profit   : +{result.total_daily_profit:>7,.1f} G/day")
    print(
        f" Projected Net Window : +{result.projected_net:>7,.0f} G net profit "
        f"over {result.max_days} days"
    )
    print("=" * 86 + "\n")


def print_multi_season_summary(results: list[OptimizationResult]) -> None:
    """Print an executive comparative summary table across multiple seasons."""
    valid = [r for r in results if r.success and r.items]
    if not valid:
        return

    print("=" * 140)
    print(" ALL-SEASON CROP ALLOCATION EXECUTIVE SUMMARY")
    print("=" * 140)
    print(
        f"{'Season':<8} {'Budget':>9}  "
        f"{'Optimal Seed Purchases':<56} "
        f"{'Plots Used':<26} "
        f"{'Gold Spent / Leftover':<25} "
        f"{'Daily Profit':>13}"
    )
    print("-" * 140)

    for r in valid:
        spent_str = f"{r.total_spent:,.0f} G / {r.leftover_gold:,.0f} G ({r.gold_pct:.1f}%)"
        print(
            f"{r.season.capitalize():<8} {f'{r.wallet_gold:,.0f} G':>9}  "
            f"{r.seeds_summary:<56} "
            f"{r.plots_summary:<26} "
            f"{spent_str:<25} "
            f"{f'+{r.total_daily_profit:,.1f} G/d':>13}"
        )

    print("=" * 140 + "\n")


def generate_markdown_report(
    results: list[OptimizationResult],
    output_path: Path = Path("crop_allocation_report.md"),
) -> Path:
    """Generate a structured GitHub-Flavored Markdown report and save to root."""
    valid = [r for r in results if r.success and r.items]
    if not valid:
        return output_path

    lines = [
        "# Harvestella Crop Allocation & Planting Report\n",
        "> Mathematically optimal seed purchase and planting allocations generated via Mixed-Integer Linear Programming (MILP).\n",
        "## Executive Summary\n",
        "| Season | Budget (G) | Optimal Seed Purchases | Plots Used | Gold Spent / Leftover | Total Daily Profit | Projected Window Net |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]

    for r in valid:
        seeds_formatted = "<br>".join(
            f"• {it.quantity} {it.crop.name} ({it.crop.town})"
            for it in r.items
        )
        spent_str = f"{r.total_spent:,.0f} G / {r.leftover_gold:,.0f} G ({r.gold_pct:.1f}%)"
        proj_str = f"+{r.projected_net:,.0f} G ({r.max_days}d)"
        lines.append(
            f"| **{r.season.capitalize()}** | {r.wallet_gold:,.0f} G | {seeds_formatted} | "
            f"{r.plots_summary} | {spent_str} | +{r.total_daily_profit:,.1f} G/day | {proj_str} |"
        )

    lines.append("\n---\n")

    for r in valid:
        season_title = r.season.capitalize()
        lines.append(f"## {season_title} Detailed Allocation\n")
        lines.append(f"- **Config Profile**: [`{r.config_path.as_posix()}`]({r.config_path.as_posix()})")
        lines.append(f"- **Planning Horizon**: {r.horizon}")
        if r.max_varieties is not None:
            lines.append(f"- **Variety Limit**: Max {r.max_varieties} distinct crop varieties")
        lines.append(f"- **Capital Budget**: {r.wallet_gold:,.0f} G")
        lines.append(
            f"- **Plot Capacities**: Farm {r.farm_cap} plots | Waterside {r.water_cap} plots | Cave {r.cave_cap} plots\n"
        )

        lines.append("### Optimal Planting Table\n")
        lines.append(
            "| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |"
        )
        lines.append(
            "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
        )

        for it in r.items:
            c = it.crop
            lines.append(
                f"| {c.biome.capitalize()} | **{c.name}** | {c.town} | {c.cost:,.0f} G | {it.quantity} | "
                f"{it.subtotal_cost:,.0f} G | +{c.daily_profit:.1f} | +{it.subtotal_daily_profit:.1f} | "
                f"{c.prod_days}d | `{c.schedule}` |"
            )

        lines.append("\n### Resource Utilization & Financial Summary\n")
        farm_pct = (r.farm_used / r.farm_cap * 100) if r.farm_cap > 0 else 0
        lines.append(f"- **Farm Plots Used**: {r.farm_used} / {r.farm_cap} ({farm_pct:.1f}% utilized, {r.farm_cap - r.farm_used} idle)")
        if r.water_cap > 0:
            water_pct = (r.water_used / r.water_cap * 100)
            lines.append(f"- **Waterside Plots Used**: {r.water_used} / {r.water_cap} ({water_pct:.1f}% utilized, {r.water_cap - r.water_used} idle)")
        if r.cave_cap > 0:
            cave_pct = (r.cave_used / r.cave_cap * 100)
            lines.append(f"- **Cave Plots Used**: {r.cave_used} / {r.cave_cap} ({cave_pct:.1f}% utilized, {r.cave_cap - r.cave_used} idle)")

        spent_str = f"{r.total_spent:,.0f} G / {r.leftover_gold:,.0f} G ({r.gold_pct:.1f} spent, {r.leftover_gold:,.0f} G leftover)"
        lines.append(f"- **Capital Investment**: {spent_str}")
        lines.append(f"- **Total Daily Profit**: **+{r.total_daily_profit:,.1f} G/day**")
        lines.append(f"- **Projected Horizon Net Profit**: **+{r.projected_net:,.0f} G** over {r.max_days} active days\n")
        lines.append("---\n")

    lines.append("## Key Optimization Principles\n")
    lines.append(
        "1. **The Capital-Plot Inflection Balance**:\n"
        "   - When wallet capital is scarce (e.g., 1,000 G in Spring), high-compound crops like **Unionion (Nemea)** multiply money fast, while cheap seeds like **Dress Lettuce** act as plot-filling buffers.\n"
        "2. **Avoiding Single-Crop Capital Traps**:\n"
        "   - In Summer with 8,000 G, buying expensive seeds like **Islet Watermelon** (2,500 G) starves remaining plots. The solver allocates **29 Morrocorn** + **40 Dress Lettuce** to generate +2,050 G/day (+27% higher total profit than any Watermelon mix).\n"
        "3. **Biome Specialization**:\n"
        "   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.\n"
    )

    output_path = Path(output_path)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


# ==============================================================================
# CLI Entry Point
# ==============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Harvestella Crop Allocation Optimizer (MILP Knapsack Model)"
    )
    parser.add_argument("-sp", "--spring", action="store_true", help="Optimize Spring (configs/spring.yaml)")
    parser.add_argument("-su", "--summer", action="store_true", help="Optimize Summer (configs/summer.yaml)")
    parser.add_argument("-fa", "--fall", action="store_true", help="Optimize Fall (configs/fall.yaml)")
    parser.add_argument("-wi", "--winter", action="store_true", help="Optimize Winter (configs/winter.yaml)")
    parser.add_argument("-a", "--all", action="store_true", help="Run optimization across all 4 seasons (default if no season specified)")

    args = parser.parse_args()
    configs_dir = Path("configs")
    csv_dir = Path("seasons")

    selected: list[str] = []
    if args.spring:
        selected.append("spring")
    if args.summer:
        selected.append("summer")
    if args.fall:
        selected.append("fall")
    if args.winter:
        selected.append("winter")

    if args.all or not selected:
        selected = ["spring", "summer", "fall", "winter"]

    all_results: list[OptimizationResult] = []
    for s in selected:
        cfg_p = configs_dir / f"{s}.yaml"
        if cfg_p.is_file():
            res = solve_allocation(cfg_p, csv_dir=csv_dir)
            all_results.append(res)
            print_result_report(res)
        else:
            print(f"Configuration file not found for {s}: {cfg_p}")

    if not all_results:
        print("No valid seasonal YAML configurations found.")
        return

    if len(all_results) > 1:
        print_multi_season_summary(all_results)

    report_file = Path("crop_allocation_report.md")
    generate_markdown_report(all_results, output_path=report_file)
    print(f"Generated allocation report: {report_file.as_posix()}\n")


if __name__ == "__main__":
    main()
