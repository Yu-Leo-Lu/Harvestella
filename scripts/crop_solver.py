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


@dataclass
class OccupiedCrop:
    """Pre-existing crop currently occupying plots in the ground."""
    crop: CropCandidate
    plant_day: int
    count: int
    harvest_days: list[int]
    occupy_days: list[int]


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
    is_preexisting: bool = False


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
    new_planting_profit: float = 0.0
    preexisting_revenue: float = 0.0
    total_season_profit: float = 0.0
    final_wallet_gold: float = 0.0
    occupied_summary: list[str] = field(default_factory=list)
    occupied_crops: list[OccupiedCrop] = field(default_factory=list)

    @property
    def gold_pct(self) -> float:
        """Percentage of starting wallet gold spent on Day current_day."""
        return (self.total_spent / self.wallet_gold * 100) if self.wallet_gold > 0 else 0.0


# ==============================================================================
# Helper Functions
# ==============================================================================

def is_town_unlocked(vendor_town: str, unlocked_towns: Any) -> bool:
    """Check if the vendor town is currently unlocked (split on '/' for multi-town)."""
    towns = [t.strip() for t in vendor_town.split("/")]
    if isinstance(unlocked_towns, (list, set, tuple)):
        return any(t in unlocked_towns for t in towns)
    if isinstance(unlocked_towns, dict):
        return any(unlocked_towns.get(t, False) for t in towns)
    return True


def parse_crop_entry(val: Any) -> tuple[int, int, int]:
    """Parse crop status into (plant_day, planted_count, store_stock).

    Supports:
      - 99               -> (0, 0, 99)
      - "(15, 51, 0)"   -> (15, 51, 0)
      - [15, 51, 0]      -> (15, 51, 0)
      - (15, 51, 0)      -> (15, 51, 0)
    """
    if val is None:
        return (0, 0, 99)
    if isinstance(val, (int, float)):
        return (0, 0, int(val))
    if isinstance(val, str):
        cleaned = val.strip("()[] \t\r\n")
        parts = [p.strip() for p in cleaned.split(",") if p.strip()]
        if len(parts) == 1:
            try:
                return (0, 0, int(parts[0]))
            except ValueError:
                return (0, 0, 99)
        if len(parts) == 2:
            try:
                return (int(parts[0]), int(parts[1]), 99)
            except ValueError:
                return (0, 0, 99)
        if len(parts) >= 3:
            try:
                return (int(parts[0]), int(parts[1]), int(parts[2]))
            except ValueError:
                return (0, 0, 99)
    if isinstance(val, (list, tuple)):
        if len(val) == 1:
            return (0, 0, int(val[0]))
        if len(val) == 2:
            return (int(val[0]), int(val[1]), 99)
        if len(val) >= 3:
            return (int(val[0]), int(val[1]), int(val[2]))
    return (0, 0, 99)


def build_occupied_crop(
    crop: CropCandidate,
    plant_day: int,
    count: int,
    current_day: int,
) -> OccupiedCrop | None:
    """Construct an OccupiedCrop instance with calculated harvest days and soil occupancy."""
    if count <= 0 or plant_day <= 0:
        return None

    if not crop.is_regrowth:
        mat_day = plant_day + crop.mature
        if mat_day < current_day:
            return None
        h_days = [mat_day] if mat_day <= 30 else []
        occ_days = list(range(current_day, mat_day))
        return OccupiedCrop(
            crop=crop,
            plant_day=plant_day,
            count=count,
            harvest_days=h_days,
            occupy_days=occ_days,
        )
    else:
        first_h = plant_day + crop.mature
        all_h = [first_h + k * crop.regrowth for k in range(crop.max_harvests)]
        h_days = [h for h in all_h if current_day <= h <= 30]
        occ_days = list(range(current_day, 31))
        return OccupiedCrop(
            crop=crop,
            plant_day=plant_day,
            count=count,
            harvest_days=h_days,
            occupy_days=occ_days,
        )


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

    active_days = list(range(current_day, 31))
    crops_cfg = cfg.get("crops", {})
    seed_stock_cfg = cfg.get("seed_stock") if cfg.get("seed_stock") is not None else crops_cfg
    planted_cfg = cfg.get("planted", []) or []
    unlocked_towns = cfg.get("unlocked_towns", {})

    with open(csv_path, encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))

    # 1. Parse crop candidates and detect currently occupied crops
    catalog: list[CropCandidate] = []
    eligible_candidates: list[CropCandidate] = []
    occupied_crops: list[OccupiedCrop] = []

    for r in raw_rows:
        crop_name = r.get("Crop Name", "").strip()
        biome = r.get("Biome", "").strip().lower()
        town = r.get("Vendor Town", "").strip()
        cost_str = r.get("Seed Cost (G)", "").strip()
        nq_str = r.get("NQ Sale (G)", "").strip()
        mature_str = r.get("Mature (Days)", "").strip()
        regrowth_str = r.get("Regrowth (Days)", "").strip()
        max_h_str = r.get("Max Harvests", "").strip()

        if not cost_str or not nq_str or not mature_str:
            continue

        try:
            cost = float(cost_str)
            nq_sale = float(nq_str)
            mature = int(mature_str)
        except ValueError:
            continue

        if cost <= 0 or nq_sale <= 0:
            continue

        is_regrowth = bool(regrowth_str and regrowth_str.isdigit() and int(regrowth_str) > 0)
        regrowth = int(regrowth_str) if is_regrowth else 0
        max_harvests = int(max_h_str) if (max_h_str and max_h_str.isdigit()) else 1

        v_stock_str = r.get("Vendor Stock", "").strip()
        vendor_stock = int(v_stock_str) if (v_stock_str and v_stock_str.isdigit()) else 99

        stock_key_town = f"{crop_name} ({town})"

        # Resolve store stock & optional legacy inline tuple: (plant_day, planted_count, store_stock)
        plant_day = 0
        planted_count = 0
        stock = vendor_stock

        entry = None
        if stock_key_town in seed_stock_cfg:
            entry = seed_stock_cfg[stock_key_town]
        elif town in seed_stock_cfg and isinstance(seed_stock_cfg[town], dict) and crop_name in seed_stock_cfg[town]:
            entry = seed_stock_cfg[town][crop_name]
        elif crop_name in seed_stock_cfg:
            entry = seed_stock_cfg[crop_name]

        if entry is not None:
            plant_day, planted_count, stock = parse_crop_entry(entry)

        candidate = CropCandidate(
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
        )
        catalog.append(candidate)

        # Track legacy pre-existing planted crops defined inline in crops/seed_stock
        if planted_count > 0 and plant_day > 0:
            occ = build_occupied_crop(candidate, plant_day, planted_count, current_day)
            if occ is not None:
                occupied_crops.append(occ)

        # Skip candidate from new purchases if town locked or stock non-positive
        if not is_town_unlocked(town, unlocked_towns):
            continue
        if stock <= 0 and (current_day > 20 or vendor_stock <= 0):
            continue

        eligible_candidates.append(candidate)

    # Parse dedicated `planted:` section (Format A: list of dicts with crop, day, count)
    if isinstance(planted_cfg, list):
        for item in planted_cfg:
            if not isinstance(item, dict):
                continue
            c_name = str(item.get("crop") or item.get("name") or "").strip()
            p_day = int(item.get("day") or item.get("plant_day") or 0)
            c_cnt = int(item.get("count") or item.get("qty") or item.get("quantity") or 0)
            if not c_name or p_day <= 0 or c_cnt <= 0:
                continue

            # Find matching candidate from complete seasonal catalog
            matched_cand = None
            for cand in catalog:
                if f"{cand.name} ({cand.town})".lower() == c_name.lower():
                    matched_cand = cand
                    break
            if matched_cand is None:
                for cand in catalog:
                    if cand.name.lower() == c_name.lower():
                        matched_cand = cand
                        break
            if matched_cand is None:
                continue

            occ = build_occupied_crop(matched_cand, p_day, c_cnt, current_day)
            if occ is not None:
                occupied_crops.append(occ)

    # 2. Determine daily plot capacity per biome across active_days
    reserve_cfg = cfg.get("reserve_plots", {})
    if isinstance(reserve_cfg, (int, float)):
        reserve = {"farm": int(reserve_cfg), "waterside": 0, "cave": 0}
    elif isinstance(reserve_cfg, dict):
        reserve = {
            "farm": int(reserve_cfg.get("farm", 0)),
            "waterside": int(reserve_cfg.get("waterside", 0)),
            "cave": int(reserve_cfg.get("cave", 0)),
        }
    else:
        reserve = {"farm": 0, "waterside": 0, "cave": 0}

    farm_physical = int(cfg.get("farm_level", 1)) * 49 if "farm_level" in cfg else int(cfg.get("farm_plots", 49))
    water_physical = int(cfg.get("waterside_plots", 81))
    cave_physical = int(cfg.get("cave_plots", 81))

    daily_biome_cap: dict[str, dict[int, int]] = {"farm": {}, "waterside": {}, "cave": {}}

    for t in active_days:
        base_f = max(0, farm_physical - reserve["farm"])
        occ_f = sum(occ.count for occ in occupied_crops if occ.crop.biome == "farm" and t in occ.occupy_days)
        daily_biome_cap["farm"][t] = max(0, base_f - occ_f)

        base_w = max(0, water_physical - reserve["waterside"])
        occ_w = sum(occ.count for occ in occupied_crops if occ.crop.biome == "waterside" and t in occ.occupy_days)
        daily_biome_cap["waterside"][t] = max(0, base_w - occ_w)

        base_c = max(0, cave_physical - reserve["cave"])
        occ_c = sum(occ.count for occ in occupied_crops if occ.crop.biome == "cave" and t in occ.occupy_days)
        daily_biome_cap["cave"][t] = max(0, base_c - occ_c)

    farm_init = daily_biome_cap["farm"][current_day]
    water_init = daily_biome_cap["waterside"][current_day]
    cave_init = daily_biome_cap["cave"][current_day]

    farm_cap = max(daily_biome_cap["farm"].values(), default=0)
    water_cap = max(daily_biome_cap["waterside"].values(), default=0)
    cave_cap = max(daily_biome_cap["cave"].values(), default=0)

    # Filter candidates to biomes with non-zero capacity
    crops = [c for c in eligible_candidates if (
        (c.biome == "farm" and farm_cap > 0) or
        (c.biome == "waterside" and water_cap > 0) or
        (c.biome == "cave" and cave_cap > 0)
    )]

    # Pre-existing arrivals from already occupied crops
    preexisting_arrivals: dict[int, float] = {d: 0.0 for d in range(current_day, 32)}
    preexisting_daily_harvests: dict[int, list[DailyHarvestEvent]] = {d: [] for d in range(current_day, 31)}
    total_preexisting_rev = 0.0

    for occ in occupied_crops:
        tot_h = len(occ.harvest_days)
        for h_idx, h in enumerate(occ.harvest_days):
            rev = occ.count * occ.crop.nq_sale
            total_preexisting_rev += rev
            arr_day = h + 1
            if arr_day in preexisting_arrivals:
                preexisting_arrivals[arr_day] += rev
            preexisting_daily_harvests[h].append(
                DailyHarvestEvent(
                    crop=occ.crop,
                    quantity=occ.count,
                    revenue=rev,
                    is_regrowth=occ.crop.is_regrowth,
                    harvest_num=h_idx + 1,
                    total_harvests=tot_h,
                    plant_day=occ.plant_day,
                    is_preexisting=True,
                )
            )

    occupied_summary = [
        f"{occ.count}x {occ.crop.name} ({occ.crop.biome.capitalize()}, planted D{occ.plant_day}, harvests: {', '.join(f'D{h}' for h in occ.harvest_days)})"
        for occ in occupied_crops
    ]

    if not crops and not occupied_crops:
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
    if use_variety_limit:
        unique_crop_names = sorted(list({crops[v["crop_idx"]].name for v in var_map}))
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
            cap = max(0, daily_biome_cap[biome][t])
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
    # wallet_gold + cum_preexisting_cash(t) - purchases_up_to(t) + shipping_up_to(t) >= 0
    # purchases_up_to(t) - shipping_up_to(t) <= wallet_gold + cum_preexisting_cash(t)
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
        cum_preexisting_cash = sum(preexisting_arrivals[d] for d in range(current_day, t + 1))
        ub_list.append(float(wallet_gold + cum_preexisting_cash))

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

    # Build Day-by-Day ledger & action events in a single pass over solution
    daily_arrivals = {d: preexisting_arrivals.get(d, 0.0) for d in range(current_day, 32)}
    daily_harvest_events: dict[int, list[DailyHarvestEvent]] = {d: [] for d in range(current_day, 31)}
    daily_plant_events: dict[int, list[DailyPlantEvent]] = {d: [] for d in range(current_day, 31)}

    # Include pre-existing harvests into daily_harvest_events
    for d in range(current_day, 31):
        if d in preexisting_daily_harvests:
            daily_harvest_events[d].extend(preexisting_daily_harvests[d])

    initial_farm = initial_water = initial_cave = 0
    day1_spent = 0.0
    new_planting_profit = 0.0

    for i, count in enumerate(solution):
        if count <= 0:
            continue
        v = var_map[i]
        c = crops[v["crop_idx"]]
        p_day = v["day"]
        cost_total = count * c.cost
        profit_subtotal = count * v["net_profit"]
        new_planting_profit += profit_subtotal

        # Day current_day initial utilization
        if p_day == current_day:
            day1_spent += cost_total
            if c.biome == "farm":
                initial_farm += count
            elif c.biome == "waterside":
                initial_water += count
            elif c.biome == "cave":
                initial_cave += count

        # Record planting event
        daily_plant_events[p_day].append(
            DailyPlantEvent(
                crop=c,
                quantity=count,
                cost=cost_total,
                harvest_days=v["harvests"],
                net_profit=profit_subtotal,
            )
        )

        # Record harvest events & schedule cash arrivals
        tot_h = len(v["harvests"])
        for h_idx, h_day in enumerate(v["harvests"]):
            rev = count * c.nq_sale
            arr_day = h_day + 1
            if arr_day in daily_arrivals:
                daily_arrivals[arr_day] += rev
            daily_harvest_events[h_day].append(
                DailyHarvestEvent(
                    crop=c,
                    quantity=count,
                    revenue=rev,
                    is_regrowth=c.is_regrowth,
                    harvest_num=h_idx + 1,
                    total_harvests=tot_h,
                    plant_day=p_day,
                    is_preexisting=False,
                )
            )

    daily_records: list[DailyRecord] = []
    current_cash = wallet_gold

    for d in range(current_day, 31):
        payout_rev = daily_arrivals.get(d, 0.0)
        payout_sources: list[str] = []
        if d - 1 in daily_harvest_events:
            prev_groups: dict[str, int] = {}
            prev_pre: dict[str, bool] = {}
            for h in daily_harvest_events[d - 1]:
                prev_groups[h.crop.name] = prev_groups.get(h.crop.name, 0) + h.quantity
                if h.is_preexisting:
                    prev_pre[h.crop.name] = True
            payout_sources = [
                f"{q}x {name}{' (pre-planted)' if prev_pre.get(name) else ''} on Day {d - 1}"
                for name, q in prev_groups.items()
            ]

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

    total_season_profit = new_planting_profit + total_preexisting_rev

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
        new_planting_profit=new_planting_profit,
        preexisting_revenue=total_preexisting_rev,
        total_season_profit=total_season_profit,
        final_wallet_gold=wallet_gold + total_season_profit,
        occupied_summary=occupied_summary,
        occupied_crops=occupied_crops,
    )

