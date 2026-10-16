# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Mixed-Integer Linear Programming (MILP).

## Executive Summary

| Season | Budget (G) | Optimal Seed Purchases | Plots Used | Gold Spent / Leftover | Total Daily Profit | Projected Window Net |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Spring** | 1,000 G | • 9 Unionion (Nemea)<br>• 1 Dress Lettuce | 10 / 70 Farm | 1,000 G / 0 G (100.0%) | +285.0 G/day | +8,550 G (30d) |
| **Summer** | 51,000 G | • 98 Carrop (Lethe) | 98 Farm, 0 Water, 0 Cave | 10,290 G / 40,710 G (20.2%) | +980.0 G/day | +2,940 G (3d) |
| **Fall** | 15,000 G | • 70 Unionion (Nemea)<br>• 12 Nectarcane<br>• 8 Sudor Pepper | 70 Farm, 12 Water, 8 Cave | 14,990 G / 10 G (99.9%) | +2,867.2 G/day | +86,016 G (30d) |
| **Winter** | 20,000 G | • 8 Chilly Plant<br>• 61 Argene Cabbage<br>• 1 Lumpotato (Argene) | 70 / 70 Farm | 19,900 G / 100 G (99.5%) | +2,109.5 G/day | +63,285 G (30d) |

---

## Spring Detailed Allocation

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Planning Horizon**: Quietus Deadline (Day 30, 30d window)
- **Capital Budget**: 1,000 G
- **Plot Capacities**: Farm 70 plots | Waterside 0 plots | Cave 0 plots

### Optimal Planting Table

| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion (Nemea)** | Nemea | 105 G | 9 | 945 G | +30.0 | +270.0 | 3d | `27, 24, 21, 18, 15, ... , 3` |
| Farm | **Dress Lettuce** | Lethe | 55 G | 1 | 55 G | +15.0 | +15.0 | 2d | `28, 26, 24, 22, 20, ... , 2` |

### Resource Utilization & Financial Summary

- **Farm Plots Used**: 10 / 70 (14.3% utilized, 60 idle)
- **Capital Investment**: 1,000 G / 0 G (100.0 spent, 0 G leftover)
- **Total Daily Profit**: **+285.0 G/day**
- **Projected Horizon Net Profit**: **+8,550 G** over 30 active days

---

## Summer Detailed Allocation

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Planning Horizon**: Next Vendor Restock (Day 21, 3d window)
- **Variety Limit**: Max 3 distinct crop varieties
- **Capital Budget**: 51,000 G
- **Plot Capacities**: Farm 98 plots | Waterside 18 plots | Cave 18 plots

### Optimal Planting Table

| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop (Lethe)** | Lethe | 105 G | 98 | 10,290 G | +10.0 | +980.0 | 1d | `29, 28, 27, 26, 25, ... , 1` |

### Resource Utilization & Financial Summary

- **Farm Plots Used**: 98 / 98 (100.0% utilized, 0 idle)
- **Waterside Plots Used**: 0 / 18 (0.0% utilized, 18 idle)
- **Cave Plots Used**: 0 / 18 (0.0% utilized, 18 idle)
- **Capital Investment**: 10,290 G / 40,710 G (20.2 spent, 40,710 G leftover)
- **Total Daily Profit**: **+980.0 G/day**
- **Projected Horizon Net Profit**: **+2,940 G** over 3 active days

---

## Fall Detailed Allocation

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Planning Horizon**: Quietus Deadline (Day 30, 30d window)
- **Capital Budget**: 15,000 G
- **Plot Capacities**: Farm 70 plots | Waterside 12 plots | Cave 12 plots

### Optimal Planting Table

| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion (Nemea)** | Nemea | 105 G | 70 | 7,350 G | +30.0 | +2100.0 | 3d | `27, 24, 21, 18, 15, ... , 3` |
| Waterside | **Nectarcane** | Shatolla/Nemea | 370 G | 12 | 4,440 G | +38.0 | +456.0 | 10d | `20, 10` |
| Cave | **Sudor Pepper** | Argene | 400 G | 8 | 3,200 G | +38.9 | +311.2 | 9d | `21, 12, 3` |

### Resource Utilization & Financial Summary

- **Farm Plots Used**: 70 / 70 (100.0% utilized, 0 idle)
- **Waterside Plots Used**: 12 / 12 (100.0% utilized, 0 idle)
- **Cave Plots Used**: 8 / 12 (66.7% utilized, 4 idle)
- **Capital Investment**: 14,990 G / 10 G (99.9 spent, 10 G leftover)
- **Total Daily Profit**: **+2,867.2 G/day**
- **Projected Horizon Net Profit**: **+86,016 G** over 30 active days

---

## Winter Detailed Allocation

- **Config Profile**: [`configs/winter.yaml`](configs/winter.yaml)
- **Planning Horizon**: Quietus Deadline (Day 30, 30d window)
- **Capital Budget**: 20,000 G
- **Plot Capacities**: Farm 70 plots | Waterside 0 plots | Cave 0 plots

### Optimal Planting Table

| Biome | Crop Name | Vendor Town | Seed Cost (G) | Qty | Subtotal Cost (G) | Daily Profit (G/d) | Total Profit (G/d) | Cycle | Planting Schedule |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Chilly Plant** | Argene | 800 G | 8 | 6,400 G | +71.4 | +571.2 | 7d | `23, 16, 9, 2` |
| Farm | **Argene Cabbage** | Argene | 220 G | 61 | 13,420 G | +25.0 | +1525.0 | 4d | `26, 22, 18, 14, 10, 6, 2` |
| Farm | **Lumpotato (Argene)** | Argene | 80 G | 1 | 80 G | +13.3 | +13.3 | 3d | `27, 24, 21, 18, 15, ... , 3` |

### Resource Utilization & Financial Summary

- **Farm Plots Used**: 70 / 70 (100.0% utilized, 0 idle)
- **Capital Investment**: 19,900 G / 100 G (99.5 spent, 100 G leftover)
- **Total Daily Profit**: **+2,109.5 G/day**
- **Projected Horizon Net Profit**: **+63,285 G** over 30 active days

---

## Key Optimization Principles

1. **The Capital-Plot Inflection Balance**:
   - When wallet capital is scarce (e.g., 1,000 G in Spring), high-compound crops like **Unionion (Nemea)** multiply money fast, while cheap seeds like **Dress Lettuce** act as plot-filling buffers.
2. **Avoiding Single-Crop Capital Traps**:
   - In Summer with 8,000 G, buying expensive seeds like **Islet Watermelon** (2,500 G) starves remaining plots. The solver allocates **29 Morrocorn** + **40 Dress Lettuce** to generate +2,050 G/day (+27% higher total profit than any Watermelon mix).
3. **Biome Specialization**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
