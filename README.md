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

Every season in Harvestella lasts exactly **30 days** before Quietus wipes out unharvested annual crops. Maximize seasonal gold by pairing universal 30-day lifecycle pacing with season-specific crop rosters:

### Universal 30-Day Seasonal Flow

1. **Days 1–10 (Capital Velocity)**:
   - Reinvest every coin into high **Cash Compound Rate** crops with short turnarounds (1–3 days) to exponentially multiply wallet gold.
2. **Days 11–20 (Plot Maximization)**:
   - Shift plots toward high **Daily NQ Profit** crops as gold stops being the bottleneck and tillable tiles / stamina become the constraint.
3. **Days 21–30 (Quietus Shutdown)**:
   - Check **Production Days** and only plant before each crop's **Latest Plant Day** ($30 - \text{Production Days}$) to prevent crops from dying on Day 30.

---

### Season-by-Season Playbook

| Season | Phase 1: High Compounding (Days 1–10) | Phase 2: Top Plot Profit (Days 11–20) | Key Deadlines & Notes |
| :--- | :--- | :--- | :--- |
| **Spring** | **Unionion** (+16.74%/d)<br>**Dress Lettuce** (+15.62%/d)<br>**Stellar Wheat** (+11.20%/d) | **Revol Pepper** (+47.8 G/d)<br>**Cucumble** (+43.7 G/d)<br>**Sudor Pepper** (+38.9 G/d)<br>**Strawbuddy** (+35.8 G/d) | • **Cucumble** cutoff is **Day 11** (19 production days).<br>• **Strawbuddy** cutoff is **Day 18** (12 production days).<br>• Plant **Unionion** or **Dress Lettuce** up to **Day 27–28**. |
| **Summer** | **Dress Lettuce** (+15.62%/d)<br>**Eden Rice** (+15.02%/d)<br>**Morrocorn** (+14.87%/d) | **Islet Watermelon** (+175.0 G/d)<br>**Seatide Garlic** (+58.3 G/d)<br>**Morrocorn** (+50.0 G/d)<br>**Revol Pepper** (+47.8 G/d) | • **Islet Watermelon** cutoff is **Day 18** (2,500 G seed, massive payout).<br>• **Shatollan Paprika** cutoff is **Day 9** (21 production days).<br>• **Morrocorn** is the ultimate hybrid (top rate & profit). |
| **Fall** | **Unionion** (+16.74%/d)<br>**Dress Lettuce** (+15.62%/d)<br>**Eden Rice** (+15.02%/d)<br>**Lumpotato** (+10.67%/d) | **Royal Eggplant** (+60.0 G/d)<br>**Revol Pepper** (+47.8 G/d)<br>**Sudor Pepper** (+38.9 G/d)<br>**Nectarcane** (+38.0 G/d) | • **Royal Eggplant** cutoff is **Day 19** (11 production days).<br>• **Revol Pepper** cutoff is **Day 14** (16 production days).<br>• Great season for cave biome peppers. |
| **Winter** | **Lumpotato** (+10.67%/d)<br>**Argene Cabbage** (+7.78%/d) | **Chilly Plant** (+71.4 G/d)<br>**Argene Cabbage** (+25.0 G/d)<br>**Lumpotato** (+13.3 G/d) | • Restricted seed catalog in Argene.<br>• **Chilly Plant** cutoff is **Day 23** (7 production days).<br>• **Lumpotato** can be planted until **Day 27** (3 production days). |

---

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute.
