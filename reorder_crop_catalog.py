"""Reorder Harvestella crop master catalog.

Sorts crops in `crop_master_catalog.csv` by:
1. Vendor Town: Lethe -> Nemea -> Shatolla -> Argene
2. Crop Name (Alphabetical)
"""

import argparse
import csv
from pathlib import Path

# Explicit ordering for towns; unlisted towns sort to the end
VENDOR_ORDER = {
    "lethe": 0,
    "nemea": 1,
    "shatolla": 2,
    "shatolla/nemea": 3,
    "argene": 4,
}


def get_sort_key(row: dict[str, str]) -> tuple[int, str]:
    """Generate sorting tuple: (town_rank, crop_name)."""
    vendor = row.get("Vendor Town", "").strip().lower()
    crop_name = row.get("Crop Name", "").strip()
    town_rank = VENDOR_ORDER.get(vendor, 99)
    return town_rank, crop_name


def reorder_catalog(input_path: Path, output_path: Path | None = None) -> list[dict[str, str]]:
    """Load, sort, and save crop master catalog."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input catalog file not found: {input_path}")

    with open(input_path, mode="r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)
        if not reader.fieldnames:
            raise ValueError(f"No headers found in {input_path}")
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    # Sort rows by town order then crop name
    rows.sort(key=get_sort_key)

    dest_path = output_path or input_path
    with open(dest_path, mode="w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Successfully reordered {len(rows)} crops in: {dest_path}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reorder Harvestella crop master catalog by vendor town and crop name."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path("crop_master_catalog.csv"),
        help="Path to crop master catalog CSV (default: crop_master_catalog.csv).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Optional destination path (default: overwrite input in-place).",
    )

    args = parser.parse_args()
    reorder_catalog(args.input, args.output)


if __name__ == "__main__":
    main()
