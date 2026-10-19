# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 24
- **Planning Timeline**: Day 24 -> Day 30 (7d Quietus window)
- **Capital Budget**: 69,775 G
- **Plot Capacities (Usable / Max)**: Farm: 236/245 | Waterside: 81/81 | Cave: 79/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D24, D26, D28, D30 | Freed D30 | +6,600 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D24, D25, D26, D27, D28 | Freed D28 | +8,450 G |
| Farm | **Seatide Garlic** | 24 | Day 21 | D27 | Freed D27 | +24,000 G |
| Farm | **Morrocorn** | 29 | Day 22 | D26 | Freed D26 | +11,600 G |
| Farm | **Carrop** | 84 | Day 23 | D24 | Freed D24 | +9,660 G |
| Waterside | **Islet Watermelon** | 4 | Day 16 | D28 | Freed D28 | +18,400 G |
| Waterside | **Islet Watermelon** | 6 | Day 18 | D30 | Freed D30 | +27,600 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D25, D28 | Freed D28 | +16,500 G |
| Waterside | **Nectarcane** | 10 | Day 17 | D24, D27 | Freed D27 | +5,000 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D24, D27, D30 | Freed D30 | +6,750 G |
| Waterside | **Honey Flower** | 19 | Day 23 | D29 | Freed D29 | +11,970 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D24, D27, D30 | Freed D30 | +7,155 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D24, D27 | Freed D27 | +22,000 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D24, D27, D30 | Freed D30 | +7,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 24**

- **Morning Wallet**: **69,775 G**
- **Harvest & Ship** *(+33,635 G arriving D25)*:
  - 84x Carrop *(Farm)* → +9,660 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 1/5)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/4)
  - 19x Nectarcane *(Waterside)* → +4,750 G (regrowth 1/2)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/3)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Curry Herbs** | Argene | 16 | 3,840 G | D30 | +1,760 G |
| Farm | **Dress Lettuce** | Lethe | 24 | 1,320 G | D26 | +720 G |
| Farm | **Stellar Wheat** | Lethe | 6 | 240 G | D26 | +90 G |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 69,750 G | **End-of-Day Wallet**: **25 G**
- **Plots Left**: Farm: 13 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **33,660 G** *(25 G carryover + 33,635 G payout)*
- **Harvest & Ship** *(+9,940 G arriving D26)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 2/5)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 13 | 2,600 G | D29 | +2,600 G |

- **Daily Seed Spent**: 2,600 G | **End-of-Day Wallet**: **31,060 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **41,000 G** *(31,060 G carryover + 9,940 G payout)*
- **Harvest & Ship** *(+17,310 G arriving D27)*:
  - 24x Dress Lettuce *(Farm)* → +2,040 G (freed)
  - 29x Morrocorn *(Farm)* → +11,600 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 3/5)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 2/4)
  - 6x Stellar Wheat *(Farm)* → +330 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 2 | 460 G | D30 | +340 G |
| Farm | **Morrocorn** | Shatolla | 57 | 11,400 G | D30 | +11,400 G |

- **Daily Seed Spent**: 11,860 G | **End-of-Day Wallet**: **29,140 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **46,450 G** *(29,140 G carryover + 17,310 G payout)*
- **Harvest & Ship** *(+46,325 G arriving D28)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 4/5)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 19x Nectarcane *(Waterside)* → +4,750 G (regrowth 2/2)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 2/3)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 23 | 1,265 G | D29 | +690 G |
| Farm | **Carrop** | Nemea | 1 | 95 G | D28 | +20 G |

- **Daily Seed Spent**: 1,360 G | **End-of-Day Wallet**: **45,090 G**
- **Plots Left**: Farm: 0 | Waterside: 10 | Cave: 44

---

#### **Day 28**

- **Morning Wallet**: **91,415 G** *(45,090 G carryover + 46,325 G payout)*
- **Harvest & Ship** *(+30,105 G arriving D29)*:
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 5/5)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 3/4)
  - 4x Islet Watermelon *(Waterside)* → +18,400 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D30 | +360 G |
| Farm | **Carrop** | Nemea | 14 | 1,330 G | D29 | +280 G |

- **Daily Seed Spent**: 1,990 G | **End-of-Day Wallet**: **89,425 G**
- **Plots Left**: Farm: 1 | Waterside: 47 | Cave: 44

---

#### **Day 29**

- **Morning Wallet**: **119,530 G** *(89,425 G carryover + 30,105 G payout)*
- **Harvest & Ship** *(+20,735 G arriving D30)*:
  - 14x Carrop *(Farm)* → +1,610 G (freed)
  - 23x Dress Lettuce *(Farm)* → +1,955 G (freed)
  - 13x Morrocorn *(Farm)* → +5,200 G (freed)
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 50 | 5,250 G | D30 | +500 G |

- **Daily Seed Spent**: 5,250 G | **End-of-Day Wallet**: **114,280 G**
- **Plots Left**: Farm: 1 | Waterside: 66 | Cave: 44

---

#### **Day 30**

- **Morning Wallet**: **135,015 G** *(114,280 G carryover + 20,735 G payout)*
- **Harvest & Ship** *(+171,355 G arriving D31)*:
  - 50x Carrop *(Farm)* → +5,750 G (freed)
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)
  - 59x Morrocorn *(Farm)* → +23,600 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 4/4)
  - 6x Islet Watermelon *(Waterside)* → +27,600 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 3/3)
  - 16x Curry Herbs *(Cave)* → +5,600 G (freed)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 3/3)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **135,015 G**

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **306,370 G** *(135,015 G carryover + 171,355 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary

- **Starting Budget**: 69,775 G
- **Pre-planted Crop Sales**: **+183,185 G**
- **New Planting Net Profit**: **+53,410 G**
- **Total Season Net Profit**: **+236,595 G**
- **Final Quietus Wallet**: **306,370 G**
