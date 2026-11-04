# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 23
- **Planning Timeline**: Day 23 -> Day 30 (8d Quietus window)
- **Capital Budget**: 97,670 G
- **Plot Capacities (Usable / Max)**: Farm: 231/245 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Bellhop** | 1 | Day 5 | D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +360 G |
| Farm | **Bellhop** | 1 | Day 6 | D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +360 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D24, D26, D28, D30 | Freed D30 | +1,320 G |
| Farm | **Shatollan Paprika** | 37 | Day 17 | D24, D26, D28, D30 | Stays Planted | +16,280 G |
| Farm | **Seatide Garlic** | 32 | Day 18 | D24 | Freed D24 | +32,000 G |
| Farm | **Morrocorn** | 51 | Day 20 | D24 | Freed D24 | +20,400 G |
| Farm | **Seatide Garlic** | 37 | Day 20 | D26 | Freed D26 | +37,000 G |
| Farm | **Carrop** | 16 | Day 22 | D23 | Freed D23 | +1,840 G |
| Farm | **Morrocorn** | 53 | Day 22 | D26 | Freed D26 | +21,200 G |
| Waterside | **Islet Watermelon** | 3 | Day 13 | D25 | Freed D25 | +13,800 G |
| Waterside | **Islet Watermelon** | 3 | Day 15 | D27 | Freed D27 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 54 | Day 17 | D29 | Freed D29 | +248,400 G |
| Waterside | **Islet Watermelon** | 15 | Day 18 | D30 | Freed D30 | +69,000 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D23, D26 | Freed D26 | +36,570 G |
| Cave | **Revol Pepper** | 12 | Day 17 | D24, D27, D30 | Stays Planted | +9,540 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 23**

- **Morning Wallet**: **97,670 G**
- **Harvest & Ship** *(+20,215 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/8)
  - 16x Carrop *(Farm)* → +1,840 G (freed)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 16 | 1,520 G | D24 | +320 G |

- **Daily Seed Spent**: 1,520 G | **End-of-Day Wallet**: **96,150 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **116,365 G** *(96,150 G carryover + 20,215 G payout)*
- **Harvest & Ship** *(+61,910 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/8)
  - 16x Carrop *(Farm)* → +1,840 G (freed)
  - 51x Morrocorn *(Farm)* → +20,400 G (freed)
  - 32x Seatide Garlic *(Farm)* → +32,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 1/4)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **52,015 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **113,925 G** *(52,015 G carryover + 61,910 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/8)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **113,925 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **127,815 G** *(113,925 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+80,975 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/8)
  - 53x Morrocorn *(Farm)* → +21,200 G (freed)
  - 37x Seatide Garlic *(Farm)* → +37,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 2/4)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 44 | 10,120 G | D30 | +7,480 G |
| Farm | **Morrocorn** | Shatolla | 46 | 9,200 G | D30 | +9,200 G |

- **Daily Seed Spent**: 19,320 G | **End-of-Day Wallet**: **108,495 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **189,470 G** *(108,495 G carryover + 80,975 G payout)*
- **Harvest & Ship** *(+17,070 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/8)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **189,470 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **206,540 G** *(189,470 G carryover + 17,070 G payout)*
- **Harvest & Ship** *(+13,690 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/8)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 3/4)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **206,540 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **220,230 G** *(206,540 G carryover + 13,690 G payout)*
- **Harvest & Ship** *(+248,490 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/8)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **220,230 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **468,720 G** *(220,230 G carryover + 248,490 G payout)*
- **Harvest & Ship** *(+211,670 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/8)
  - 90x Morrocorn *(Farm)* → +36,000 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 4/4)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **468,720 G**
- **Plots Left**: Farm: 192 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **680,390 G** *(468,720 G carryover + 211,670 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 23–30)

- **Starting Wallet (Day 23)**: 97,670 G
- **Ending Wallet (Day 31 Quietus)**: **680,390 G**
- **Pre-planted Crop Sales**: **+531,070 G**
- **New Planting Net Profit**: **+51,650 G**
- **Net Profit (8 days)**: **+582,720 G**
- **Average Daily Profit**: **+72,840 G/day** *(over 8 active days)*
