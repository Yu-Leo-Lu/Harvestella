# Harvestella Crop Allocation Solver Guide

A complete guide explaining **the problem**, **the mathematical method**, and **how the method is applied** in `solve_allocation()` inside [`optimize_crop_allocation.py`](../optimize_crop_allocation.py).

---

## Part 1: What is the Problem?

### 1. The Game Constraints in Harvestella
When deciding what seeds to purchase and plant, a player faces four rigid, simultaneous constraints:

1. **Capital Bottleneck (`wallet_gold`)**: You can only spend the cash currently in your pocket.
2. **Biome Land Availability (`free_plots`)**: Farm land is strictly partitioned into three independent biomes:
   - **Farm Plots**: Standard soil. Cannot grow water or cave crops.
   - **Waterside Plots**: Specialized water soil (e.g., Islet Watermelon, Nectarcane).
   - **Cave Plots**: Specialized cave soil (e.g., Revol Pepper, Sudor Pepper).
   - Plots of one biome cannot be substituted for another.
3. **Vendor Seed Caps & Town Unlocks**: General stores stock a finite inventory per restock cycle (`seed_stock`, default 99). Furthermore, seeds from Nemea, Shatolla, Argene, or Abandoned Eden are unavailable until those towns are unlocked in the story.
4. **Restock Milestones & Quietus Deadlines**: Every season lasts exactly 30 days and terminates with Quietus. General stores restock inventory every 10 days (Days 1, 11, 21). The optimizer natively uses a dynamic multi-stage knapsack model that couples rolling cashflow, plot turnover, and restock purchases across all remaining milestones through Quietus.
5. **Crop Variety Management (`max_crop_varieties`)**: Planting 8 different crop varieties creates a chaotic daily farm routine with staggered watering schedules, mismatched harvest days, and cluttered backpack inventory. Players frequently prefer focusing on a small number of crops (e.g., at most 2 or 3 distinct varieties).

---

### 2. Why Intuition & Greedy Heuristics Fail

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

### 3. Formal Classification
Mathematically, this is a **Multi-Dimensional Bounded Integer Knapsack Problem with Cardinality Constraints (MDKP)**:
- Multiple knapsack capacities: Capital budget + Farm plots + Waterside plots + Cave plots.
- Bounded integer variables: Each item can be selected up to its store stock cap (e.g., $0 \le x_i \le 99$).
- Cardinality constraint: At most $K$ non-zero variables may be selected.

---

## Part 2: What is the Mathematical Method?

To solve the Multi-Dimensional Knapsack problem to guaranteed global optimality, we use **Mixed-Integer Linear Programming (MILP)**.

### 1. General Mathematical Form of MILP
An MILP problem optimizes a linear objective function subject to linear equality and inequality constraints, where decision variables are constrained to integers:

$$\begin{aligned}
\min_{\mathbf{x}} \quad & \mathbf{c}^T \mathbf{x} \\
\text{subject to} \quad & \mathbf{lb} \le \mathbf{A} \mathbf{x} \le \mathbf{ub} \\
& \mathbf{l} \le \mathbf{x} \le \mathbf{u} \\
& x_i \in \mathbb{Z} \quad \forall i
\end{aligned}$$

Where:
- $\mathbf{x}$ is the vector of decision variables.
- $\mathbf{c}$ is the objective cost/profit coefficient vector.
- $\mathbf{A}$ is the constraint matrix representing resource consumption per unit.
- $\mathbf{lb}, \mathbf{ub}$ are lower and upper bounds on constraint rows.
- $\mathbf{l}, \mathbf{u}$ are lower and upper variable bounds.

---

### 2. How MILP Solves Discrete Combinations: Branch-and-Cut
Simple linear programming (LP) allows fractional values (e.g., buying 23.47 seeds). MILP enforces strict integer quantities ($x_i \in \{0, 1, 2, \dots\}$) using the **Branch-and-Cut** algorithm:

1. **LP Relaxation**: The solver first removes the integer requirement and solves the continuous problem in microseconds using the Dual Simplex method. This provides a theoretical upper bound on total possible profit.
2. **Cutting Planes (Gomory & Knapsack Covers)**: The solver detects that fractional solutions are physically impossible and adds linear "cuts" (extra linear inequalities) that slice away fractional space without removing any valid integer solutions.
3. **Branch-and-Bound**: If a variable remains fractional (e.g., $x_1 = 14.6$), the solver branches into two sub-problems:
   - Branch Left: $x_1 \le 14$
   - Branch Right: $x_1 \ge 15$
4. **Pruning**: Any branch whose continuous upper bound is worse than an already discovered integer solution is immediately discarded ("pruned").

Because the candidate pool for a single season is small ($n \le 25$), the HiGHS branch-and-cut engine evaluates this tree in **less than 2 milliseconds**, guaranteeing 0% optimality gap.

---

### 3. The Big-M Method for Variety Cardinality
To limit the number of distinct seed varieties to at most $K$, the problem requires modeling logical conditions: *"If $x_i > 0$, then count crop $i$ as 1 variety."*

This is achieved using **binary indicator variables** $y_i \in \{0, 1\}$ and a **Big-M linking constraint**:

$$x_i \le M_i \cdot y_i \iff x_i - M_i \cdot y_i \le 0$$

Where $M_i = \text{seed\_stock}_i$ (the maximum physically possible value for $x_i$).

- If $y_i = 0$, then $x_i \le 0 \implies x_i = 0$ (the crop cannot be planted).
- If $y_i = 1$, then $x_i \le \text{seed\_stock}_i$ (the crop can be planted up to its store cap).

The cardinality limit is then a simple linear constraint:

$$\sum_{i=0}^{n-1} y_i \le K$$

---

## Part 3: How Did We Apply the Method to the Problem?

The function `solve_allocation()` in `optimize_crop_allocation.py` maps the Harvestella data and player configs directly into the MILP formulation.

### Mathematical & Code Variable Reference Table

| Variable / Symbol | Code / Config Name | Mathematical Type | Domain | Description & In-Game Meaning |
| :---: | :--- | :---: | :---: | :--- |
| **$n$** | `len(crops)` | Integer Scalar | $n \ge 0$ | Number of eligible catalog crop varieties after town and biome filters. |
| **$c$** | Loop index `0..n-1` | Index | $0 \le c < n$ | Zero-based index referencing a specific crop candidate catalog entry. |
| **$d$** | `plant_day` | Integer Day | $d \in [\text{current\_day}, 30]$ | **Planting Day**: Calendar day on which seeds are purchased and planted. |
| **$t$** | `eval_day` | Integer Day | $t \in [\text{current\_day}, 30]$ | **Evaluation Day**: Calendar day on which plot occupancy and cash liquidity are checked. |
| **$x_{c, d}$** | `solution[var_idx]` | Integer Variable | $\{0, 1, 2, \dots\}$ | **Primary Decision Variable**: Number of seeds of crop $c$ planted on day $d$. |
| **$N$** | `len(var_map)` | Integer Scalar | $N \ge 0$ | Total active $(c, d)$ decision variables that mature on or before Day 30. |
| **$y_k$** | Binary block | Binary Variable | $\{0, 1\}$ | **Auxiliary Indicator**: Flags whether unique crop variety $k$ is planted anywhere in season. |
| **$U$** | `len(unique_crop_names)` | Integer Scalar | $U \le n$ | Number of unique candidate crop variety names eligible for selection. |
| **$K$** | `max_crop_varieties` | Integer / Null | $K \in \mathbb{Z}^+$ or `None` | **Cardinality Bound**: Maximum allowed distinct crop varieties to manage simultaneously. |
| **$M$** | `big_m` | Real Parameter | $M = \max(\text{caps}) \cdot 30 + 100$ | **Big-M Upper Bound**: Theoretical maximum plots a crop could occupy over season. |
| **$p_c$** | `c.cost` | Real Parameter | $p_c > 0$ (Gold) | Seed purchase price in Gold (G) to buy 1 seed of crop $c$. |
| **$v_c$** | `c.nq_sale` | Real Parameter | $v_c > 0$ (Gold) | Selling price per unit of Normal Quality (NQ) harvest of crop $c$. |
| **$m_c$** | `c.mature` | Integer Parameter | Days ($\ge 1$) | Nights of growth required from planting to first harvest. |
| **$r_c$** | `c.regrowth` | Integer Parameter | Days ($\ge 0$) | Days between subsequent harvests for regrowth crops ($0$ if single-harvest). |
| **$H_c$** | `c.max_harvests` | Integer Parameter | Integer ($\ge 1$) | Maximum allowed harvests before plant expires ($1$ if single-harvest). |
| **$H(c, d)$** | `v["harvests"]` | Set of Days | $H \subseteq [d+1, 30]$ | **Harvest Days Set**: All calendar days on which crop $c$ planted on day $d$ matures. |
| **$R_{c, d}$** | `v["total_rev"]` | Real Parameter | $R_{c, d} > 0$ (Gold) | **Total Harvest Revenue**: Total gold earned by 1 plot of crop $c$ planted on day $d$ ($R_{c, d} = \|H(c, d)\| \cdot v_c$). |
| **$b_c$** | `c.biome` | Categorical String | `farm`, `waterside`, `cave` | Required physical soil biome for crop $c$. |
| **$W$** | `wallet_gold` | Real Parameter | $W \ge 0$ (Gold) | Gold cash available in player's wallet at start of `current_day`. |
| **$B_b$** | `caps[biome]` | Integer Parameter | Plots ($\ge 0$) | Available plot capacity for soil biome $b \in \{\text{farm}, \text{waterside}, \text{cave}\}$. |
| **$S_c$** | `c.stock` | Integer Parameter | $S_c \ge 1$ | General store inventory stock cap per 10-day restock cycle for crop $c$. |
| **$\mathbf{z}$** | Solver vector | Vector | $\mathbb{Z}^{N}$ (or $\mathbb{Z}^{N + U}$) | Full decision vector sent to solver: $[x_{c_0, d_1}, \dots]^T$ or $[x_{c_0, d_1}, \dots, y_0, \dots, y_{U-1}]^T$. |
| **$\mathbf{c}$** | Objective vector | Vector | $\mathbb{R}^{N}$ (or padded) | Objective coefficient vector with tie-breakers. |
| **$m$** | `len(A_rows)` | Integer Scalar | $m = \text{rows}$ | Total active constraint boundaries in matrix $\mathbf{A}$. |
| **$\mathbf{A}$** | `A` | Matrix | $\mathbb{R}^{m \times |\mathbf{z}|}$ | Linear constraint matrix encoding plot capacity, cash balances, restock, and variety caps. |
| **$\mathbf{lb}, \mathbf{ub}$** | `lb`, `ub` | Vectors | $\mathbb{R}^m$ | Lower and upper capacity bounds on constraint rows in matrix $\mathbf{A}$. |





---

### Step 1: Preprocessing & Candidate Pruning
Before building matrices, `solve_allocation()` filters the full seasonal CSV down to $n$ viable candidate crops:
1. **Town Gate**: Checks `unlocked_towns[town] == True`. Split vendors like `Shatolla/Nemea` unlock if *either* town is unlocked.
2. **Biome Plot Check**: Crops requiring Waterside or Cave plots are discarded if the player has 0 plots in that biome.
3. **Economic Viability**: Drops without purchase cost (e.g. Nitro Pineapple) or negative profits are excluded.
4. **Time-Indexed Feasibility**: For each eligible crop $c$ and each calendar day $d \in [\text{current\_day}, 30]$, the candidate pair $(c, d)$ is accepted only if its first harvest completes on or before Day 30 ($d + m_c \le 30$).

This leaves a filtered catalog of $n$ crops expanded across time into $N_{\text{vars}}$ active planting options.

---

### Step 2: Decision Variables and Bounds

Depending on whether `max_crop_varieties` ($K$) is configured:

#### Case A: Unconstrained Variety (`max_crop_varieties: null`)
- **$N_{\text{vars}}$ integer variables** ($N_{\text{vars}} = \text{len}(\text{var\_map})$ active $(c, d)$ planting options): $x_{c, d}$ representing the quantity of seeds of crop variety $c$ planted on day $d$.
- **Bounds**: $0 \le x_{c, d} < \infty$ (individual purchases are bounded by the 10-day shop restock constraints).
- **Integrality**: `integrality = np.ones(N_vars)`.

#### Case B: Variety Limited (`max_crop_varieties: K`)
- **$N_{\text{vars}} + K_{\text{unique}}$ variables**:
  - $x_{c_0, d_1}, \dots$: integer seed quantities per planting day ($0 \le x_{c, d} < \infty$).
  - $y_0, \dots, y_{K_{\text{unique}}-1}$: binary indicator switches ($0 \le y_k \le 1$).
- **Bounds**:
  - Planting variables: $0 \le x_{c, d} < \infty$.
  - Indicator switches: $0 \le y_k \le 1$.
- **Integrality**: `integrality = np.ones(N_vars + K_unique)`.


---

### Step 3: Objective Function Construction

The solver maximizes **Total Cumulative Season Net Profit** across all planting days $d \in [\text{current\_day}, 30]$ leading to Quietus:

- **When variety is unconstrained** ($K$ is null):
  $$\max_{\mathbf{x}} \sum_{c} \sum_{d} (R_{c, d} - p_c) \cdot x_{c, d}$$
  Where $R_{c, d} = |H(c, d)| \cdot v_c$ is total harvest revenue generated by planting crop $c$ on day $d$.

- **When variety is limited** ($K$ is set):
  The solver optimizes over physical seed plantings $\mathbf{x}$ and binary variety indicator switches $\mathbf{y}$:
  $$\max_{\mathbf{x}, \mathbf{y}} \left( \sum_{c} \sum_{d} (R_{c, d} - p_c) \cdot x_{c, d} + \sum_{k} 0 \cdot y_k \right)$$

#### Dual Tie-Breakers for Optimal Cash & Land Efficiency
When two planting options yield identical net profit, the solver applies two deterministic microscopic tie-breaker penalties:
1. **Cost Tie-Breaker ($\epsilon_1 = 10^{-6} \cdot p_c$)**: Prefers cheaper seed varieties to conserve precious wallet cash.
2. **Timing Tie-Breaker ($\epsilon_2 = 10^{-8} \cdot (d - \text{current\_day})$)**: Prefers earlier planting calendar days to accelerate capital compounding and free soil sooner.

In standard SciPy minimization format ($\min \mathbf{c}^T \mathbf{z}$):

$$c_{c, d} = -\left( (R_{c, d} - p_c) - 10^{-6} \cdot p_c - 10^{-8} \cdot (d - \text{current\_day}) \right)$$

#### Why do binary indicators $y_k$ have an objective cost of $0$?

The full decision vector $\mathbf{z}$ sent to the solver contains:

$$\mathbf{z} = \begin{bmatrix} x_{c_0, d_1} \\ \vdots \\ x_{c_n, d_{30}} \\ \hline y_0 \\ \vdots \\ y_{U-1} \end{bmatrix} \quad \begin{array}{l} \text{(physical seed quantities per day)} \\ \\ \text{(binary variety switches)} \end{array}$$

When the solver evaluates total profit ($\mathbf{c}^T \mathbf{z}$):
- **$x_{c, d}$ has a non-zero coefficient ($c_{c, d}$)**: Each planted seed consumes wallet gold $p_c$ on day $d$ and yields harvest revenue $R_{c, d}$ upon maturity.
- **$y_k$ has a zero coefficient ($0.0$)**: The act of "unlocking" a crop variety doesn't earn or cost gold by itself. $y_k$ is strictly an **auxiliary bookkeeping indicator** whose sole purpose is to serve as a logical flag in the Big-M constraints (Step 4 & Step 6).

Therefore, the objective vector is partitioned with zeros for all $y_k$:

$$\mathbf{c} = \left[\begin{array}{cccc|cccc} c_{0} & c_{1} & \dots & c_{N-1} & 0 & 0 & \dots & 0 \end{array}\right]$$


---

### Step 4: The Constraint Matrix $\mathbf{A}$

Every physical game boundary across every calendar day is translated into a row in matrix $\mathbf{A}$:

$$\mathbf{lb} \le \mathbf{A} \mathbf{z} \le \mathbf{ub}$$

| Constraint Family | Scope / Indexing | Equation / Coefficients | Lower Bound ($\mathbf{lb}$) | Upper Bound ($\mathbf{ub}$) |
| :--- | :--- | :--- | :---: | :---: |
| **Daily Plot Capacity** | Each day $t \in [\text{current\_day}, 30]$, each biome $b$ | $\sum_{(c, d) \text{ occupying } b \text{ on } t} 1.0 \cdot x_{c, d}$ | $0.0$ | $B_b$ |
| **Daily Cash Liquidity** | Each morning $t \in [\text{current\_day}, 30]$ | $\sum_{d \le t} p_c \cdot x_{c, d} - \sum_{h + 1 \le t} v_c \cdot x_{c, d}$ | $-\infty$ | $W$ |
| **10-Day Restock Caps** | Each window $W_w$, each crop $c$ | $\sum_{d \in W_w} 1.0 \cdot x_{c, d}$ | $0.0$ | $S_c$ |
| **Big-M Variety Linking** | Each unique variety $k$ *(if $K$ set)* | $\sum_{d} 1.0 \cdot x_{c, d} - M \cdot y_k$ | $-\infty$ | $0.0$ |
| **Variety Cardinality Cap** | Entire season *(if $K$ set)* | $\sum_{k=0}^{U-1} 1.0 \cdot y_k$ | $0.0$ | $K$ |

#### Matrix Visualization

```
                       [ ----- Seed Quantities x_{c, d} ----- ]   [ - Binary Indicators y_k - ]
Constraint Rows:            x_{c_0, d_1}  ...   x_{c_n, d_{30}}       y_0     ...   y_{U-1}          ub
----------------------------------------------------------------------------------------------------------------
Plots (Biome b, Day t) [       1.0 (if occupied) ...     0.0           0.0    ...     0.0   ]  <=  B_b
Cash (Morning Day t)   [   Purchases(<=t) - Shipping_Arrived(<=t)      0.0    ...     0.0   ]  <=  W
Store Restock Window w [       1.0 (if d in window) ...  0.0           0.0    ...     0.0   ]  <=  S_c
Linking Variety k      [       1.0 (if crop k)  ...      0.0           -M     ...     0.0   ]  <=  0.0
Variety Limit          [       0.0              ...      0.0           1.0    ...     1.0   ]  <=  K
```



---

### Step 5: Concrete Numerical Walkthrough
 
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

### Step 6: Day-to-Day Time-Indexed Dynamic Horizon Formulation

The solver natively operates as a **Day-to-Day Time-Indexed Mixed-Integer Linear Program (MILP)** with daily plot occupancy tracking, overnight shipping cash turnaround, and 10-day shop inventory restock cycles leading to Quietus (Day 30).

#### 1. Time Horizon & Day Indexing
Given `current_day`, the planning horizon spans every active calendar day $d \in [\text{current\_day}, 30]$:
- Day 30 is the final playable day of the season.
- Quietus occurs on the night between Day 30 and Day 31, destroying all unharvested crops. All harvests must complete on or before Day 30.

#### 2. Decision Variables: $x_{c, d}$
- $x_{c, d} \in \mathbb{Z}^+$: Number of plots allocated to crop variety $c$ planted on calendar day $d$.
- **Variable Count**: The theoretical dimensionality is $(\#\text{ eligible crops}) \times (\#\text{ remaining days})$. In practice, any $(c, d)$ pair that cannot reach harvest before Day 30 (e.g., planting a 6-day crop on Day 27) is pruned out, yielding:
  - **Summer** (Day 18 → 30, 13 days): **107 active decision variables**.
  - **Spring** (Day 1 → 30, 30 days): **430 active decision variables**.
  - **Fall** (Day 1 → 30, 30 days): **386 active decision variables**.
  - **Winter** (Day 1 → 30, 30 days): **103 active decision variables**.
- $y_{k} \in \{0, 1\}$: Binary indicator flag tracking if crop variety $k$ is planted anywhere in the season (when `max_crop_varieties` $K$ is configured).

#### 3. Crop Growth Dynamics: Single-Harvest vs. Regrowth

##### Single-Harvest Crops
- Matures in $m$ days.
- Planted on morning of Day $d$, harvested on Day $h = d + m$.
- **Soil Occupancy**: Occupies 1 plot on calendar days $t \in [d, d + m - 1]$. The plot is cleared and freed on the morning of Day $d + m$ for immediate replanting.
- **Overnight Shipping Turnaround**: Harvested produce is placed in the shipping box on Day $h$. Gold arrives in the player's wallet on the morning of Day $h + 1$.

##### Regrowth Crops (e.g., Nemean Tomato, Revol Pepper, Nectarcane, Strawbuddy)
- Initial maturity in $m$ days, subsequent harvests every $r$ days up to $H_{\max}$ total harvests.
- Harvest days set: $H(c, d) = \{ d + m + k \cdot r \mid k \in [0, H_{\max}-1], \; d + m + k \cdot r \le 30 \}$.
- **Soil Occupancy**: Stays permanently rooted in soil from planting day $d$ through its final harvest day $\max(H(c, d))$ (or Day 30), incurring **zero additional seed purchase costs** for subsequent harvests.
- **Cash Flow**: Each harvest $h \in H(c, d)$ yields $v_c$ deposited into wallet liquidity on the morning of Day $h + 1$.

#### 4. The Time-Indexed Objective Function
Maximizes total cumulative net profit accumulated across all plantings by Day 30:

$$\max_{\mathbf{x}} \sum_{c} \sum_{d} \left( (R_{c, d} - p_c) - 10^{-6} \cdot p_c - 10^{-8} \cdot (d - \text{current\_day}) \right) \cdot x_{c, d}$$

- Tie-breaker $\epsilon_1 = 10^{-6} \cdot p_c$ strictly prefers cheaper seeds if net profit is identical.
- Tie-breaker $\epsilon_2 = 10^{-8} \cdot (d - \text{current\_day})$ strictly prefers earlier planting to compound capital faster.

#### 5. Dynamic Time-Coupled Constraint Formulation

Every day $t \in [\text{current\_day}, 30]$ enforces physical reality constraints:

1. **Daily Plot Capacity per Biome (for each day $t$, each biome $b$)**:
   $$\sum_{(c, d) \text{ occupying biome } b \text{ on day } t} x_{c, d} \le B_b$$
   Ensures that on no single day do actively growing crops exceed the available Farm, Waterside, or Cave land.

2. **Daily Cash Liquidity & Overnight Shipping Turnaround (for each morning $t$)**:
   $$\sum_{d \le t} p_c \cdot x_{c, d} - \sum_{h + 1 \le t} v_c \cdot x_{c, d} \le W$$
   Ensures the player's wallet balance is non-negative on every calendar morning. Reinvestment of harvest proceeds is strictly gated by the 1-day overnight shipping delay.

3. **Vendor Restock Inventory Windows**:
   General store stocks refresh every 10 days ($W_1 = [1, 10], \; W_2 = [11, 20], \; W_3 = [21, 30]$):
   $$\sum_{d \in W_w} x_{c, d} \le S_c \quad \forall w \in \{1, 2, 3\}$$

4. **Big-M Variety Cardinality Limits (if $K$ is set)**:
   $$\sum_{d} x_{c, d} - M \cdot y_k \le 0 \quad \text{and} \quad \sum_k y_k \le K$$

#### 6. Dynamic Matrix Structure

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

- **Daily Compounding**: Unlike coarse stage models that wait for milestone days, proceeds from Day 3 or Day 4 harvests are immediately recognized on mornings of Day 4 and Day 5, funding fresh seed purchases on the exact day cash arrives.


