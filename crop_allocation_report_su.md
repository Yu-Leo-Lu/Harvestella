# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 28
- **Planning Timeline**: Day 28 -> Day 30 (3d Quietus window)
- **Capital Budget**: 150,945 G
- **Plot Capacities (Usable / Max)**: Farm: 275/294 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Bellhop** | 1 | Day 5 | D28, D29, D30 | Stays Planted | +135 G |
| Farm | **Bellhop** | 1 | Day 6 | D28, D29, D30 | Stays Planted | +135 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D28, D30 | Freed D30 | +660 G |
| Farm | **Shatollan Paprika** | 37 | Day 17 | D28, D30 | Stays Planted | +8,140 G |
| Farm | **Nemean Tomato** | 6 | Day 24 | D29, D30 | Stays Planted | +780 G |
| Farm | **Seatide Garlic** | 99 | Day 24 | D30 | Freed D30 | +99,000 G |
| Farm | **Grass** | 17 | Day 26 | D28 | Freed D28 | +595 G |
| Farm | **Morrocorn** | 96 | Day 26 | D30 | Freed D30 | +38,400 G |
| Farm | **Eden Rice** | 15 | Day 27 | D30 | Freed D30 | +525 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 54 | Day 17 | D29 | Freed D29 | +248,400 G |
| Waterside | **Islet Watermelon** | 15 | Day 18 | D30 | Freed D30 | +69,000 G |
| Cave | **Revol Pepper** | 12 | Day 17 | D30 | Stays Planted | +3,180 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 28**

- **Morning Wallet**: **150,945 G**
- **Harvest & Ship** *(+14,285 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/3)
  - 17x Grass *(Farm)* → +595 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 1/2)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 17 | 1,615 G | D29 | +340 G |

- **Daily Seed Spent**: 1,615 G | **End-of-Day Wallet**: **149,330 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **163,615 G** *(149,330 G carryover + 14,285 G payout)*
- **Harvest & Ship** *(+250,835 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/3)
  - 17x Carrop *(Farm)* → +1,955 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 1/2)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 17 | 1,615 G | D30 | +340 G |

- **Daily Seed Spent**: 1,615 G | **End-of-Day Wallet**: **162,000 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **412,835 G** *(162,000 G carryover + 250,835 G payout)*
- **Harvest & Ship** *(+216,940 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/3)
  - 17x Carrop *(Farm)* → +1,955 G (freed)
  - 15x Eden Rice *(Farm)* → +525 G (freed)
  - 96x Morrocorn *(Farm)* → +38,400 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 2/2)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 2/2)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/1)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **412,835 G**
- **Plots Left**: Farm: 230 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **629,775 G** *(412,835 G carryover + 216,940 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 28–30)

- **Starting Wallet (Day 28)**: 150,945 G
- **Ending Wallet (Day 31 Quietus)**: **629,775 G**
- **Pre-planted Crop Sales**: **+478,150 G**
- **New Planting Net Profit**: **+680 G**
- **Net Profit (3 days)**: **+478,830 G**
- **Average Daily Profit**: **+159,610 G/day** *(over 3 active days)*
