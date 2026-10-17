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

#### Sample Optimizer Output (Daily Action Plan):
```
======================================================================================
 HARVESTELLA CROP ALLOCATION OPTIMIZER: SUMMER
======================================================================================
 Config File     : configs/summer.yaml
 Current Day     : Day 18
 Planning Timeline: Day 18 -> Day 30 (13d Quietus window)
 Capital Budget  : 51,600 G
 Plot Capacities : Farm 60 -> 196 | Waterside 36 -> 81 | Cave 54 -> 81
--------------------------------------------------------------------------------------
 OPTIMAL DAILY ACTION PLAN (Day-to-Day Time-Indexed Compounding Model)
--------------------------------------------------------------------------------------
 [Day 18] Morning Wallet: 51,600 G
   Biome      Crop Name          Vendor      Qty  Seed Spent Harvest Days     Net Profit
   ----------------------------------------------------------------------------------
   Farm       Carrop             Lethe        34      3,570 G D19             +       340 G
   Farm       Nemean Tomato      Nemea        26      4,420 G D23..D28 (6x)   +     5,720 G
   Waterside  Islet Watermelon   Shatolla      3      7,500 G D30             +     6,300 G
   Waterside  Nectarcane         Shatolla     33     12,210 G D22, D25, D28   +    12,540 G
   Spent Today: 45,300 G | End-of-Day Wallet: 6,300 G

 [Day 19] Morning Wallet: 6,300 G
   Harvest & Ship: 34x Carrop (Farm) (Single harvest, soil freed) -> +3,910 G
   Biome      Crop Name          Vendor      Qty  Seed Spent Harvest Days     Net Profit
   ----------------------------------------------------------------------------------
   Farm       Carrop             Lethe        19      1,995 G D20             +       190 G
   Farm       Stellar Wheat      Lethe        48      1,920 G D21             +       720 G
   Spent Today: 5,910 G | End-of-Day Wallet: 390 G

 [Day 20] Morning Wallet: 4,300 G | Payout Arrived: +3,910 G
   Harvest & Ship: 40x Carrop (Farm) (Single harvest, soil freed) -> +4,600 G
   ...
 [Day 31 - Quietus Morning] Final Payout Arrived: +73,515 G | Final Wallet: 145,240 G
--------------------------------------------------------------------------------------
 RESOURCE UTILIZATION & FINANCIAL SUMMARY
--------------------------------------------------------------------------------------
 Total Season Net Profit: +  93,640 G across all restock stages
 Final Projected Wallet :  145,240 G on Day 30 (Quietus)
======================================================================================
```

---

### Configuring Your Farm Profile

Customize your farm parameters in `configs/<season>.yaml`:

```yaml
# Current Game Calendar & Budget
current_day: 18           # Optimize starting from today through Day 30 (Quietus)
wallet_gold: 51600        # Current gold in pocket

# Optional Variety Limit (Cardinality Constraint):
# Set to an integer (e.g., 2 or 3) to limit farm management chaos, or null for unconstrained
max_crop_varieties: null

# Physical Available Plot Capacities
# Supports static numbers OR dynamic stepped milestone schedules as you expand land
free_plots:
  farm:
    start: 60             # Plots free right now on current_day
    19: 114               # Expands to 114 on Day 19
    22: 156               # Expands to 156 on Day 22
    30: 196               # Final farm capacity on Day 30
  waterside: 36           # Static 36 water plots
  cave: 54                # Static 54 cave plots

# Story Unlock Gates (set to false if a town vendor is not yet reached in the story)
unlocked_towns:
  Lethe: true
  Nemea: true
  Shatolla: true
  Argene: true
  Abandoned Eden: false

# Store Inventory Overrides (default: 99 per 10-day restock cycle)
# Useful if you already bought seeds earlier in the current 10-day window
seed_stock:
  Morrocorn (Lethe): 0    # Sold out
  Carrop (Nemea): 21      # 21 remaining in stock
  Islet Watermelon: 99
```

---

### Renovator Plot Expansion Benchmarks (Levels 1–9)

Farm expansions are permanent (they carry over into all future seasons) and are purchased in batches from the Renovator in Lethe. Use this table as a reference for the `farm` capacity values to configure in your YAML files:

| Farm Level | Upgrade Cost | Plot Increment | Total Farm Tiles | Cost / Tile | Payback @ 35 G/d | Strategic Assessment |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| Level 1 | Free | Starting (7×7) | 49 tiles | — | — | Starting plot; stamina-constrained. |
| Level 2 | 3,000 G | +49 tiles (7×7) | 98 tiles | 61.2 G | 1.7 days | Rush post-Ch 2; <2 day payback. |
| Level 3 | 8,000 G | +49 tiles (7×7) | 147 tiles | 163.3 G | 4.7 days | Completes top row (21×7) for Summer. |
| Level 4 | 15,000 G | +49 tiles (7×7) | 196 tiles | 306.1 G | 8.7 days | Breaks into row 2; needs Sprinklers. |
| Level 5 | 25,000 G | +49 tiles (7×7) | 245 tiles | 510.2 G | 14.6 days | Mid-game scale; pair with Makers. |
| Level 6 | 40,000 G | +49 tiles (7×7) | 294 tiles | 816.3 G | 23.3 days | Completes row 2; needs charged hammer. |
| Level 7 | 80,000 G | +49 tiles (7×7) | 343 tiles | 1,632.7 G | 46.6 days | Late-game expansion (~1.5 season payback). |
| Level 8 | 120,000 G | +49 tiles (7×7) | 392 tiles | 2,449.0 G | 70.0 days | Dedicated space for fruit tree orchards. |
| Level 9 (Max) | 200,000 G | +49 tiles (7×7) | 441 tiles | 4,081.6 G | 116.6 days | Completionist goal (full 21×21). |

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
├── optimize_crop_allocation.py         # Day-to-Day Planting Schedule & Report Generator CLI
├── build_crop_data.py                  # Master Data Pipeline (reorders, splits, computes metrics)
├── crop_master_catalog.csv             # Complete Master Agricultural Data
│
├── docs/                               # 📁 Detailed Mathematical & Economic Guides
│   ├── crop_solver_guide.md            # MILP formulation, Big-M method, and Solver Walkthrough
│   └── crop_metrics_guide.md           # ROI & Daily Profit Formulas
│
├── configs/                            # 📁 User Season Configurations (Gold, Plots, Horizons)
│   ├── spring.yaml, summer.yaml, fall.yaml, winter.yaml
│
├── seasons/                            # 📁 Per-Season Analyzed Data CSVs
│   ├── spring.csv, summer.csv, fall.csv, winter.csv
│
└── scripts/                            # 📁 Pipeline Engine & Solver Modules
    ├── crop_solver.py                  # Time-Indexed MILP Engine & Daily Ledger Simulation
    ├── compute_crop_metrics.py
    ├── split_crops_by_season.py
    └── reorder_crop_catalog.py
```

---

### Deep-Dive Reference Guides

- **[Crop Allocation Solver Guide](docs/crop_solver_guide.md)**:
  Detailed mathematical documentation of `solve_allocation()` in `scripts/crop_solver.py`:
  - Day-to-Day Time-Indexed MILP model with overnight cash compounding.
  - Multi-Dimensional Bounded Integer Knapsack classification.
  - Big-M method for `max_crop_varieties` cardinality constraints.
  - Full variable reference table, Summer numerical walkthrough, and `DailyRecord` simulation ledger.
- **[Crop Metrics & Economics Guide](docs/crop_metrics_guide.md)**:
  Formulas and definitions for Cash Compound Rate (%/day), Daily NQ Profit (G/d), Production Days, and Quietus Planting Schedules.

---

## License

This project is licensed under the MIT License - feel free to use, modify, and distribute.
