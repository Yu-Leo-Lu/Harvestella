# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 29
- **Planning Timeline**: Day 29 -> Day 30 (2d Quietus window)
- **Capital Budget**: 66,290 G
- **Plot Capacities (Usable / Max)**: Farm: 286/294 | Waterside: 81/81 | Cave: 79/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D30 | Freed D30 | +1,650 G |
| Farm | **Seatide Garlic** | 99 | Day 24 | D30 | Freed D30 | +99,000 G |
| Farm | **Morrocorn** | 14 | Day 25 | D29 | Freed D29 | +5,600 G |
| Farm | **Morrocorn** | 83 | Day 26 | D30 | Freed D30 | +33,200 G |
| Farm | **Carrop** | 25 | Day 28 | D29 | Freed D29 | +2,875 G |
| Farm | **Dress Lettuce** | 36 | Day 28 | D30 | Freed D30 | +3,060 G |
| Farm | **Stellar Wheat** | 14 | Day 28 | D30 | Freed D30 | +770 G |
| Waterside | **Islet Watermelon** | 1 | Day 17 | D29 | Freed D29 | +4,600 G |
| Waterside | **Islet Watermelon** | 3 | Day 18 | D30 | Freed D30 | +13,800 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D30 | Freed D30 | +2,250 G |
| Waterside | **Honey Flower** | 19 | Day 23 | D29 | Freed D29 | +11,970 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D30 | Freed D30 | +2,385 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D30 | Freed D30 | +2,500 G |
| Cave | **Curry Herbs** | 16 | Day 24 | D30 | Freed D30 | +5,600 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 29**

- **Morning Wallet**: **66,290 G**
- **Harvest & Ship** *(+25,045 G arriving D30)*:
  - 25x Carrop *(Farm)* → +2,875 G (freed)
  - 14x Morrocorn *(Farm)* → +5,600 G (freed)
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)
  - 1x Islet Watermelon *(Waterside)* → +4,600 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 24 | 2,520 G | D30 | +240 G |
| Farm | **Carrop** | Nemea | 15 | 1,425 G | D30 | +300 G |

- **Daily Seed Spent**: 3,945 G | **End-of-Day Wallet**: **62,345 G**
- **Plots Left**: Farm: 0 | Waterside: 69 | Cave: 44

---

#### **Day 30**

- **Morning Wallet**: **87,390 G** *(62,345 G carryover + 25,045 G payout)*
- **Harvest & Ship** *(+168,700 G arriving D31)*:
  - 39x Carrop *(Farm)* → +4,485 G (freed)
  - 36x Dress Lettuce *(Farm)* → +3,060 G (freed)
  - 83x Morrocorn *(Farm)* → +33,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/1)
  - 14x Stellar Wheat *(Farm)* → +770 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 1/1)
  - 16x Curry Herbs *(Cave)* → +5,600 G (freed)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/1)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 1/1)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **87,390 G**
- **Plots Left**: Farm: 286 | Waterside: 81 | Cave: 79

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **256,090 G** *(87,390 G carryover + 168,700 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 29–30)

- **Starting Wallet (Day 29)**: 66,290 G
- **Ending Wallet (Day 31 Quietus)**: **256,090 G**
- **Pre-planted Crop Sales**: **+189,260 G**
- **New Planting Net Profit**: **+540 G**
- **Net Profit (2 days)**: **+189,800 G**
- **Average Daily Profit**: **+94,900 G/day** *(over 2 active days)*
