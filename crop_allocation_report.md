# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 22
- **Planning Timeline**: Day 22 -> Day 30 (9d Quietus window)
- **Capital Budget**: 120,180 G
- **Plot Capacities (Usable / Max)**: Farm: 232/245 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D22 | Freed D22 | +7,700 G |
| Farm | **Bellhop** | 1 | Day 5 | D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +405 G |
| Farm | **Bellhop** | 1 | Day 6 | D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +405 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D22, D24, D26, D28, D30 | Freed D30 | +1,650 G |
| Farm | **Shatollan Paprika** | 37 | Day 17 | D22, D24, D26, D28, D30 | Stays Planted | +20,350 G |
| Farm | **Seatide Garlic** | 32 | Day 18 | D24 | Freed D24 | +32,000 G |
| Farm | **Morrocorn** | 51 | Day 20 | D24 | Freed D24 | +20,400 G |
| Farm | **Seatide Garlic** | 37 | Day 20 | D26 | Freed D26 | +37,000 G |
| Waterside | **Islet Watermelon** | 3 | Day 13 | D25 | Freed D25 | +13,800 G |
| Waterside | **Islet Watermelon** | 3 | Day 15 | D27 | Freed D27 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 54 | Day 17 | D29 | Freed D29 | +248,400 G |
| Waterside | **Islet Watermelon** | 15 | Day 18 | D30 | Freed D30 | +69,000 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D23, D26 | Freed D26 | +36,570 G |
| Cave | **Revol Pepper** | 12 | Day 17 | D24, D27, D30 | Stays Planted | +9,540 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 22**

- **Morning Wallet**: **120,180 G**
- **Harvest & Ship** *(+12,190 G arriving D23)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/9)
  - 110x Shatollan Paprika *(Farm)* → +12,100 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 16 | 1,520 G | D23 | +320 G |
| Farm | **Morrocorn** | Shatolla | 54 | 10,800 G | D26 | +10,800 G |

- **Daily Seed Spent**: 12,320 G | **End-of-Day Wallet**: **107,860 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **120,050 G** *(107,860 G carryover + 12,190 G payout)*
- **Harvest & Ship** *(+20,215 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/9)
  - 16x Carrop *(Farm)* → +1,840 G (freed)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 16 | 1,520 G | D24 | +320 G |

- **Daily Seed Spent**: 1,520 G | **End-of-Day Wallet**: **118,530 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **138,745 G** *(118,530 G carryover + 20,215 G payout)*
- **Harvest & Ship** *(+61,910 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/9)
  - 16x Carrop *(Farm)* → +1,840 G (freed)
  - 51x Morrocorn *(Farm)* → +20,400 G (freed)
  - 32x Seatide Garlic *(Farm)* → +32,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 2/5)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **74,395 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **136,305 G** *(74,395 G carryover + 61,910 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/9)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **136,305 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **150,195 G** *(136,305 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+81,375 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/9)
  - 54x Morrocorn *(Farm)* → +21,600 G (freed)
  - 37x Seatide Garlic *(Farm)* → +37,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 3/5)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 46 | 10,580 G | D30 | +7,820 G |
| Farm | **Morrocorn** | Shatolla | 45 | 9,000 G | D30 | +9,000 G |

- **Daily Seed Spent**: 19,580 G | **End-of-Day Wallet**: **130,615 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **211,990 G** *(130,615 G carryover + 81,375 G payout)*
- **Harvest & Ship** *(+17,070 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/9)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **211,990 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **229,060 G** *(211,990 G carryover + 17,070 G payout)*
- **Harvest & Ship** *(+13,690 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/9)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 4/5)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **229,060 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **242,750 G** *(229,060 G carryover + 13,690 G payout)*
- **Harvest & Ship** *(+248,490 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/9)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **242,750 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **491,240 G** *(242,750 G carryover + 248,490 G payout)*
- **Harvest & Ship** *(+212,070 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 9/9)
  - 91x Morrocorn *(Farm)* → +36,400 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 5/5)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **491,240 G**
- **Plots Left**: Farm: 193 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **703,310 G** *(491,240 G carryover + 212,070 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 22–30)

- **Starting Wallet (Day 22)**: 120,180 G
- **Ending Wallet (Day 31 Quietus)**: **703,310 G**
- **Pre-planted Crop Sales**: **+520,220 G**
- **New Planting Net Profit**: **+62,910 G**
- **Net Profit (9 days)**: **+583,130 G**
- **Average Daily Profit**: **+64,792 G/day** *(over 9 active days)*
