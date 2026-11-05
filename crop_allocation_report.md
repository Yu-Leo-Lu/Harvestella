# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 24
- **Planning Timeline**: Day 24 -> Day 30 (7d Quietus window)
- **Capital Budget**: 67,060 G
- **Plot Capacities (Usable / Max)**: Farm: 276/294 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Bellhop** | 1 | Day 5 | D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +315 G |
| Farm | **Bellhop** | 1 | Day 6 | D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +315 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D24, D26, D28, D30 | Freed D30 | +1,320 G |
| Farm | **Shatollan Paprika** | 37 | Day 17 | D24, D26, D28, D30 | Stays Planted | +16,280 G |
| Farm | **Seatide Garlic** | 32 | Day 18 | D24 | Freed D24 | +32,000 G |
| Farm | **Morrocorn** | 51 | Day 20 | D24 | Freed D24 | +20,400 G |
| Farm | **Seatide Garlic** | 37 | Day 20 | D26 | Freed D26 | +37,000 G |
| Farm | **Morrocorn** | 53 | Day 22 | D26 | Freed D26 | +21,200 G |
| Farm | **Carrop** | 16 | Day 23 | D24 | Freed D24 | +1,840 G |
| Farm | **Nemean Tomato** | 6 | Day 24 | D29, D30 | Stays Planted | +780 G |
| Farm | **Grass** | 20 | Day 24 | D26 | Freed D26 | +700 G |
| Farm | **Eden Rice** | 15 | Day 24 | D27 | Freed D27 | +525 G |
| Waterside | **Islet Watermelon** | 3 | Day 13 | D25 | Freed D25 | +13,800 G |
| Waterside | **Islet Watermelon** | 3 | Day 15 | D27 | Freed D27 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 54 | Day 17 | D29 | Freed D29 | +248,400 G |
| Waterside | **Islet Watermelon** | 15 | Day 18 | D30 | Freed D30 | +69,000 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D26 | Freed D26 | +18,285 G |
| Cave | **Revol Pepper** | 12 | Day 17 | D24, D27, D30 | Stays Planted | +9,540 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 24**

- **Morning Wallet**: **67,060 G**
- **Harvest & Ship** *(+61,910 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/7)
  - 16x Carrop *(Farm)* → +1,840 G (freed)
  - 51x Morrocorn *(Farm)* → +20,400 G (freed)
  - 32x Seatide Garlic *(Farm)* → +32,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 1/4)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 4 | 380 G | D25 | +80 G |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,730 G | **End-of-Day Wallet**: **2,330 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **64,240 G** *(2,330 G carryover + 61,910 G payout)*
- **Harvest & Ship** *(+14,350 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/7)
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 4 | 380 G | D26 | +80 G |

- **Daily Seed Spent**: 380 G | **End-of-Day Wallet**: **63,860 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **78,210 G** *(63,860 G carryover + 14,350 G payout)*
- **Harvest & Ship** *(+82,135 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/7)
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 20x Grass *(Farm)* → +700 G (freed)
  - 53x Morrocorn *(Farm)* → +21,200 G (freed)
  - 37x Seatide Garlic *(Farm)* → +37,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 2/4)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Carrop** | Nemea | 18 | 1,710 G | D27 | +360 G |
| Farm | **Morrocorn** | Shatolla | 46 | 9,200 G | D30 | +9,200 G |

- **Daily Seed Spent**: 22,410 G | **End-of-Day Wallet**: **55,800 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **137,935 G** *(55,800 G carryover + 82,135 G payout)*
- **Harvest & Ship** *(+19,665 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/7)
  - 18x Carrop *(Farm)* → +2,070 G (freed)
  - 15x Eden Rice *(Farm)* → +525 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 33 | 3,135 G | D28 | +660 G |

- **Daily Seed Spent**: 3,135 G | **End-of-Day Wallet**: **134,800 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **154,465 G** *(134,800 G carryover + 19,665 G payout)*
- **Harvest & Ship** *(+17,485 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/7)
  - 33x Carrop *(Farm)* → +3,795 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 3/4)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 29 | 1,595 G | D30 | +870 G |
| Farm | **Carrop** | Nemea | 4 | 380 G | D29 | +80 G |

- **Daily Seed Spent**: 1,975 G | **End-of-Day Wallet**: **152,490 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **169,975 G** *(152,490 G carryover + 17,485 G payout)*
- **Harvest & Ship** *(+249,340 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/7)
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 1/2)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 4 | 380 G | D30 | +80 G |

- **Daily Seed Spent**: 380 G | **End-of-Day Wallet**: **169,595 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **418,935 G** *(169,595 G carryover + 249,340 G payout)*
- **Harvest & Ship** *(+217,385 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/7)
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 29x Dress Lettuce *(Farm)* → +2,465 G (freed)
  - 96x Morrocorn *(Farm)* → +38,400 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 2/2)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 4/4)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **418,935 G**
- **Plots Left**: Farm: 231 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **636,320 G** *(418,935 G carryover + 217,385 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 24–30)

- **Starting Wallet (Day 24)**: 67,060 G
- **Ending Wallet (Day 31 Quietus)**: **636,320 G**
- **Pre-planted Crop Sales**: **+514,700 G**
- **New Planting Net Profit**: **+54,560 G**
- **Net Profit (7 days)**: **+569,260 G**
- **Average Daily Profit**: **+81,323 G/day** *(over 7 active days)*
