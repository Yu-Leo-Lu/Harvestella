# Harvestella Agricultural Economics & Metrics Guide

A concise reference guide explaining how to compute the core metrics in `compute_crop_metrics.py` and how to apply them across a 30-day season.

## 1. Farming Constraints in Harvestella

1. **Cash (G)**: Limited wallet capital for buying seeds.
2. **Plots**: Limited tilled farm tiles and daily watering stamina.
3. **Shipping Delay (+1d)**: Shipped crops pay out the next morning (Turnaround = Growth Days + 1).
4. **Quietus Deadline**: Every season lasts 30 days. Unharvested annual crops die on Day 30.

## 2. Metric Overview

| Metric | What It Measures | The Question It Answers | When to Use |
| :--- | :--- | :--- | :--- |
| **Cash Compound Rate (%/day)** | Return on Capital (Gold efficiency) | *"How fast will my wallet multiply if I reinvest every payout?"* | **Low Gold / Bootstrapping** (Wallet < ~6k–10k G: free plots exceed gold; cannot afford 99-seed stacks) |
| **Daily NQ Profit (G/d)** | Return on Space & Time (Plot efficiency) | *"How much raw gold does each tilled tile produce per day?"* | **High Gold / Plot-Constrained** (Wallet ≥ ~6k–10k G: can easily buy out 99-cap compound seeds; plots are bottleneck) |
| **Production Days** | Crop Lifecycle & Soil Commitment | *"How many total calendar days will this crop occupy the plot?"* | **Plot Scheduling & Crop Rotation** (Turnaround planning before replanting) |
| **Planting Schedule** | Quietus Rotation Cadence | *"What are all the planting dates that align with the Day 30 Quietus cutoff?"* | **Season-Long Rotation Planning** (Zero dead plot days before Quietus) |

## 3. Cash Compound Rate (%/day)

### Formula

For single crops (accounting for $+1\text{d}$ shipping delay):
$$r = \left(\left(\frac{p}{s}\right)^{\frac{1}{m + 1}} - 1\right) \times 100\%$$

For repeat crops (realized cash velocity across active production run):
$$r = \left(\left(\frac{n \cdot p}{s}\right)^{\frac{1}{m + (n - 1) \cdot g + 1}} - 1\right) \times 100\%$$

Where:
* $p$ = sell price
* $s$ = seed cost
* $m$ = mature days
* $g$ = regrowth days
* $n$ = harvest count (capped by Max Harvests or season)
* $m + (n - 1) \cdot g + 1$ = cash realization days (growth days plus overnight payout delay)

### Examples

#### Single Crop: Dress Lettuce ($m = 2$)
$$\left(\left(\frac{85}{55}\right)^{\frac{1}{2 + 1}} - 1\right) \times 100\% = \mathbf{+15.62\%/\text{day}}$$

#### Repeat Crop: Shatollan Paprika ($m = 5, g = 2, n = 9$)
* Seed Cost: $s = 250\text{ G}$, NQ Sale: $p = 110\text{ G}$
* Total Realization Days: $5 + (9 - 1) \cdot 2 + 1 = 22\text{ days}$
* Total Revenue: $9 \times 110 = 990\text{ G}$
* Wealth Multiplier: $\frac{990}{250} = 3.96$
$$\left((3.96)^{\frac{1}{22}} - 1\right) \times 100\% = \mathbf{+6.46\%/\text{day}}$$


## 4. Production Days

### Formula

For single crops:
$$d_{\text{prod}} = m\text{ days}$$

For repeat crops:
$$d_{\text{prod}} = m + (n - 1) \cdot g\text{ days}$$

Where:
* $m$ = mature / initial growth days
* $g$ = regrowth days
* $n$ = total harvest count (capped by $\text{Max Harvests}$ or season duration)

### Examples
* **Dress Lettuce**: $m = 2 \implies \mathbf{2\text{ days}}$
* **Carrop**: $m = 1 \implies \mathbf{1\text{ day}}$
* **Strawbuddy** ($m = 4, g = 2, n = 5$): $4 + (5 - 1) \times 2 = \mathbf{12\text{ days}}$
* **Cucumble** ($m = 4, g = 3, n = 6$): $4 + (6 - 1) \times 3 = \mathbf{19\text{ days}}$
* **Shatollan Paprika** ($m = 5, g = 2, n = 9$): $5 + (9 - 1) \times 2 = \mathbf{21\text{ days}}$
* **Bellhop Seeds** ($m = 7, g = 1, n = 24$): $7 + (24 - 1) \times 1 = \mathbf{30\text{ days}}$


## 5. Daily NQ Profit

### Formula

For single crops:
$$\delta = \frac{p - s}{m}$$

For repeat crops:
$$\delta = \frac{(n \cdot p) - s}{m + (n - 1) \cdot g} = \frac{(n \cdot p) - s}{d_{\text{prod}}}$$

Where:
* $p$ = NQ sell price
* $s$ = seed cost
* $m$ = mature days
* $g$ = regrowth days
* $n$ = harvest count (capped by $\text{Max Harvests}$ or season duration)
* $d_{\text{prod}} = m + (n - 1) \cdot g$ = total active production days

### Examples
* **Dress Lettuce**: $\frac{85 - 55}{2} = \mathbf{+15.0\text{ G/d}}$
* **Cucumble** ($m=4, g=3, n=6$): $\frac{(6 \cdot 200) - 370}{19} = \frac{830}{19} = \mathbf{+43.7\text{ G/d}}$


## 6. Planting Schedule

### Formula

Descending calendar days stepping backwards from Day 30 by Production Days ($d_{\text{prod}}$), synchronizing consecutive harvests directly into Quietus with **zero wasted plot days**:

$$S = [30 - d_{\text{prod}}, 30 - 2d_{\text{prod}}, \dots] \quad (\text{for all days } > 0)$$

Where:
* $d_{\text{prod}}$ = Production Days ($m$ for single crops, $m + (n - 1) \cdot g$ for repeat crops)
* *Display truncation*: Schedules with $\ge 8$ dates truncate cleanly to 7 elements: `d1, d2, d3, d4, d5, ... , dn`.

### Examples
* **Seatide Garlic** ($d_{\text{prod}} = 6\text{d}$): $30 - 6 = \mathbf{24, 18, 12, 6}$
* **Islet Watermelon** ($d_{\text{prod}} = 12\text{d}$): $30 - 12 = \mathbf{18, 6}$
* **Morrocorn** ($d_{\text{prod}} = 4\text{d}$): $30 - 4 = \mathbf{26, 22, 18, 14, 10, 6, 2}$
* **Dress Lettuce** ($d_{\text{prod}} = 2\text{d}$): $30 - 2 = \mathbf{28, 26, 24, 22, 20, \dots, 2}$
* **Cucumble** ($d_{\text{prod}} = 19\text{d}$): $30 - 19 = \mathbf{11}$
