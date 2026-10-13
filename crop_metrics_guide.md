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
| **Cash Compound Rate (%/day)** | Return on Capital (Gold efficiency) | *"How fast will my wallet multiply if I reinvest every payout?"* | **Low Gold / Early Game** (You have free farm plots, but an empty wallet) |
| **Daily NQ Profit (G/d)** | Return on Space & Time (Plot efficiency) | *"How much raw gold does each tilled tile produce per day?"* | **High Gold / Mid-to-Late Game** (You have plenty of gold, but limited farm tiles & watering stamina) |
| **Capital Days ($G \cdot d$)** | Liquidity & Capital Lockup | *"How much cash is frozen in the soil, and for how many days?"* | **Cash Flow Management** (Ensuring you don't run out of gold before crops pay out) |
| **Latest Plant Day** | Quietus Harvest Cutoff | *"What is the last calendar day to plant and still get maximum harvests?"* | **Late Season Planning** (Avoiding crops withering on Day 30) |

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


## 4. Capital Days (G*d)

### Formula
$$k = s \cdot (m + 1)$$

Where:
* $s$ = seed cost
* $m$ = mature / growth days (with $+1$ for shipping payout delay)

### Examples
* **Dress Lettuce**: $55 \times 3 = \mathbf{165\text{ G}\cdot\text{d}}$ *(ultra-safe liquidity)*
* **Morrocorn (Shatolla)**: $200 \times 5 = \mathbf{1,000\text{ G}\cdot\text{d}}$ *(Lethe: $230 \times 5 = \mathbf{1,150\text{ G}\cdot\text{d}}$)*
* **Lantern Pumpkin**: $3,750 \times 12 = \mathbf{45,000\text{ G}\cdot\text{d}}$ *(extreme cash freeze)*

## 5. Daily NQ Profit

### Formula

For single crops:
$$\delta = \frac{p - s}{m}$$

For repeat crops:
$$\delta = \frac{(n \cdot p) - s}{m + (n - 1) \cdot g}$$

Where:
* $p$ = NQ sell price
* $s$ = seed cost
* $m$ = mature days
* $g$ = regrowth days
* $n$ = harvest count (capped by $\text{Max Harvests}$ or season duration)
* $m + (n - 1) \cdot g$ = total active growth days

### Examples
* **Dress Lettuce**: $\frac{85 - 55}{2} = \mathbf{+15.0\text{ G/d}}$
* **Cucumble** ($m=4, g=3, n=6$): $\frac{(6 \cdot 200) - 370}{4 + (5 \cdot 3)} = \frac{830}{19} = \mathbf{+43.7\text{ G/d}}$

## 6. Latest Plant Day

### Formula

For single crops (latest day to reap a harvest before Quietus):
$$l = 30 - m$$

For repeat crops (latest day to achieve full harvest run of $n$ yields):
$$l = 30 - [m + (n - 1) \cdot g]$$

Where:
* $m$ = mature days
* $g$ = regrowth days
* $n$ = harvest count achieved before Quietus
* $l$ = latest plant day

### Examples

#### Single Crop: Dress Lettuce ($m = 2$)

Dress Lettuce takes 2 days to mature. To harvest on or before Day 30 prior to Quietus:

$$l = 30 - 2 = \mathbf{\text{Day } 28}$$

*(Planting on the morning of Day 28 yields on the morning of Day 30, right before Quietus).*

#### Repeat Crop: Cucumble ($m = 4$, $g = 3$, $n = 6$)

Cucumble yields its 1st harvest on Day $p + 4$, and each of the remaining 5 harvests every 3 days ($5 \times 3 = 15$ days), requiring $4 + 15 = 19$ growth days total for all 6 harvests:

$$l = 30 - 19 = \mathbf{\text{Day } 11}$$
