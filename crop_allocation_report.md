# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 26
- **Planning Timeline**: Day 26 -> Day 30 (5d Quietus window)
- **Capital Budget**: 653,260 G
- **Plot Capacities (Usable / Max)**: Farm: 363/441 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Rainbow Bean** | 7 | Day 13 | D27 | Freed D27 | +280 G |
| Farm | **Rainbow Bean** | 26 | Day 16 | D26, D28, D30 | Freed D30 | +3,120 G |
| Farm | **Lantern Pumpkin** | 18 | Day 19 | D30 | Freed D30 | +67,500 G |
| Farm | **Royal Eggplant** | 297 | Day 19 | D26, D28 | Freed D28 | +285,120 G |
| Farm | **Morrocorn** | 15 | Day 22 | D26 | Freed D26 | +6,000 G |
| Waterside | **Nectarcane** | 55 | Day 19 | D26, D29 | Freed D29 | +27,500 G |
| Waterside | **Honey Flower** | 22 | Day 23 | D29 | Freed D29 | +13,860 G |
| Cave | **Revol Pepper** | 57 | Day 13 | D26, D29 | Freed D29 | +30,210 G |
| Cave | **Revol Pepper** | 22 | Day 17 | D27, D30 | Stays Planted | +11,660 G |
| Cave | **Sudor Pepper** | 2 | Day 19 | D28 | Freed D28 | +500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 26**

- **Morning Wallet**: **653,260 G**
- **Harvest & Ship** *(+178,455 G arriving D27)*:
  - 15x Morrocorn *(Farm)* → +6,000 G (freed)
  - 26x Rainbow Bean *(Farm)* → +1,040 G (regrowth 1/3)
  - 297x Royal Eggplant *(Farm)* → +142,560 G (regrowth 1/2)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 1/2)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 15 | 3,000 G | D30 | +3,000 G |

- **Daily Seed Spent**: 3,000 G | **End-of-Day Wallet**: **650,260 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **828,715 G** *(650,260 G carryover + 178,455 G payout)*
- **Harvest & Ship** *(+6,110 G arriving D28)*:
  - 7x Rainbow Bean *(Farm)* → +280 G (regrowth 1/1)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 7 | 735 G | D30 | +630 G |

- **Daily Seed Spent**: 735 G | **End-of-Day Wallet**: **827,980 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **834,090 G** *(827,980 G carryover + 6,110 G payout)*
- **Harvest & Ship** *(+144,100 G arriving D29)*:
  - 26x Rainbow Bean *(Farm)* → +1,040 G (regrowth 2/3)
  - 297x Royal Eggplant *(Farm)* → +142,560 G (regrowth 2/2)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 38 | 2,090 G | D30 | +1,140 G |
| Farm | **Grass** | Lethe | 99 | 2,970 G | D30 | +495 G |
| Farm | **Stellar Wheat** | Lethe | 10 | 400 G | D30 | +150 G |

- **Daily Seed Spent**: 5,460 G | **End-of-Day Wallet**: **828,630 G**
- **Plots Left**: Farm: 150 | Waterside: 0 | Cave: 2

---

#### **Day 29**

- **Morning Wallet**: **972,730 G** *(828,630 G carryover + 144,100 G payout)*
- **Harvest & Ship** *(+42,715 G arriving D30)*:
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 2/2)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **972,730 G**
- **Plots Left**: Farm: 150 | Waterside: 77 | Cave: 59

---

#### **Day 30**

- **Morning Wallet**: **1,015,445 G** *(972,730 G carryover + 42,715 G payout)*
- **Harvest & Ship** *(+88,980 G arriving D31)*:
  - 38x Dress Lettuce *(Farm)* → +3,230 G (freed)
  - 99x Grass *(Farm)* → +3,465 G (freed)
  - 18x Lantern Pumpkin *(Farm)* → +67,500 G (freed)
  - 15x Morrocorn *(Farm)* → +6,000 G (freed)
  - 26x Rainbow Bean *(Farm)* → +1,040 G (regrowth 3/3)
  - 10x Stellar Wheat *(Farm)* → +550 G (freed)
  - 7x Unionion *(Farm)* → +1,365 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **1,015,445 G**
- **Plots Left**: Farm: 363 | Waterside: 77 | Cave: 59

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **1,104,425 G** *(1,015,445 G carryover + 88,980 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 26–30)

- **Starting Wallet (Day 26)**: 653,260 G
- **Ending Wallet (Day 31 Quietus)**: **1,104,425 G**
- **Pre-planted Crop Sales**: **+445,750 G**
- **New Planting Net Profit**: **+5,415 G**
- **Net Profit (5 days)**: **+451,165 G**
- **Average Daily Profit**: **+90,233 G/day** *(over 5 active days)*
