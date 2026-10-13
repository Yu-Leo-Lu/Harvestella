# Harvestella Agricultural Economics & Metrics Guide

A concise reference guide explaining how to compute the core metrics in `compute_crop_metrics.py` and how to apply them across a 30-day season.

## 1. Farming Constraints in Harvestella

1. **Cash (G)**: Limited wallet capital for buying seeds.
2. **Plots**: Limited tilled farm tiles and daily watering stamina.
3. **Shipping Delay (+1d)**: Shipped crops pay out the next morning (Turnaround = Growth Days + 1).
4. **Quietus Deadline**: Every season lasts 30 days. Unharvested annual crops die on Day 30.

## 2. Metric Overview

| Metric | Why We Need It | When to Use |
| :--- | :--- | :--- |
| **Cash Compound Rate** | Multiplies small amounts of gold as fast as possible. | Early season / Low wallet gold |
| **Capital Days** | Tracks how much gold is frozen in the soil and for how long. | Managing cash flow to avoid running out of gold |
| **Daily NQ Profit** | Measures normal quality net gold earned per plot per active growth day. | Comparing profit efficiency across different growth cycle lengths |
| **Latest Plant Day** | Tells the exact cutoff date to plant without losing a harvest cycle. | Mid-to-late season / Quietus planning |

## 3. Cash Compound Rate (%/day)

### Formula

For single crops (accounting for $+1\text{d}$ shipping delay):
$$r = \left(\left(\frac{p}{s}\right)^{\frac{1}{d + 1}} - 1\right) \times 100\%$$

For repeat crops (30-day wealth compounding):
$$r = \left(\left(\frac{n \cdot p}{s}\right)^{\frac{1}{30}} - 1\right) \times 100\%$$

Where:
* $p$ = sell price
* $s$ = seed cost
* $d$ = growth days
* $n = \lfloor 30 / d \rfloor$ (harvest count)

### Examples
* **Unionion**: $\left(\left(\frac{195}{105}\right)^{\frac{1}{4}} - 1\right) \times 100\% = \mathbf{+16.74\%/\text{day}}$
* **Dress Lettuce**: $\left(\left(\frac{85}{55}\right)^{\frac{1}{3}} - 1\right) \times 100\% = \mathbf{+15.62\%/\text{day}}$
* **Morrocorn (Shatolla)**: $\left(\left(\frac{400}{200}\right)^{\frac{1}{5}} - 1\right) \times 100\% = \mathbf{+14.87\%/\text{day}}$ *(Lethe @ 230 G: $\mathbf{+11.70\%/\text{day}}$)*

## 4. Capital Days (G*d)

### Formula
$$k = s \cdot (d + 1)$$

Where:
* $s$ = seed cost
* $d$ = growth days (with $+1$ for shipping payout delay)

### Examples
* **Dress Lettuce**: $55 \times 3 = \mathbf{165\text{ G}\cdot\text{d}}$ *(ultra-safe liquidity)*
* **Morrocorn (Shatolla)**: $200 \times 5 = \mathbf{1,000\text{ G}\cdot\text{d}}$ *(Lethe: $230 \times 5 = \mathbf{1,150\text{ G}\cdot\text{d}}$)*
* **Lantern Pumpkin**: $3,750 \times 12 = \mathbf{45,000\text{ G}\cdot\text{d}}$ *(extreme cash freeze)*

## 5. Daily NQ Profit

### Formula

For single crops:
$$\delta = \frac{p - s}{d}$$

For repeat crops:
$$\delta = \frac{(n \cdot p) - s}{n \cdot d}$$

Where:
* $p$ = NQ sell price
* $s$ = seed cost
* $d$ = cycle days
* $n = \lfloor 30 / d \rfloor$ (harvest count)
* $n \cdot d$ = total active growth days

### Examples
* **Unionion**: $\frac{195 - 105}{3} = \mathbf{+30.0\text{ G/d}}$
* **Dress Lettuce**: $\frac{85 - 55}{2} = \mathbf{+15.0\text{ G/d}}$
* **Morrocorn (Shatolla)**: $\frac{400 - 200}{4} = \mathbf{+50.0\text{ G/d}}$
* **Nemean Tomato**: $\frac{(6 \cdot 65) - 170}{6 \cdot 5} = \frac{220}{30} = \mathbf{+7.3\text{ G/d}}$

## 6. Latest Plant Day

### Formula
$$L = 30 - (n \cdot d)$$

Where:
* $n = \lfloor 30 / d \rfloor$ (harvest count)
* $d$ = cycle days
* $n \cdot d$ = total growth days needed for maximum harvests

### Example: Nectarcane ($d = 4$, $n = 7$)

Crops grow overnight. A 4-day crop planted on Day $P$ yields its first harvest on Day $P + 4$, requiring $7 \times 4 = 28$ growth days total for all 7 harvests:

* **Planted on Day 1**: Harvests on Days 5, 9, 13, 17, 21, 25, **29** (7 full harvests).
* **Planted on Day 2**: Harvests on Days 6, 10, 14, 18, 22, 26, **30** (7 full harvests on the season's last day).
* **Planted on Day 3**: 7th harvest lands on **Day 31 $\rightarrow$ Quietus** (crop withers; only 6 harvests).

$$L = 30 - 28 = \mathbf{\text{Day } 2}$$
