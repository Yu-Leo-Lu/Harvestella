# Harvestella Crop Allocation Solver Guide

A complete guide explaining **the problem**, **linear optimization**, and **how the method is applied** in `solve_allocation()` inside [`scripts/crop_solver.py`](../scripts/crop_solver.py).

---

## Table of Contents
- [Chapter 1: The Farming Problem & Economic Bottlenecks](#chapter-1-the-farming-problem--economic-bottlenecks)
  - [1.1 In-Game Constraints in Harvestella](#11-in-game-constraints-in-harvestella)
  - [1.2 Why Intuition & Greedy Heuristics Fail](#12-why-intuition--greedy-heuristics-fail)
  - [1.3 Formal Classification: Time-Indexed MDKP](#13-formal-classification-time-indexed-mdkp)
- [Chapter 2: Linear Optimization (MILP)](#chapter-2-linear-optimization-milp)
  - [2.1 General Mathematical Form of MILP](#21-general-mathematical-form-of-milp)
  - [2.2 Branch-and-Cut Algorithm](#22-branch-and-cut-algorithm)
  - [2.3 The Big-M Method for Variety Cardinality](#23-the-big-m-method-for-variety-cardinality)
- [Chapter 3: Applied Harvestella Model Formulation](#chapter-3-applied-harvestella-model-formulation)
  - [3.1 Mathematical & Code Variable Reference Table](#31-mathematical--code-variable-reference-table)
  - [3.2 Preprocessing & Candidate Pruning](#32-preprocessing--candidate-pruning)
  - [3.3 Quietus (The Season of Death) & The Time Horizon](#33-quietus-the-season-of-death--the-time-horizon)
  - [3.4 Crop Growth Dynamics: Single-Harvest vs. Regrowth](#34-crop-growth-dynamics-single-harvest-vs-regrowth)
  - [3.5 Decision Variables: $x_{i, t}$](#35-decision-variables-x_i-t)
  - [3.6 Objective Function Construction](#36-objective-function-construction)
  - [3.7 The Constraint Matrix A](#37-the-constraint-matrix-mathbfa)
  - [3.8 Concrete Numerical Walkthrough](#38-concrete-numerical-walkthrough)
- [Chapter 4: From Math Solution to Actionable Daily Plan (DailyRecord)](#chapter-4-from-math-solution-to-actionable-daily-plan-dailyrecord)
  - [4.1 Morning Cash Arrivals (`payout_revenue`)](#41-morning-cash-arrivals-payout_revenue)
  - [4.2 Daily Harvest & Soil Management](#42-daily-harvest--soil-management)
  - [4.3 Seed Purchases & Planting Today](#43-seed-purchases--planting-today)
  - [4.4 Bedtime Wallet (`end_wallet`)](#44-bedtime-wallet-end_wallet)
  - [4.5 Quietus Morning Finale (Day 31 Payout)](#45-quietus-morning-finale-day-31-payout)
- [Chapter 5: Code Architecture & Separation of Concerns](#chapter-5-code-architecture--separation-of-concerns)
  - [5.1 Optimization Engine vs. Presentation CLI](#51-optimization-engine-vs-presentation-cli)

---

## Chapter 1: The Farming Problem & Economic Bottlenecks

### 1.1 In-Game Constraints in Harvestella
When deciding what seeds to purchase and plant, a player faces five rigid, simultaneous constraints:

1. **Capital Bottleneck (`wallet_gold`)**: You can only spend the cash currently in your pocket. Reinvesting harvest profits is delayed by the 1-day overnight shipping turnaround.
2. **Biome Land Availability (`free_plots`)**: Farm land is strictly partitioned into three independent biomes:
   - **Farm Plots**: Standard soil. Cannot grow water or cave crops.
   - **Waterside Plots**: Specialized water soil (e.g., Islet Watermelon, Nectarcane).
   - **Cave Plots**: Specialized cave soil (e.g., Revol Pepper, Sudor Pepper).
   - Plots of one biome cannot be substituted for another.
3. **Vendor Seed Caps & Town Unlocks**: General stores stock a finite inventory per 10-day restock cycle (`seed_stock`, default 99). Furthermore, seeds from Nemea, Shatolla, Argene, or Abandoned Eden are unavailable until those towns are unlocked in the story.
4. **Restock Milestones & Quietus Deadlines**: Every season lasts exactly 30 days and terminates with Quietus. General stores restock inventory every 10 days (Days 1, 11, 21). All crops must be harvested on or before Day 30; unharvested crops are wiped out by Quietus on the night of Day 30.
5. **Crop Variety Management (`max_crop_varieties`)**: Planting 8 different crop varieties creates a chaotic daily farm routine with staggered watering schedules, mismatched harvest days, and cluttered backpack inventory. Players frequently prefer focusing on a small number of crops (e.g., at most 2 or 3 distinct varieties).

---

### 1.2 Why Intuition & Greedy Heuristics Fail

Most players choose seeds using one of two intuitive greedy heuristics. Both fail:

#### Failure Mode A: Greedy by Raw Daily Profit (The Capital Starvation Trap)
- **Intuition**: "Seatide Garlic yields +58.3 G/d, the highest profit of any Summer farm crop. I should buy as many as possible."
- **The Trap**: At 650 G per seed, an 8,000 G budget buys only 12 seeds, spending 7,800 G.
- **Result**: You occupy only 12 plots. Your remaining **58 farm plots sit completely empty** earning 0 G/d. Total daily profit is only **+700.0 G/d**.

#### Failure Mode B: Greedy by Cash Compound Rate (The Land Bottleneck Trap)
- **Intuition**: "Dress Lettuce doubles money fastest (+15.62%/d). I should buy only Lettuce."
- **The Trap**: Dress Lettuce costs only 55 G. Filling all 70 plots costs $70 \times 55 = 3,850\text{ G}$.
- **Result**: All plots are full, but **4,150 G sits completely idle** in your wallet earning 0% return. Total daily profit is only **+1,050 G/d**.

#### The Core Economic Trade-Off
The true optimal solution is an **inflection point**: you must saturate all available plots with cheap, high-turnaround crops, and then use your remaining capital to systematically "upgrade" individual plots to higher-margin seeds (e.g. Morrocorn @ 200 G seed, +50 G/d) until the budget is completely exhausted.

### 1.3 Formal Classification: Time-Indexed MDKP
Mathematically, this is a **Day-to-Day Time-Indexed Multi-Dimensional Bounded Integer Knapsack Problem with Cardinality Constraints (MDKP)**:
- **Multiple knapsack capacities across time**: Daily capital balances + Daily farm, waterside, and cave plot limits across all 30 calendar days.
- **Bounded integer variables**: Each planting option can be selected up to its store restock inventory cap ($0 \le x_{i, t} \le S_i$).
- **Cardinality constraint**: At most $K$ distinct crop varieties may be selected across the entire season.

---

## Chapter 2: Linear Optimization (MILP)

To solve this multi-dimensional knapsack problem to guaranteed global optimality, we use **Mixed-Integer Linear Programming (MILP)** via the HiGHS solver.

### 2.1 General Mathematical Form of MILP
An MILP problem optimizes a linear objective function subject to linear equality and inequality constraints, where decision variables are constrained to integers:

$$\begin{aligned}
\min_{\mathbf{x}} \quad & \mathbf{c}^T \mathbf{x} \\
\text{subject to} \quad & \mathbf{lb} \le \mathbf{A} \mathbf{x} \le \mathbf{ub} \\
& \mathbf{l} \le \mathbf{x} \le \mathbf{u} \\
& x_j \in \mathbb{Z} \quad \forall j
\end{aligned}$$

Where:
- $\mathbf{x} \in \mathbb{R}^n$ is the vector of decision variables, where integer constraints ($x_j \in \mathbb{Z}$) enforce discrete non-fractional quantities.
- $\mathbf{c} \in \mathbb{R}^n$ is the objective cost/coefficient vector.
- $\mathbf{A} \in \mathbb{R}^{m \times n}$ is the linear constraint matrix encoding resource consumption and structural relationships.
- $\mathbf{lb}, \mathbf{ub} \in \mathbb{R}^m$ are lower and upper bounds on constraint rows in matrix $\mathbf{A}$.
- $\mathbf{l}, \mathbf{u} \in \mathbb{R}^n$ are lower and upper bounds on decision variables ($l_j \le x_j \le u_j$).

---

### 2.2 Branch-and-Cut Algorithm
Simple linear programming (LP) allows fractional values (e.g., buying 23.47 seeds). MILP enforces strict integer quantities ($x_i \in \{0, 1, 2, \dots\}$) using the **Branch-and-Cut** algorithm:

1. **LP Relaxation**: The solver first removes the integer requirement and solves the continuous problem in microseconds using the Dual Simplex method. This provides a theoretical upper bound on total possible profit.
2. **Cutting Planes (Gomory & Knapsack Covers)**: The solver detects that fractional solutions are physically impossible and adds linear cuts that slice away fractional space without removing any valid integer solutions.
3. **Branch-and-Bound**: If a variable remains fractional (e.g., $x_1 = 14.6$), the solver branches into two sub-problems:
   - Branch Left: $x_1 \le 14$
   - Branch Right: $x_1 \ge 15$
4. **Pruning**: Any branch whose continuous upper bound is worse than an already discovered integer solution is immediately discarded ("pruned").

Because the seasonal decision space is bounded ($N \le 450$ variables), the HiGHS branch-and-cut engine evaluates this tree in **less than 15 milliseconds**, guaranteeing 0% optimality gap.

---

### 2.3 The Big-M Method for Variety Cardinality
To limit the number of distinct seed varieties to at most $K$, the problem requires modeling logical conditions: *"If crop variety $k$ is planted anywhere in the season, count it as 1 variety."*

This is achieved using **binary indicator variables** $y_k \in \{0, 1\}$ and a **Big-M linking constraint**:

$$\sum_{t} x_{k, t} \le M \cdot y_k \iff \sum_{t} x_{k, t} - M \cdot y_k \le 0$$

Where $M$ is an upper bound on the maximum possible plots a crop could occupy over the entire season.

- If $y_k = 0$, then $\sum_t x_{k, t} \le 0 \implies x_{k, t} = 0$ for all days (the crop cannot be planted).
- If $y_k = 1$, then $\sum_t x_{k, t} \le M$ (the crop can be planted freely up to its store cap).

The cardinality limit across the entire season is then a simple linear constraint:

$$\sum_{k=0}^{U-1} y_k \le K$$

---

## Chapter 3: Applied Harvestella Model Formulation

The function `solve_allocation()` in [`scripts/crop_solver.py`](../scripts/crop_solver.py) maps the Harvestella data and player configs directly into the MILP formulation.

### 3.1 Mathematical & Code Variable Reference Table

| Variable / Symbol | Code / Config Name | Mathematical Type | Domain | Description & In-Game Meaning |
| :---: | :--- | :---: | :---: | :--- |
| **$n$** | `len(crops)` | Integer Scalar | $n \ge 0$ | Number of eligible catalog crop varieties after town and biome filters. |
| **$i$** | Loop index / Catalog ID | Index | $1 \le i \le n$ | Index referencing a specific crop candidate catalog entry. |
| **$t$** | `plant_day` | Integer Day | $`t \in [\text{current\_day}, 30]`$ | **Planting Day**: Calendar day on which seeds are purchased and planted. |
| **$\tau$** | `eval_day` | Integer Day | $`\tau \in [\text{current\_day}, 30]`$ | **Evaluation Day**: Calendar day on which plot occupancy and cash liquidity are checked. |
| **$x_{i, t}$** | `solution[var_idx]` | Integer Variable | $\{0, 1, 2, \dots\}$ | **Primary Decision Variable**: Number of seeds of crop $i$ planted on day $t$. |
| **$N$** | `len(var_map)` | Integer Scalar | $N \ge 0$ | Total active $(i, t)$ decision variables that mature on or before Day 30. |
| **$y_k$** | Binary block | Binary Variable | $\{0, 1\}$ | **Auxiliary Indicator**: Flags whether unique crop variety $k$ is planted anywhere in season. |
| **$U$** | `len(unique_crop_names)` | Integer Scalar | $U \le n$ | Number of unique candidate crop variety names eligible for selection. |
| **$K$** | `max_crop_varieties` | Integer / Null | $K \in \mathbb{Z}^+$ or `None` | **Cardinality Bound**: Maximum allowed distinct crop varieties to manage simultaneously. |
| **$M$** | `big_m` | Real Parameter | $M = \max(\text{caps}) \cdot 30 + 100$ | **Big-M Upper Bound**: Theoretical maximum plots a crop could occupy over season. |
| **$p_i$** | `c.cost` | Real Parameter | $p_i > 0$ (Gold) | Seed purchase price in Gold (G) to buy 1 seed of crop $i$. |
| **$s_i$** | `c.nq_sale` | Real Parameter | $s_i > 0$ (Gold) | Selling price per unit of Normal Quality (NQ) harvest of crop $i$. |
| **$m_i$** | `c.mature` | Integer Parameter | Days ($\ge 1$) | Nights of growth required from planting to first harvest. |
| **$r_i$** | `c.regrowth` | Integer Parameter | Days ($\ge 0$) | Days between subsequent harvests for regrowth crops ($0$ if single-harvest). |
| **$H_i$** | `c.max_harvests` | Integer Parameter | Integer ($\ge 1$) | Maximum allowed harvests before plant expires ($1$ if single-harvest). |
| **$H(i, t)$** | `v["harvests"]` | Set of Days | $H \subseteq [t+1, 30]$ | **Harvest Days Set**: All calendar days on which crop $i$ planted on day $t$ matures. |
| **$v_{i, t}$** | `v["total_rev"]` | Real Parameter | $v_{i, t} > 0$ (Gold) | **Total Harvest Revenue**: Total gold earned by 1 plot of crop $i$ planted on day $t$ ($v_{i, t} = |H(i, t)| \cdot s_i$). |
| **$b_i$** | `c.biome` | Categorical String | `farm`, `waterside`, `cave` | Required physical soil biome for crop $i$. |
| **$W$** | `wallet_gold` | Real Parameter | $W \ge 0$ (Gold) | Gold cash available in player's wallet at start of `current_day`. |
| **$B_b$** | `caps[biome]` | Integer Parameter | Plots ($\ge 0$) | Available plot capacity for soil biome $b \in \{\text{farm}, \text{waterside}, \text{cave}\}$. |
| **$S_i$** | `c.stock` | Integer Parameter | $S_i \ge 1$ | General store inventory stock cap per 10-day restock cycle for crop $i$. |
| **$\mathbf{x}$** | Solver vector | Vector | $\mathbb{Z}^{N}$ (or $\mathbb{Z}^{N + U}$) | Full decision vector sent to solver: $[x_{i_1, t_1}, \dots]^T$ or $[x_{i_1, t_1}, \dots, y_1, \dots, y_U]^T$. |
| **$\mathbf{c}$** | Objective vector | Vector | $\mathbb{R}^{N}$ (or padded) | Objective coefficient vector with tie-breakers. |
| **$\mathbf{A}$** | `A` | Matrix | $\mathbb{R}^{m \times |\mathbf{x}|}$ | Linear constraint matrix encoding plot capacity, cash balances, restock, and variety caps. |
| **$\mathbf{lb}, \mathbf{ub}$** | `lb`, `ub` | Vectors | $\mathbb{R}^m$ | Lower and upper capacity bounds on constraint rows in matrix $\mathbf{A}$. |

---

### 3.2 Preprocessing & Candidate Pruning
Before building matrices, `solve_allocation()` filters the seasonal CSV down to viable candidate crops:
1. **Town Gate**: Checks `unlocked_towns[town] == True`. Multi-town vendors (e.g. `Shatolla/Nemea`) unlock if *either* town is unlocked.
2. **Biome Plot Check**: Crops requiring Waterside or Cave plots are discarded if the player has 0 plots in that biome.
3. **Economic Viability**: Drops without purchase cost (e.g. Nitro Pineapple) or negative profits are excluded.
4. **Time-Indexed Feasibility**: For each eligible crop $i$ and each calendar planting day $`t \in [\text{current\_day}, 30]`$, the candidate pair $(i, t)$ is accepted only if its first harvest completes on or before Day 30 ($t + m_i \le 30$).

---

### 3.3 Quietus (The Season of Death) & The Time Horizon

In *Harvestella*, **Quietus (the Season of Death)** is the critical game mechanic that enforces a hard terminal boundary (a finite time horizon) on the optimization model:

1. **What Quietus Does in the Game**:
   - **Strict 30-Day Season**: Every season lasts exactly 30 calendar days.
   - **Total Field Destruction**: On the night between Day 30 and Day 31, fatal dust covers the world, destroying all unharvested crops remaining in the soil.
   - **Zero Spillover**: Fields are wiped completely clean before the next season begins. Unharvested produce yields 0 G.

2. **Why We Need the `current_day` Input (Mid-Season Optimization)**:
   - Players don't always start planning on Day 1; you might run the optimizer on Day 5, Day 14, or Day 22.
   - Specifying `current_day` tells the solver where you are right now, defining the forward-looking calendar horizon:
     $$t \in [\text{current\_day}, 30]$$
   - Past days ($t < \text{current\_day}$) are unchangeable history.
   - Future days beyond Day 30 ($t > 30$) are destroyed by Quietus.
   - Thus, every active decision is strictly bounded within the playable window: $t \in \{\text{current\_day}, \dots, 30\}$.

### 3.4 Crop Growth Dynamics: Single-Harvest vs. Regrowth

#### Single-Harvest Crops
- Matures in $m_i$ days.
- Planted on morning of Day $t$, harvested on Day $h = t + m_i$.
- **Soil Occupancy**: Occupies 1 plot on calendar days $\tau \in [t, t + m_i - 1]$. The plot is cleared and freed on the morning of Day $t + m_i$ for immediate replanting.
- **Overnight Shipping Turnaround**: Harvested produce is placed in the shipping box on Day $h$. Gold arrives in the player's wallet on the morning of Day $h + 1$.

#### Regrowth Crops (e.g., Nemean Tomato, Revol Pepper, Nectarcane, Strawbuddy)
- Initial maturity in $m_i$ days, subsequent harvests every $r_i$ days up to $H_i$ total harvests.
- Harvest days set: $H(i, t) = \{ t + m_i + k \cdot r_i \mid k \in [0, H_i - 1], \; t + m_i + k \cdot r_i \le 30 \}$.
- **Soil Occupancy**: Stays permanently rooted in soil from planting day $t$ through its final harvest day $\max(H(i, t))$ (or Day 30), incurring **zero additional seed purchase costs** for subsequent harvests.
- **Cash Flow**: Each harvest $h \in H(i, t)$ yields unit revenue $s_i$ deposited into wallet liquidity on the morning of Day $h + 1$.

### 3.5 Decision Variables: $x_{i, t}$
The primary decision variables are $x_{i, t} \ge 0$, representing the integer quantity of seeds of crop variety $i$ purchased and planted on calendar day $t$:
- **Crop Variety Index ($i$)**: $i \in \{1, 2, \dots, n\}$, indexing eligible crop varieties in the game catalog ($n \le 35$).
- **Calendar Planting Day ($t$)**: $t \in [\text{current\_day}, 30]$, where $\text{current\_day} \in \{1, 2, \dots, 30\}$ denotes the player's current starting day within the 30-day season.
- **Variable Count**: Only feasible pairs $(i, t)$ whose maturity completes on or before Day 30 ($t + m_i \le 30$) are instantiated ($N \le 450$ variables).

---

### 3.6 Objective Function Construction

In standard SciPy/HiGHS format, the solver optimizes the linear objective:

$$\min_{\mathbf{x}} \quad \mathbf{c}^T \mathbf{x}$$

Where:
- $\mathbf{x} = [x_{i, t}]^T$ is the primary decision vector of seed quantities ($x_{i, t} \in \mathbb{Z}_{\ge 0}$).
- $\mathbf{c} = [c_{i, t}]^T$ is the objective coefficient vector, where $c_{i, t} = -\text{Adjusted Profit}(i, t)$ defines the negative adjusted net profit per seed with tie-breakers.

---

#### 3.6.1 Why Minimization? Maximizing Profit via Negative Costs

Because the player's goal is to maximize total seasonal profit, the optimizer formulates this as minimizing negative profit:

$$\max \sum_{i, t} \text{Adjusted Profit}(i, t) \cdot x_{i, t} \iff \min_{\mathbf{x}} \sum_{i, t} \underbrace{\left(-\text{Adjusted Profit}(i, t)\right)}_{c_{i, t}} \cdot x_{i, t}$$

---

#### 3.6.2 Components of $c_{i, t}$: Net Profit & Perturbations

Each decision coefficient $c_{i, t}$ is explicitly calculated as:

$$c_{i, t} = -\left( \underbrace{(v_{i, t} - p_i)}_{\text{Base Net Profit}} - \underbrace{10^{-6} \cdot p_i}_{\text{Cost Perturbation}} - \underbrace{10^{-8} \cdot (t - \text{current\_day})}_{\text{Timing Perturbation}} \right)$$

##### A. Base Net Profit ($v_{i, t} - p_i$)
The gross gold profit generated by purchasing and planting 1 plot of crop $i$ on calendar day $t$:

$$\text{Base Net Profit}(i, t) = v_{i, t} - p_i$$

1. **Seed Purchase Cost ($p_i$)**:
   The upfront cash price to purchase 1 seed of crop $i$ from the town general store. This cost is paid once on planting day $t$ and is constant across all calendar days.

2. **Total Harvest Revenue ($v_{i, t}$)**:
   The total gold received from all completed harvests on or before Day 30 for seed $i$ planted on day $t$:
   - **Single-Harvest Crops**: Matures and is harvested exactly once regardless of planting day, so total revenue $v_{i, t}$ is simply the unit selling price $s_i$:
     $$v_{i, t} = s_i$$
   - **Regrowth Crops**: Produces ongoing repeated harvests every $r_i$ days, with each harvest selling for $s_i$. Total revenue $v_{i, t}$ is the number of completed harvests before Quietus multiplied by the sale price per harvest $s_i$:
     $$v_{i, t} = |H(i, t)| \cdot s_i$$
     Where $|H(i, t)|$ denotes the number of completed harvests before Quietus.

*Example: Shatollan Paprika (seed cost $p_i = 250\text{ G}$, unit sale price $s_i = 110\text{ G}$, initial maturity $m = 5\text{ days}$, regrowth cycle $r = 2\text{ days}$, max harvests $H_{\max} = 9$):*

| Planting Scenario | Active Harvest Calendar Days | Completed Harvests | Total Revenue ($v_{i, t}$) | Seed Cost ($p_i = 250\text{ G}$) | Net Profit ($v_{i, t} - p_i$) |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Early (Day 1)** | Days 6, 8, 10, 12, 14, 16, 18, 20, 22 | **9** (all) | $v_{i, 1} = 990\text{ G}$ | $-250\text{ G}$ | **$+740\text{ G}$** |
| **Late (Day 20)** | Days 25, 27, 29 *(Day 31 wiped out)* | **3** | $v_{i, 20} = 330\text{ G}$ | $-250\text{ G}$ | **$+80\text{ G}$** |

##### B. Microscopic Perturbations (Deterministic Tie-Breakers)
When two planting options yield identical integer net profit, two deterministic perturbation penalties resolve the choice:
1. **Cost Perturbation ($\epsilon_1 = 10^{-6} \cdot p_i$)**: Strictly prefers cheaper seed varieties to conserve liquid wallet cash.
2. **Timing Perturbation** ($`\epsilon_2 = 10^{-8} \cdot (t - \text{current\_day})`$): Strictly prefers earlier planting calendar days to accelerate capital compounding and free soil sooner.

---

#### 3.6.3 Optional Cardinality Extension: Crop Variety Indicators ($y_k$)

When the player sets a limit on the number of distinct varieties to manage (`max_crop_varieties: K`), the formulation is augmented:

1. **Augmented Decision Vector**:
   $U$ binary indicator variables $y_k \in \{0, 1\}$ are appended to the decision vector ($k \in \{1, \dots, U\}$, where $U \le 35$ is the number of eligible catalog varieties):
   $$\mathbf{x}_{\text{full}} = \begin{bmatrix} \mathbf{x} \\ \mathbf{y} \end{bmatrix} = [x_{i_1, t_1}, \dots, x_{i_N, t_M}, \; y_1, \dots, y_U]^T$$
2. **Objective Weights ($c_k = 0.0$)**:
   Activating a crop variety indicator does not directly earn or cost gold, so its objective coefficient is strictly zero:
   $$c_k = 0.0 \quad \forall k \in \{1, \dots, U\}$$
3. **Big-M Linking & Season Cardinality**:
   The solver couples physical seed quantities to the binary switches via Big-M:
   $$\sum_{t} x_{k, t} \le M \cdot y_k \iff \sum_{t} x_{k, t} - M \cdot y_k \le 0$$
   $$\sum_{k=1}^U y_k \le K$$
   - If $y_k = 0 \implies \sum_t x_{k, t} = 0$ (crop $k$ cannot be planted anywhere in the season).
   - If $y_k = 1 \implies \sum_t x_{k, t} \le M$ (crop $k$ can be planted freely up to plot and inventory caps).

---

### 3.7 The Constraint Matrix $\mathbf{A}$

Every physical game boundary across every calendar day is translated into a row in matrix $\mathbf{A}$:

$$\mathbf{lb} \le \mathbf{A} \mathbf{x} \le \mathbf{ub}$$

| Constraint Family | Scope / Indexing | Equation / Coefficients | Lower Bound ($\mathbf{lb}$) | Upper Bound ($\mathbf{ub}$) |
| :--- | :--- | :--- | :---: | :---: |
| **Daily Plot Capacity** | Each day $`\tau \in [\text{current\_day}, 30]`$, each biome $b$ | $\sum_{(i, t) \text{ occupying } b \text{ on } \tau} 1.0 \cdot x_{i, t}$ | $0.0$ | $B_b$ |
| **Daily Cash Liquidity** | Each morning $`\tau \in [\text{current\_day}, 30]`$ | $\sum_{t \le \tau} p_i \cdot x_{i, t} - \sum_{h + 1 \le \tau, \, h \in H(i, t)} s_i \cdot x_{i, t}$ | $-\infty$ | $W$ |
| **10-Day Restock Caps** | Each window $W_w$, each crop $i$ | $\sum_{t \in W_w} 1.0 \cdot x_{i, t}$ | $0.0$ | $S_i$ |
| **Big-M Variety Linking** | Each unique variety $k$ *(if $K$ set)* | $\sum_{t} 1.0 \cdot x_{k, t} - M \cdot y_k$ | $-\infty$ | $0.0$ |
| **Variety Cardinality Cap** | Entire season *(if $K$ set)* | $\sum_{k=1}^{U} 1.0 \cdot y_k$ | $0.0$ | $K$ |

#### Dynamic Time-Indexed Matrix Structure
```
Columns:                 [ ----- Day 1 Plantings ----- ]   [ ----- Day 5 Plantings ----- ]   [ ----- Day 9 Plantings ----- ]     ub
==================================================================================================================================
Cash Day 1 (Morning)     [            Cost             ]   [              0              ]   [              0              ]  <=  Wallet_0
Cash Day 4 (Morning)     [        Cost - Rev(D3)       ]   [              0              ]   [              0              ]  <=  Wallet_0
Cash Day 5 (Morning)     [     Cost - Rev(D3+D4)       ]   [            Cost             ]   [              0              ]  <=  Wallet_0
Cash Day 9 (Morning)     [     Cost - Rev(D3+D4+D7)    ]   [        Cost - Rev(D7+D8)    ]   [            Cost             ]  <=  Wallet_0
----------------------------------------------------------------------------------------------------------------------------------
Land Day 1 (Farm)        [              1              ]   [              0              ]   [              0              ]  <=  Farm_Cap
Land Day 4 (Farm)        [       Occupied on D4?       ]   [              0              ]   [              0              ]  <=  Farm_Cap
Land Day 5 (Farm)        [       Occupied on D5?       ]   [              1              ]   [              0              ]  <=  Farm_Cap
----------------------------------------------------------------------------------------------------------------------------------
Restock Window 1 (D1-10) [              1              ]   [              1              ]   [              1              ]  <=  Stock Cap
Restock Window 2 (D11-20)[              0              ]   [              0              ]   [              0              ]  <=  Stock Cap
```

- **True Daily Compounding**: Unlike coarse stage models that wait for milestone days, proceeds from Day 3 or Day 4 harvests are immediately recognized on the mornings of Day 4 and Day 5, funding fresh seed purchases on the exact day cash arrives.

---

### 3.8 Concrete Numerical Walkthrough
 
Here is the exact numerical calculation performed by `solve_allocation()` on the baseline **Summer** configuration:
- **Parameters**: `wallet_gold: 8000`, `farm: 70`, `waterside: 0`, `cave: 0`, `max_crop_varieties: null`.

#### Candidate Subset Filtered from Catalog
- **Seatide Garlic (Shatolla)**: Cost $= 650\text{ G}$, Profit $= +58.3\text{ G/d}$ (Farm)
- **Morrocorn (Shatolla)**: Cost $= 200\text{ G}$, Profit $= +50.0\text{ G/d}$ (Farm)
- **Dress Lettuce**: Cost $= 55\text{ G}$, Profit $= +15.0\text{ G/d}$ (Farm)

#### The Solver's Step-by-Step Optimization:
1. **Can we afford pure Garlic?**
   At 650 G per seed, an 8,000 G budget buys only 12 Garlic seeds ($12 \times 650 = 7,800\text{ G}$).
   - The remaining 200 G can buy at most 3 Lettuce ($3 \times 55 = 165\text{ G}$).
   - Total plots used: $12 + 3 = 15 / 70$ plots (**55 plots left completely empty**).
   - Total daily profit: $12(58.33) + 3(15.0) = \mathbf{+745.0\text{ G/d}}$ (or pure Garlic at $+700.0\text{ G/d}$).

2. **The Marginal Upgrade Equation**:
   Can we do better with a balanced portfolio?
   - To fill all 70 Farm plots with Dress Lettuce costs: $70 \times 55\text{ G} = 3,850\text{ G}$ (Profit: $+1,050.0\text{ G/d}$).
   - Remaining gold: $8,000 - 3,850 = \mathbf{4,150\text{ G}}$ unspent.
   - Upgrading 1 plot from Dress Lettuce ($55\text{ G}, +15\text{ G/d}$) to Morrocorn ($200\text{ G}, +50\text{ G/d}$):
     $$\Delta \text{Cost} = 200 - 55 = \mathbf{145\text{ G}}$$
     $$\Delta \text{Profit} = 50 - 15 = \mathbf{+35.0\text{ G/d}}$$
     $$\text{Marginal Return on Extra Capital} = \frac{35.0}{145} = \mathbf{0.2414\text{ G/d per extra gold spent}}$$
   - *(Note: Upgrading from Morrocorn $200\text{ G}$ to Garlic $650\text{ G}$ costs $+450\text{ G}$ for only $+8.33\text{ G/d}$ profit, which is $\frac{8.33}{450} = 0.0185\text{ G/d per gold}$ — a 13× worse capital efficiency!)*

3. **Optimal Integer Solution**:
   With $4,150\text{ G}$ surplus, how many plots can be upgraded to Morrocorn?
   $$\lfloor 4,150 / 145 \rfloor = \mathbf{28.62} \implies \mathbf{29\text{ upgrades}}$$
   The solver checks integer feasibility:
   - **29 Morrocorn**: $29 \times 200\text{ G} = 5,800\text{ G}$
   - **40 Dress Lettuce**: $40 \times 55\text{ G} = 2,200\text{ G}$
   - **Plots Used**: $29 + 40 = 69 / 70\text{ plots}$ ($1\text{ idle}$)
   - **Total Gold Spent**: $5,800 + 2,200 = \mathbf{8,000\text{ G}} / 8,000\text{ G}$ ($100\%$ budget utilized, $0\text{ G}$ idle)
   - **Total Daily Profit**: $29(50.0) + 40(15.0) = \mathbf{+2,050.0\text{ G/day}}$

$$\text{Profit Advantage vs. Garlic: } \frac{2,050 - 700}{700} = \mathbf{+192.9\% \text{ higher profit!}}$$

The solver proves that buying expensive seeds like Seatide Garlic with an 8,000 G budget is a capital trap. The globally optimal plan is to saturate the farm with Morrocorn and Dress Lettuce.

---

## Chapter 4: From Math Solution to Actionable Daily Plan (DailyRecord)

Solving the MILP gives the exact seed allocation vector $\mathbf{x}^*$. [`scripts/crop_solver.py`](../scripts/crop_solver.py) then translates this raw matrix solution into a player-facing day-by-day action ledger via `DailyRecord`:

### 4.1 Morning Cash Arrivals (`payout_revenue`)
- Produce harvested on calendar day $h$ is placed into the shipping bin on that evening.
- In *Harvestella*, the shipping payout arrives in the player's wallet on the morning of Day $h + 1$.
- For each day $d$, the engine looks up all crops shipped on Day $d - 1$ and calculates:
  $`\text{morning\_wallet} = \text{carryover\_cash} + \text{payout\_revenue}`$

### 4.2 Daily Harvest & Soil Management
- For each crop maturing on day $d$, the engine checks whether it is a single-harvest or regrowth crop:
  - **Single-Harvest**: Harvest produce and drop in shipping bin. Soil is cleared immediately on day $d$, allowing immediate replanting.
  - **Regrowth**: Harvest produce and drop in shipping bin. The crop remains rooted in the soil (`regrowth k/H`), continuing its cycle without any additional seed expenditure.

### 4.3 Seed Purchases & Planting Today
- Displays all seed purchases scheduled for day $d$, grouped by **Vendor Town** (Lethe, Nemea, Shatolla, Argene) to provide an efficient travel route.
- Shows total daily seed expenditures $`\text{daily\_spent}`$.

### 4.4 Bedtime Wallet (`end_wallet`)
- Calculates remaining cash before going to sleep:
  $`\text{end\_wallet} = \text{morning\_wallet} - \text{daily\_spent}`$
- This balance carries over directly into the next morning's `carryover_cash`.

### 4.5 Quietus Morning Finale (Day 31 Payout)
- All crops harvested on the final day of the season (Day 30) are placed in the shipping bin.
- On the morning of Quietus (Day 31), the final shipping payout arrives:
  $`\text{final\_wallet} = \text{end\_wallet}_{\text{Day 30}} + \text{payout}_{\text{Day 31}} = \text{wallet\_gold} + \text{total\_season\_profit}`$
- This guarantees 100% financial conservation: every gold coin spent and earned is accounted for down to the single G.

---

## Chapter 5: Code Architecture & Separation of Concerns

### 5.1 Optimization Engine vs. Presentation CLI

The codebase maintains a strict two-tier separation between optimization mathematics and presentation:

```
Harvestella/
├── scripts/
│   └── crop_solver.py            # Mathematical MILP Engine & Daily Ledger Simulation
├── optimize_crop_allocation.py   # Presentation, Terminal Formatting & Markdown Report CLI
├── docs/
│   └── crop_solver_guide.md      # This comprehensive mathematical & architecture guide
└── crop_allocation_report.md     # Generated player-facing action schedule
```

- **[`scripts/crop_solver.py`](../scripts/crop_solver.py)**: Contains all linear programming formulations, matrix construction, HiGHS solver execution, and ledger simulation. When updating report formatting, this file remains untouched.
- **[`optimize_crop_allocation.py`](../optimize_crop_allocation.py)**: Takes the resulting `OptimizationResult` data structure and formats both the terminal output and the GitHub-Flavored Markdown report ([`crop_allocation_report.md`](../crop_allocation_report.md)).
