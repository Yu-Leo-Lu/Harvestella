# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Mixed-Integer Linear Programming (MILP).

## Executive Summary

| Season | Budget (G) | Optimal Seed Purchases | Plots Used | Gold Spent / Leftover | Total Daily Profit | Projected Window Net |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Summer** | 8,000 G | • 29 Morrocorn (Shatolla)<br>• 40 Dress Lettuce | 69 Farm, 0 Water, 0 Cave | 8,000 G / 0 G (100.0%) | +2,050.0 G/day | +61,500 G (30d) |

---

## Summer Detailed Allocation

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Planning Horizon**: Quietus Deadline (Day 30, 30d window)
- **Capital Budget**: 8,000 G
- **Plot Capacities**: Farm 70 plots | Waterside 12 plots | Cave 12 plots

### Optimal Planting Table

| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn (Shatolla)** | Shatolla | 200 G | 29 | 5,800 G | +50.0 | +1450.0 | 4d | `26, 22, 18, 14, 10, 6, 2` |
| Farm | **Dress Lettuce** | Lethe | 55 G | 40 | 2,200 G | +15.0 | +600.0 | 2d | `28, 26, 24, 22, 20, ... , 2` |

### Resource Utilization & Financial Summary

- **Farm Plots Used**: 69 / 70 (98.6% utilized, 1 idle)
- **Waterside Plots Used**: 0 / 12 (0.0% utilized, 12 idle)
- **Cave Plots Used**: 0 / 12 (0.0% utilized, 12 idle)
- **Capital Investment**: 8,000 G / 0 G (100.0 spent, 0 G leftover)
- **Total Daily Profit**: **+2,050.0 G/day**
- **Projected Horizon Net Profit**: **+61,500 G** over 30 active days

---

## Key Optimization Principles

1. **The Capital-Plot Inflection Balance**:
   - When wallet capital is scarce (e.g., 1,000 G in Spring), high-compound crops like **Unionion (Nemea)** multiply money fast, while cheap seeds like **Dress Lettuce** act as plot-filling buffers.
2. **Avoiding Single-Crop Capital Traps**:
   - In Summer with 8,000 G, buying expensive seeds like **Islet Watermelon** (2,500 G) starves remaining plots. The solver allocates **29 Morrocorn** + **40 Dress Lettuce** to generate +2,050 G/day (+27% higher total profit than any Watermelon mix).
3. **Biome Specialization**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
