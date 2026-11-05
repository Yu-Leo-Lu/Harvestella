# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 27
- **Planning Timeline**: Day 27 -> Day 30 (4d Quietus window)
- **Capital Budget**: 133,495 G
- **Plot Capacities (Usable / Max)**: Farm: 275/294 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Bellhop** | 1 | Day 5 | D27, D28, D29, D30 | Stays Planted | +180 G |
| Farm | **Bellhop** | 1 | Day 6 | D27, D28, D29, D30 | Stays Planted | +180 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D28, D30 | Freed D30 | +660 G |
| Farm | **Shatollan Paprika** | 37 | Day 17 | D28, D30 | Stays Planted | +8,140 G |
| Farm | **Eden Rice** | 15 | Day 24 | D27 | Freed D27 | +525 G |
| Farm | **Nemean Tomato** | 6 | Day 24 | D29, D30 | Stays Planted | +780 G |
| Farm | **Seatide Garlic** | 99 | Day 24 | D30 | Freed D30 | +99,000 G |
| Farm | **Grass** | 17 | Day 26 | D28 | Freed D28 | +595 G |
| Farm | **Morrocorn** | 96 | Day 26 | D30 | Freed D30 | +38,400 G |
| Waterside | **Islet Watermelon** | 3 | Day 15 | D27 | Freed D27 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 54 | Day 17 | D29 | Freed D29 | +248,400 G |
| Waterside | **Islet Watermelon** | 15 | Day 18 | D30 | Freed D30 | +69,000 G |
| Cave | **Revol Pepper** | 12 | Day 17 | D27, D30 | Stays Planted | +6,360 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 27**

- **Morning Wallet**: **133,495 G**
- **Harvest & Ship** *(+17,595 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/4)
  - 15x Eden Rice *(Farm)* → +525 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 15 | 1,425 G | D28 | +300 G |

- **Daily Seed Spent**: 1,425 G | **End-of-Day Wallet**: **132,070 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **149,665 G** *(132,070 G carryover + 17,595 G payout)*
- **Harvest & Ship** *(+16,010 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/4)
  - 15x Carrop *(Farm)* → +1,725 G (freed)
  - 17x Grass *(Farm)* → +595 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 1/2)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 10 | 550 G | D30 | +300 G |
| Farm | **Carrop** | Nemea | 22 | 2,090 G | D29 | +440 G |

- **Daily Seed Spent**: 2,640 G | **End-of-Day Wallet**: **147,025 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **163,035 G** *(147,025 G carryover + 16,010 G payout)*
- **Harvest & Ship** *(+251,410 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/4)
  - 22x Carrop *(Farm)* → +2,530 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 1/2)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 22 | 2,090 G | D30 | +440 G |

- **Daily Seed Spent**: 2,090 G | **End-of-Day Wallet**: **160,945 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **412,355 G** *(160,945 G carryover + 251,410 G payout)*
- **Harvest & Ship** *(+217,840 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/4)
  - 22x Carrop *(Farm)* → +2,530 G (freed)
  - 10x Dress Lettuce *(Farm)* → +850 G (freed)
  - 96x Morrocorn *(Farm)* → +38,400 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 2/2)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 2/2)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **412,355 G**
- **Plots Left**: Farm: 230 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **630,195 G** *(412,355 G carryover + 217,840 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 27–30)

- **Starting Wallet (Day 27)**: 133,495 G
- **Ending Wallet (Day 31 Quietus)**: **630,195 G**
- **Pre-planted Crop Sales**: **+495,220 G**
- **New Planting Net Profit**: **+1,480 G**
- **Net Profit (4 days)**: **+496,700 G**
- **Average Daily Profit**: **+124,175 G/day** *(over 4 active days)*
