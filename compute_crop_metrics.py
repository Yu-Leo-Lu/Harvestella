"""Compute financial metrics for Harvestella seasonal crops.

Loads seasonal CSV files from the `seasons/` directory and computes:
1. Daily NQ Profit
2. True Cash Compounded Rate (%/day)
3. Production Days
4. Latest Plant Day (to achieve maximum harvests within a 30-day season)

Outputs are sorted by Daily NQ Profit descending by default.
"""

import argparse
import csv
import math
import re
from pathlib import Path
from typing import Any

SEASON_LENGTH_DAYS = 30

TREE_CROPS = {
    "Grouply Grape",
    "Princess Chestnut",
    "SnowCap Mikan",
    "Lococonut",
    "Wisty Peach",
    "Numblemon",
    "Macocoa",
    "Promised Fruit",
    "Moonfruit",
}


def parse_int_metric(val: Any) -> int | None:
    """Parse integer value from CSV cell. Returns None if empty or non-numeric."""
    if val is None:
        return None
    s = str(val).strip()
    if not s or s in ("—", "-", "N/A"):
        return None
    cleaned = re.sub(r"[^\d]", "", s)
    return int(cleaned) if cleaned else None


def parse_growth(row: dict[str, str]) -> tuple[int, int | None, int | None, bool]:
    """Parse growth parameters: Mature (Days), Regrowth (Days), Max Harvests.

    Returns (mature_days, regrowth_days, max_harvests, is_repeat).
    """
    mature_days = parse_int_metric(row.get("Mature (Days)") or row.get("Mature Days")) or 1
    regrowth_days = parse_int_metric(row.get("Regrowth (Days)") or row.get("Regrowth"))
    is_repeat = regrowth_days is not None and regrowth_days > 0

    max_harvests_raw = row.get("Max Harvests", "").strip()
    max_harvests = parse_int_metric(max_harvests_raw) if is_repeat else 1

    return mature_days, regrowth_days, max_harvests, is_repeat


def compute_crop_row(row: dict[str, str]) -> dict[str, Any]:
    """Calculate the financial and scheduling metrics for a crop entry."""
    crop_name = row.get("Crop Name", "").strip()
    biome_str = row.get("Biome", "")
    growth_season = row.get("Growth Season", "")
    max_harvests_str = row.get("Max Harvests", "")

    seed_cost = parse_int_metric(row.get("Seed Cost (G)") or row.get("Seed Cost"))
    basic_sell = parse_int_metric(row.get("NQ Sale (G)") or row.get("NQ Sale"))
    mature_days, regrowth_days, max_harvests, is_repeat = parse_growth(row)

    is_all_year = all(s in growth_season.lower() for s in ["spring", "summer", "fall", "winter"])
    is_tree = (
        "tree" in biome_str.lower()
        or "tree" in max_harvests_str.lower()
        or is_all_year
        or crop_name in TREE_CROPS
    )

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
        possible_in_season = (
            1 + (SEASON_LENGTH_DAYS - mature_days) // regrowth_days
            if mature_days <= SEASON_LENGTH_DAYS
            else 0
        )
        harvest_count = min(max_harvests, possible_in_season) if max_harvests else possible_in_season
        required_growth_days = (
            mature_days + (harvest_count - 1) * regrowth_days if harvest_count > 0 else mature_days
        )
        total_revenue = harvest_count * basic_sell
        net_profit = total_revenue - seed_cost
        daily_profit = net_profit / required_growth_days if required_growth_days > 0 else 0.0
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
    if not is_repeat:
        multiplier = basic_sell / seed_cost
        if multiplier > 0:
            daily_rate = (math.pow(multiplier, 1.0 / turnaround_days) - 1.0) * 100.0
            compounded_rate_str = f"+{daily_rate:.2f}%" if daily_rate >= 0 else f"{daily_rate:.2f}%"
        else:
            compounded_rate_str = "0.00%"
    else:
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


def analyze_csv_file(
    csv_path: Path,
    save_enriched: bool = False,
    output_path: Path | None = None,
    sort_by: str = "profit",
) -> list[dict[str, Any]]:
    """Load a seasonal CSV, compute metrics, print table, and optionally save."""
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)
        if not reader.fieldnames:
            raise ValueError(f"No headers found in {csv_path}")
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    computed_cols = [
        "Daily NQ Profit",
        "Cash Compound Rate",
        "Production Days",
        "Latest Plant Day",
    ]

    base_cols = [col for col in fieldnames if col not in computed_cols]
    out_fieldnames = base_cols + computed_cols
    enriched_rows = []

    for row in rows:
        computed = compute_crop_row(row)
        clean_row = {k: v for k, v in row.items() if k not in computed_cols}
        clean_row.update(computed)
        enriched_rows.append(clean_row)

    # Sort rows: defaults to Daily NQ Profit descending
    if sort_by.lower() in ("compound", "rate", "cash"):
        enriched_rows.sort(
            key=lambda r: (
                parse_numeric_metric(r.get("Cash Compound Rate")),
                parse_numeric_metric(r.get("Daily NQ Profit")),
            ),
            reverse=True,
        )
    else:
        enriched_rows.sort(
            key=lambda r: (
                parse_numeric_metric(r.get("Daily NQ Profit")),
                parse_numeric_metric(r.get("Cash Compound Rate")),
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
        regrow_val = parse_int_metric(r.get("Regrowth (Days)") or r.get("Regrowth"))
        regrow_display = f"{regrow_val}d" if regrow_val else "-"

        max_h_val = r.get("Max Harvests", "").strip()
        if not max_h_val or max_h_val in ("—", "-"):
            max_h_display = "1"
        elif "multi" in max_h_val.lower() or "tree" in max_h_val.lower():
            max_h_display = "Tree"
        else:
            max_h_display = max_h_val

        cost_val = parse_int_metric(r.get("Seed Cost (G)") or r.get("Seed Cost"))
        seed_cost_display = f"{cost_val:,} G" if cost_val is not None else "-"

        mature_val = parse_int_metric(r.get("Mature (Days)") or r.get("Mature Days"))
        mature_display = f"{mature_val}d" if mature_val else "-"

        print(
            header_fmt.format(
                r.get("Crop Name", "")[:18],
                r.get("Vendor Town", "")[:12],
                seed_cost_display[:9],
                mature_display[:7],
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
    parser.add_argument(
        "--sort",
        type=str,
        default="profit",
        choices=["profit", "compound"],
        help="Metric to sort by: 'profit' (Daily NQ Profit, default) or 'compound' (Cash Compound Rate).",
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
            analyze_csv_file(f, save_enriched=args.save, sort_by=args.sort)
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

        analyze_csv_file(target_file, save_enriched=args.save, output_path=args.output, sort_by=args.sort)


if __name__ == "__main__":
    main()
