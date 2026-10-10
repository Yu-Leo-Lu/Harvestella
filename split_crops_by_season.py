"""Split Harvestella crop catalog into four separate seasonal CSV files.

Reads crop_master_catalog.csv and generates seasonal CSV tables for:
- Spring (spring.csv)
- Summer (summer.csv)
- Fall (fall.csv)
- Winter (winter.csv)
"""

import argparse
import csv
from pathlib import Path


SEASONS = ["Spring", "Summer", "Fall", "Winter"]


def split_catalog_by_season(
    input_file: Path,
    output_dir: Path,
    include_all_year_everywhere: bool = False,
) -> dict[str, int]:
    """Read master crop catalog and write seasonal CSV files."""
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_file, mode="r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)
        if not reader.fieldnames:
            raise ValueError("Input CSV has no header row.")

        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    counts: dict[str, int] = {}

    for season in SEASONS:
        season_lower = season.lower()
        season_rows: list[dict[str, str]] = []

        for row in rows:
            availability = row.get("Season Availability", "")
            avail_lower = availability.lower()

            # Check if this crop belongs in this season
            matches_season = season_lower in avail_lower
            if include_all_year_everywhere and "all year" in avail_lower:
                matches_season = True

            if matches_season:
                season_rows.append(row)

        out_path = output_dir / f"{season.lower()}.csv"
        with open(out_path, mode="w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(season_rows)

        counts[season] = len(season_rows)

    return counts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Harvestella master crop catalog into 4 seasonal CSV tables."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path("crop_master_catalog.csv"),
        help="Path to the master crop catalog CSV (default: crop_master_catalog.csv)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("seasons"),
        help="Output directory for seasonal CSVs (default: seasons)",
    )
    parser.add_argument(
        "--all-year-all-seasons",
        action="store_true",
        help="If set, crops marked '(All Year)' will appear in all 4 seasons instead of just their primary season.",
    )

    args = parser.parse_args()

    # Resolve relative paths against current working directory
    input_path = args.input.resolve()
    output_directory = args.output_dir.resolve()

    print(f"Reading from: {input_path}")
    print(f"Output directory: {output_directory}")

    counts = split_catalog_by_season(
        input_file=input_path,
        output_dir=output_directory,
        include_all_year_everywhere=args.all_year_all_seasons,
    )

    print("\nSuccessfully generated seasonal CSVs:")
    for season, count in counts.items():
        out_file = output_directory / f"{season.lower()}.csv"
        print(f"  - {season:6s}: {count:2d} crops -> {out_file.name}")


if __name__ == "__main__":
    main()
