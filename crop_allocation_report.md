# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 27
- **Planning Timeline**: Day 27 -> Day 30 (4d Quietus window)
- **Capital Budget**: 19,065 G
- **Plot Capacities (Usable / Max)**: Farm: 237/245 | Waterside: 81/81 | Cave: 79/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D28, D30 | Freed D30 | +3,300 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D27, D28 | Freed D28 | +3,380 G |
| Farm | **Seatide Garlic** | 99 | Day 24 | D30 | Freed D30 | +99,000 G |
| Farm | **Morrocorn** | 14 | Day 25 | D29 | Freed D29 | +5,600 G |
| Farm | **Morrocorn** | 83 | Day 26 | D30 | Freed D30 | +33,200 G |
| Waterside | **Islet Watermelon** | 2 | Day 15 | D27 | Freed D27 | +9,200 G |
| Waterside | **Islet Watermelon** | 3 | Day 16 | D28 | Freed D28 | +13,800 G |
| Waterside | **Nectarcane** | 10 | Day 17 | D27 | Freed D27 | +2,500 G |
| Waterside | **Islet Watermelon** | 3 | Day 18 | D30 | Freed D30 | +13,800 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D28 | Freed D28 | +8,250 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D27, D30 | Freed D30 | +4,500 G |
| Waterside | **Honey Flower** | 19 | Day 23 | D29 | Freed D29 | +11,970 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D27, D30 | Freed D30 | +4,770 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D27 | Freed D27 | +11,000 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D27, D30 | Freed D30 | +5,000 G |
| Cave | **Curry Herbs** | 16 | Day 24 | D30 | Freed D30 | +5,600 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 27**

- **Morning Wallet**: **19,065 G**
- **Harvest & Ship** *(+31,525 G arriving D28)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 1/2)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 19x Nectarcane *(Waterside)* → +4,750 G (regrowth 1/1)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/2)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 1/1)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **19,065 G**
- **Plots Left**: Farm: 0 | Waterside: 14 | Cave: 44

---

#### **Day 28**

- **Morning Wallet**: **50,590 G** *(19,065 G carryover + 31,525 G payout)*
- **Harvest & Ship** *(+25,390 G arriving D29)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 2/2)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/2)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 25 | 1,375 G | D30 | +750 G |
| Farm | **Carrop** | Nemea | 1 | 95 G | D29 | +20 G |

- **Daily Seed Spent**: 1,470 G | **End-of-Day Wallet**: **49,120 G**
- **Plots Left**: Farm: 0 | Waterside: 50 | Cave: 44

---

#### **Day 29**

- **Morning Wallet**: **74,510 G** *(49,120 G carryover + 25,390 G payout)*
- **Harvest & Ship** *(+17,685 G arriving D30)*:
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 14x Morrocorn *(Farm)* → +5,600 G (freed)
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 14 | 1,330 G | D30 | +280 G |

- **Daily Seed Spent**: 1,330 G | **End-of-Day Wallet**: **73,180 G**
- **Plots Left**: Farm: 1 | Waterside: 69 | Cave: 44

---

#### **Day 30**

- **Morning Wallet**: **90,865 G** *(73,180 G carryover + 17,685 G payout)*
- **Harvest & Ship** *(+164,120 G arriving D31)*:
  - 14x Carrop *(Farm)* → +1,610 G (freed)
  - 25x Dress Lettuce *(Farm)* → +2,125 G (freed)
  - 83x Morrocorn *(Farm)* → +33,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 2/2)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 2/2)
  - 16x Curry Herbs *(Cave)* → +5,600 G (freed)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 2/2)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **90,865 G**
- **Plots Left**: Farm: 237 | Waterside: 81 | Cave: 79

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **254,985 G** *(90,865 G carryover + 164,120 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 27–30)

- **Starting Wallet (Day 27)**: 19,065 G
- **Ending Wallet (Day 31 Quietus)**: **254,985 G**
- **Pre-planted Crop Sales**: **+234,870 G**
- **New Planting Net Profit**: **+1,050 G**
- **Net Profit (4 days)**: **+235,920 G**
- **Average Daily Profit**: **+58,980 G/day** *(over 4 active days)*
