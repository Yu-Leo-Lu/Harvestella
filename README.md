# Harvestella Agricultural Economics & Crop Profit Optimizer

A data-driven toolkit and Mixed-Integer Linear Programming (MILP) optimizer for maximizing farming profits in Square Enix's Harvestella.

> ⚡ **Quick Navigation**: [The Big Picture](#the-big-picture-why-crop-allocation-is-hard) • [Quick Start & Solver](#quick-start--workflow) • [Farm Expansion Benchmarks](#renovator-plot-expansion-benchmarks-levels-19) • [Data Pipeline](#1-click-data-preparation-pipeline) • [Project Architecture](#project-architecture--documentation)

---

## The Big Picture: Why Crop Allocation is Hard

In *Harvestella*, deciding what seeds to buy is not a simple matter of looking up a "best crop" tier list. A player faces four rigid, simultaneous in-game bottlenecks that interact non-linearly:

### The 4 In-Game Bottlenecks

1. **Capital Budget Limit (`wallet_gold`)**: You can only spend the liquid cash currently in your pocket.
2. **Biome Soil Partitioning (`free_plots`)**: Farm land is strictly partitioned into three incompatible soil types:
   - Farm Plots: Standard soil.
   - Waterside Plots: Specialized water soil (e.g., Islet Watermelon, Nectarcane).
   - Cave Plots: Specialized cave soil (e.g., Revol Pepper, Sudor Pepper).
   - *Plots of one biome cannot grow crops from another.*
3. **Vendor Shop Inventory Caps & Town Story Unlocks**: General stores carry a finite stock per 10-day cycle (`seed_stock`, default 99). Furthermore, seeds from Nemea, Shatolla, Argene, or Abandoned Eden are unavailable until those towns are unlocked in the story.
4. **Planning Deadlines (Quietus vs. Restocks)**:
   - Quietus (Day 30): Every season lasts exactly 30 days and terminates with Quietus. All annual crops die on Day 30 without payout.
   - Vendor Restocks (Days 1, 11, 21): Shops refresh stock every 10 days. Slow crops that overhang a restock day lock up your plot capacity and freeze your capital.

---

### The Dual Economic Engines: Capital Compounding vs. Land Efficiency

When evaluating crops, players encounter two fundamentally different economic metrics:

| Economic Engine | Metric | What It Measures | In-Game Role |
| :--- | :---: | :--- | :--- |
| Capital Compounding | Cash Compound Rate (%/day) | Return on Gold ($\text{Gold earned per Gold spent}$) | The Growth Engine: When starting out with low gold (Day 1, 1,000 G), you cannot afford expensive seeds. High-compound crops (e.g. Dress Lettuce at $+15.6\%/\text{d}$) multiply your wallet exponentially ($W_t = W_0 (1+r)^t$) over short 1–2 day sprints, rapidly building capital for farm expansions. |
| Land Efficiency | Daily NQ Profit (G/d) | Return on Land ($\text{Gold earned per Plot occupied}$) | The Revenue Engine: Once your wallet has enough cash to fill all available plots, idle gold in your pocket earns 0% return. You want every square foot of dirt generating maximum raw gold per day. |

---

### The Single-Seed Traps: Why Intuition Fails

To see why simple rules of thumb fail, consider a standard benchmark scenario entering Summer (Season 2, with 8,000 G saved from Spring):
- Season & Timing: Summer, Day 1 (Full 30-day Quietus planning horizon)
- Starting Budget: 8,000 G (accumulated from Spring harvests)
- Available Land: 70 standard Farm plots (Level 1 farm)
- Town Unlocks: Lethe and Shatolla unlocked

Most players follow simple greedy heuristics and fall into one of two traps:

#### Trap A: Greedy by Raw Daily Profit (The Capital Starvation Trap)
- *"Seatide Garlic yields +58.3 G/d, the highest profit of any Summer farm crop. I should spend all my money on Garlic."*
- At 650 G per seed, an 8,000 G budget buys only 12 seeds (spending 7,800 G).
- Result: You occupy only 12 plots while 58 farm plots sit empty, earning only +700.0 G/d.

#### Trap B: Greedy by Compound Velocity (The Land Bottleneck Trap)
- *"Dress Lettuce doubles money fastest (+15.62%/d). I should buy only Lettuce."*
- At 55 G per seed, filling all 70 plots costs only $70 \times 55 = 3,850\text{ G}$.
- Result: All plots are occupied, but 4,150 G sits idle in your wallet earning 0% return. Total daily profit is only +1,050.0 G/d.

---

### The Solution: How the Optimizer Harmonizes Both Engines

The true optimal solution is an **inflection point** that balances both forces:

1. **Plot-Filling**: Uses cheap, high-compounding crops (like Dress Lettuce) to ensure no farm tile sits idle.
2. **Marginal Upgrading**: Systematically upgrades individual plots to higher-margin crops (like Morrocorn @ 200 G seed, +50 G/d) until both land and gold are exhausted.

> [!IMPORTANT]
> ### 🌾 The Power of Balanced Allocation (Summer 8,000 G Benchmark)
> 
> Look at what happens to your plots and cash across all three strategies on the same 70 Farm plots:
> 
> | Strategy | Farm Plots Occupied | Gold Capital Spent | Daily Profit | What Went Wrong? |
> | :--- | :---: | :---: | :---: | :--- |
> | Pure Garlic | 12 / 70 (17.1%) | 7,800 G / 8,000 G | +700.0 G/d | Capital Starvation: 650 G seeds deplete cash; 58 plots sit empty! |
> | Pure Lettuce | 70 / 70 (100%) | 3,850 G / 8,000 G | +1,050.0 G/d | Land Bottleneck: Farm is full, but 4,150 G sits idle in your pocket. |
> | **MILP Optimizer** | **69 / 70 (98.6%)** | **8,000 G / 8,000 G (100%)** | **+2,050.0 G/d** | **Optimal Sweet Spot**: Nearly full farm, 100% working capital! |
> 
> The optimizer proposes **29 Morrocorn** + **40 Dress Lettuce**:
> - Spending exactly 8,000 G (0 G left idle).
> - Planting 69 of 70 plots (only 1 tile left open).
> - Delivering **+2,050.0 G/day** — nearly 3× the profit of Garlic (+192.9%) and double the profit of Lettuce (+95.2%)!

---

## Quick Start & Workflow

### Prerequisites
- Python 3.10+
- Install required packages:
  ```bash
  pip install pyyaml scipy numpy
  ```

---

### 1-Click Allocation Optimization

Run the optimizer across all four seasons. This prints formatted terminal summary tables and automatically updates [`crop_allocation_report.md`](crop_allocation_report.md) in the project root:

```bash
python optimize_crop_allocation.py -a
```

To optimize a single season profile:
```bash
python optimize_crop_allocation.py -sp   # Spring
python optimize_crop_allocation.py -su   # Summer
python optimize_crop_allocation.py -fa   # Fall
python optimize_crop_allocation.py -wi   # Winter
```

#### Sample Optimizer Output Table:
```
============================================================================================================================================
 ALL-SEASON CROP ALLOCATION EXECUTIVE SUMMARY
============================================================================================================================================
Season      Budget  Optimal Seed Purchases                                   Plots Used                 Gold Spent / Leftover      Daily Profit
--------------------------------------------------------------------------------------------------------------------------------------------
Spring     1,000 G  9 Unionion (Nemea), 1 Dress Lettuce                      10 / 70 Farm               1,000 G / 0 G (100.0%)       +285.0 G/d
Summer     8,000 G  29 Morrocorn (Shatolla), 40 Dress Lettuce                69 / 70 Farm               8,000 G / 0 G (100.0%)     +2,050.0 G/d
Fall      15,000 G  70 Unionion (Nemea), 12 Nectarcane, 8 Sudor Pepper       70 Farm, 12 Water, 8 Cave  14,990 G / 10 G (99.9%)    +2,867.2 G/d
Winter    20,000 G  8 Chilly Plant, 61 Argene Cabbage, 1 Lumpotato (Argene)  70 / 70 Farm               19,900 G / 100 G (99.5%)   +2,109.5 G/d
============================================================================================================================================
```

---

### Configuring Your Farm Profile

Customize your farm parameters in `configs/<season>.yaml`:

```yaml
season: summer
current_day: 1
wallet_gold: 8000

# Planning Horizon:
# - "quietus"      : Strict Day 30 season-end cutoff (crops must mature by Day 30)
# - "next_restock" : Mid-season 10-day shop refresh cutoff (Days 11, 21, or 31)
horizon: quietus

# Optional Variety Limit (Cardinality Constraint):
# Set to an integer (e.g., 2 or 3) to limit farm management chaos, or null for unconstrained
max_crop_varieties: null

# Physical Available Plot Capacities
free_plots:
  farm: 70
  waterside: 12
  cave: 12

# Story Unlock Gates
unlocked_towns:
  Lethe: true
  Nemea: true
  Shatolla: true
  Argene: true
  Abandoned Eden: false
```

---

### Renovator Plot Expansion Benchmarks (Levels 1–9)

Farm expansions are permanent (they carry over into all future seasons) and are purchased in batches from the Renovator in Lethe. Use this table as a reference for the `farm` capacity values to configure in your YAML files:

| Farm Level | Upgrade Cost | Plot Increment | Total Farm Tiles | Cost / Tile | Payback @ 35 G/d | Strategic Assessment |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Level 1 | Free | Starting (10×7) | 70 tiles | — | — | Starting plot. Capital-constrained early on. |
| **Level 2** | **3,000 G** | **+56 tiles** (8×7) | **126 tiles** | 53.6 G | 1.5 days | **Highest ROI in the game.** Rush in Spring Year 1. |
| Level 3 | 8,000 G | +21 tiles (3×7) | 147 tiles | 381.0 G | 10.9 days | Stepping stone to Level 4. |
| **Level 4** | **15,000 G** | **+70 tiles** (10×7) | **217 tiles** | 214.3 G | 6.1 days | **Major expansion leap.** Pays back in under a week. |
| Level 5 | 25,000 G | +56 tiles (8×7) | 273 tiles | 446.4 G | 12.8 days | Solid mid-game goal. |
| Level 6 | 40,000 G | +21 tiles (3×7) | 294 tiles | 1,904.8 G | 54.4 days | Expensive bridge tier to Level 7. |
| Level 7 | 80,000 G | +70 tiles (10×7) | 364 tiles | 1,142.9 G | 32.7 days | Late-game industrial farming. |
| Level 8 | 120,000 G | +56 tiles (8×7) | 420 tiles | 2,142.9 G | 61.2 days | End-game passive orchard empire. |
| Level 9 (Max) | 200,000 G | +21 tiles (3×7) | 441 tiles | 9,523.8 G | 272.1 days | Completionist flex tier. |

> [!TIP]
> **The Level 4 Working Capital Rule**: Upgrading to Level 4 costs 15,000 G, but buying seeds to plant across all 217 plots requires an additional 7,000–15,000 G. Never spend down to 0 G to buy the expansion—wait until your wallet reaches **~22,000–25,000 G** so your newly acquired plots don't sit empty.

---

### 1-Click Data Preparation Pipeline

To rebuild the catalog, regenerate seasonal CSV files, and compute/enrich all profit and scheduling metrics:

```bash
python build_crop_data.py
```

This automated pipeline:
1. Reorders [`crop_master_catalog.csv`](crop_master_catalog.csv) by story vendor progression.
2. Splits crops into clean seasonal CSV tables in `seasons/` (`spring.csv`, `summer.csv`, etc.).
3. Computes Daily NQ Profit, Cash Compound Rate, Production Days, and Quietus-aligned Planting Schedules for every crop.

---

## Project Architecture & Documentation

### Directory Structure

```
Harvestella/
├── README.md                           # Main Project Overview & Strategy Guide
├── crop_allocation_report.md           # Generated Markdown Report from Optimizer
├── optimize_crop_allocation.py         # Mixed-Integer Linear Programming Optimizer CLI
├── build_crop_data.py                  # Master Data Pipeline (reorders, splits, computes metrics)
├── crop_master_catalog.csv             # Complete Master Agricultural Data
│
├── docs/                               # 📁 Detailed Mathematical & Economic Guides
│   ├── crop_allocation_solver_guide.md # MILP formulation, Big-M method, and Solver Walkthrough
│   └── crop_metrics_guide.md           # ROI & Daily Profit Formulas
│
├── configs/                            # 📁 User Season Configurations (Gold, Plots, Horizons)
│   ├── spring.yaml, summer.yaml, fall.yaml, winter.yaml
│
├── seasons/                            # 📁 Per-Season Analyzed Data CSVs
│   ├── spring.csv, summer.csv, fall.csv, winter.csv
│
└── scripts/                            # 📁 Pipeline Engine Modules
    ├── compute_crop_metrics.py
    ├── split_crops_by_season.py
    └── reorder_crop_catalog.py
```

---

### Deep-Dive Reference Guides

- **[Crop Allocation Solver Guide](docs/crop_allocation_solver_guide.md)**:
  Detailed mathematical documentation of `solve_allocation()`:
  - Multi-Dimensional Bounded Integer Knapsack classification.
  - Mixed-Integer Linear Programming (MILP) canonical formulation.
  - Big-M method for `max_crop_varieties` cardinality constraints ($x_i - M_i y_i \le 0$).
  - Full variable reference table and Summer 8k G numerical calculation walkthrough.
- **[Crop Metrics & Economics Guide](docs/crop_metrics_guide.md)**:
  Formulas and definitions for Cash Compound Rate (%/day), Daily NQ Profit (G/d), Production Days, and Quietus Planting Schedules.

---

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute.
