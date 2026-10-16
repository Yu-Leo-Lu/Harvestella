# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Mixed-Integer Linear Programming (MILP).

## Executive Summary

| Season | Budget (G) | Optimal Seed Purchases | Plots Used | Gold Spent / Leftover | Total Daily Profit | Projected Window Net |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Summer** | 51,600 G | • 16 Seatide Garlic (Shatolla)<br>• 24 Nemean Tomato (Nemea)<br>• 21 Carrop (Nemea)<br>• 36 Honey Flower (Shatolla)<br>• 53 Sudor Pepper (Argene)<br>• 1 Curry Herbs (Argene) | 61 Farm, 36 Water, 54 Cave | 51,595 G / 5 G (100.0%) | +5,462.0 G/day | +65,544 G (12d) |

---

## Summer Detailed Allocation

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Planning Horizon**: Quietus Deadline (Day 30, 12d window)
- **Capital Budget**: 51,600 G
- **Plot Capacities**: Farm 61 plots | Waterside 36 plots | Cave 54 plots

### Optimal Planting Table

| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 650 G | 16 | 10,400 G | +58.3 | +932.8 | 6d | `24, 18, 12, 6` |
| Farm | **Nemean Tomato** | Nemea | 170 G | 24 | 4,080 G | +22.0 | +528.0 | 10d | `20, 10` |
| Farm | **Carrop** | Nemea | 95 G | 21 | 1,995 G | +20.0 | +420.0 | 1d | `29, 28, 27, 26, 25, ... , 1` |
| Waterside | **Honey Flower** | Shatolla | 380 G | 36 | 13,680 G | +41.7 | +1501.2 | 6d | `24, 18, 12, 6` |
| Cave | **Sudor Pepper** | Argene | 400 G | 53 | 21,200 G | +38.9 | +2061.7 | 9d | `21, 12, 3` |
| Cave | **Curry Herbs** | Argene | 240 G | 1 | 240 G | +18.3 | +18.3 | 6d | `24, 18, 12, 6` |

### Resource Utilization & Financial Summary

- **Farm Plots Used**: 61 / 61 (100.0% utilized, 0 idle)
- **Waterside Plots Used**: 36 / 36 (100.0% utilized, 0 idle)
- **Cave Plots Used**: 54 / 54 (100.0% utilized, 0 idle)
- **Capital Investment**: 51,595 G / 5 G (100.0 spent, 5 G leftover)
- **Total Daily Profit**: **+5,462.0 G/day**
- **Projected Horizon Net Profit**: **+65,544 G** over 12 active days

---

## Key Optimization Principles

1. **The Capital-Plot Inflection Balance**:
   - When wallet capital is scarce (e.g., 1,000 G in Spring), high-compound crops like **Unionion (Nemea)** multiply money fast, while cheap seeds like **Dress Lettuce** act as plot-filling buffers.
2. **Avoiding Single-Crop Capital Traps**:
   - In Summer with 8,000 G, buying expensive seeds like **Islet Watermelon** (2,500 G) starves remaining plots. The solver allocates **29 Morrocorn** + **40 Dress Lettuce** to generate +2,050 G/day (+27% higher total profit than any Watermelon mix).
3. **Biome Specialization**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
