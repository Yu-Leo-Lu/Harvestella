# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 18
- **Planning Timeline**: Day 18 -> Day 30 (13d Quietus window)
- **Capital Budget**: 51,600 G
- **Plot Capacities**: Farm 61 | Waterside 36 | Cave 54

### Optimal Planting Timeline

#### Stage 1: Day 18 → Day 20 (3-day window)

- **Starting Cash**: 51,600 G | **Stage Spent**: 54,015 G | **Farm Plots Used**: 101 / 61

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 18 | Farm | **Nemean Tomato** | Nemea | 21 | 3,570 G | Day 23..28 (6x) | +4,620 G |
| Day 18 | Farm | **Carrop** | Nemea | 21 | 1,995 G | Day 19 | +420 G |
| Day 18 | Farm | **Carrop** | Lethe | 8 | 840 G | Day 19 | +80 G |
| Day 18 | Farm | **Stellar Wheat** | Lethe | 11 | 440 G | Day 20 | +165 G |
| Day 18 | Waterside | **Islet Watermelon** | Shatolla | 5 | 12,500 G | Day 30 | +10,500 G |
| Day 18 | Waterside | **Nectarcane** | Shatolla | 31 | 11,470 G | Day 22, Day 25, Day 28 | +11,780 G |
| Day 18 | Cave | **Sudor Pepper** | Argene | 48 | 19,200 G | Day 21, Day 24, Day 27 | +16,800 G |
| Day 19 | Farm | **Stellar Wheat** | Lethe | 15 | 600 G | Day 21 | +225 G |
| Day 20 | Farm | **Stellar Wheat** | Lethe | 25 | 1,000 G | Day 22 | +375 G |
| Day 20 | Cave | **Sudor Pepper** | Argene | 6 | 2,400 G | Day 23, Day 26, Day 29 | +2,100 G |

- **Stage Harvest Revenue Arrived**: +3,335 G | **Projected Cash at Stage End**: **920 G**

#### Stage 2: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 920 G | **Stage Spent**: 34,370 G | **Farm Plots Used**: 131 / 61

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 21 | Farm | **Stellar Wheat** | Lethe | 15 | 600 G | Day 23 | +225 G |
| Day 22 | Farm | **Carrop** | Nemea | 21 | 1,995 G | Day 23 | +420 G |
| Day 22 | Farm | **Carrop** | Lethe | 4 | 420 G | Day 23 | +40 G |
| Day 23 | Farm | **Seatide Garlic** | Shatolla | 30 | 19,500 G | Day 29 | +10,500 G |
| Day 24 | Farm | **Seatide Garlic** | Shatolla | 10 | 6,500 G | Day 30 | +3,500 G |
| Day 29 | Farm | **Carrop** | Lethe | 51 | 5,355 G | Day 30 | +510 G |

- **Stage Harvest Revenue Arrived**: +108,445 G | **Projected Cash at Stage End**: **74,995 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 61 / 61 (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 36 / 36 (100.0% utilized, 0 idle)
- **Cave Plots Used (Init)**: 48 / 54 (88.9% utilized, 6 idle)
- **Initial Capital Spent**: 50,015 G / 51,600 G (96.9% spent, 1,585 G leftover)
- **Total Cumulative Season Net Profit**: **+62,260 G** across all restock stages
- **Final Projected Wallet**: **113,860 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
