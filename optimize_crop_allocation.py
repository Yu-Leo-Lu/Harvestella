"""Harvestella Crop Allocation Optimizer & Report Generator.

Orchestrates linear programming optimization via scripts.crop_solver and formats
actionable day-by-day gameplay schedules for terminal and GitHub-Flavored Markdown.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import yaml

from scripts.crop_solver import (
    CropCandidate,
    DailyHarvestEvent,
    DailyPlantEvent,
    DailyRecord,
    OptimizationResult,
    solve_allocation,
)

__all__ = [
    "CropCandidate",
    "DailyHarvestEvent",
    "DailyPlantEvent",
    "DailyRecord",
    "OptimizationResult",
    "generate_markdown_report",
    "main",
    "print_result_report",
    "roll_config_to_day",
    "solve_allocation",
]


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
    for b_name, b_usable, b_phys in [
        ("Farm", result.base_farm, result.farm_physical or result.base_farm),
        ("Waterside", result.base_water, result.water_physical or result.base_water),
        ("Cave", result.base_cave, result.cave_physical or result.base_cave),
    ]:
        if b_phys > 0:
            cap_strs.append(f"{b_name} {b_usable}/{b_phys}")
        else:
            cap_strs.append(f"{b_name} 0")
    print(f" Plot Capacities : {' | '.join(cap_strs)}")
    if result.occupied_crops:
        print(" Pre-planted Crops in Field:")
        for occ in result.occupied_crops:
            h_str = ", ".join(f"D{h}" for h in occ.harvest_days) if occ.harvest_days else "No harvest before Quietus"
            rev = occ.count * len(occ.harvest_days) * occ.crop.nq_sale
            reg_info = "regrowth" if occ.crop.is_regrowth else "soil freed"
            h_label = f"Harvests: {h_str}" if len(occ.harvest_days) > 1 else f"Harvest {h_str}"
            print(f"   * {occ.count}x {occ.crop.name} ({occ.crop.biome.capitalize()}) -- Planted D{occ.plant_day} -> {h_label} (+{rev:,.0f} G, {reg_info})")
    print("-" * 86)

    if not result.success:
        print(f" [!] ERROR: {result.status_message}\n")
        return

    if not result.daily_records:
        print(f" [i] {result.status_message}\n")
        return

    print(" OPTIMAL DAILY ACTION PLAN (Day-to-Day Time-Indexed Compounding Model)")
    print("-" * 86)
    for rec in result.daily_records:
        payout_info = f" | Payout Arrived: +{rec.payout_revenue:,.0f} G" if rec.payout_revenue > 0 else ""
        print(f" [Day {rec.day}] Morning Wallet: {rec.morning_wallet:,.0f} G{payout_info}")
        if rec.harvests:
            harvest_groups: dict[tuple[str, str], list[DailyHarvestEvent]] = {}
            for h in rec.harvests:
                harvest_groups.setdefault((h.crop.name, h.crop.biome), []).append(h)
            h_lines = []
            for (c_name, b_name), h_list in harvest_groups.items():
                tot_qty = sum(x.quantity for x in h_list)
                tot_rev = sum(x.revenue for x in h_list)
                sample_h = h_list[0]
                r_tag = f" (Regrowth {sample_h.harvest_num}/{sample_h.total_harvests})" if sample_h.is_regrowth else " (Single harvest, soil freed)"
                h_lines.append(f"{tot_qty}x {c_name} ({b_name.capitalize()}){r_tag} -> +{tot_rev:,.0f} G")
            print(f"   Harvest & Ship: {'; '.join(h_lines)}")

        if rec.plantings:
            print(f"   {'Biome':<10} {'Crop Name':<18} {'Vendor':<10} {'Qty':>4} {'Seed Spent':>11} {'Harvest Days':<15} {'Net Profit':>11}")
            print("   " + "-" * 82)
            for it in rec.plantings:
                c = it.crop
                if len(it.harvest_days) == 1:
                    h_str = f"D{it.harvest_days[0]}"
                elif len(it.harvest_days) > 3:
                    h_str = f"D{it.harvest_days[0]}..D{it.harvest_days[-1]} ({len(it.harvest_days)}x)"
                else:
                    h_str = ", ".join(f"D{d}" for d in it.harvest_days)
                print(
                    f"   {c.biome.capitalize():<10} {c.name:<18} {c.town:<10} {it.quantity:>4} "
                    f"{it.cost:>10,.0f} G {h_str:<15} +{it.net_profit:>10,.0f} G"
                )
            print(f"   Spent Today: {rec.daily_spent:,.0f} G | End-of-Day Wallet: {rec.end_wallet:,.0f} G\n")
        else:
            print(f"   (No plantings scheduled) | End-of-Day Wallet: {rec.end_wallet:,.0f} G\n")

    carryover = result.daily_records[-1].end_wallet if result.daily_records else result.wallet_gold
    if result.quietus_payout > 0:
        print(f" [Day 31 - Quietus Morning] Morning Wallet: {result.final_wallet_gold:,.0f} G ({carryover:,.0f} G carryover + {result.quietus_payout:,.0f} G payout)\n")
    else:
        print(f" [Day 31 - Quietus Morning] Morning Wallet: {result.final_wallet_gold:,.0f} G\n")

    active_days = max(1, 31 - result.current_day)
    avg_daily_profit = result.total_season_profit / active_days
    timeline_str = f"Days {result.current_day}-30" if result.current_day < 30 else f"Day {result.current_day}"
    day_plural = "days" if active_days > 1 else "day"

    print("-" * 86)
    print(f" SEASON FINANCIAL SUMMARY ({timeline_str})")
    print("-" * 86)
    print(f" Starting Wallet (Day {result.current_day:<2}) : {result.wallet_gold:>12,.0f} G")
    print(f" Ending Wallet (Day 31)   : {result.final_wallet_gold:>12,.0f} G")
    if result.preexisting_revenue > 0:
        print(f" Pre-planted Crop Sales   : +{result.preexisting_revenue:>11,.0f} G")
        print(f" New Planting Net Profit  : +{result.new_planting_profit:>11,.0f} G")
    print(f" Net Profit ({active_days} {day_plural})      : +{result.total_season_profit:>11,.0f} G")
    print(f" Average Daily Profit     : +{avg_daily_profit:>11,.0f} G/day (over {active_days} active {day_plural})")
    if result.wallet_gold > 0:
        growth_mult = result.final_wallet_gold / result.wallet_gold
        pct_return = (result.total_season_profit / result.wallet_gold) * 100
        print(f" Capital Growth           : {growth_mult:>12.2f}x (+{pct_return:,.1f}%)")
    print("=" * 86 + "\n")


def generate_markdown_report(
    results: list[OptimizationResult],
    output_path: Path = Path("crop_allocation_report.md"),
) -> Path:
    """Generate a structured GitHub-Flavored Markdown report mirroring the terminal report."""
    valid = [r for r in results if r.success and r.daily_records]
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
        for b_name, b_usable, b_phys in [
            ("Farm", r.base_farm, r.farm_physical or r.base_farm),
            ("Waterside", r.base_water, r.water_physical or r.base_water),
            ("Cave", r.base_cave, r.cave_physical or r.base_cave),
        ]:
            if b_phys > 0:
                cap_strs.append(f"{b_name}: {b_usable}/{b_phys}")
        lines.append(f"- **Plot Capacities (Usable / Max)**: {' | '.join(cap_strs)}\n")
        if r.occupied_crops:
            lines.append("### 🌾 Pre-Planted Crop Field Status\n")
            lines.append("| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |")
            lines.append("| :--- | :--- | :---: | :---: | :--- | :--- | :---: |")
            for occ in r.occupied_crops:
                h_str = ", ".join(f"D{h}" for h in occ.harvest_days) if occ.harvest_days else "None"
                rev = occ.count * len(occ.harvest_days) * occ.crop.nq_sale
                if occ.crop.is_regrowth:
                    first_h = occ.plant_day + occ.crop.mature
                    lifetime_harvests = [first_h + k * occ.crop.regrowth for k in range(occ.crop.max_harvests)]
                    last_h = lifetime_harvests[-1] if lifetime_harvests else 30
                    if last_h <= 30:
                        soil_status = f"Freed D{last_h}"
                    else:
                        soil_status = "Stays Planted"
                else:
                    soil_status = f"Freed D{occ.harvest_days[0]}" if occ.harvest_days else "Stays Planted"
                lines.append(
                    f"| {occ.crop.biome.capitalize()} | **{occ.crop.name}** | {occ.count} | "
                    f"Day {occ.plant_day} | {h_str} | {soil_status} | +{rev:,.0f} G |"
                )
            lines.append("")

        lines.append("### Optimal Daily Action Plan (Day-by-Day Timeline)\n")
        for rec in r.daily_records:
            lines.append(f"#### **Day {rec.day}**\n")
            if rec.payout_revenue > 0:
                lines.append(f"- **Morning Wallet**: **{rec.morning_wallet:,.0f} G** *({rec.carryover_cash:,.0f} G carryover + {rec.payout_revenue:,.0f} G payout)*")
            else:
                lines.append(f"- **Morning Wallet**: **{rec.morning_wallet:,.0f} G**")

            if rec.harvests:
                tot_harvest_rev = sum(h.revenue for h in rec.harvests)
                arr_day = rec.day + 1
                lines.append(f"- **Harvest & Ship** *(+{tot_harvest_rev:,.0f} G arriving D{arr_day})*:")

                harvest_groups: dict[tuple[str, str], list[DailyHarvestEvent]] = {}
                for h in rec.harvests:
                    harvest_groups.setdefault((h.crop.name, h.crop.biome), []).append(h)

                biome_order = {"farm": 1, "waterside": 2, "cave": 3}
                sorted_groups = sorted(
                    harvest_groups.items(),
                    key=lambda item: (biome_order.get(item[0][1], 99), item[0][0])
                )

                for (c_name, b_name), h_list in sorted_groups:
                    tot_qty = sum(x.quantity for x in h_list)
                    tot_rev = sum(x.revenue for x in h_list)
                    sample_h = h_list[0]
                    if sample_h.is_regrowth:
                        status = f"regrowth {sample_h.harvest_num}/{sample_h.total_harvests}"
                    else:
                        status = "freed"
                    lines.append(
                        f"  - {tot_qty}x {c_name} *({b_name.capitalize()})* → +{tot_rev:,.0f} G ({status})"
                    )

            if rec.plantings:
                lines.append("\n##### 🌱 Seed Purchases & Planting\n")
                lines.append("| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |")
                lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
                for it in rec.plantings:
                    c = it.crop
                    if len(it.harvest_days) == 1:
                        h_str = f"D{it.harvest_days[0]}"
                    elif len(it.harvest_days) > 3:
                        h_str = f"D{it.harvest_days[0]}..D{it.harvest_days[-1]} ({len(it.harvest_days)}x)"
                    else:
                        h_str = ", ".join(f"D{d}" for d in it.harvest_days)
                    lines.append(
                        f"| {c.biome.capitalize()} | **{c.name}** | {c.town} | {it.quantity} | "
                        f"{it.cost:,.0f} G | {h_str} | +{it.net_profit:,.0f} G |"
                    )
                lines.append(
                    f"\n- **Daily Seed Spent**: {rec.daily_spent:,.0f} G | **End-of-Day Wallet**: **{rec.end_wallet:,.0f} G**"
                )
                slots_parts = []
                if r.base_farm > 0:
                    slots_parts.append(f"Farm: {rec.farm_slots_left}")
                if r.base_water > 0:
                    slots_parts.append(f"Waterside: {rec.water_slots_left}")
                if r.base_cave > 0:
                    slots_parts.append(f"Cave: {rec.cave_slots_left}")
                if slots_parts:
                    lines.append(f"- **Plots Left**: {' | '.join(slots_parts)}\n")
            else:
                lines.append("\n- *No seed purchases or planting scheduled today.*")
                lines.append(f"- **End-of-Day Wallet**: **{rec.end_wallet:,.0f} G**\n")

            lines.append("---\n")

        # Quietus Morning section
        lines.append("#### **Day 31 (Quietus Morning)**\n")
        carryover = r.daily_records[-1].end_wallet if r.daily_records else r.wallet_gold
        if r.quietus_payout > 0:
            lines.append(f"- **Morning Wallet**: **{r.final_wallet_gold:,.0f} G** *({carryover:,.0f} G carryover + {r.quietus_payout:,.0f} G payout)*")
        else:
            lines.append(f"- **Morning Wallet**: **{r.final_wallet_gold:,.0f} G**")
        lines.append("- ❄️ *Quietus has arrived. All unharvested field crops wither.*\n")
        lines.append("---\n")

        active_days = max(1, 31 - r.current_day)
        avg_daily_profit = r.total_season_profit / active_days
        active_days_label = f"Days {r.current_day}–30" if r.current_day < 30 else f"Day {r.current_day}"
        day_plural = "days" if active_days > 1 else "day"

        lines.append(f"### 🏆 Season Financial Summary ({active_days_label})\n")
        lines.append(f"- **Starting Wallet (Day {r.current_day})**: {r.wallet_gold:,.0f} G")
        lines.append(f"- **Ending Wallet (Day 31 Quietus)**: **{r.final_wallet_gold:,.0f} G**")
        if r.preexisting_revenue > 0:
            lines.append(f"- **Pre-planted Crop Sales**: **+{r.preexisting_revenue:,.0f} G**")
            lines.append(f"- **New Planting Net Profit**: **+{r.new_planting_profit:,.0f} G**")
        lines.append(f"- **Net Profit ({active_days} {day_plural})**: **+{r.total_season_profit:,.0f} G**")
        lines.append(f"- **Average Daily Profit**: **+{avg_daily_profit:,.0f} G/day** *(over {active_days} active {day_plural})*")
        if r.wallet_gold > 0:
            growth_mult = r.final_wallet_gold / r.wallet_gold
            pct_return = (r.total_season_profit / r.wallet_gold) * 100
            lines.append(f"- **Capital Growth**: **{growth_mult:.2f}x** *(+{pct_return:,.1f}% return on starting purse)*\n")
        else:
            lines.append("- **Capital Growth**: **N/A** *(Starting purse: 0 G)*\n")



    output_path = Path(output_path)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


# ==============================================================================
# Config Roll-Forward In-Place
# ==============================================================================

def roll_config_to_day(config_path: Path, target_day: int) -> None:
    """Fast-forward a seasonal config to the morning of target_day in-place."""
    config_path = Path(config_path)
    if not config_path.is_file():
        print(f"Error: Configuration file not found: {config_path}")
        return

    with open(config_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    season = str(cfg.get("season", config_path.stem)).strip().lower()
    res = solve_allocation(config_path, csv_dir=Path("seasons"))
    if not res.success:
        print(f"Cannot roll forward {config_path}: solver failed - {res.status_message}")
        return

    if target_day <= res.current_day:
        print(f"Error: target_day ({target_day}) must be greater than current_day ({res.current_day}).")
        return
    if target_day > 30:
        print(f"Error: target_day ({target_day}) cannot exceed Day 30 (Quietus).")
        return

    snapshot = res.get_day_snapshot(target_day)

    # Load crop catalog metadata to preserve Town groupings, biomes, and G/d annotations
    csv_path = Path("seasons") / f"{season}.csv"
    crop_meta: dict[tuple[str, str], dict[str, Any]] = {}
    name_town_map: dict[str, list[str]] = {}
    crop_biome_map: dict[str, str] = {}
    if csv_path.is_file():
        with open(csv_path, encoding="utf-8") as f_csv:
            for r in csv.DictReader(f_csv):
                c_name = r.get("Crop Name", "").strip()
                town = r.get("Vendor Town", "").strip()
                biome = r.get("Biome", "").strip().lower()
                profit_str = r.get("Daily NQ Profit (G/d)", "").strip()
                cost_str = r.get("Seed Cost (G)", "").strip()
                if not c_name or not town or not cost_str or not profit_str:
                    continue
                try:
                    profit_val = float(profit_str)
                    cost_val = float(cost_str)
                except ValueError:
                    continue
                if cost_val <= 0:
                    continue
                crop_meta[(c_name, town)] = {
                    "name": c_name,
                    "town": town,
                    "biome": biome,
                    "profit": profit_val,
                }
                name_town_map.setdefault(c_name, []).append(town)
                crop_biome_map[c_name.lower()] = biome

    # Format output YAML cleanly
    season_title = season.capitalize()
    lines = [
        "# ==============================================================================",
        f"# Harvestella Planting Optimizer Configuration: {season_title}",
        "# ==============================================================================",
        "",
        f"current_day: {snapshot['current_day']}",
        f"wallet_gold: {snapshot['wallet_gold']}",
    ]

    max_vars = cfg.get("max_crop_varieties", None)
    if max_vars is not None:
        lines.append(f"max_crop_varieties: {max_vars} # Optional limit on distinct seed varieties")
    else:
        lines.append("max_crop_varieties: null # Optional limit on distinct seed varieties (e.g. 2, 3, or null for unlimited)")

    lines.extend([
        "",
        "# ------------------------------------------------------------------------------",
        "# 1. Farm & Biome Plot Capacities",
        "# Usable plots = Physical plots (farm_level * 49) - Reserved plots",
        "# ------------------------------------------------------------------------------",
    ])

    if "farm_level" in cfg:
        lines.append(f"farm_level: {cfg.get('farm_level', 1)}         # Renovator level (each level adds 49 plots)")
    elif "farm_plots" in cfg:
        lines.append(f"farm_plots: {cfg.get('farm_plots', 49)}")
    lines.append(f"waterside_plots: {cfg.get('waterside_plots', 81)}   # Biome capacity (default: 81)")
    lines.append(f"cave_plots: {cfg.get('cave_plots', 81)}        # Biome capacity (default: 81)")
    lines.append("")
    lines.append("# Reserved plots excluded from optimizer (fruit trees, quest crops, makers)")
    lines.append("reserve_plots:")
    res_plots = cfg.get("reserve_plots", {})
    if isinstance(res_plots, dict):
        lines.append(f"  farm: {res_plots.get('farm', 0)}")
        lines.append(f"  waterside: {res_plots.get('waterside', 0)}")
        lines.append(f"  cave: {res_plots.get('cave', 0)}")
    else:
        lines.append(f"  farm: {int(res_plots) if res_plots else 0}")
        lines.append("  waterside: 0")
        lines.append("  cave: 0")

    lines.extend([
        "",
        "# ------------------------------------------------------------------------------",
        "# 2. Currently Planted on Farm (Active Batches)",
        "# ------------------------------------------------------------------------------",
        "planted:",
    ])

    planted_items = snapshot.get("planted", [])
    if planted_items:
        biome_groups = [
            [p for p in planted_items if crop_biome_map.get(p["crop"].lower(), "farm") == "farm"],
            [p for p in planted_items if crop_biome_map.get(p["crop"].lower(), "farm") == "waterside"],
            [p for p in planted_items if crop_biome_map.get(p["crop"].lower(), "farm") == "cave"],
        ]
        has_group = False
        for group in biome_groups:
            if not group:
                continue
            if has_group:
                lines.append("")
            for p in group:
                lines.append(f"  - {{ crop: {p['crop']}, day: {p['day']}, count: {p['count']} }}")
            has_group = True
    else:
        lines.append("  # - { crop: Morrocorn, day: 1, count: 10 }")

    lines.extend([
        "",
        "# ------------------------------------------------------------------------------",
        "# 3. Store Seed Inventory (Remaining Vendor Stock)",
        "# ------------------------------------------------------------------------------",
        "seed_stock:",
    ])

    town_order = ["Lethe", "Nemea", "Shatolla", "Argene", "Abandoned Eden"]
    all_towns: list[str] = []
    for t in town_order:
        if any(meta["town"] == t for meta in crop_meta.values()):
            all_towns.append(t)
    for meta in crop_meta.values():
        if meta["town"] not in all_towns:
            all_towns.append(meta["town"])

    stock_items = snapshot.get("seed_stock", {})

    for idx, town in enumerate(all_towns):
        town_crops = [meta for meta in crop_meta.values() if meta["town"] == town]
        if not town_crops:
            continue
        town_crops.sort(key=lambda m: m["profit"], reverse=True)

        if idx > 0:
            lines.append("")
        lines.append(f"  # {town}")

        for meta in town_crops:
            c_name = meta["name"]
            is_multi = len(name_town_map.get(c_name, [])) > 1
            std_key = f"{c_name} ({town})" if is_multi else c_name

            stock_val = None
            if std_key in stock_items:
                stock_val = stock_items[std_key]
            elif f"{c_name} Seeds" in stock_items:
                std_key = f"{c_name} Seeds"
                stock_val = stock_items[std_key]
            elif c_name in stock_items:
                stock_val = stock_items[c_name]
            else:
                stock_val = 99

            biome_tag = ""
            if meta["biome"] == "cave":
                biome_tag = " (Cave)"
            elif meta["biome"] == "waterside":
                biome_tag = " (Waterside)"

            key_col = f"{std_key}:"
            lines.append(f"  {key_col:<24} {stock_val:<2} # +{meta['profit']:.1f} G/d{biome_tag}")

    lines.extend([
        "",
        "# ------------------------------------------------------------------------------",
        "# 4. Town Story Progression (set to false if vendor is not yet unlocked)",
        "# ------------------------------------------------------------------------------",
        "unlocked_towns:",
    ])

    unlocked = cfg.get("unlocked_towns", {})
    if isinstance(unlocked, dict):
        for town, status in unlocked.items():
            lines.append(f"  {town}: {'true' if status else 'false'}")
    else:
        lines.append("  Lethe: true")
        lines.append("  Nemea: true")
        lines.append("  Shatolla: true")
        lines.append("  Argene: true")
        lines.append("  Abandoned Eden: false")

    lines.append("")

    config_path.write_text("\n".join(lines), encoding="utf-8")

    season_flag = f"-{season[:2]}"
    print("=" * 86)
    print(f" [+] Fast-forwarded {config_path.as_posix()} to Day {target_day} in-place")
    print("=" * 86)
    print(f"  * Current Day   : Day {target_day}")
    print(f"  * Morning Wallet: {snapshot['wallet_gold']:,} G")
    print(f"  * Active Batches: {len(planted_items)} batches in ground")
    print(f"  * Store Stocks  : Refreshed for Cycle (Days {snapshot['current_day']}-30)")
    print("-" * 86)
    print(f" Review/tweak {config_path.as_posix()} in your editor, then solve via:")
    print(f"   python optimize_crop_allocation.py {season_flag}\n")


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
    parser.add_argument("-r", "--roll-to", type=int, metavar="DAY", help="Fast-forward season config to morning of DAY in-place")
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

    # If -r/--roll-to is specified, require exactly one season to roll forward
    if args.roll_to is not None:
        if not selected or len(selected) > 1:
            print("Please specify a single season flag to roll forward (e.g. -su -r 22 or -sp -r 15).")
            return
        target_season = selected[0]
        cfg_p = configs_dir / f"{target_season}.yaml"
        roll_config_to_day(cfg_p, args.roll_to)
        return

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
