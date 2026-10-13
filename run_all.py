"""Run the complete Harvestella crop data pipeline.

Executes all steps in sequence:
1. Reorder master catalog (reorder_crop_catalog.py)
2. Split catalog into seasonal CSVs (split_crops_by_season.py)
3. Compute and enrich metrics for all seasons (compute_crop_metrics.py)
"""

import argparse
from pathlib import Path

from compute_crop_metrics import analyze_csv_file
from reorder_crop_catalog import reorder_catalog
from split_crops_by_season import split_catalog_by_season


def run_pipeline(
    catalog_path: Path = Path("crop_master_catalog.csv"),
    seasons_dir: Path = Path("seasons"),
    save_enriched: bool = True,
    include_all_year: bool = False,
) -> None:
    """Execute the full data pipeline in sequence."""
    print("=" * 80)
    print(" HARVESTELLA CROP DATA PIPELINE")
    print("=" * 80)

    # Step 1: Reorder Master Catalog
    print("\n[Step 1/3] Reordering crop master catalog...")
    reorder_catalog(input_path=catalog_path)

    # Step 2: Split into Seasonal CSVs
    print("\n[Step 2/3] Splitting catalog into seasonal files...")
    counts = split_catalog_by_season(
        input_file=catalog_path,
        output_dir=seasons_dir,
        include_all_year_everywhere=include_all_year,
    )
    for season, count in counts.items():
        print(f"  - {season}: {count} crops -> {seasons_dir / f'{season.lower()}.csv'}")

    # Step 3: Compute & Enrich Financial Metrics
    print(f"\n[Step 3/3] Computing crop metrics (save={save_enriched})...")
    seasonal_files = sorted(seasons_dir.glob("*.csv"))
    if not seasonal_files:
        print(f"Warning: No seasonal CSV files found in '{seasons_dir}'.")
        return

    for csv_file in seasonal_files:
        analyze_csv_file(csv_file, save_enriched=save_enriched)

    print("=" * 80)
    print(" Pipeline completed successfully!")
    print("=" * 80)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run all Harvestella data scripts: reorder catalog, split seasons, and compute metrics."
    )
    parser.add_argument(
        "-c",
        "--catalog",
        type=Path,
        default=Path("crop_master_catalog.csv"),
        help="Path to master crop catalog (default: crop_master_catalog.csv).",
    )
    parser.add_argument(
        "-d",
        "--seasons-dir",
        type=Path,
        default=Path("seasons"),
        help="Directory for seasonal CSV files (default: seasons).",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not save computed metrics back to seasonal CSVs (only print tables).",
    )
    parser.add_argument(
        "--include-all-year",
        action="store_true",
        help="Include all-year crops across every seasonal file.",
    )

    args = parser.parse_args()
    run_pipeline(
        catalog_path=args.catalog,
        seasons_dir=args.seasons_dir,
        save_enriched=not args.no_save,
        include_all_year=args.include_all_year,
    )


if __name__ == "__main__":
    main()
