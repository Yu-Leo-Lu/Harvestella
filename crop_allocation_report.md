# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 20
- **Planning Timeline**: Day 20 -> Day 30 (11d Quietus window)
- **Capital Budget**: 11,980 G
- **Plot Capacities (Usable / Max)**: Farm: 98/147

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D21, D24, D27 | Freed D27 | +1,800 G |
| Farm | **Cucumble** | 11 | Day 11 | D21, D24, D27, D30 | Freed D30 | +8,800 G |
| Farm | **Nemean Tomato** | 3 | Day 12 | D20, D21, D22 | Freed D22 | +585 G |
| Farm | **Cucumble** | 6 | Day 13 | D20, D23, D26, D29 | Stays Planted | +4,800 G |
| Farm | **Nemean Tomato** | 10 | Day 13 | D20, D21, D22, D23 | Freed D23 | +2,600 G |
| Farm | **Strawbuddy** | 2 | Day 13 | D21, D23, D25 | Freed D25 | +780 G |
| Farm | **Cucumble** | 5 | Day 14 | D21, D24, D27, D30 | Stays Planted | +4,000 G |
| Farm | **Strawbuddy** | 22 | Day 17 | D21, D23, D25, D27, D29 | Freed D29 | +14,300 G |
| Farm | **Tingle Radish** | 6 | Day 17 | D21 | Freed D21 | +3,180 G |
| Farm | **Strawbuddy** | 16 | Day 18 | D22, D24, D26, D28, D30 | Freed D30 | +10,400 G |
| Farm | **Unionion** | 14 | Day 19 | D22 | Freed D22 | +2,730 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 20**

- **Morning Wallet**: **11,980 G**
- **Harvest & Ship** *(+2,045 G arriving D21)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 1/4)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 1/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **11,980 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **14,025 G** *(11,980 G carryover + 2,045 G payout)*
- **Harvest & Ship** *(+10,945 G arriving D22)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 1/3)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 2/3)
  - 24x Strawbuddy *(Farm)* → +3,120 G (regrowth 1/3)
  - 6x Tingle Radish *(Farm)* → +3,180 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D22 | +120 G |

- **Daily Seed Spent**: 570 G | **End-of-Day Wallet**: **13,455 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **24,400 G** *(13,455 G carryover + 10,945 G payout)*
- **Harvest & Ship** *(+6,345 G arriving D23)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 3/3)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 1/5)
  - 14x Unionion *(Farm)* → +2,730 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 23 | 8,970 G | D26 | +3,220 G |

- **Daily Seed Spent**: 8,970 G | **End-of-Day Wallet**: **15,430 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **21,775 G** *(15,430 G carryover + 6,345 G payout)*
- **Harvest & Ship** *(+4,970 G arriving D24)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/4)
  - 10x Nemean Tomato *(Farm)* → +650 G (regrowth 4/4)
  - 24x Strawbuddy *(Farm)* → +3,120 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 10 | 1,050 G | D26 | +900 G |

- **Daily Seed Spent**: 1,050 G | **End-of-Day Wallet**: **20,725 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **25,695 G** *(20,725 G carryover + 4,970 G payout)*
- **Harvest & Ship** *(+5,880 G arriving D25)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 2/3)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **25,695 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **31,575 G** *(25,695 G carryover + 5,880 G payout)*
- **Harvest & Ship** *(+3,120 G arriving D26)*:
  - 24x Strawbuddy *(Farm)* → +3,120 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 2 | 190 G | D26 | +40 G |

- **Daily Seed Spent**: 190 G | **End-of-Day Wallet**: **31,385 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **34,505 G** *(31,385 G carryover + 3,120 G payout)*
- **Harvest & Ship** *(+17,650 G arriving D27)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 3/4)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 3/5)
  - 23x Tingle Radish *(Farm)* → +12,190 G (freed)
  - 10x Unionion *(Farm)* → +1,950 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 35 | 13,650 G | D30 | +4,900 G |

- **Daily Seed Spent**: 13,650 G | **End-of-Day Wallet**: **20,855 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **38,505 G** *(20,855 G carryover + 17,650 G payout)*
- **Harvest & Ship** *(+6,660 G arriving D28)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 3/3)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D30 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **38,190 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **44,850 G** *(38,190 G carryover + 6,660 G payout)*
- **Harvest & Ship** *(+2,080 G arriving D29)*:
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **44,850 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **46,930 G** *(44,850 G carryover + 2,080 G payout)*
- **Harvest & Ship** *(+4,060 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 4/4)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 22 | 2,090 G | D30 | +440 G |

- **Daily Seed Spent**: 2,090 G | **End-of-Day Wallet**: **44,840 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **48,900 G** *(44,840 G carryover + 4,060 G payout)*
- **Harvest & Ship** *(+26,945 G arriving D31)*:
  - 22x Carrop *(Farm)* → +2,530 G (freed)
  - 16x Cucumble *(Farm)* → +3,200 G (regrowth 4/4)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 5/5)
  - 35x Tingle Radish *(Farm)* → +18,550 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **48,900 G**
- **Plots Left**: Farm: 87

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **75,845 G** *(48,900 G carryover + 26,945 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 20–30)

- **Starting Wallet (Day 20)**: 11,980 G
- **Ending Wallet (Day 31 Quietus)**: **75,845 G**
- **Pre-planted Crop Sales**: **+53,975 G**
- **New Planting Net Profit**: **+9,890 G**
- **Net Profit (11 days)**: **+63,865 G**
- **Average Daily Profit**: **+5,806 G/day** *(over 11 active days)*
