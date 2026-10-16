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
4. **Planning Horizon Deadlines**: Every season lasts exactly 30 days and terminates with Quietus. All annual crops die on Day 30 without payout. Alternatively, during the season, vendor shops restock every 10 days (Days 1, 11, 21), meaning cash invested into crops must mature before the next shopping day.
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
| **$n$** | `len(candidates)` | Integer Scalar | $n \ge 0$ | Total number of **eligible crop varieties** available this season after pruning locked towns, biomes, and deadlines. |
| **$i$** | Loop index `0..n-1` | Index | $0 \le i < n$ | Zero-based index referencing a specific crop candidate (e.g., $i=0$ for Dress Lettuce, $i=1$ for Morrocorn). |
| **$x_i$** | Result dictionary value | Integer Variable | $\{0, 1, \dots, \text{stock}_i\}$ | **Primary Decision Variable**: Number of physical seeds of crop variety $i$ to purchase and plant. |
| **$y_i$** | `y_0..y_{n-1}` | Binary Variable | $\{0, 1\}$ | **Auxiliary Indicator Variable**: Flags whether crop $i$ is selected ($y_i = 1$ if $x_i > 0$, else $y_i = 0$). Used only when $K$ is set. |
| **$K$** | `max_crop_varieties` | Integer / Null | $K \in \mathbb{Z}^+$ or `None` | **Cardinality Bound**: Maximum allowed number of distinct crop varieties the player wants to manage simultaneously. |
| **$M_i$** | `seed_stock[name]` | Integer Parameter | $M_i \ge 1$ (default 99) | **Big-M Upper Bound**: Maximum vendor shop inventory stock cap for crop $i$. |
| **$\text{Cost}_i$** | `cand.cost` | Real Parameter | $\text{Cost}_i > 0$ (Gold) | Purchase price in Gold (G) to buy 1 seed of crop $i$ from the vendor store. |
| **$\text{Profit}_i$** | `cand.daily_profit` | Real Parameter | $\text{G / day}$ | Expected daily Normal Quality (NQ) net profit per plot for crop $i$. |
| **$d_{\text{prod}}$** | `cand.prod_days` | Integer Parameter | Days ($\ge 1$) | Days required from planting to harvest. For re-harvest crops, effective days per harvest. |
| **$\text{Biome}_i$** | `cand.biome` | Categorical String | `farm`, `waterside`, `cave` | The required physical soil type where crop $i$ must be planted. |
| **$W$** | `wallet_gold` | Real Parameter | $W \ge 0$ (Gold) | Total gold cash currently available in player's wallet to spend on seeds. |
| **$F$** | `farm_capacity` | Integer Parameter | Plots ($\ge 0$) | Total unplanted standard Farm soil plots (`free_plots.farm`). |
| **$S$** | `waterside_capacity` | Integer Parameter | Plots ($\ge 0$) | Total unplanted Waterside soil plots (`free_plots.waterside`). |
| **$C$** | `cave_capacity` | Integer Parameter | Plots ($\ge 0$) | Total unplanted Cave soil plots (`free_plots.cave`). |
| **$\mathbf{x}$** | Solver vector | Vector | $\mathbb{Z}^n$ (or $\mathbb{Z}^{2n}$) | The full decision vector sent to solver: $[x_0, \dots, x_{n-1}]^T$ or $[x_0, \dots, x_{n-1}, y_0, \dots, y_{n-1}]^T$. |
| **$\mathbf{c}$** | `c` | Vector | $\mathbb{R}^n$ (or $\mathbb{R}^{2n}$) | Objective coefficient vector ($c_i = -\text{Profit}_i + 10^{-6} \cdot \text{Cost}_i$). Padded with $0$s for $y_i$. |
| **$m$** | `len(A_rows)` | Integer Scalar | $m = 4$ (or $n+5$) | Total number of active constraint boundaries: 4 shared resource limits (budget, farm land, waterside land, cave land). If variety limit $K$ is set, adds $n$ Big-M variety-linking constraints plus 1 variety cap constraint ($m = 4 + n + 1 = n + 5$). |
| **$\mathbf{A}$** | `A_rows` | Matrix | $\mathbb{R}^{m \times n}$ (or $m \times 2n$) | Linear constraint matrix encoding budget, land capacity, Big-M linking, and variety caps ($m$ rows by variables). |
| **$\mathbf{lb}, \mathbf{ub}$** | `lb_list`, `ub_list` | Vectors | $\mathbb{R}^m$ | Lower and upper capacity limits for each of the $m$ constraint rows in matrix $\mathbf{A}$. |

---

### Step 1: Preprocessing & Candidate Pruning
Before building matrices, `solve_allocation()` filters the full seasonal CSV down to $n$ viable candidate crops:
1. **Town Gate**: Checks `unlocked_towns[town] == True`. Split vendors like `Shatolla/Nemea` unlock if *either* town is unlocked.
2. **Horizon Feasibility**:
   - For **Quietus**: Candidate must satisfy $\text{current\_day} \le 30 - d_{\text{prod}}$ (or $d_{\text{prod}} \le 30$ on Day 1).
   - For **Restock**: Candidate must satisfy $d_{\text{prod}} \le R - \text{current\_day}$ where $R \in \{11, 21, 31\}$.
3. **Biome Plot Check**: Crops requiring Waterside or Cave plots are discarded if the player has 0 plots in that biome.
4. **Economic Viability**: Drops without purchase cost (e.g. Nitro Pineapple) or negative profits are excluded.

This leaves an eligible set of $n$ candidates ($i = 0, \dots, n-1$).

---

### Step 2: Decision Variables and Bounds

Depending on whether `max_crop_varieties` ($K$) is set:

#### Case A: Unconstrained Variety (`max_crop_varieties: null`)
- **$n$ integer variables** ($n = \text{len}(\text{candidates})$ eligible crop varieties): $x_0, x_1, \dots, x_{n-1}$ representing the quantity of each seed variety to purchase and plant.
- **Bounds**: $0 \le x_i \le \text{seed\_stock}_i$.
- **Integrality**: `integrality = np.ones(n)`.

#### Case B: Variety Limited (`max_crop_varieties: K`)
- **$2n$ variables**:
  - $x_0, \dots, x_{n-1}$: integer seed quantities ($0 \le x_i \le \text{seed\_stock}_i$).
  - $y_0, \dots, y_{n-1}$: binary indicator variables ($0 \le y_i \le 1$).
- **Bounds**:
  - Seed variables: $0 \le x_i \le \text{seed\_stock}_i$.
  - Indicator variables: $0 \le y_i \le 1$.
- **Integrality**: `integrality = np.ones(2 * n)`.

---

### Step 3: Objective Function Construction

We want to maximize total daily profit:

- **When variety is unconstrained** ($K$ is null):
  $$\max_{\mathbf{x}} \sum_{i=0}^{n-1} \text{Daily NQ Profit}_i \cdot x_i$$

- **When variety is limited** ($K$ is set):
  The solver optimizes over both seed counts $\mathbf{x}$ and indicator switches $\mathbf{y}$:
  $$\max_{\mathbf{x}, \mathbf{y}} \left( \sum_{i=0}^{n-1} \text{Daily NQ Profit}_i \cdot x_i + \sum_{i=0}^{n-1} 0 \cdot y_i \right)$$

To break ties when two seeds have equal profit, we add a microscopic tie-breaker penalty ($\epsilon = 10^{-6} \cdot \text{cost}_i$). This strictly instructs the solver to prefer the cheaper seed to preserve cash.

In standard SciPy minimization format ($\min \mathbf{c}^T \mathbf{x}$):

$$c_i = -\text{Daily NQ Profit}_i + 10^{-6} \cdot \text{Seed Cost}_i$$

#### Why do binary indicators $y_i$ have an objective cost of $0$?

The full decision vector sent to the solver contains $2n$ variables:

$$\mathbf{z} = \begin{bmatrix} x_0 \\ \vdots \\ x_{n-1} \\ \hline y_0 \\ \vdots \\ y_{n-1} \end{bmatrix} \quad \begin{array}{l} \text{(physical seed quantities)} \\ \\ \text{(binary variety switches)} \end{array}$$

When the solver evaluates total profit ($\mathbf{c}^T \mathbf{z}$):
- **$x_i$ has a non-zero coefficient ($c_i$)**: Each planted seed consumes wallet gold and yields harvest profit.
- **$y_i$ has a zero coefficient ($0.0$)**: The act of "choosing" a crop variety doesn't earn or cost gold by itself. $y_i$ is strictly an **auxiliary bookkeeping variable** whose sole purpose is to serve as a logical flag in the constraints (Step 4).

Therefore, the objective vector is partitioned with zeros for all $y_i$:

$$\mathbf{c} = \left[\begin{array}{cccc|cccc} c_0 & c_1 & \dots & c_{n-1} & 0 & 0 & \dots & 0 \end{array}\right]$$

---

### Step 4: The Constraint Matrix $\mathbf{A}$

Every real-game boundary is translated into a row in matrix $\mathbf{A}$:

$$\mathbf{lb} \le \mathbf{A} \mathbf{x} \le \mathbf{ub}$$

| Row # | Constraint Description | Equation / Coefficients | Lower Bound ($\mathbf{lb}$) | Upper Bound ($\mathbf{ub}$) |
| :---: | :--- | :--- | :---: | :---: |
| **Row 0** | **Capital Budget** | $\sum \text{Seed Cost}_i \cdot x_i$ | $0.0$ | `wallet_gold` |
| **Row 1** | **Farm Plots** | $\sum_{i \in \text{Farm}} 1.0 \cdot x_i$ | $0.0$ | `farm_capacity` |
| **Row 2** | **Waterside Plots** | $\sum_{i \in \text{Water}} 1.0 \cdot x_i$ | $0.0$ | `waterside_capacity` |
| **Row 3** | **Cave Plots** | $\sum_{i \in \text{Cave}} 1.0 \cdot x_i$ | $0.0$ | `cave_capacity` |
| **Rows $4 \dots 4+n-1$** | **Big-M Linking** *(if $K$ set)* | $1.0 \cdot x_i - \text{stock}_i \cdot y_i$ | $-\infty$ | $0.0$ |
| **Row $4+n$** | **Variety Limit** *(if $K$ set)* | $\sum_{i=0}^{n-1} 1.0 \cdot y_i$ | $0.0$ | $K$ |

#### Matrix Visualization

```
                       [ --- Seed Quantities x_i --- ]   [ - Binary Indicators y_i - ]
Constraint Rows:            x_0       x_1   ...   x_{n-1}     y_0     y_1   ...   y_{n-1}         ub
---------------------------------------------------------------------------------------------------------
Budget               [   Cost_0    Cost_1   ...  Cost_{n-1}    0       0    ...      0     ]  <=  wallet_gold
Farm Land            [   Farm_0    Farm_1   ...  Farm_{n-1}    0       0    ...      0     ]  <=  farm_cap
Waterside Land       [  Water_0   Water_1   ... Water_{n-1}    0       0    ...      0     ]  <=  water_cap
Cave Land            [   Cave_0    Cave_1   ...  Cave_{n-1}    0       0    ...      0     ]  <=  cave_cap
---------------------------------------------------------------------------------------------------------
Linking Crop 0       [     1         0      ...      0      -Stock_0   0    ...      0     ]  <=  0.0
Linking Crop 1       [     0         1      ...      0         0    -Stock_1...      0     ]  <=  0.0
...                  [    ...       ...     ...     ...       ...     ...   ...     ...    ]  <=  0.0
Linking Crop n-1     [     0         0      ...      1         0       0    ...  -Stock_{n-1}]  <=  0.0
---------------------------------------------------------------------------------------------------------
Variety Cap          [     0         0      ...      0         1       1    ...      1     ]  <=  K
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
