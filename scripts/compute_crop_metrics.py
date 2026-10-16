"""Compute financial metrics for Harvestella seasonal crops.

Loads seasonal CSV files from the `seasons/` directory and computes:
1. Daily NQ Profit (G/d)
2. Cash Compound Rate (%/d)
3. Production (Days)
4. Planting Schedule

All computed columns in the CSV are stored as pure numeric values (or comma-separated schedules).
Outputs are sorted by Daily NQ Profit descending by default.
"""

import argparse
import csv
import math
import re
from pathlib import Path
from typing import Any

# ==============================================================================
# 1. Constants & Configuration
# ==============================================================================

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

COMPUTED_COLUMNS = [
    "Daily NQ Profit (G/d)",
    "Cash Compound Rate (%/d)",
    "Production (Days)",
    "Planting Schedule",
]

LEGACY_AND_COMPUTED_COLS = {
    *COMPUTED_COLUMNS,
    "Daily NQ Profit",
    "Cash Compound Rate",
    "Production Days",
    "Latest Plant Day",
    "Planting Schedule",
    "Planting Schedules",
    "Capital Days",
    "Daily Profit",
}


# ==============================================================================
# 2. Data Parsing Utilities
# ==============================================================================

def parse_int_metric(val: Any) -> int | None:
    """Parse integer value from CSV cell. Returns None if empty or non-numeric."""
    if val is None:
        return None
    s = str(val).strip()
    if not s or s in ("—", "-", "N/A"):
        return None
    cleaned = re.sub(r"[^\d]", "", s)
    return int(cleaned) if cleaned else None


def parse_float_metric(val: Any) -> float:
    """Parse float value for sorting. Returns -inf for empty/non-numeric."""
    if val is None or val == "":
        return -float("inf")
    try:
        return float(val)
    except (ValueError, TypeError):
        return -float("inf")


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


def is_tree_crop(row: dict[str, str], crop_name: str) -> bool:
    """Identify whether a crop is a multi-season orchard tree."""
    biome_str = row.get("Biome", "").lower()
    max_harvests_str = row.get("Max Harvests", "").lower()
    growth_season = row.get("Growth Season", "").lower()
    growth_tokens = {s.strip() for s in growth_season.split(",")}

    is_all_year = (
        all(c in growth_tokens for c in ["sp", "su", "fa", "wi"])
        or all(s in growth_season for s in ["spring", "summer", "fall", "winter"])
        or "all" in growth_season
    )
    return (
        "tree" in biome_str
        or "tree" in max_harvests_str
        or is_all_year
        or crop_name in TREE_CROPS
    )


# ==============================================================================
# 3. Financial & Schedule Metric Calculations
# ==============================================================================

def generate_planting_schedule(season_length: int, cycle_days: int) -> str:
    """Generate a descending list of Quietus-aligned planting calendar days.

    Starting from (season_length - cycle_days), steps backwards by cycle_days
    so every harvest cycle finishes cleanly on or before Quietus (Day 30)
    with zero dead plot days between rotations.
    If items < 8, returns the full comma-separated list.
    If items >= 8, truncates to 7 display elements: first 5 items, '...', last item.
    Example: 6d cycle in 30d season -> "24, 18, 12, 6".
    Example: 2d cycle in 30d season -> "28, 26, 24, 22, 20, ... , 2".
    """
    if cycle_days <= 0 or cycle_days > season_length:
        return ""
    days: list[str] = []
    current = season_length - cycle_days
    if current == 0:
        return "1"
    while current > 0:
        days.append(str(current))
        current -= cycle_days
    if len(days) < 8:
        return ", ".join(days)
    return f"{', '.join(days[:5])}, ... , {days[-1]}"


def compute_crop_row(row: dict[str, str]) -> dict[str, Any]:
    """Calculate financial and scheduling metrics as pure numeric values for CSV."""
    crop_name = row.get("Crop Name", "").strip()

    # Trees (multi-season investments) do not have single-season annual metrics
    if is_tree_crop(row, crop_name):
        return {col: "" for col in COMPUTED_COLUMNS}

    seed_cost = parse_int_metric(row.get("Seed Cost (G)") or row.get("Seed Cost"))
    basic_sell = parse_int_metric(row.get("NQ Sale (G)") or row.get("NQ Sale"))
    mature_days, regrowth_days, max_harvests, is_repeat = parse_growth(row)

    # Foraged / free drops with no purchase cost (e.g. Nitro Pineapple)
    if seed_cost is None or seed_cost <= 0:
        if basic_sell is not None:
            profit_per_cycle = basic_sell
            daily_profit = profit_per_cycle / mature_days if mature_days > 0 else 0.0
            schedule = generate_planting_schedule(SEASON_LENGTH_DAYS, mature_days)
            return {
                "Daily NQ Profit (G/d)": round(daily_profit, 1),
                "Cash Compound Rate (%/d)": "",
                "Production (Days)": mature_days,
                "Planting Schedule": schedule,
            }
        return {col: "" for col in COMPUTED_COLUMNS}

    if is_repeat and regrowth_days:
        possible_in_season = (
            1 + (SEASON_LENGTH_DAYS - mature_days) // regrowth_days
            if mature_days <= SEASON_LENGTH_DAYS
            else 0
        )
        harvest_count = min(max_harvests, possible_in_season) if max_harvests else possible_in_season
        active_days = (
            mature_days + (harvest_count - 1) * regrowth_days if harvest_count > 0 else mature_days
        )
        total_revenue = harvest_count * basic_sell
        net_profit = total_revenue - seed_cost
        daily_profit = net_profit / active_days if active_days > 0 else 0.0

        wealth_ratio = total_revenue / seed_cost
        realization_days = active_days + 1
        daily_rate = (
            (math.pow(wealth_ratio, 1.0 / realization_days) - 1.0) * 100.0
            if wealth_ratio > 0
            else None
        )
    else:
        active_days = mature_days
        profit_per_cycle = basic_sell - seed_cost
        daily_profit = profit_per_cycle / mature_days
        turnaround_days = mature_days + 1

        multiplier = basic_sell / seed_cost
        daily_rate = (
            (math.pow(multiplier, 1.0 / turnaround_days) - 1.0) * 100.0
            if multiplier > 0
            else 0.0
        )

    schedule = generate_planting_schedule(SEASON_LENGTH_DAYS, active_days)

    return {
        "Daily NQ Profit (G/d)": round(daily_profit, 1),
        "Cash Compound Rate (%/d)": round(daily_rate, 2) if daily_rate is not None else "",
        "Production (Days)": active_days,
        "Planting Schedule": schedule,
    }


# ==============================================================================
# 4. Presentation & Table Formatting
# ==============================================================================

def format_schedule_for_display(schedule_str: str) -> str:
    """Format planting schedule for table display."""
    return schedule_str if schedule_str else "-"


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

    base_cols = [col for col in fieldnames if col not in LEGACY_AND_COMPUTED_COLS]
    out_fieldnames = base_cols + COMPUTED_COLUMNS
    enriched_rows = []

    for row in rows:
        computed = compute_crop_row(row)
        clean_row = {k: v for k, v in row.items() if k not in LEGACY_AND_COMPUTED_COLS}
        clean_row.update(computed)
        enriched_rows.append(clean_row)

    # Sort rows: defaults to Daily NQ Profit descending
    is_compound_sort = sort_by.lower() in ("compound", "rate", "cash")
    primary_key = "Cash Compound Rate (%/d)" if is_compound_sort else "Daily NQ Profit (G/d)"
    secondary_key = "Daily NQ Profit (G/d)" if is_compound_sort else "Cash Compound Rate (%/d)"

    enriched_rows.sort(
        key=lambda r: (
            parse_float_metric(r.get(primary_key)),
            parse_float_metric(r.get(secondary_key)),
        ),
        reverse=True,
    )

    # Print summary table to console with formatted units
    print(f"\n{'='*159}")
    print(f" Seasonal Analysis: {csv_path.name.upper()} (30-Day Season)")
    print(f"{'='*159}")
    header_fmt = "{:<18} | {:<10} | {:<9} | {:<7} | {:<7} | {:<7} | {:<16} | {:<16} | {:<14} | {:<28}"
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
            "Planting Schedule",
        )
    )
    print("-" * 159)

    for r in enriched_rows:
        regrow_val = parse_int_metric(r.get("Regrowth (Days)") or r.get("Regrowth"))
        regrow_display = f"{regrow_val}d" if regrow_val else "-"

        max_h_val = str(r.get("Max Harvests", "")).strip()
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

        profit_val = r.get("Daily NQ Profit (G/d)")
        if profit_val != "" and profit_val is not None:
            profit_display = f"+{float(profit_val):.1f} G/d"
        elif max_h_display == "Tree":
            profit_display = "Tree"
        else:
            profit_display = "-"

        rate_val = r.get("Cash Compound Rate (%/d)")
        if rate_val != "" and rate_val is not None:
            rate_display = f"+{float(rate_val):.2f}%"
        elif max_h_display == "Tree":
            rate_display = "Tree"
        elif cost_val is None:
            rate_display = "Free Drop"
        else:
            rate_display = "-"

        prod_val = r.get("Production (Days)")
        prod_display = f"{prod_val}d" if prod_val != "" and prod_val is not None else "Tree"

        sched_val = str(r.get("Planting Schedule", "")).strip()
        sched_display = (
            format_schedule_for_display(sched_val)
            if sched_val
            else ("Tree" if max_h_display == "Tree" else "-")
        )

        print(
            header_fmt.format(
                r.get("Crop Name", "")[:18],
                r.get("Vendor Town", "")[:10],
                seed_cost_display[:9],
                mature_display[:7],
                regrow_display[:7],
                max_h_display[:7],
                profit_display[:16],
                rate_display[:16],
                prod_display[:14],
                sched_display[:28],
            )
        )
    print(f"{'='*159}\n")

    if save_enriched:
        dest_path = output_path or csv_path
        with open(dest_path, mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=out_fieldnames)
            writer.writeheader()
            writer.writerows(enriched_rows)
        print(f"Saved enriched CSV with computed metrics to: {dest_path}")

    return enriched_rows


def resolve_target_file(input_str: str | None, seasons_dir: Path) -> Path:
    """Resolve CLI input string to an existing seasonal CSV file path."""
    if input_str:
        p = Path(input_str)
        if p.exists():
            return p
        if (seasons_dir / p.name).exists():
            return seasons_dir / p.name
        if (seasons_dir / f"{p.name}.csv").exists():
            return seasons_dir / f"{p.name}.csv"
        raise FileNotFoundError(f"Cannot find CSV file matching '{input_str}'.")

    default_spring = seasons_dir / "spring.csv"
    if default_spring.exists():
        return default_spring

    csvs = list(seasons_dir.glob("*.csv"))
    if not csvs:
        raise FileNotFoundError("No CSV files found in seasons/ directory.")
    return csvs[0]


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
        try:
            target_file = resolve_target_file(args.input, seasons_dir)
        except FileNotFoundError as err:
            print(f"Error: {err}")
            return
        analyze_csv_file(target_file, save_enriched=args.save, output_path=args.output, sort_by=args.sort)


if __name__ == "__main__":
    main()
