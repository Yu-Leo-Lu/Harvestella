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

For repeat crops (30-day wealth compounding):
$$r = \left(\left(\frac{n \cdot p}{s}\right)^{\frac{1}{30}} - 1\right) \times 100\%$$

Where:
* $p$ = sell price
* $s$ = seed cost
* $m$ = mature / growth days
* $n = \lfloor 30 / m \rfloor$ (harvest count)

### Examples
* **Unionion (Nemea)**: $\left(\left(\frac{195}{105}\right)^{\frac{1}{4}} - 1\right) \times 100\% = \mathbf{+16.74\%/\text{day}}$ *(Lethe @ 130 G: $\mathbf{+10.67\%/\text{day}}$)*
* **Dress Lettuce**: $\left(\left(\frac{85}{55}\right)^{\frac{1}{3}} - 1\right) \times 100\% = \mathbf{+15.62\%/\text{day}}$
* **Morrocorn (Shatolla)**: $\left(\left(\frac{400}{200}\right)^{\frac{1}{5}} - 1\right) \times 100\% = \mathbf{+14.87\%/\text{day}}$ *(Lethe @ 230 G: $\mathbf{+11.70\%/\text{day}}$)*

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
$$\delta = \frac{(n \cdot p) - s}{m + (n - 1) \cdot r}$$

Where:
* $p$ = NQ sell price
* $s$ = seed cost
* $m$ = mature days
* $r$ = regrowth days
* $n$ = harvest count (capped by $\text{Max Harvests}$ or season duration)
* $m + (n - 1) \cdot r$ = total active growth days

### Examples
* **Unionion (Nemea)**: $\frac{195 - 105}{3} = \mathbf{+30.0\text{ G/d}}$ *(Lethe @ 130 G: $\mathbf{+21.7\text{ G/d}}$)*
* **Dress Lettuce**: $\frac{85 - 55}{2} = \mathbf{+15.0\text{ G/d}}$
* **Morrocorn (Shatolla)**: $\frac{400 - 200}{4} = \mathbf{+50.0\text{ G/d}}$
* **Cucumble** ($m=4, r=3, n=6$): $\frac{(6 \cdot 200) - 370}{4 + (5 \cdot 3)} = \frac{830}{19} = \mathbf{+43.7\text{ G/d}}$
* **Nemean Tomato** ($m=5, r=1, n=6$): $\frac{(6 \cdot 65) - 170}{5 + (5 \cdot 1)} = \frac{220}{10} = \mathbf{+22.0\text{ G/d}}$
* **Bellhop Seeds** ($m=7, r=1, n=24$): $\frac{(24 \cdot 45) - 560}{7 + (23 \cdot 1)} = \frac{520}{30} = \mathbf{+17.3\text{ G/d}}$

## 6. Latest Plant Day

### Formula

For single crops (latest day to reap a harvest before Quietus):
$$l = 30 - m$$

For repeat crops (latest day to achieve full harvest run of $n$ yields):
$$l = 30 - [m + (n - 1) \cdot r]$$

Where:
* $m$ = mature days
* $r$ = regrowth days
* $n$ = harvest count achieved before Quietus
* $l$ = latest plant day

### Examples

#### Single Crop: Dress Lettuce ($m = 2$)

Dress Lettuce takes 2 days to mature. To harvest on or before Day 30 prior to Quietus:

$$l = 30 - 2 = \mathbf{\text{Day } 28}$$

*(Planting on the morning of Day 28 yields on the morning of Day 30, right before Quietus).*

#### Repeat Crop: Cucumble ($m = 4$, $r = 3$, $n = 6$)

Cucumble yields its 1st harvest on Day $p + 4$, and each of the remaining 5 harvests every 3 days ($5 \times 3 = 15$ days), requiring $4 + 15 = 19$ growth days total for all 6 harvests:

$$l = 30 - 19 = \mathbf{\text{Day } 11}$$
