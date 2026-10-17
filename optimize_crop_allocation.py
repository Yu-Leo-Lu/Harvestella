"""Harvestella Crop Allocation Optimizer & Report Generator.

Orchestrates linear programming optimization via scripts.crop_solver and formats
actionable day-by-day gameplay schedules for terminal and GitHub-Flavored Markdown.
"""

from __future__ import annotations

import argparse
from pathlib import Path

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
    for b_name, b_init, b_cap in [("Farm", result.farm_init, result.farm_cap), ("Waterside", result.water_init, result.water_cap), ("Cave", result.cave_init, result.cave_cap)]:
        if b_cap > 0:
            if b_init == b_cap:
                cap_strs.append(f"{b_name} {b_cap}")
            else:
                cap_strs.append(f"{b_name} {b_init} -> {b_cap}")
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

    if result.quietus_payout > 0:
        q_src = f" ({', '.join(result.quietus_sources)})" if result.quietus_sources else ""
        print(f" [Day 31 - Quietus Morning] Final Payout Arrived: +{result.quietus_payout:,.0f} G{q_src} | Final Wallet: {result.final_wallet_gold:,.0f} G\n")

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
    if result.preexisting_revenue > 0:
        print(f" Pre-planted Crop Sales: +{result.preexisting_revenue:>8,.0f} G")
        print(f" New Planting Net Profit: +{result.new_planting_profit:>8,.0f} G")
    print(f" Total Season Net Profit: +{result.total_season_profit:>8,.0f} G across all restock stages")
    print(f" Final Projected Wallet : {result.final_wallet_gold:>8,.0f} G on Day 30 (Quietus)")
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
        for b_name, b_init, b_cap in [("Farm", r.farm_init, r.farm_cap), ("Waterside", r.water_init, r.water_cap), ("Cave", r.cave_init, r.cave_cap)]:
            if b_cap > 0:
                if b_init == b_cap:
                    cap_strs.append(f"{b_name} {b_cap}")
                else:
                    cap_strs.append(f"{b_name} {b_init} -> {b_cap}")
            else:
                cap_strs.append(f"{b_name} 0")
        lines.append(f"- **Plot Capacities**: {' | '.join(cap_strs)}\n")
        if r.occupied_crops:
            lines.append("### 🌾 Pre-Planted Crop Field Status\n")
            lines.append("| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |")
            lines.append("| :--- | :--- | :---: | :---: | :--- | :--- | :---: |")
            for occ in r.occupied_crops:
                h_str = ", ".join(f"D{h}" for h in occ.harvest_days) if occ.harvest_days else "None"
                rev = occ.count * len(occ.harvest_days) * occ.crop.nq_sale
                if occ.crop.is_regrowth:
                    soil_status = "Stays Planted *(Regrowth)*"
                else:
                    soil_status = f"Freed D{occ.harvest_days[0]}" if occ.harvest_days else "Freed before Quietus"
                lines.append(
                    f"| {occ.crop.biome.capitalize()} | **{occ.crop.name}** | {occ.count} | "
                    f"Day {occ.plant_day} | {h_str} | {soil_status} | +{rev:,.0f} G |"
                )
            lines.append("")

        lines.append("### Optimal Daily Action Plan (Day-by-Day Timeline)\n")
        for rec in r.daily_records:
            lines.append(f"#### **Day {rec.day}**\n")
            if rec.payout_revenue > 0:
                src_str = ", ".join(rec.payout_sources) if rec.payout_sources else f"Day {rec.day - 1} shipping"
                lines.append(f"- 📬 **Payout**: **+{rec.payout_revenue:,.0f} G** *(from {src_str})*")
                lines.append(f"- **Morning Wallet**: **{rec.morning_wallet:,.0f} G** *({rec.carryover_cash:,.0f} G carryover + {rec.payout_revenue:,.0f} G)*")
            else:
                lines.append(f"- **Morning Wallet**: **{rec.morning_wallet:,.0f} G**")

            if rec.harvests:
                harvest_groups: dict[tuple[str, str], list[DailyHarvestEvent]] = {}
                for h in rec.harvests:
                    harvest_groups.setdefault((h.crop.name, h.crop.biome), []).append(h)

                if len(harvest_groups) == 1:
                    (c_name, b_name), h_list = next(iter(harvest_groups.items()))
                    tot_qty = sum(x.quantity for x in h_list)
                    tot_rev = sum(x.revenue for x in h_list)
                    sample_h = h_list[0]
                    arr_day = rec.day + 1
                    if sample_h.is_regrowth:
                        detail = f"regrowth {sample_h.harvest_num}/{sample_h.total_harvests} (stays planted)"
                    else:
                        detail = "single harvest (soil freed)"
                    lines.append(
                        f"- 🌾 **Harvest & Ship**: {tot_qty}x {c_name} *({b_name.capitalize()})* — {detail} → +{tot_rev:,.0f} G *(arrives morning D{arr_day})*"
                    )
                else:
                    lines.append("- 🌾 **Harvest & Ship**:")
                    for (c_name, b_name), h_list in harvest_groups.items():
                        tot_qty = sum(x.quantity for x in h_list)
                        tot_rev = sum(x.revenue for x in h_list)
                        sample_h = h_list[0]
                        arr_day = rec.day + 1
                        if sample_h.is_regrowth:
                            detail = f"regrowth {sample_h.harvest_num}/{sample_h.total_harvests} (stays planted)"
                        else:
                            detail = "single harvest (soil freed)"
                        lines.append(
                            f"  - {tot_qty}x {c_name} *({b_name.capitalize()})* — {detail} → +{tot_rev:,.0f} G *(arrives morning D{arr_day})*"
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
                    f"\n- **Daily Seed Spent**: {rec.daily_spent:,.0f} G | **End-of-Day Wallet**: **{rec.end_wallet:,.0f} G**\n"
                )
            else:
                lines.append("\n- *No seed purchases or planting scheduled today.*")
                lines.append(f"- **End-of-Day Wallet**: **{rec.end_wallet:,.0f} G**\n")

            lines.append("---\n")

        # Quietus Morning section
        lines.append("### ❄️ Quietus Morning (Day 31 Finale & Summary)\n")
        q_src_str = f"Day 30 final harvest: {', '.join(r.quietus_sources)}" if r.quietus_sources else "Day 30 final harvest"
        lines.append(f"- 📬 **Final Shipping Payout**: **+{r.quietus_payout:,.0f} G** *(from {q_src_str})*")
        lines.append(f"- **Starting Budget**: {r.wallet_gold:,.0f} G")
        lines.append(f"- **Total Season Net Profit**: **+{r.total_season_profit:,.0f} G**")
        lines.append(f"- 🏆 **Final Quietus Wallet**: **{r.final_wallet_gold:,.0f} G**\n")

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
        if r.preexisting_revenue > 0:
            lines.append(f"- **Pre-planted Crop Sales**: **+{r.preexisting_revenue:,.0f} G**")
            lines.append(f"- **New Planting Net Profit**: **+{r.new_planting_profit:,.0f} G**")
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
