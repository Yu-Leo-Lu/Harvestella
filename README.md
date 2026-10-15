# Harvestella Agricultural Economics & Crop Profit Optimizer

A data-driven toolkit and guide for maximizing farming profits in Square Enix's **Harvestella**.

This repository models realistic agricultural economics in Harvestella, accounting for actual in-game constraints: the **30-day season**, the season-ending **Quietus** disaster, **overnight shipping delays (+1 day payout)**, biome/plot requirements, and initial cash constraints.

---

## Features

- **Comprehensive Crop Master Catalog (`crop_master_catalog.csv`)**:
  - Detailed pricing, growth cycles, repeat harvest intervals, biome/land requirements (Farm, Waterside, Cave), vendor towns, and seasonal availability.
- **Realistic Game Mechanics Modeling**:
  - **Shipping Delay (+1d)**: Shipped crops yield gold the following morning, impacting cash turnaround.
  - **Quietus Deadlines**: Seasons run exactly 30 days. Unharvested annual crops die on Day 30 without payout.
  - **Single vs. Repeat Harvests**: Distinct mathematical models for one-time plantings versus recurring crops (e.g., Nemean Tomato, Morrocorn, Islet Watermelon) and multi-season orchard trees.
- **Core Financial & Scheduling Metrics**:
  - **Daily NQ Profit**: Normal quality daily gold return per farm plot per growth day ($G/\text{day}$).
  - **Cash Compound Rate (%/day)**: Daily exponential growth rate of capital—essential when starting with low gold.
  - **Production Days**: Total active lifecycle days a crop occupies the plot through all harvest cycles.
  - **Latest Plant Day**: The exact cutoff calendar day to plant seeds without forfeiting a harvest cycle before Quietus ($30 - \text{Production Days}$).
- **Automated CLI Tools**:
  - `run_all.py`: Runs the complete pipeline (reorders catalog, splits seasons, computes & saves metrics).
  - `compute_crop_metrics.py`: Computes financial and scheduling rankings across seasons.
  - `split_crops_by_season.py`: Generates clean, per-season CSV data subsets from the master catalog.
  - `reorder_crop_catalog.py`: Reorders the master catalog by vendor town and crop name.

---

## Repository Structure

```text
Harvestella/
├── crop_master_catalog.csv    # Master catalog of all crops, costs, cycles, and biomes
├── crop_metrics_guide.md      # Mathematical derivation and formula guide for metrics
├── run_all.py                 # Master pipeline runner (reorder -> split -> compute)
├── compute_crop_metrics.py    # CLI tool to calculate profit, compound rates, and deadlines
├── split_crops_by_season.py   # Utility to regenerate seasonal CSV files from master catalog
├── reorder_crop_catalog.py    # Utility to sort master catalog by vendor town and crop name
├── seasons/                   # Per-season CSV data
│   ├── spring.csv
│   ├── summer.csv
│   ├── fall.csv
│   └── winter.csv
└── archive/                   # Reference analysis tables and legacy farming guides
```

---

## Quick Start

### Prerequisites
- Python 3.10+ (uses standard library only—no external pip packages required).

### 1. Run Complete Pipeline (One-Click)

To reorder the catalog, regenerate seasonal CSVs, and compute/save all metrics in one command:
```bash
python run_all.py
```

### 2. Compute Crop Economics & Schedules

To analyze a specific season (e.g., Spring):
```bash
python compute_crop_metrics.py -i spring
```

To analyze all seasons simultaneously:
```bash
python compute_crop_metrics.py --all
# or using shorthand:
python compute_crop_metrics.py -a
```

To compute metrics and write the calculated columns directly into the CSV files in `seasons/`:
```bash
python compute_crop_metrics.py -a -s
# or combined:
python compute_crop_metrics.py -as
```

To output the analysis to a custom file:
```bash
python compute_crop_metrics.py -i summer -o summer_analyzed.csv
```

### 2. Regenerate Seasonal CSVs

If you update `crop_master_catalog.csv`, regenerate the seasonal tables using:
```bash
python split_crops_by_season.py
```

Include all-year crops across every seasonal file:
```bash
python split_crops_by_season.py --include-all-year
```

---

## Core Financial Metrics

For full mathematical definitions, derivations, and formulas, see [crop_metrics_guide.md](file:///c:/Users/leona/GitHub/Harvestella/crop_metrics_guide.md).

| Metric | Formula / Concept | When to Prioritize |
| :--- | :--- | :--- |
| **Cash Compound Rate (%/day)** | $r = \left(\left(\frac{\text{Sell}}{\text{Seed}}\right)^{\frac{1}{\text{Days} + 1}} - 1\right) \times 100\%$ | **Early Game / Low Gold:** Maximize the speed at which your initial wallet multiplies. |
| **Daily NQ Profit** | $\delta = \frac{\text{Net Profit}}{\text{Production Days}}$ | **Cycle Efficiency & Plot Profit:** Compares normal quality profit generation velocity per plot across crops of different harvest lengths. |
| **Production Days** | Single: $m\text{ days}$ <br> Repeat: $m + (n - 1) \cdot g\text{ days}$ | **Turnaround Planning:** Total calendar time the crop occupies the soil before the plot is freed up. |
| **Latest Plant Day** | $30 - \text{Production Days}$ | **Quietus Management:** Cutoff day to plant without withering at Quietus or losing harvest cycles. |

---

## Strategy Cheat-Sheet

1. **Days 1–10 (Capital Accumulation)**:
   - Prioritize high **Cash Compound Rate** crops with fast turnarounds to exponentially grow your bankroll.
   - *Top Picks*: **Unionion** (+16.74%/day), **Dress Lettuce** (+15.62%/day), and **Carrop**.
2. **Days 11–20 (Transition & Expansion)**:
   - As your wallet grows and tillable plots become the bottleneck, transition towards higher **Daily NQ Profit** crops.
   - *Top Picks*: **Morrocorn** (Summer — Shatolla at +50.0 G/d / Lethe at +42.5 G/d), **Seatide Garlic** (+58.3 G/d), **Islet Watermelon** (+175.0 G/d), and **Chilly Plant** (Winter at +71.4 G/d).
3. **Days 21–30 (Quietus Deadline Awareness)**:
   - Check the **Latest Plant Day** column before buying seeds late in the month.
   - Planting after the cutoff will result in lost harvests or withered crops when Quietus strikes on Day 30.

---

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute.
