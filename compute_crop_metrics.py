"""Compute financial metrics for Harvestella seasonal crops.

Loads seasonal CSV files from the `seasons/` directory and computes:
1. Daily NQ Profit (G/d)
2. Cash Compound Rate (%/d)
3. Production (Days)
4. Latest Plant Day

All computed columns in the CSV are stored as pure numeric values.
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

COMPUTED_COLUMNS = [
    "Daily NQ Profit (G/d)",
    "Cash Compound Rate (%/d)",
    "Production (Days)",
    "Latest Plant Day",
]

LEGACY_AND_COMPUTED_COLS = {
    *COMPUTED_COLUMNS,
    "Daily NQ Profit",
    "Cash Compound Rate",
    "Production Days",
    "Capital Days",
    "Daily Profit",
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


def compute_crop_row(row: dict[str, str]) -> dict[str, Any]:
    """Calculate financial and scheduling metrics as pure numeric values for CSV."""
    crop_name = row.get("Crop Name", "").strip()
    biome_str = row.get("Biome", "")
    growth_season = row.get("Growth Season", "")
    max_harvests_str = row.get("Max Harvests", "")

    seed_cost = parse_int_metric(row.get("Seed Cost (G)") or row.get("Seed Cost"))
    basic_sell = parse_int_metric(row.get("NQ Sale (G)") or row.get("NQ Sale"))
    mature_days, regrowth_days, max_harvests, is_repeat = parse_growth(row)

    growth_tokens = {s.strip().lower() for s in growth_season.split(",")}
    is_all_year = (
        all(c in growth_tokens for c in ["sp", "su", "fa", "wi"])
        or all(s in growth_season.lower() for s in ["spring", "summer", "fall", "winter"])
        or "all" in growth_season.lower()
    )
    is_tree = (
        "tree" in biome_str.lower()
        or "tree" in max_harvests_str.lower()
        or is_all_year
        or crop_name in TREE_CROPS
    )

    # Trees (multi-season investments) do not have single-season annual metrics
    if is_tree:
        return {col: "" for col in COMPUTED_COLUMNS}

    # Foraged / free drops with no purchase cost (e.g. Nitro Pineapple)
    if seed_cost is None or seed_cost <= 0:
        if basic_sell is not None:
            profit_per_cycle = basic_sell
            daily_profit = profit_per_cycle / mature_days if mature_days > 0 else 0.0
            latest_start_day = max(1, SEASON_LENGTH_DAYS - mature_days)
            return {
                "Daily NQ Profit (G/d)": round(daily_profit, 1),
                "Cash Compound Rate (%/d)": "",
                "Production (Days)": mature_days,
                "Latest Plant Day": latest_start_day,
            }
        return {col: "" for col in COMPUTED_COLUMNS}

    if is_repeat and regrowth_days:
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
        latest_start_day = max(1, SEASON_LENGTH_DAYS - required_growth_days)

        wealth_ratio = total_revenue / seed_cost
        realization_days = required_growth_days + 1
        daily_rate = (
            (math.pow(wealth_ratio, 1.0 / realization_days) - 1.0) * 100.0
            if wealth_ratio > 0
            else None
        )
        active_days = required_growth_days
    else:
        profit_per_cycle = basic_sell - seed_cost
        daily_profit = profit_per_cycle / mature_days
        turnaround_days = mature_days + 1
        latest_start_day = max(1, SEASON_LENGTH_DAYS - mature_days)

        multiplier = basic_sell / seed_cost
        daily_rate = (
            (math.pow(multiplier, 1.0 / turnaround_days) - 1.0) * 100.0
            if multiplier > 0
            else 0.0
        )
        active_days = mature_days

    return {
        "Daily NQ Profit (G/d)": round(daily_profit, 1),
        "Cash Compound Rate (%/d)": round(daily_rate, 2) if daily_rate is not None else "",
        "Production (Days)": active_days,
        "Latest Plant Day": latest_start_day,
    }


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

        latest_val = r.get("Latest Plant Day")
        latest_display = f"Day {latest_val}" if latest_val != "" and latest_val is not None else "Day 1 (All)"

        print(
            header_fmt.format(
                r.get("Crop Name", "")[:18],
                r.get("Vendor Town", "")[:12],
                seed_cost_display[:9],
                mature_display[:7],
                regrow_display[:7],
                max_h_display[:7],
                profit_display[:19],
                rate_display[:18],
                prod_display[:15],
                latest_display[:16],
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
