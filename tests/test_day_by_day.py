"""Test suite for Day-to-Day Time-Indexed Crop Allocation Optimization."""

import csv
from pathlib import Path
import unittest
import numpy as np
import yaml
from scipy.optimize import Bounds, LinearConstraint, milp


def run_season(config_name="spring"):
    config_path = Path(f"configs/{config_name}.yaml")
    if not config_path.is_file():
        print(f"Skipping {config_name}: not found")
        return None
    with open(config_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    season = config_name
    csv_path = Path(f"seasons/{season}.csv")
    with open(csv_path, encoding="utf-8") as f:
        raw_rows = list(csv.DictReader(f))

    current_day = int(cfg.get("current_day", 1))
    wallet_gold = float(cfg.get("wallet_gold", 0.0))
    free_plots = cfg.get("free_plots", {})
    farm_cap = int(free_plots.get("farm", 0))
    water_cap = int(free_plots.get("waterside", 0))
    cave_cap = int(free_plots.get("cave", 0))
    unlocked_towns = cfg.get("unlocked_towns", {})
    seed_stock = cfg.get("seed_stock", {})

    def is_town_unlocked(vendor_town: str) -> bool:
        towns = [t.strip() for t in vendor_town.split("/")]
        return any(unlocked_towns.get(t, False) for t in towns)

    crops = []
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

        if cost <= 0 or nq_sale <= 0 or not is_town_unlocked(town):
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

        if stock <= 0 and (current_day > 20 or vendor_stock <= 0):
            continue

        crops.append({
            "name": crop_name,
            "town": town,
            "biome": biome,
            "cost": cost,
            "nq_sale": nq_sale,
            "mature": mature,
            "is_regrowth": is_regrowth,
            "regrowth": regrowth,
            "max_harvests": max_harvests,
            "stock": stock,
            "vendor_stock": vendor_stock,
        })

    active_days = list(range(current_day, 31))
    var_map = []
    for c_idx, c in enumerate(crops):
        for d in active_days:
            if not c["is_regrowth"]:
                h_day = d + c["mature"]
                if h_day <= 30:
                    var_map.append({
                        "crop_idx": c_idx,
                        "day": d,
                        "harvests": [h_day],
                        "occupy_days": list(range(d, h_day)),
                        "cost": c["cost"],
                        "rev": c["nq_sale"],
                        "profit": c["nq_sale"] - c["cost"],
                        "biome": c["biome"],
                    })
            else:
                harvests = []
                for k in range(c["max_harvests"]):
                    h = d + c["mature"] + k * c["regrowth"]
                    if h <= 30:
                        harvests.append(h)
                    else:
                        break
                if harvests:
                    last_h = max(harvests)
                    var_map.append({
                        "crop_idx": c_idx,
                        "day": d,
                        "harvests": harvests,
                        "occupy_days": list(range(d, last_h)),
                        "cost": c["cost"],
                        "rev": len(harvests) * c["nq_sale"],
                        "profit": len(harvests) * c["nq_sale"] - c["cost"],
                        "biome": c["biome"],
                    })

    n_vars = len(var_map)
    c_obj = np.array([-v["profit"] for v in var_map])

    A_rows = []
    lb_list = []
    ub_list = []

    # 1. Daily plot capacity
    for d in active_days:
        for b_name, b_cap in [("farm", farm_cap), ("waterside", water_cap), ("cave", cave_cap)]:
            row = [0.0] * n_vars
            has_b = False
            for i, v in enumerate(var_map):
                if v["biome"] == b_name and d in v["occupy_days"]:
                    row[i] = 1.0
                    has_b = True
            if has_b:
                A_rows.append(row)
                lb_list.append(0.0)
                ub_list.append(float(b_cap))

    # 2. Cumulative cash flow constraints
    for t in active_days:
        row = [0.0] * n_vars
        for i, v in enumerate(var_map):
            if v["day"] <= t:
                row[i] += v["cost"]
            for h in v["harvests"]:
                if h + 1 <= t:
                    row[i] -= c["nq_sale"]
        A_rows.append(row)
        lb_list.append(-np.inf)
        ub_list.append(float(wallet_gold))

    # 3. 10-day restock inventory constraints
    windows = [(1, 10), (11, 20), (21, 30)]
    for w_start, w_end in windows:
        if w_end < current_day:
            continue
        is_current_window = (w_start <= current_day <= w_end)
        for c_idx, c in enumerate(crops):
            cap = c["stock"] if is_current_window else c["vendor_stock"]
            row = [0.0] * n_vars
            has_relevant = False
            for i, v in enumerate(var_map):
                if v["crop_idx"] == c_idx and w_start <= v["day"] <= w_end:
                    row[i] = 1.0
                    has_relevant = True
            if has_relevant:
                A_rows.append(row)
                lb_list.append(0.0)
                ub_list.append(float(cap))

    A = np.array(A_rows)
    constraints = LinearConstraint(A, lb_list, ub_list)
    integrality = np.ones(n_vars)
    bounds = Bounds(0, np.inf)

    res = milp(
        c=c_obj,
        integrality=integrality,
        bounds=bounds,
        constraints=constraints,
        options={"disp": False, "mip_rel_gap": 0.015, "time_limit": 8},
    )

    profit = -res.fun if res.x is not None else 0
    print(f"[{season.upper()}] Variables: {n_vars} | Status: {res.status} ({res.message}) | Total Profit: +{profit:,.0f} G", flush=True)
    return res


class TestDayByDayOptimization(unittest.TestCase):
    def test_spring_optimization(self):
        res = run_season("spring")
        self.assertIsNotNone(res)
        self.assertIn(res.status, [0, 1])

    def test_summer_optimization(self):
        res = run_season("summer")
        self.assertIsNotNone(res)
        self.assertIn(res.status, [0, 1])

    def test_fall_optimization(self):
        res = run_season("fall")
        self.assertIsNotNone(res)
        self.assertIn(res.status, [0, 1])

    def test_winter_optimization(self):
        res = run_season("winter")
        self.assertIsNotNone(res)
        self.assertIn(res.status, [0, 1])


if __name__ == "__main__":
    unittest.main()
