"""Harvestella Crop Allocation Optimizer.

Computes mathematically optimal seed purchases and planting allocations
using a Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP) model
via scipy.optimize.milp (HiGHS solver).
Accounts for multi-biome plot capacities (Farm, Waterside, Cave), wallet gold,
vendor town unlocks, seed shop inventory caps per 10-day restock cycle,
overnight shipping cash turnaround, and reinvestment across the 30-day season.
"""

from __future__ import annotations

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
class DailyHarvestEvent:
    """Crop harvest event occurring on a specific day."""
    crop: CropCandidate
    quantity: int
    revenue: float
    is_regrowth: bool
    harvest_num: int
    total_harvests: int
    plant_day: int


@dataclass
class DailyPlantEvent:
    """Crop seed purchase and planting event occurring on a specific day."""
    crop: CropCandidate
    quantity: int
    cost: float
    harvest_days: list[int]
    net_profit: float


@dataclass
class DailyRecord:
    """Complete day ledger: morning arrivals, harvests, purchases/plantings, and end-of-day wallet."""
    day: int
    carryover_cash: float
    payout_revenue: float
    payout_sources: list[str]
    morning_wallet: float
    harvests: list[DailyHarvestEvent] = field(default_factory=list)
    plantings: list[DailyPlantEvent] = field(default_factory=list)
    daily_spent: float = 0.0
    end_wallet: float = 0.0


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
    daily_records: list[DailyRecord] = field(default_factory=list)
    quietus_payout: float = 0.0
    quietus_sources: list[str] = field(default_factory=list)
    total_season_profit: float = 0.0
    final_wallet_gold: float = 0.0

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

    # Compute daily cash arrivals timeline from solution
    daily_arrivals = {d: 0.0 for d in active_days}
    daily_arrivals[31] = 0.0  # Quietus morning arrivals from Day 30 harvest

    for i, count in enumerate(solution):
        if count <= 0:
            continue
        v = var_map[i]
        c = crops[v["crop_idx"]]
        for h in v["harvests"]:
            arr_day = h + 1
            if arr_day in daily_arrivals:
                daily_arrivals[arr_day] += count * c.nq_sale

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

    # Build Day-by-Day ledger & action events
    daily_harvest_events: dict[int, list[DailyHarvestEvent]] = {d: [] for d in range(current_day, 31)}
    daily_plant_events: dict[int, list[DailyPlantEvent]] = {d: [] for d in range(current_day, 31)}
    total_season_profit = 0.0

    for i, count in enumerate(solution):
        if count <= 0:
            continue
        v = var_map[i]
        c = crops[v["crop_idx"]]
        p_day = v["day"]
        cost_total = count * c.cost
        profit_subtotal = count * v["net_profit"]
        total_season_profit += profit_subtotal

        daily_plant_events[p_day].append(
            DailyPlantEvent(
                crop=c,
                quantity=count,
                cost=cost_total,
                harvest_days=v["harvests"],
                net_profit=profit_subtotal,
            )
        )

        tot_h = len(v["harvests"])
        for h_idx, h_day in enumerate(v["harvests"]):
            rev = count * c.nq_sale
            daily_harvest_events[h_day].append(
                DailyHarvestEvent(
                    crop=c,
                    quantity=count,
                    revenue=rev,
                    is_regrowth=c.is_regrowth,
                    harvest_num=h_idx + 1,
                    total_harvests=tot_h,
                    plant_day=p_day,
                )
            )

    daily_records: list[DailyRecord] = []
    current_cash = wallet_gold

    for d in range(current_day, 31):
        payout_rev = daily_arrivals.get(d, 0.0)
        payout_sources: list[str] = []
        if d - 1 in daily_harvest_events:
            prev_groups: dict[str, int] = {}
            for h in daily_harvest_events[d - 1]:
                prev_groups[h.crop.name] = prev_groups.get(h.crop.name, 0) + h.quantity
            payout_sources = [f"{q}x {name} on Day {d - 1}" for name, q in prev_groups.items()]

        carryover = current_cash
        morning_cash = carryover + payout_rev

        # Harvests occurring today (d)
        harvests_today = sorted(
            daily_harvest_events[d],
            key=lambda h: (h.crop.biome, h.crop.name)
        )

        # Plantings occurring today (d) - sorted by Vendor Town, then Biome, then Name
        biome_order = {"farm": 1, "waterside": 2, "cave": 3}
        plantings_today = sorted(
            daily_plant_events[d],
            key=lambda p: (p.crop.town, biome_order.get(p.crop.biome, 99), p.crop.name)
        )

        daily_spent = sum(p.cost for p in plantings_today)
        end_cash = morning_cash - daily_spent
        current_cash = end_cash

        daily_records.append(
            DailyRecord(
                day=d,
                carryover_cash=carryover,
                payout_revenue=payout_rev,
                payout_sources=payout_sources,
                morning_wallet=morning_cash,
                harvests=harvests_today,
                plantings=plantings_today,
                daily_spent=daily_spent,
                end_wallet=end_cash,
            )
        )

    # Quietus morning (Day 31) payout
    quietus_payout = daily_arrivals.get(31, 0.0)
    quietus_sources: list[str] = []
    if 30 in daily_harvest_events:
        d30_groups: dict[str, int] = {}
        for h in daily_harvest_events[30]:
            d30_groups[h.crop.name] = d30_groups.get(h.crop.name, 0) + h.quantity
        quietus_sources = [f"{q}x {name}" for name, q in d30_groups.items()]

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
        daily_records=daily_records,
        quietus_payout=quietus_payout,
        quietus_sources=quietus_sources,
        total_season_profit=total_season_profit,
        final_wallet_gold=wallet_gold + total_season_profit,
    )

