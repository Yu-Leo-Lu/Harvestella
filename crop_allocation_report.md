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

- **Starting Cash**: 51,600 G | **Stage Spent**: 56,685 G | **Farm Plots Used**: 102 / 61

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 18 | Farm | **Carrop** | Nemea | 21 | 1,995 G | Day 19 | +420 G |
| Day 18 | Farm | **Carrop** | Lethe | 30 | 3,150 G | Day 19 | +300 G |
| Day 18 | Farm | **Stellar Wheat** | Lethe | 10 | 400 G | Day 20 | +150 G |
| Day 18 | Waterside | **Islet Watermelon** | Shatolla | 10 | 25,000 G | Day 30 | +21,000 G |
| Day 18 | Waterside | **Nectarcane** | Shatolla | 10 | 3,700 G | Day 22, Day 25, Day 28 | +3,800 G |
| Day 18 | Cave | **Sudor Pepper** | Argene | 38 | 15,200 G | Day 21, Day 24, Day 27 | +13,300 G |
| Day 19 | Farm | **Stellar Wheat** | Lethe | 41 | 1,640 G | Day 21 | +615 G |
| Day 20 | Cave | **Sudor Pepper** | Argene | 14 | 5,600 G | Day 23, Day 26, Day 29 | +4,900 G |

- **Stage Harvest Revenue Arrived**: +5,865 G | **Projected Cash at Stage End**: **780 G**

#### Stage 2: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 780 G | **Stage Spent**: 31,665 G | **Farm Plots Used**: 123 / 61

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 21 | Farm | **Morrocorn** | Shatolla | 1 | 200 G | Day 25 | +200 G |
| Day 21 | Cave | **Sudor Pepper** | Argene | 1 | 400 G | Day 24, Day 27, Day 30 | +350 G |
| Day 22 | Farm | **Morrocorn** | Shatolla | 60 | 12,000 G | Day 26 | +12,000 G |
| Day 24 | Waterside | **Honey Flower** | Shatolla | 16 | 6,080 G | Day 30 | +4,000 G |
| Day 25 | Farm | **Morrocorn** | Lethe | 1 | 230 G | Day 29 | +170 G |
| Day 26 | Farm | **Morrocorn** | Shatolla | 38 | 7,600 G | Day 30 | +7,600 G |
| Day 26 | Farm | **Morrocorn** | Lethe | 22 | 5,060 G | Day 30 | +3,740 G |
| Day 29 | Farm | **Carrop** | Nemea | 1 | 95 G | Day 30 | +20 G |

- **Stage Harvest Revenue Arrived**: +74,605 G | **Projected Cash at Stage End**: **43,720 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 61 / 61 (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 20 / 36 (55.6% utilized, 16 idle)
- **Cave Plots Used (Init)**: 38 / 54 (70.4% utilized, 16 idle)
- **Initial Capital Spent**: 49,445 G / 51,600 G (95.8% spent, 2,155 G leftover)
- **Total Cumulative Season Net Profit**: **+72,565 G** across all restock stages
- **Final Projected Wallet**: **124,165 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
