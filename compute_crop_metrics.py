"""Compute financial metrics for Harvestella seasonal crops.

Loads seasonal CSV files from the `seasons/` directory and computes:
1. True Cash Compounded Rate (%/day)
2. Daily NQ Profit
3. Latest Start Date (to achieve maximum harvests within a 30-day season)
"""

import argparse
import csv
import math
import re
from pathlib import Path
from typing import Any

SEASON_LENGTH_DAYS = 30


def clean_currency(val: str) -> float | None:
    """Parse strings like '200 G', '1,000 G', or '30' into float. Returns None for '—'."""
    if not val or val.strip() in ("—", "-", ""):
        return None
    cleaned = re.sub(r"[^\d.]", "", val)
    return float(cleaned) if cleaned else None


def parse_growth(row: dict[str, str]) -> tuple[int, int | None, int | None, bool]:
    """Parse growth parameters: Mature Days, Regrowth, Max Harvests.

    Returns (mature_days, regrowth_days, max_harvests, is_repeat).
    """
    mature_val = row.get("Mature Days") or row.get("Harvest Cycle", "")
    regrowth_val = row.get("Regrowth", "")
    max_harvests_val = row.get("Max Harvests", "")

    # Mature days
    match_m = re.search(r"(\d+)", mature_val)
    mature_days = int(match_m.group(1)) if match_m else 1

    # Regrowth
    regrowth_days = None
    is_repeat = False
    if regrowth_val and regrowth_val.strip() not in ("—", "-", "", "N/A"):
        match_r = re.search(r"(\d+)", regrowth_val)
        if match_r:
            regrowth_days = int(match_r.group(1))
            is_repeat = True
    elif "repeat" in mature_val.lower():
        is_repeat = True
        regrowth_days = mature_days

    # Max harvests
    max_harvests = None
    if max_harvests_val and max_harvests_val.strip() not in ("—", "-", "", "N/A"):
        match_h = re.search(r"(\d+)", max_harvests_val)
        if match_h:
            max_harvests = int(match_h.group(1))
    if not is_repeat:
        max_harvests = 1

    return mature_days, regrowth_days, max_harvests, is_repeat


def compute_crop_row(row: dict[str, str]) -> dict[str, Any]:
    """Calculate the financial and scheduling metrics for a crop entry."""
    crop_name = row.get("Crop Name", "").strip()
    seed_cost_str = row.get("Seed Cost", "")
    basic_sell_str = row.get("NQ Sale", "")
    biome_str = row.get("Biome", "")
    growth_season = row.get("Growth Season", "")

    seed_cost = clean_currency(seed_cost_str)
    basic_sell = clean_currency(basic_sell_str)
    mature_days, regrowth_days, max_harvests, is_repeat = parse_growth(row)

    is_all_year = all(s in growth_season.lower() for s in ["spring", "summer", "fall", "winter"])
    is_tree = "tree" in biome_str.lower() or is_all_year or "sapling" in crop_name.lower() or crop_name in [
        "Grouply Grape",
        "Princess Chestnut",
        "SnowCap Mikan",
        "Lococonut",
        "Wisty Peach",
        "Numblemon",
        "Macocoa",
        "Promised Fruit",
        "Moonfruit",
    ]

    # Special handling for Trees (Multi-Season investments)
    if is_tree:
        return {
            "Daily NQ Profit": "Multi-Season (Tree)",
            "Cash Compound Rate": "Tree",
            "Production Days": "Tree",
            "Latest Plant Day": "Day 1 (All Year)",
        }

    # Handling for drops / foraged crops with no purchase cost (e.g. Nitro Pineapple)
    if seed_cost is None or seed_cost <= 0:
        if basic_sell is not None:
            profit_per_cycle = basic_sell
            daily_profit = profit_per_cycle / mature_days if mature_days > 0 else 0.0
            latest_start_day = max(1, SEASON_LENGTH_DAYS - mature_days)
            days_unit = "day" if mature_days == 1 else "days"
            return {
                "Daily NQ Profit": f"+{daily_profit:.1f} G/d",
                "Cash Compound Rate": "Free Drop",
                "Production Days": f"{mature_days} {days_unit}",
                "Latest Plant Day": f"Day {latest_start_day}",
            }
        return {
            "Daily NQ Profit": "N/A",
            "Cash Compound Rate": "N/A",
            "Production Days": "N/A",
            "Latest Plant Day": "N/A",
        }

    if is_repeat and regrowth_days:
        # Repeat crop: 1st harvest at mature_days, subsequent harvests every regrowth_days
        if mature_days <= SEASON_LENGTH_DAYS:
            possible_in_season = 1 + (SEASON_LENGTH_DAYS - mature_days) // regrowth_days
        else:
            possible_in_season = 0
        harvest_count = min(max_harvests, possible_in_season) if max_harvests else possible_in_season
        required_growth_days = mature_days + (harvest_count - 1) * regrowth_days if harvest_count > 0 else mature_days
        total_revenue = harvest_count * basic_sell
        net_profit = total_revenue - seed_cost
        daily_profit = net_profit / required_growth_days if required_growth_days > 0 else 0.0
        turnaround_days = mature_days + 1
    else:
        # Single crop: buy seed and sell every cycle
        harvest_count = SEASON_LENGTH_DAYS // mature_days
        required_growth_days = harvest_count * mature_days
        profit_per_cycle = basic_sell - seed_cost
        daily_profit = profit_per_cycle / mature_days
        turnaround_days = mature_days + 1

    # Latest Plant Day before Quietus (Day 30):
    # - Repeat crops: latest day to achieve full multi-harvest run
    # - Single crops: latest day to plant and achieve a harvest before Quietus
    if is_repeat:
        latest_start_day = max(1, SEASON_LENGTH_DAYS - required_growth_days)
    else:
        latest_start_day = max(1, SEASON_LENGTH_DAYS - mature_days)
    latest_start_date_str = f"Day {latest_start_day}"

    # Cash Compound Rate (%/day)
    # Accounting for shipping delay (Growth + 1 day cash turnaround)
    multiplier = basic_sell / seed_cost

    if not is_repeat:
        # Single crop: wallet compounding velocity per replant cycle
        if multiplier > 0:
            daily_rate = (math.pow(multiplier, 1.0 / turnaround_days) - 1.0) * 100.0
            compounded_rate_str = f"+{daily_rate:.2f}%" if daily_rate >= 0 else f"{daily_rate:.2f}%"
        else:
            compounded_rate_str = "0.00%"
    else:
        # Repeat crop: realized cash velocity across full production run
        total_revenue = harvest_count * basic_sell
        wealth_ratio = total_revenue / seed_cost
        realization_days = required_growth_days + 1
        if wealth_ratio > 0:
            daily_rate = (math.pow(wealth_ratio, 1.0 / realization_days) - 1.0) * 100.0
            compounded_rate_str = f"+{daily_rate:.2f}%" if daily_rate >= 0 else f"{daily_rate:.2f}%"
        else:
            compounded_rate_str = "Neg."

    # Production Days (Total active growth days)
    active_days = required_growth_days if is_repeat else mature_days
    days_unit = "day" if active_days == 1 else "days"
    production_days_str = f"{active_days} {days_unit}"

    # Format daily profit string with sign and G/d
    daily_profit_sign = "+" if daily_profit > 0 else ""
    daily_profit_str = f"{daily_profit_sign}{daily_profit:,.1f} G/d"

    return {
        "Daily NQ Profit": daily_profit_str,
        "Cash Compound Rate": compounded_rate_str,
        "Production Days": production_days_str,
        "Latest Plant Day": latest_start_date_str,
    }


def parse_numeric_metric(val: Any) -> float:
    """Parse percentage or profit string into float for sorting. Returns -inf for non-numeric (e.g. Tree, N/A)."""
    if val is None:
        return -float("inf")
    s = str(val).strip()
    if s.lower() in ("tree", "n/a", "neg.", "") or "multi-season" in s.lower():
        return -float("inf")
    cleaned = re.sub(r"[^\d.-]", "", s)
    try:
        return float(cleaned)
    except ValueError:
        return -float("inf")


def analyze_csv_file(csv_path: Path, save_enriched: bool = False, output_path: Path | None = None) -> list[dict[str, Any]]:
    """Load a seasonal CSV, compute metrics, print table, and optionally save."""
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)
        if not reader.fieldnames:
            raise ValueError(f"No headers found in {csv_path}")
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    new_cols = [
        "Daily NQ Profit",
        "Cash Compound Rate",
        "Production Days",
        "Latest Plant Day",
    ]

    legacy_and_new_cols = {
        "Full Season Net Profit (Basic)",
        "True Cash Compounded Rate (%/day)",
        "Latest Start Date (Full Season)",
        "Daily Net Profit (Basic)",
        "Daily Profit (Basic)",
        "Daily Profit",
        "Daily NQ Profit",
        "Full Net Profit (Basic)",
        "Cash Compound Rate",
        "Production Days",
        "Capital Days",
        "Latest Plant Day",
        "Harvest Cycle",
    }

    out_fieldnames = [col for col in fieldnames if col not in legacy_and_new_cols] + new_cols
    enriched_rows = []

    for row in rows:
        computed = compute_crop_row(row)
        clean_row = {k: v for k, v in row.items() if k not in legacy_and_new_cols}
        clean_row.update(computed)
        enriched_rows.append(clean_row)

    # Sort by Cash Compound Rate descending, then Daily NQ Profit descending
    enriched_rows.sort(
        key=lambda r: (
            parse_numeric_metric(r.get("Cash Compound Rate")),
            parse_numeric_metric(r.get("Daily NQ Profit")),
        ),
        reverse=True,
    )

    # Print summary table to console
    print(f"\n{'='*144}")
    print(f" Seasonal Analysis: {csv_path.name.upper()} (30-Day Season)")
    print(f"{'='*144}")
    header_fmt = "{:<18} | {:<12} | {:<9} | {:<7} | {:<7} | {:<7} | {:<19} | {:<18} | {:<15} | {:<16}"
    print(
        header_fmt.format(
            "Crop Name",
            "Town",
            "Seed Cost",
            "Mature",
            "Regrow",
            "Max H.",
            "Daily NQ Profit",
            "Cash Compound Rate",
            "Production Days",
            "Latest Plant Day",
        )
    )
    print("-" * 144)

    for r in enriched_rows:
        regrow_display = r.get("Regrowth", "-")
        if regrow_display in ("—", "", None):
            regrow_display = "-"
        max_h_display = r.get("Max Harvests", "1")
        if max_h_display in ("—", "", None):
            max_h_display = "1"
        elif "multi" in max_h_display.lower():
            max_h_display = "Tree"

        seed_cost_display = r.get("Seed Cost", "-")
        if seed_cost_display in ("—", "", None):
            seed_cost_display = "-"

        print(
            header_fmt.format(
                r.get("Crop Name", "")[:18],
                r.get("Vendor Town", "")[:12],
                seed_cost_display[:9],
                (r.get("Mature Days") or r.get("Harvest Cycle", ""))[:7],
                regrow_display[:7],
                max_h_display[:7],
                r.get("Daily NQ Profit", "")[:19],
                r.get("Cash Compound Rate", "")[:18],
                r.get("Production Days", "")[:15],
                r.get("Latest Plant Day", "")[:16],
            )
        )
    print(f"{'='*144}\n")

    if save_enriched:
        dest_path = output_path or csv_path
        with open(dest_path, mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=out_fieldnames)
            writer.writeheader()
            writer.writerows(enriched_rows)
        print(f"Saved enriched CSV with computed metrics to: {dest_path}")

    return enriched_rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute Harvestella crop seasonal profit, compounded cash rate, and latest start date."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default=None,
        help="Path or name of CSV in seasons/ (e.g., seasons/spring.csv or 'spring').",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Process all CSV files in seasons/ directory.",
    )
    parser.add_argument(
        "-s",
        "--save",
        action="store_true",
        help="Save calculated metrics back to the CSV file(s).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Custom output file path (only used when single input is provided).",
    )

    args = parser.parse_args()
    seasons_dir = Path("seasons")

    if args.all:
        if not seasons_dir.exists():
            print(f"Error: Directory '{seasons_dir}' does not exist.")
            return
        files = sorted(seasons_dir.glob("*.csv"))
        if not files:
            print(f"No CSV files found in {seasons_dir}.")
            return
        for f in files:
            analyze_csv_file(f, save_enriched=args.save)
    else:
        # Determine target file
        target_file: Path
        if args.input:
            p = Path(args.input)
            if p.exists():
                target_file = p
            elif (seasons_dir / p.name).exists():
                target_file = seasons_dir / p.name
            elif (seasons_dir / f"{p.name}.csv").exists():
                target_file = seasons_dir / f"{p.name}.csv"
            else:
                print(f"Error: Cannot find CSV file matching '{args.input}'.")
                return
        else:
            # Default to spring.csv if present, else first CSV in seasons/
            default_spring = seasons_dir / "spring.csv"
            if default_spring.exists():
                target_file = default_spring
            else:
                csvs = list(seasons_dir.glob("*.csv"))
                if not csvs:
                    print("No CSV files found in seasons/ directory.")
                    return
                target_file = csvs[0]

        analyze_csv_file(target_file, save_enriched=args.save, output_path=args.output)


if __name__ == "__main__":
    main()
