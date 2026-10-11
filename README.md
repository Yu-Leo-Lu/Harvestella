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
- **Four Core Financial Metrics**:
  - **Cash Compound Rate (%/day)**: Daily exponential growth rate of capital—essential when starting with low gold.
  - **Capital Days ($G \cdot d$)**: Liquidity risk indicator tracking how much capital is locked up and for how long.
  - **Full Season Net Profit**: Maximum net gold generated per farm plot across the full 30-day season.
  - **Latest Plant Day**: The exact cutoff calendar day to plant seeds without forfeiting a harvest cycle before Quietus.
- **Automated CLI Tools**:
  - `compute_crop_metrics.py`: Computes financial and scheduling rankings across seasons.
  - `split_crops_by_season.py`: Generates clean, per-season CSV data subsets from the master catalog.

---

## Repository Structure

```text
Harvestella/
├── crop_master_catalog.csv    # Master catalog of all crops, costs, cycles, and biomes
├── crop_metrics_guide.md      # Mathematical derivation and formula guide for metrics
├── compute_crop_metrics.py    # CLI tool to calculate profit, compound rates, and deadlines
├── split_crops_by_season.py   # Utility to regenerate seasonal CSV files from master catalog
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

### 1. Compute Crop Economics & Schedules

To analyze a specific season (e.g., Spring):
```bash
python compute_crop_metrics.py -i spring
```

To analyze all seasons simultaneously:
```bash
python compute_crop_metrics.py --all
```

To compute metrics and write the calculated columns directly into the CSV files in `seasons/`:
```bash
python compute_crop_metrics.py --all --save
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
| **Capital Days ($G \cdot d$)** | $k = \text{Seed Cost} \times (\text{Growth Days} + 1)$ | **Cash Flow & Liquidity:** Low values mean your cash is returned quickly, keeping you agile. |
| **Full Season Net Profit** | $\pi = (n \times \text{Sell}) - \text{Seed Cost}$ | **Late Game / Plot-Constrained:** Maximize total revenue per tilled tile over 30 days. |
| **Latest Plant Day** | $L = 30 - (n \times \text{Cycle Days})$ | **Quietus Management:** Plant before this day to guarantee the maximum possible harvest count. |

---

## Strategy Cheat-Sheet

1. **Days 1–10 (Capital Accumulation)**:
   - Prioritize high **Cash Compound Rate** crops with fast turnarounds to exponentially grow your bankroll.
   - *Top Picks*: **Unionion** (+16.74%/day), **Dress Lettuce** (+15.62%/day), and **Carrop**.
2. **Days 11–20 (Transition & Expansion)**:
   - As your wallet grows and tillable plots become the bottleneck, transition towards higher **Full Season Net Profit** crops.
   - *Top Picks*: **Morrocorn** (Summer — Shatolla at +1,400 G / Lethe at +1,190 G), **Argene Cabbage** / **Chilly Plant** (Winter).
3. **Days 21–30 (Quietus Deadline Awareness)**:
   - Check the **Latest Plant Day** column before buying seeds late in the month.
   - Planting after the cutoff will result in lost harvests or withered crops when Quietus strikes on Day 30.

---

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute.
