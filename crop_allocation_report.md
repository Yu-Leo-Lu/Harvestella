# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 18
- **Planning Timeline**: Day 18 -> Day 30 (13d Quietus window)
- **Capital Budget**: 51,600 G
- **Plot Capacities**: Farm 61 -> 145 | Waterside 36 -> 81 | Cave 54 -> 81

### Optimal Planting Timeline

#### Stage 1: Day 18 → Day 20 (3-day window)

- **Starting Cash**: 51,600 G | **Stage Spent**: 52,655 G | **Farm (Peak)**: 61 / 61 (Seeds: 79) | **Waterside (Peak)**: 36 / 36 | **Cave (Peak)**: 53 / 54

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 18 | Farm | **Nemean Tomato** | Nemea | 8 | 1,360 G | Day 23..28 (6x) | +1,760 G |
| Day 18 | Farm | **Carrop** | Nemea | 11 | 1,045 G | Day 19 | +220 G |
| Day 18 | Farm | **Stellar Wheat** | Lethe | 42 | 1,680 G | Day 20 | +630 G |
| Day 18 | Waterside | **Islet Watermelon** | Shatolla | 6 | 15,000 G | Day 30 | +12,600 G |
| Day 18 | Waterside | **Nectarcane** | Shatolla | 30 | 11,100 G | Day 22, Day 25, Day 28 | +11,400 G |
| Day 18 | Cave | **Sudor Pepper** | Argene | 51 | 20,400 G | Day 21, Day 24, Day 27 | +17,850 G |
| Day 19 | Farm | **Carrop** | Nemea | 10 | 950 G | Day 20 | +200 G |
| Day 20 | Farm | **Stellar Wheat** | Lethe | 8 | 320 G | Day 22 | +120 G |
| Day 20 | Cave | **Sudor Pepper** | Argene | 2 | 800 G | Day 23, Day 26, Day 29 | +700 G |

- **Stage Harvest Revenue Arrived**: +1,265 G | **Projected Cash at Stage End**: **210 G**

#### Stage 2: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 210 G | **Stage Spent**: 66,120 G | **Farm (Peak)**: 144 / 145 (Seeds: 344) | **Waterside (Peak)**: 80 / 81 | **Cave (Peak)**: 68 / 81

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 21 | Farm | **Morrocorn** | Shatolla | 4 | 800 G | Day 25 | +800 G |
| Day 21 | Farm | **Carrop** | Nemea | 12 | 1,140 G | Day 22 | +240 G |
| Day 21 | Farm | **Dress Lettuce** | Lethe | 29 | 1,595 G | Day 23 | +870 G |
| Day 22 | Farm | **Morrocorn** | Shatolla | 8 | 1,600 G | Day 26 | +1,600 G |
| Day 22 | Farm | **Carrop** | Nemea | 12 | 1,140 G | Day 23 | +240 G |
| Day 23 | Farm | **Dress Lettuce** | Lethe | 69 | 3,795 G | Day 25 | +2,070 G |
| Day 23 | Cave | **Curry Herbs** | Argene | 15 | 3,600 G | Day 29 | +1,650 G |
| Day 24 | Waterside | **Honey Flower** | Shatolla | 44 | 16,720 G | Day 30 | +11,000 G |
| Day 25 | Farm | **Morrocorn** | Shatolla | 66 | 13,200 G | Day 29 | +13,200 G |
| Day 26 | Farm | **Morrocorn** | Shatolla | 20 | 4,000 G | Day 30 | +4,000 G |
| Day 26 | Farm | **Morrocorn** | Lethe | 50 | 11,500 G | Day 30 | +8,500 G |
| Day 29 | Farm | **Carrop** | Nemea | 74 | 7,030 G | Day 30 | +1,480 G |

- **Stage Harvest Revenue Arrived**: +116,810 G | **Projected Cash at Stage End**: **50,900 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 61 / 61 (expands to 145) (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 36 / 36 (expands to 81) (100.0% utilized, 0 idle)
- **Cave Plots Used (Init)**: 51 / 54 (expands to 81) (94.4% utilized, 3 idle)
- **Initial Capital Spent**: 50,585 G / 51,600 G (98.0% spent, 1,015 G leftover)
- **Total Cumulative Season Net Profit**: **+91,130 G** across all restock stages
- **Final Projected Wallet**: **142,730 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
