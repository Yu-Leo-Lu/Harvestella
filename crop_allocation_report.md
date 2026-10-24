# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 17
- **Planning Timeline**: Day 17 -> Day 30 (14d Quietus window)
- **Capital Budget**: 4,975 G
- **Plot Capacities (Usable / Max)**: Farm: 98/147

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D18, D21, D24, D27 | Freed D27 | +2,400 G |
| Farm | **Nemean Tomato** | 6 | Day 9 | D17, D18, D19 | Freed D19 | +1,170 G |
| Farm | **Cucumble** | 11 | Day 11 | D18, D21, D24, D27, D30 | Freed D30 | +11,000 G |
| Farm | **Nemean Tomato** | 3 | Day 12 | D17, D18, D19, D20, D21, D22 | Freed D22 | +1,170 G |
| Farm | **Cucumble** | 6 | Day 13 | D17, D20, D23, D26, D29 | Stays Planted | +6,000 G |
| Farm | **Nemean Tomato** | 10 | Day 13 | D18, D19, D20, D21, D22, D23 | Freed D23 | +3,900 G |
| Farm | **Strawbuddy** | 2 | Day 13 | D17, D19, D21, D23, D25 | Freed D25 | +1,300 G |
| Farm | **Cucumble** | 5 | Day 14 | D18, D21, D24, D27, D30 | Stays Planted | +5,000 G |
| Farm | **Unionion** | 15 | Day 15 | D18 | Freed D18 | +2,925 G |
| Farm | **Tingle Radish** | 6 | Day 16 | D20 | Freed D20 | +3,180 G |
| Farm | **Dress Lettuce** | 3 | Day 16 | D18 | Freed D18 | +255 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 17**

- **Morning Wallet**: **4,975 G**
- **Harvest & Ship** *(+2,045 G arriving D18)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 1/5)
  - 9x Nemean Tomato *(Farm)* → +585 G (regrowth 1/3)
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D19 | +180 G |
| Farm | **Strawbuddy** | Nemea | 21 | 4,620 G | D21..D29 (5x) | +9,030 G |

- **Daily Seed Spent**: 4,950 G | **End-of-Day Wallet**: **25 G**
- **Plots Left**: Farm: 1

---

#### **Day 18**

- **Morning Wallet**: **2,070 G** *(25 G carryover + 2,045 G payout)*
- **Harvest & Ship** *(+8,215 G arriving D19)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 1/4)
  - 3x Dress Lettuce *(Farm)* → +255 G (freed)
  - 19x Nemean Tomato *(Farm)* → +1,235 G (regrowth 2/3)
  - 15x Unionion *(Farm)* → +2,925 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Strawbuddy** | Nemea | 9 | 1,980 G | D22..D30 (5x) | +3,870 G |

- **Daily Seed Spent**: 1,980 G | **End-of-Day Wallet**: **90 G**
- **Plots Left**: Farm: 10

---

#### **Day 19**

- **Morning Wallet**: **8,305 G** *(90 G carryover + 8,215 G payout)*
- **Harvest & Ship** *(+2,005 G arriving D20)*:
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)
  - 19x Nemean Tomato *(Farm)* → +1,235 G (regrowth 3/3)
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 21 | 8,190 G | D23 | +2,940 G |
| Farm | **Unionion** | Nemea | 1 | 105 G | D22 | +90 G |

- **Daily Seed Spent**: 8,295 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **2,015 G** *(10 G carryover + 2,005 G payout)*
- **Harvest & Ship** *(+5,225 G arriving D21)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/5)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 4/6)
  - 6x Tingle Radish *(Farm)* → +3,180 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 6 | 630 G | D23 | +540 G |

- **Daily Seed Spent**: 630 G | **End-of-Day Wallet**: **1,385 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **6,610 G** *(1,385 G carryover + 5,225 G payout)*
- **Harvest & Ship** *(+7,635 G arriving D22)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 2/4)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 5/6)
  - 23x Strawbuddy *(Farm)* → +2,990 G (regrowth 3/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **6,610 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **14,245 G** *(6,610 G carryover + 7,635 G payout)*
- **Harvest & Ship** *(+2,210 G arriving D23)*:
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 6/6)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 1/5)
  - 1x Unionion *(Farm)* → +195 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 4 | 1,560 G | D26 | +560 G |

- **Daily Seed Spent**: 1,560 G | **End-of-Day Wallet**: **12,685 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **14,895 G** *(12,685 G carryover + 2,210 G payout)*
- **Harvest & Ship** *(+17,140 G arriving D24)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 3/5)
  - 10x Nemean Tomato *(Farm)* → +650 G (regrowth 6/6)
  - 23x Strawbuddy *(Farm)* → +2,990 G (regrowth 4/5)
  - 21x Tingle Radish *(Farm)* → +11,130 G (freed)
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 37 | 3,885 G | D26 | +3,330 G |

- **Daily Seed Spent**: 3,885 G | **End-of-Day Wallet**: **11,010 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **28,150 G** *(11,010 G carryover + 17,140 G payout)*
- **Harvest & Ship** *(+4,970 G arriving D25)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 3/4)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **28,150 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **33,120 G** *(28,150 G carryover + 4,970 G payout)*
- **Harvest & Ship** *(+2,990 G arriving D26)*:
  - 23x Strawbuddy *(Farm)* → +2,990 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 2 | 190 G | D26 | +40 G |

- **Daily Seed Spent**: 190 G | **End-of-Day Wallet**: **32,930 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **35,920 G** *(32,930 G carryover + 2,990 G payout)*
- **Harvest & Ship** *(+11,935 G arriving D27)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 4/5)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 3/5)
  - 4x Tingle Radish *(Farm)* → +2,120 G (freed)
  - 37x Unionion *(Farm)* → +7,215 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 43 | 16,770 G | D30 | +6,020 G |

- **Daily Seed Spent**: 16,770 G | **End-of-Day Wallet**: **19,150 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **31,085 G** *(19,150 G carryover + 11,935 G payout)*
- **Harvest & Ship** *(+6,530 G arriving D28)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 4/4)
  - 21x Strawbuddy *(Farm)* → +2,730 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D30 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **30,770 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **37,300 G** *(30,770 G carryover + 6,530 G payout)*
- **Harvest & Ship** *(+1,170 G arriving D29)*:
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **37,300 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **38,470 G** *(37,300 G carryover + 1,170 G payout)*
- **Harvest & Ship** *(+3,930 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 5/5)
  - 21x Strawbuddy *(Farm)* → +2,730 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 21 | 1,995 G | D30 | +420 G |

- **Daily Seed Spent**: 1,995 G | **End-of-Day Wallet**: **36,475 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **40,405 G** *(36,475 G carryover + 3,930 G payout)*
- **Harvest & Ship** *(+30,160 G arriving D31)*:
  - 21x Carrop *(Farm)* → +2,415 G (freed)
  - 16x Cucumble *(Farm)* → +3,200 G (regrowth 5/5)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 5/5)
  - 43x Tingle Radish *(Farm)* → +22,790 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **40,405 G**
- **Plots Left**: Farm: 87

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **70,565 G** *(40,405 G carryover + 30,160 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 17–30)

- **Starting Wallet (Day 17)**: 4,975 G
- **Ending Wallet (Day 31 Quietus)**: **70,565 G**
- **Pre-planted Crop Sales**: **+38,300 G**
- **New Planting Net Profit**: **+27,290 G**
- **Net Profit (14 days)**: **+65,590 G**
- **Average Daily Profit**: **+4,685 G/day** *(over 14 active days)*
