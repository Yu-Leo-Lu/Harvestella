# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 28
- **Planning Timeline**: Day 28 -> Day 30 (3d Quietus window)
- **Capital Budget**: 50,665 G
- **Plot Capacities (Usable / Max)**: Farm: 286/294 | Waterside: 81/81 | Cave: 79/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D28, D30 | Freed D30 | +3,300 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D28 | Freed D28 | +1,690 G |
| Farm | **Seatide Garlic** | 99 | Day 24 | D30 | Freed D30 | +99,000 G |
| Farm | **Morrocorn** | 14 | Day 25 | D29 | Freed D29 | +5,600 G |
| Farm | **Morrocorn** | 83 | Day 26 | D30 | Freed D30 | +33,200 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 4 | Day 18 | D30 | Freed D30 | +18,400 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D28 | Freed D28 | +8,250 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D30 | Freed D30 | +2,250 G |
| Waterside | **Honey Flower** | 19 | Day 23 | D29 | Freed D29 | +11,970 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D30 | Freed D30 | +2,385 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D30 | Freed D30 | +2,500 G |
| Cave | **Curry Herbs** | 16 | Day 24 | D30 | Freed D30 | +5,600 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 28**

- **Morning Wallet**: **50,665 G**
- **Harvest & Ship** *(+20,790 G arriving D29)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 1/1)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/2)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 25 | 2,625 G | D29 | +250 G |
| Farm | **Dress Lettuce** | Lethe | 36 | 1,980 G | D30 | +1,080 G |
| Farm | **Stellar Wheat** | Lethe | 14 | 560 G | D30 | +210 G |

- **Daily Seed Spent**: 5,165 G | **End-of-Day Wallet**: **45,500 G**
- **Plots Left**: Farm: 0 | Waterside: 49 | Cave: 44

---

#### **Day 29**

- **Morning Wallet**: **66,290 G** *(45,500 G carryover + 20,790 G payout)*
- **Harvest & Ship** *(+20,445 G arriving D30)*:
  - 25x Carrop *(Farm)* → +2,875 G (freed)
  - 14x Morrocorn *(Farm)* → +5,600 G (freed)
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 24 | 2,520 G | D30 | +240 G |
| Farm | **Carrop** | Nemea | 15 | 1,425 G | D30 | +300 G |

- **Daily Seed Spent**: 3,945 G | **End-of-Day Wallet**: **62,345 G**
- **Plots Left**: Farm: 0 | Waterside: 68 | Cave: 44

---

#### **Day 30**

- **Morning Wallet**: **82,790 G** *(62,345 G carryover + 20,445 G payout)*
- **Harvest & Ship** *(+173,300 G arriving D31)*:
  - 39x Carrop *(Farm)* → +4,485 G (freed)
  - 36x Dress Lettuce *(Farm)* → +3,060 G (freed)
  - 83x Morrocorn *(Farm)* → +33,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 2/2)
  - 14x Stellar Wheat *(Farm)* → +770 G (freed)
  - 4x Islet Watermelon *(Waterside)* → +18,400 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 1/1)
  - 16x Curry Herbs *(Cave)* → +5,600 G (freed)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/1)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 1/1)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **82,790 G**
- **Plots Left**: Farm: 286 | Waterside: 81 | Cave: 79

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **256,090 G** *(82,790 G carryover + 173,300 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 28–30)

- **Starting Wallet (Day 28)**: 50,665 G
- **Ending Wallet (Day 31 Quietus)**: **256,090 G**
- **Pre-planted Crop Sales**: **+203,345 G**
- **New Planting Net Profit**: **+2,080 G**
- **Net Profit (3 days)**: **+205,425 G**
- **Average Daily Profit**: **+68,475 G/day** *(over 3 active days)*
