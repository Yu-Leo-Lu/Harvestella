# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 25
- **Planning Timeline**: Day 25 -> Day 30 (6d Quietus window)
- **Capital Budget**: 34,530 G
- **Plot Capacities (Usable / Max)**: Farm: 236/245 | Waterside: 81/81 | Cave: 79/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D26, D28, D30 | Freed D30 | +4,950 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D25, D26, D27, D28 | Freed D28 | +6,760 G |
| Farm | **Seatide Garlic** | 24 | Day 21 | D27 | Freed D27 | +24,000 G |
| Farm | **Morrocorn** | 29 | Day 22 | D26 | Freed D26 | +11,600 G |
| Farm | **Dress Lettuce** | 24 | Day 24 | D26 | Freed D26 | +2,040 G |
| Farm | **Seatide Garlic** | 99 | Day 24 | D30 | Freed D30 | +99,000 G |
| Farm | **Stellar Wheat** | 6 | Day 24 | D26 | Freed D26 | +330 G |
| Waterside | **Islet Watermelon** | 2 | Day 13 | D25 | Freed D25 | +9,200 G |
| Waterside | **Islet Watermelon** | 5 | Day 16 | D28 | Freed D28 | +23,000 G |
| Waterside | **Nectarcane** | 10 | Day 17 | D27 | Freed D27 | +2,500 G |
| Waterside | **Islet Watermelon** | 3 | Day 18 | D30 | Freed D30 | +13,800 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D25, D28 | Freed D28 | +16,500 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D27, D30 | Freed D30 | +4,500 G |
| Waterside | **Honey Flower** | 19 | Day 23 | D29 | Freed D29 | +11,970 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D27, D30 | Freed D30 | +4,770 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D27 | Freed D27 | +11,000 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D27, D30 | Freed D30 | +5,000 G |
| Cave | **Curry Herbs** | 16 | Day 24 | D30 | Freed D30 | +5,600 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 25**

- **Morning Wallet**: **34,530 G**
- **Harvest & Ship** *(+19,140 G arriving D26)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 1/4)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 13 | 2,600 G | D29 | +2,600 G |

- **Daily Seed Spent**: 2,600 G | **End-of-Day Wallet**: **31,930 G**
- **Plots Left**: Farm: 0 | Waterside: 2 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **51,070 G** *(31,930 G carryover + 19,140 G payout)*
- **Harvest & Ship** *(+17,310 G arriving D27)*:
  - 24x Dress Lettuce *(Farm)* → +2,040 G (freed)
  - 29x Morrocorn *(Farm)* → +11,600 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 2/4)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/3)
  - 6x Stellar Wheat *(Farm)* → +330 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 2 | 460 G | D30 | +340 G |
| Farm | **Morrocorn** | Shatolla | 57 | 11,400 G | D30 | +11,400 G |

- **Daily Seed Spent**: 11,860 G | **End-of-Day Wallet**: **39,210 G**
- **Plots Left**: Farm: 0 | Waterside: 2 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **56,520 G** *(39,210 G carryover + 17,310 G payout)*
- **Harvest & Ship** *(+46,325 G arriving D28)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 3/4)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 19x Nectarcane *(Waterside)* → +4,750 G (regrowth 1/1)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/2)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 24 | 2,520 G | D28 | +240 G |

- **Daily Seed Spent**: 2,520 G | **End-of-Day Wallet**: **54,000 G**
- **Plots Left**: Farm: 0 | Waterside: 12 | Cave: 44

---

#### **Day 28**

- **Morning Wallet**: **100,325 G** *(54,000 G carryover + 46,325 G payout)*
- **Harvest & Ship** *(+37,350 G arriving D29)*:
  - 24x Carrop *(Farm)* → +2,760 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 4/4)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 2/3)
  - 5x Islet Watermelon *(Waterside)* → +23,000 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 14 | 1,470 G | D29 | +140 G |
| Farm | **Dress Lettuce** | Lethe | 36 | 1,980 G | D30 | +1,080 G |

- **Daily Seed Spent**: 3,450 G | **End-of-Day Wallet**: **96,875 G**
- **Plots Left**: Farm: 0 | Waterside: 50 | Cave: 44

---

#### **Day 29**

- **Morning Wallet**: **134,225 G** *(96,875 G carryover + 37,350 G payout)*
- **Harvest & Ship** *(+18,780 G arriving D30)*:
  - 14x Carrop *(Farm)* → +1,610 G (freed)
  - 13x Morrocorn *(Farm)* → +5,200 G (freed)
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 12 | 1,260 G | D30 | +120 G |
| Farm | **Carrop** | Nemea | 15 | 1,425 G | D30 | +300 G |

- **Daily Seed Spent**: 2,685 G | **End-of-Day Wallet**: **131,540 G**
- **Plots Left**: Farm: 0 | Waterside: 69 | Cave: 44

---

#### **Day 30**

- **Morning Wallet**: **150,320 G** *(131,540 G carryover + 18,780 G payout)*
- **Harvest & Ship** *(+156,950 G arriving D31)*:
  - 27x Carrop *(Farm)* → +3,105 G (freed)
  - 36x Dress Lettuce *(Farm)* → +3,060 G (freed)
  - 59x Morrocorn *(Farm)* → +23,600 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 3/3)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 2/2)
  - 16x Curry Herbs *(Cave)* → +5,600 G (freed)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 2/2)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **150,320 G**

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **307,270 G** *(150,320 G carryover + 156,950 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 25–30)

- **Starting Wallet (Day 25)**: 34,530 G
- **Ending Wallet (Day 31 Quietus)**: **307,270 G**
- **Pre-planted Crop Sales**: **+256,520 G**
- **New Planting Net Profit**: **+16,220 G**
- **Net Profit (6 days)**: **+272,740 G**
- **Average Daily Profit**: **+45,457 G/day** *(over 6 active days)*
- **Capital Growth**: **8.90x** *(+789.9% return on starting purse)*
