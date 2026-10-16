"""Harvestella Crop Allocation Optimizer.

Computes mathematically optimal seed purchases and planting allocations
using a Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP) model
via scipy.optimize.milp (HiGHS solver).
Accounts for multi-biome plot capacities (Farm, Waterside, Cave), wallet gold,
vendor town unlocks, seed shop inventory caps per 10-day restock cycle,
overnight shipping cash turnaround, and reinvestment across the 30-day season.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


# ==============================================================================
# Data Structures
# ==============================================================================

@dataclass
class CropCandidate:
    """Catalog parameters for a candidate crop variety."""
    name: str
    town: str
    biome: str
    cost: float
    nq_sale: float
    mature: int
    is_regrowth: bool = False
    regrowth: int = 0
    max_harvests: int = 1
    stock: int = 99
    vendor_stock: int = 99
    daily_profit: float = 0.0
    prod_days: int = 0

    def __post_init__(self) -> None:
        if self.prod_days <= 0:
            if self.is_regrowth and self.regrowth > 0:
                self.prod_days = self.mature + (self.max_harvests - 1) * self.regrowth
            else:
                self.prod_days = self.mature
        if self.daily_profit <= 0 and self.prod_days > 0:
            total_rev = (self.max_harvests if self.is_regrowth else 1) * self.nq_sale
            self.daily_profit = (total_rev - self.cost) / self.prod_days


@dataclass
class StageCropItem:
    """Allocation of a crop variety planted on a specific day within a restock stage."""
    crop: CropCandidate
    plant_day: int
    plots_allocated: int
    rotations: int
    harvest_day: int
    harvest_days: list[int]
    seeds_consumed: int
    subtotal_cost: float
    subtotal_revenue: float
    subtotal_net_profit: float


@dataclass
class StageResult:
    """Optimization outcome and financial ledger for a single restock stage."""
    stage_idx: int
    start_day: int
    end_day: int
    window_days: int
    items: list[StageCropItem] = field(default_factory=list)
    starting_cash: float = 0.0
    cash_spent: float = 0.0
    cash_remaining: float = 0.0
    revenue_generated: float = 0.0
    farm_used: int = 0
    farm_cap: int = 0
    farm_seeds: int = 0
    water_used: int = 0
    water_cap: int = 0
    water_seeds: int = 0
    cave_used: int = 0
    cave_cap: int = 0
    cave_seeds: int = 0


@dataclass
class OptimizationResult:
    """Overall season optimization result across all restock stages to Quietus."""
    season: str
    config_path: Path
    current_day: int = 1
    timeline: str = ""
    wallet_gold: float = 0.0
    total_spent: float = 0.0
    leftover_gold: float = 0.0
    farm_used: int = 0
    farm_init: int = 0
    farm_cap: int = 0
    water_used: int = 0
    water_init: int = 0
    water_cap: int = 0
    cave_used: int = 0
    cave_init: int = 0
    cave_cap: int = 0
    success: bool = True
    status_message: str = "Optimal solution found."
    max_varieties: int | None = None
    stages: list[StageResult] = field(default_factory=list)
    total_season_profit: float = 0.0
    final_wallet_gold: float = 0.0

    @property
    def items(self) -> list[StageCropItem]:
        """Immediate Stage 1 planting allocations."""
        return self.stages[0].items if self.stages else []

    @property
    def gold_pct(self) -> float:
        """Percentage of starting wallet gold spent on Day current_day."""
        return (self.total_spent / self.wallet_gold * 100) if self.wallet_gold > 0 else 0.0


# ==============================================================================
# Helper Functions
# ==============================================================================

def is_town_unlocked(vendor_town: str, unlocked_towns: dict[str, bool]) -> bool:
    """Check if the vendor town is currently unlocked (split on '/' for multi-town)."""
    towns = [t.strip() for t in vendor_town.split("/")]
    return any(unlocked_towns.get(t, False) for t in towns)


def get_plot_capacity(biome_cfg: Any, day: int, current_day: int = 1) -> int:
    """Resolve daily plot capacity from a scalar or a stepped schedule {start: N, day: N}."""
    if biome_cfg is None:
        return 0
    if isinstance(biome_cfg, (int, float)):
        return max(0, int(biome_cfg))
    if isinstance(biome_cfg, dict):
        milestones: dict[int, int] = {}
        for k, v in biome_cfg.items():
            k_str = str(k).strip().lower()
            try:
                val = max(0, int(v))
            except (ValueError, TypeError):
                continue
            if k_str in ("start", "now", "init", "current", "base"):
                milestones[current_day] = val
            elif k_str.isdigit():
                milestones[int(k_str)] = val

        if not milestones:
            return 0

        sorted_days = sorted(milestones.keys())
        valid = [m for m in sorted_days if m <= day]
        if valid:
            return milestones[max(valid)]
        return milestones[sorted_days[0]]
    return 0


# ==============================================================================
# Core Day-to-Day Optimization Engine
# ==============================================================================

def solve_allocation(
    config_path: Path,
    csv_dir: Path = Path("seasons"),
) -> OptimizationResult:
    """Solve the day-to-day time-indexed crop allocation MILP for a config profile."""
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
    days_window = 30 if current_day == 1 else max(0, 30 - current_day + 1)
    timeline_desc = f"Day {current_day} -> Day 30 ({days_window}d Quietus window)"

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
    active_days = list(range(current_day, 31))

    farm_init = get_plot_capacity(free_plots.get("farm"), current_day, current_day)
    water_init = get_plot_capacity(free_plots.get("waterside"), current_day, current_day)
    cave_init = get_plot_capacity(free_plots.get("cave"), current_day, current_day)

    farm_cap = max((get_plot_capacity(free_plots.get("farm"), d, current_day) for d in active_days), default=0)
    water_cap = max((get_plot_capacity(free_plots.get("waterside"), d, current_day) for d in active_days), default=0)
    cave_cap = max((get_plot_capacity(free_plots.get("cave"), d, current_day) for d in active_days), default=0)

    unlocked_towns = cfg.get("unlocked_towns", {})
    seed_stock = cfg.get("seed_stock", {})

    with open(csv_path, encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))

    # 1. Parse crop candidates
    crops: list[CropCandidate] = []
    for r in raw_rows:
        crop_name = r.get("Crop Name", "").strip()
        biome = r.get("Biome", "").strip().lower()
        town = r.get("Vendor Town", "").strip()
        cost_str = r.get("Seed Cost (G)", "").strip()
        nq_str = r.get("NQ Sale (G)", "").strip()
        mature_str = r.get("Mature (Days)", "").strip()
        regrowth_str = r.get("Regrowth (Days)", "").strip()
        max_h_str = r.get("Max Harvests", "").strip()
        profit_str = r.get("Daily NQ Profit (G/d)", "").strip()
        prod_str = r.get("Production (Days)", "").strip()

        if not cost_str or not nq_str or not mature_str:
            continue
        try:
            cost = float(cost_str)
            nq_sale = float(nq_str)
            mature = int(mature_str)
            daily_profit = float(profit_str) if profit_str else 0.0
            prod_days = int(prod_str) if prod_str else 0
        except ValueError:
            continue

        if cost <= 0 or nq_sale <= 0:
            continue
        if not is_town_unlocked(town, unlocked_towns):
            continue
        if biome == "farm" and farm_cap <= 0:
            continue
        if biome == "waterside" and water_cap <= 0:
            continue
        if biome == "cave" and cave_cap <= 0:
            continue

        is_regrowth = bool(regrowth_str and regrowth_str.isdigit() and int(regrowth_str) > 0)
        regrowth = int(regrowth_str) if is_regrowth else 0
        max_harvests = int(max_h_str) if (max_h_str and max_h_str.isdigit()) else 1

        v_stock_str = r.get("Vendor Stock", "").strip()
        vendor_stock = int(v_stock_str) if (v_stock_str and v_stock_str.isdigit()) else 99

        stock_key_town = f"{crop_name} ({town})"
        if stock_key_town in seed_stock:
            stock = int(seed_stock[stock_key_town])
        elif town in seed_stock and isinstance(seed_stock[town], dict) and crop_name in seed_stock[town]:
            stock = int(seed_stock[town][crop_name])
        elif crop_name in seed_stock:
            stock = int(seed_stock[crop_name])
        else:
            stock = vendor_stock

        # If both current stock and future vendor restock are non-positive, skip crop
        if stock <= 0 and (current_day > 20 or vendor_stock <= 0):
            continue

        crops.append(
            CropCandidate(
                name=crop_name,
                town=town,
                biome=biome,
                cost=cost,
                nq_sale=nq_sale,
                mature=mature,
                is_regrowth=is_regrowth,
                regrowth=regrowth,
                max_harvests=max_harvests,
                stock=stock,
                vendor_stock=vendor_stock,
                daily_profit=daily_profit,
                prod_days=prod_days,
            )
        )

    if not crops:
        return OptimizationResult(
            season=season,
            config_path=config_path,
            current_day=current_day,
            timeline=timeline_desc,
            wallet_gold=wallet_gold,
            leftover_gold=wallet_gold,
            farm_init=farm_init,
            farm_cap=farm_cap,
            water_init=water_init,
            water_cap=water_cap,
            cave_init=cave_init,
            cave_cap=cave_cap,
            status_message="No eligible crops match current filters (unlocked towns or plot capacity).",
        )

    # 2. Build time-indexed decision variables: (crop_idx, plant_day)
    # plant_day in [current_day .. 30]
    var_map: list[dict[str, Any]] = []

    for c_idx, c in enumerate(crops):
        for d in active_days:
            if not c.is_regrowth:
                harvest_day = d + c.mature
                if harvest_day <= 30:
                    harvests = [harvest_day]
                    occupy_days = list(range(d, harvest_day))
                    total_rev = c.nq_sale
                    net_profit = total_rev - c.cost
                    var_map.append({
                        "crop_idx": c_idx,
                        "day": d,
                        "harvests": harvests,
                        "occupy_days": occupy_days,
                        "total_rev": total_rev,
                        "net_profit": net_profit,
                    })
            else:
                harvests = []
                for k in range(c.max_harvests):
                    h_day = d + c.mature + k * c.regrowth
                    if h_day <= 30:
                        harvests.append(h_day)
                    else:
                        break
                if harvests:
                    total_rev = len(harvests) * c.nq_sale
                    net_profit = total_rev - c.cost
                    if net_profit > 0:
                        last_h = max(harvests)
                        occupy_days = list(range(d, min(31, last_h + 1)))
                        var_map.append({
                            "crop_idx": c_idx,
                            "day": d,
                            "harvests": harvests,
                            "occupy_days": occupy_days,
                            "total_rev": total_rev,
                            "net_profit": net_profit,
                        })

    n_vars = len(var_map)
    if n_vars == 0:
        return OptimizationResult(
            season=season,
            config_path=config_path,
            current_day=current_day,
            timeline=timeline_desc,
            wallet_gold=wallet_gold,
            leftover_gold=wallet_gold,
            farm_cap=farm_cap,
            water_cap=water_cap,
            cave_cap=cave_cap,
            status_message="No crops can reach harvest before Day 30 (Quietus).",
        )

    # 3. Variety Limit variables (if active)
    use_variety_limit = max_varieties is not None
    unique_crop_names: list[str] = []
    crop_to_idx: dict[str, int] = {}
    if use_variety_limit:
        unique_crop_names = sorted(list({crops[v["crop_idx"]].name for v in var_map}))
        crop_to_idx = {name: idx for idx, name in enumerate(unique_crop_names)}
        total_vars = n_vars + len(unique_crop_names)
    else:
        total_vars = n_vars

    # Objective: Maximize total cumulative net profit (minimize negative profit)
    c_obj = np.zeros(total_vars)
    for i, v in enumerate(var_map):
        c = crops[v["crop_idx"]]
        # Tie-breakers: prefer cheaper seeds and earlier planting
        c_obj[i] = -(v["net_profit"] - 1e-6 * c.cost - 1e-8 * (v["day"] - current_day))

    A_rows: list[list[float]] = []
    lb_list: list[float] = []
    ub_list: list[float] = []

    # 4. Constraint Row Formulation
    # A) Daily Plot Capacity per Biome for each day t in [current_day .. 30]
    for t in active_days:
        for biome in ["farm", "waterside", "cave"]:
            cap = get_plot_capacity(free_plots.get(biome), t, current_day)
            if cap <= 0:
                continue
            row = [0.0] * total_vars
            has_relevant = False
            for i, v in enumerate(var_map):
                c = crops[v["crop_idx"]]
                if c.biome == biome and t in v["occupy_days"]:
                    row[i] = 1.0
                    has_relevant = True
            if has_relevant:
                A_rows.append(row)
                lb_list.append(0.0)
                ub_list.append(float(cap))

    # B) Daily Cash Liquidity on each day t in [current_day .. 30]
    # wallet_gold - purchases_up_to(t) + shipping_up_to(t) >= 0
    # purchases_up_to(t) - shipping_up_to(t) <= wallet_gold
    for t in active_days:
        row = [0.0] * total_vars
        for i, v in enumerate(var_map):
            c = crops[v["crop_idx"]]
            if v["day"] <= t:
                row[i] += c.cost
            for h in v["harvests"]:
                # Overnight shipping: proceeds arrive on morning of harvest + 1
                if h + 1 <= t:
                    row[i] -= c.nq_sale
        A_rows.append(row)
        lb_list.append(-np.inf)
        ub_list.append(float(wallet_gold))

    # C) Seed stock inventory limits per 10-day vendor restock cycle
    windows = [(1, 10), (11, 20), (21, 30)]
    for w_start, w_end in windows:
        if w_end < current_day:
            continue
        is_current_window = (w_start <= current_day <= w_end)
        for c_idx, c in enumerate(crops):
            cap = c.stock if is_current_window else c.vendor_stock
            row = [0.0] * total_vars
            has_relevant = False
            for i, v in enumerate(var_map):
                if v["crop_idx"] == c_idx and w_start <= v["day"] <= w_end:
                    row[i] = 1.0
                    has_relevant = True
            if has_relevant:
                A_rows.append(row)
                lb_list.append(0.0)
                ub_list.append(float(cap))

    # D) Big-M linking for variety cardinality limit (if active)
    if use_variety_limit and max_varieties is not None:
        big_m = float(max(farm_cap, water_cap, cave_cap) * 30 + 100)
        for u_idx, u_name in enumerate(unique_crop_names):
            link_row = [0.0] * total_vars
            has_u = False
            for i, v in enumerate(var_map):
                if crops[v["crop_idx"]].name == u_name:
                    link_row[i] = 1.0
                    has_u = True
            if has_u:
                link_row[n_vars + u_idx] = -big_m
                A_rows.append(link_row)
                lb_list.append(-np.inf)
                ub_list.append(0.0)

        card_row = [0.0] * total_vars
        for u_idx in range(len(unique_crop_names)):
            card_row[n_vars + u_idx] = 1.0
        A_rows.append(card_row)
        lb_list.append(0.0)
        ub_list.append(float(max_varieties))

    A = np.array(A_rows)
    lb = np.array(lb_list)
    ub = np.array(ub_list)

    var_lb = np.zeros(total_vars)
    var_ub = np.full(total_vars, np.inf)
    if use_variety_limit:
        var_ub[n_vars:] = 1.0

    bounds = Bounds(lb=var_lb, ub=var_ub)
    constraints = LinearConstraint(A, lb, ub)
    integrality = np.ones(total_vars)

    # 5. Solve via SciPy HiGHS Branch-and-Cut MILP
    res = milp(
        c=c_obj,
        constraints=constraints,
        bounds=bounds,
        integrality=integrality,
        options={"disp": False, "mip_rel_gap": 0.015, "time_limit": 10},
    )

    if res.x is None:
        return OptimizationResult(
            season=season,
            config_path=config_path,
            success=False,
            status_message=f"MILP solver failed: {res.status} - {res.message}",
        )

    solution = np.round(res.x[:n_vars]).astype(int)

    # 6. Partition daily allocations into 10-day restock stages
    stage_boundaries = [(1, 10), (11, 20), (21, 30)]
    active_stages = [
        (max(current_day, w_start), w_end)
        for w_start, w_end in stage_boundaries
        if w_end >= current_day
    ]

    stage_results: list[StageResult] = []
    total_season_profit = 0.0

    # Compute daily cash timeline
    daily_purchases = {d: 0.0 for d in active_days}
    daily_arrivals = {d: 0.0 for d in active_days}
    daily_arrivals[31] = 0.0  # Quietus morning arrivals from Day 30 harvest

    for i, count in enumerate(solution):
        if count <= 0:
            continue
        v = var_map[i]
        c = crops[v["crop_idx"]]
        daily_purchases[v["day"]] += count * c.cost
        for h in v["harvests"]:
            arr_day = h + 1
            if arr_day in daily_arrivals:
                daily_arrivals[arr_day] += count * c.nq_sale

    running_cash = wallet_gold

    for s_idx, (s_start, s_end) in enumerate(active_stages):
        st_items: list[StageCropItem] = []
        stage_spent = 0.0
        stage_rev = 0.0
        st_farm = st_water = st_cave = 0

        for i, count in enumerate(solution):
            if count <= 0:
                continue
            v = var_map[i]
            c = crops[v["crop_idx"]]
            p_day = v["day"]
            if not (s_start <= p_day <= s_end):
                continue

            cost_total = count * c.cost
            rev_total = count * v["total_rev"]
            profit_subtotal = count * v["net_profit"]

            stage_spent += cost_total
            total_season_profit += profit_subtotal

            if c.biome == "farm":
                st_farm += count
            elif c.biome == "waterside":
                st_water += count
            elif c.biome == "cave":
                st_cave += count

            item = StageCropItem(
                crop=c,
                plant_day=p_day,
                plots_allocated=count,
                rotations=len(v["harvests"]),
                harvest_day=max(v["harvests"]),
                harvest_days=v["harvests"],
                seeds_consumed=count,
                subtotal_cost=cost_total,
                subtotal_revenue=rev_total,
                subtotal_net_profit=profit_subtotal,
            )
            st_items.append(item)

        # Revenue arriving during this stage
        for d in range(s_start, s_end + 1):
            stage_rev += daily_arrivals.get(d, 0.0)

        # Sort items by plant day, then biome
        biome_order = {"farm": 1, "waterside": 2, "cave": 3}
        st_items.sort(key=lambda it: (it.plant_day, biome_order.get(it.crop.biome, 99), -it.crop.daily_profit))

        # Peak plots occupied simultaneously on any day during this stage
        stage_farm_cap = max((get_plot_capacity(free_plots.get("farm"), d, current_day) for d in range(s_start, s_end + 1)), default=0)
        stage_water_cap = max((get_plot_capacity(free_plots.get("waterside"), d, current_day) for d in range(s_start, s_end + 1)), default=0)
        stage_cave_cap = max((get_plot_capacity(free_plots.get("cave"), d, current_day) for d in range(s_start, s_end + 1)), default=0)

        peak_farm = peak_water = peak_cave = 0
        for d in range(s_start, s_end + 1):
            occ_f = occ_w = occ_c = 0
            for i, count in enumerate(solution):
                if count <= 0:
                    continue
                v = var_map[i]
                if d in v["occupy_days"]:
                    c = crops[v["crop_idx"]]
                    if c.biome == "farm":
                        occ_f += count
                    elif c.biome == "waterside":
                        occ_w += count
                    elif c.biome == "cave":
                        occ_c += count
            peak_farm = max(peak_farm, occ_f)
            peak_water = max(peak_water, occ_w)
            peak_cave = max(peak_cave, occ_c)

        cash_remaining = running_cash - stage_spent
        stage_results.append(
            StageResult(
                stage_idx=s_idx + 1,
                start_day=s_start,
                end_day=s_end,
                window_days=s_end - s_start + 1,
                items=st_items,
                starting_cash=running_cash,
                cash_spent=stage_spent,
                cash_remaining=cash_remaining,
                revenue_generated=stage_rev,
                farm_used=int(peak_farm),
                farm_cap=stage_farm_cap,
                farm_seeds=int(st_farm),
                water_used=int(peak_water),
                water_cap=stage_water_cap,
                water_seeds=int(st_water),
                cave_used=int(peak_cave),
                cave_cap=stage_cave_cap,
                cave_seeds=int(st_cave),
            )
        )
        running_cash = cash_remaining + stage_rev

    # Day current_day initial utilization
    initial_farm = initial_water = initial_cave = 0
    day1_spent = 0.0
    for i, count in enumerate(solution):
        if count <= 0:
            continue
        v = var_map[i]
        c = crops[v["crop_idx"]]
        if v["day"] == current_day:
            day1_spent += count * c.cost
            if c.biome == "farm":
                initial_farm += count
            elif c.biome == "waterside":
                initial_water += count
            elif c.biome == "cave":
                initial_cave += count

    return OptimizationResult(
        season=season,
        config_path=config_path,
        current_day=current_day,
        timeline=timeline_desc,
        wallet_gold=wallet_gold,
        total_spent=day1_spent,
        leftover_gold=wallet_gold - day1_spent,
        farm_used=initial_farm,
        farm_init=farm_init,
        farm_cap=farm_cap,
        water_used=initial_water,
        water_init=water_init,
        water_cap=water_cap,
        cave_used=initial_cave,
        cave_init=cave_init,
        cave_cap=cave_cap,
        success=True,
        status_message="Optimal solution found." if res.status == 0 else f"Feasible solution found: {res.message}",
        max_varieties=max_varieties,
        stages=stage_results,
        total_season_profit=total_season_profit,
        final_wallet_gold=wallet_gold + total_season_profit,
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
    print(f" Config File     : {result.config_path}")
    print(f" Current Day     : Day {result.current_day}")
    print(f" Planning Timeline: {result.timeline}")
    if result.max_varieties is not None:
        print(f" Variety Limit   : Max {result.max_varieties} distinct crop varieties")
    print(f" Capital Budget  : {result.wallet_gold:,.0f} G")
    cap_strs = []
    for b_name, b_init, b_cap in [("Farm", result.farm_init, result.farm_cap), ("Waterside", result.water_init, result.water_cap), ("Cave", result.cave_init, result.cave_cap)]:
        if b_cap > 0:
            if b_init == b_cap:
                cap_strs.append(f"{b_name} {b_cap}")
            else:
                cap_strs.append(f"{b_name} {b_init} -> {b_cap}")
        else:
            cap_strs.append(f"{b_name} 0")
    print(f" Plot Capacities : {' | '.join(cap_strs)}")
    print("-" * 86)

    if not result.success:
        print(f" [!] ERROR: {result.status_message}\n")
        return

    if not result.stages:
        print(f" [i] {result.status_message}\n")
        return

    print(" OPTIMAL PLANTING TIMELINE (Day-to-Day Time-Indexed Compounding Model)")
    print("-" * 86)
    for st in result.stages:
        print(f" [Stage {st.stage_idx}: Day {st.start_day} -> Day {st.end_day} ({st.window_days}d window)]")
        plot_summaries = []
        if st.farm_cap > 0:
            plot_summaries.append(f"Farm (Peak): {st.farm_used}/{st.farm_cap} (Seeds: {st.farm_seeds})")
        if st.water_cap > 0:
            plot_summaries.append(f"Waterside (Peak): {st.water_used}/{st.water_cap} (Seeds: {st.water_seeds})")
        if st.cave_cap > 0:
            plot_summaries.append(f"Cave (Peak): {st.cave_used}/{st.cave_cap} (Seeds: {st.cave_seeds})")
        plot_line = " | ".join(plot_summaries) if plot_summaries else "No active biomes"

        print(
            f"  Starting Cash : {st.starting_cash:,.0f} G | "
            f"Stage Spent: {st.cash_spent:,.0f} G | "
            f"{plot_line}"
        )
        print(
            f"  {'Plant':<8} {'Biome':<10} {'Crop Name':<18} {'Vendor':<10} "
            f"{'Qty':>4} {'Seed Spent':>11} {'Harvest Days':<15} {'Net Profit':>11}"
        )
        print("  " + "-" * 82)
        for it in st.items:
            c = it.crop
            h_str = ", ".join(f"D{d}" for d in it.harvest_days)
            if len(h_str) > 14:
                h_str = f"D{it.harvest_days[0]}..D{it.harvest_days[-1]}"
            print(
                f"  Day {it.plant_day:<4} "
                f"{c.biome.capitalize():<10} "
                f"{c.name:<18} "
                f"{c.town:<10} "
                f"{it.plots_allocated:>4} "
                f"{it.subtotal_cost:>10,.0f} G "
                f"{h_str:<15} "
                f"+{it.subtotal_net_profit:>10,.0f} G"
            )
        net_end = st.cash_remaining + st.revenue_generated
        print(f"  Stage Harvest Revenue Arrived: +{st.revenue_generated:,.0f} G | Projected Cash at Stage End: {net_end:,.0f} G\n")

    print("-" * 86)
    print(" RESOURCE UTILIZATION & FINANCIAL SUMMARY")
    print("-" * 86)

    farm_pct = (result.farm_used / result.farm_init * 100) if result.farm_init > 0 else 0
    cap_farm_note = f"{result.farm_init}" if result.farm_init == result.farm_cap else f"{result.farm_init} (expands to {result.farm_cap})"
    print(
        f" Farm Plots Used (Init): {result.farm_used:>3} / {result.farm_init:<3} "
        f"({farm_pct:>5.1f}% utilized on Day {result.current_day}, capacity: {cap_farm_note})"
    )
    if result.water_cap > 0:
        water_pct = (result.water_used / result.water_init * 100) if result.water_init > 0 else 0
        w_note = f"{result.water_init}" if result.water_init == result.water_cap else f"{result.water_init} (expands to {result.water_cap})"
        print(
            f" Waterside Plots (Init): {result.water_used:>3} / {result.water_init:<3} "
            f"({water_pct:>5.1f}% utilized on Day {result.current_day}, capacity: {w_note})"
        )
    if result.cave_cap > 0:
        cave_pct = (result.cave_used / result.cave_init * 100) if result.cave_init > 0 else 0
        c_note = f"{result.cave_init}" if result.cave_init == result.cave_cap else f"{result.cave_init} (expands to {result.cave_cap})"
        print(
            f" Cave Plots Used (Init): {result.cave_used:>3} / {result.cave_init:<3} "
            f"({cave_pct:>5.1f}% utilized on Day {result.current_day}, capacity: {c_note})"
        )

    print(
        f" Initial Capital Spent : {result.total_spent:>8,.0f} G / {result.wallet_gold:,.0f} G "
        f"({result.gold_pct:>5.1f}% spent, {result.leftover_gold:,.0f} G leftover)"
    )
    print(f" Total Season Net Profit: +{result.total_season_profit:>8,.0f} G across all restock stages")
    print(f" Final Projected Wallet : {result.final_wallet_gold:>8,.0f} G on Day 30 (Quietus)")
    print("=" * 86 + "\n")


def generate_markdown_report(
    results: list[OptimizationResult],
    output_path: Path = Path("crop_allocation_report.md"),
) -> Path:
    """Generate a structured GitHub-Flavored Markdown report mirroring the terminal report."""
    valid = [r for r in results if r.success and r.stages]
    if not valid:
        return output_path

    lines: list[str] = [
        "# Harvestella Crop Allocation & Planting Report\n",
        "> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).\n",
    ]

    for idx, r in enumerate(valid):
        season_title = r.season.upper() if r.season else "UNKNOWN"
        lines.append(f"## {season_title} Optimization Plan\n")
        lines.append(f"- **Config Profile**: [`{r.config_path.as_posix()}`]({r.config_path.as_posix()})")
        lines.append(f"- **Current Day**: Day {r.current_day}")
        lines.append(f"- **Planning Timeline**: {r.timeline}")
        if r.max_varieties is not None:
            lines.append(f"- **Variety Limit**: Max {r.max_varieties} distinct crop varieties")
        lines.append(f"- **Capital Budget**: {r.wallet_gold:,.0f} G")
        cap_strs = []
        for b_name, b_init, b_cap in [("Farm", r.farm_init, r.farm_cap), ("Waterside", r.water_init, r.water_cap), ("Cave", r.cave_init, r.cave_cap)]:
            if b_cap > 0:
                if b_init == b_cap:
                    cap_strs.append(f"{b_name} {b_cap}")
                else:
                    cap_strs.append(f"{b_name} {b_init} -> {b_cap}")
            else:
                cap_strs.append(f"{b_name} 0")
        lines.append(f"- **Plot Capacities**: {' | '.join(cap_strs)}\n")

        lines.append("### Optimal Planting Timeline\n")
        for st in r.stages:
            lines.append(f"#### Stage {st.stage_idx}: Day {st.start_day} → Day {st.end_day} ({st.window_days}-day window)\n")
            plot_summaries = []
            if st.farm_cap > 0:
                plot_summaries.append(f"**Farm (Peak)**: {st.farm_used} / {st.farm_cap} (Seeds: {st.farm_seeds})")
            if st.water_cap > 0:
                plot_summaries.append(f"**Waterside (Peak)**: {st.water_used} / {st.water_cap}")
            if st.cave_cap > 0:
                plot_summaries.append(f"**Cave (Peak)**: {st.cave_used} / {st.cave_cap}")
            plot_str = " | ".join(plot_summaries) if plot_summaries else "No plots"
            lines.append(
                f"- **Starting Cash**: {st.starting_cash:,.0f} G | "
                f"**Stage Spent**: {st.cash_spent:,.0f} G | "
                f"{plot_str}\n"
            )
            lines.append(
                "| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |"
            )
            lines.append(
                "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
            )
            for it in st.items:
                c = it.crop
                h_str = ", ".join(f"Day {d}" for d in it.harvest_days)
                if len(h_str) > 24:
                    h_str = f"Day {it.harvest_days[0]}..{it.harvest_days[-1]} ({len(it.harvest_days)}x)"
                lines.append(
                    f"| Day {it.plant_day} | {c.biome.capitalize()} | **{c.name}** | {c.town} | {it.plots_allocated} | "
                    f"{it.subtotal_cost:,.0f} G | {h_str} | +{it.subtotal_net_profit:,.0f} G |"
                )
            net_end = st.cash_remaining + st.revenue_generated
            lines.append(
                f"\n- **Stage Harvest Revenue Arrived**: +{st.revenue_generated:,.0f} G | "
                f"**Projected Cash at Stage End**: **{net_end:,.0f} G**\n"
            )

        lines.append("### Resource Utilization & Financial Summary\n")
        farm_pct = (r.farm_used / r.farm_init * 100) if r.farm_init > 0 else 0
        cap_farm_note = f"{r.farm_init}" if r.farm_init == r.farm_cap else f"{r.farm_init} (expands to {r.farm_cap})"
        lines.append(
            f"- **Farm Plots Used (Init)**: {r.farm_used} / {cap_farm_note} "
            f"({farm_pct:.1f}% utilized, {r.farm_init - r.farm_used} idle)"
        )
        if r.water_cap > 0:
            water_pct = (r.water_used / r.water_init * 100) if r.water_init > 0 else 0
            w_note = f"{r.water_init}" if r.water_init == r.water_cap else f"{r.water_init} (expands to {r.water_cap})"
            lines.append(
                f"- **Waterside Plots (Init)**: {r.water_used} / {w_note} "
                f"({water_pct:.1f}% utilized, {r.water_init - r.water_used} idle)"
            )
        if r.cave_cap > 0:
            cave_pct = (r.cave_used / r.cave_init * 100) if r.cave_init > 0 else 0
            c_note = f"{r.cave_init}" if r.cave_init == r.cave_cap else f"{r.cave_init} (expands to {r.cave_cap})"
            lines.append(
                f"- **Cave Plots Used (Init)**: {r.cave_used} / {c_note} "
                f"({cave_pct:.1f}% utilized, {r.cave_init - r.cave_used} idle)"
            )

        lines.append(
            f"- **Initial Capital Spent**: {r.total_spent:,.0f} G / {r.wallet_gold:,.0f} G "
            f"({r.gold_pct:.1f}% spent, {r.leftover_gold:,.0f} G leftover)"
        )
        lines.append(f"- **Total Cumulative Season Net Profit**: **+{r.total_season_profit:,.0f} G** across all restock stages")
        lines.append(f"- **Final Projected Wallet**: **{r.final_wallet_gold:,.0f} G** on Day 30 (Quietus)\n")

        lines.append("---\n")

    lines.append("## Key Optimization Principles\n")
    lines.append(
        "1. **Day-to-Day Rolling Capital Reinvestment**:\n"
        "   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).\n"
        "2. **Soil Occupancy & Regrowth Dynamics**:\n"
        "   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.\n"
        "3. **Biome Specialization & Plot Balancing**:\n"
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
        description="Harvestella Crop Allocation Optimizer (Day-to-Day Time-Indexed MILP Model)"
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

    report_file = Path("crop_allocation_report.md")
    generate_markdown_report(all_results, output_path=report_file)
    print(f"Generated allocation report: {report_file.as_posix()}\n")


if __name__ == "__main__":
    main()
