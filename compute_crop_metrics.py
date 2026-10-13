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


def parse_cycle(val: str) -> tuple[int, bool]:
    """Parse cycle string like '4 days', '5 days/repeat', '1 day'.

    Returns (cycle_days, is_repeat).
    """
    is_repeat = "repeat" in val.lower()
    match = re.search(r"(\d+)", val)
    cycle_days = int(match.group(1)) if match else 1
    return cycle_days, is_repeat


def compute_crop_row(row: dict[str, str]) -> dict[str, Any]:
    """Calculate the financial and scheduling metrics for a crop entry."""
    crop_name = row.get("Crop Name", "").strip()
    seed_cost_str = row.get("Seed Cost", "")
    basic_sell_str = row.get("NQ Sale", "")
    cycle_str = row.get("Harvest Cycle", "")
    biome_str = row.get("Biome", "")
    growth_season = row.get("Growth Season", "")
    fruit_season = row.get("Fruit Season", "")

    seed_cost = clean_currency(seed_cost_str)
    basic_sell = clean_currency(basic_sell_str)
    cycle_days, is_repeat = parse_cycle(cycle_str)

    is_all_year = all(s in growth_season.lower() for s in ["spring", "summer", "fall", "winter"])
    is_tree = "tree" in biome_str.lower() or is_all_year or "sapling" in crop_name.lower() or seed_cost and seed_cost >= 2000 and "repeat" in cycle_str and crop_name in [
        "Grouply Grape",
        "Princess Chestnut",
        "SnowCap Mikan",
        "Lococonut",
        "Wisty Peach",
        "Numblemon",
    ]

    # Special handling for Trees (Multi-Season investments)
    if is_tree:
        return {
            "Daily NQ Profit": "Multi-Season (Tree)",
            "Cash Compound Rate": "Tree",
            "Capital Days": "Tree",
            "Latest Plant Day": "Day 1 (All Year)",
        }

    if seed_cost is None or basic_sell is None or seed_cost <= 0:
        return {
            "Daily NQ Profit": "N/A",
            "Cash Compound Rate": "N/A",
            "Capital Days": "N/A",
            "Latest Plant Day": "N/A",
        }

    # Number of harvests possible within a standard 30-day season
    harvest_count = SEASON_LENGTH_DAYS // cycle_days
    required_growth_days = harvest_count * cycle_days

    # Daily NQ Profit
    if is_repeat:
        # Repeat crop: buy seed once, harvest harvest_count times over full season
        total_revenue = harvest_count * basic_sell
        net_profit = total_revenue - seed_cost
        daily_profit = net_profit / required_growth_days if required_growth_days > 0 else 0.0
    else:
        # Single crop: buy seed and sell every cycle
        profit_per_cycle = basic_sell - seed_cost
        daily_profit = profit_per_cycle / cycle_days

    # Latest Plant Day to reach full season profit before Quietus (Day 30)
    latest_start_day = max(1, SEASON_LENGTH_DAYS - required_growth_days)
    latest_start_date_str = f"Day {latest_start_day}"

    # Cash Compound Rate (%/day)
    # Accounting for shipping delay (Growth + 1 day cash turnaround)
    turnaround_days = cycle_days + 1
    multiplier = basic_sell / seed_cost

    if not is_repeat:
        # Single crop: wallet compounding velocity per replant cycle
        if multiplier > 0:
            daily_rate = (math.pow(multiplier, 1.0 / turnaround_days) - 1.0) * 100.0
            compounded_rate_str = f"+{daily_rate:.2f}%" if daily_rate >= 0 else f"{daily_rate:.2f}%"
        else:
            compounded_rate_str = "0.00%"
    else:
        # Repeat crop: 30-day realized cash compounded velocity
        total_revenue = harvest_count * basic_sell
        wealth_ratio = total_revenue / seed_cost
        if wealth_ratio > 0:
            daily_rate = (math.pow(wealth_ratio, 1.0 / SEASON_LENGTH_DAYS) - 1.0) * 100.0
            compounded_rate_str = f"+{daily_rate:.2f}%" if daily_rate >= 0 else f"{daily_rate:.2f}%"
        else:
            compounded_rate_str = "Neg."

    # Capital Days (Seed Cost * Turnaround Days)
    capital_days = seed_cost * turnaround_days
    capital_days_str = f"{capital_days:,.0f} G*d"

    # Format daily profit string with sign and G/d
    daily_profit_sign = "+" if daily_profit > 0 else ""
    daily_profit_str = f"{daily_profit_sign}{daily_profit:,.1f} G/d"

    return {
        "Daily NQ Profit": daily_profit_str,
        "Cash Compound Rate": compounded_rate_str,
        "Capital Days": capital_days_str,
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
        "Capital Days",
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
        "Capital Days",
        "Latest Plant Day",
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
    print(f"\n{'='*134}")
    print(f" Seasonal Analysis: {csv_path.name.upper()} (30-Day Season)")
    print(f"{'='*134}")
    header_fmt = "{:<18} | {:<14} | {:<9} | {:<10} | {:<19} | {:<18} | {:<12} | {:<16}"
    print(
        header_fmt.format(
            "Crop Name",
            "Town",
            "Seed Cost",
            "Cycle",
            "Daily NQ Profit",
            "Cash Compound Rate",
            "Capital Days",
            "Latest Plant Day",
        )
    )
    print("-" * 134)

    for r in enriched_rows:
        print(
            header_fmt.format(
                r.get("Crop Name", "")[:18],
                r.get("Vendor Town", "")[:14],
                r.get("Seed Cost", "")[:9],
                r.get("Harvest Cycle", "")[:10],
                r.get("Daily NQ Profit", "")[:19],
                r.get("Cash Compound Rate", "")[:18],
                r.get("Capital Days", "")[:12],
                r.get("Latest Plant Day", "")[:16],
            )
        )
    print(f"{'='*134}\n")

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
