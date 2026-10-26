# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 24
- **Planning Timeline**: Day 24 -> Day 30 (7d Quietus window)
- **Capital Budget**: 24,050 G
- **Plot Capacities (Usable / Max)**: Farm: 98/147

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D24, D27 | Freed D27 | +1,200 G |
| Farm | **Cucumble** | 11 | Day 11 | D24, D27, D30 | Freed D30 | +6,600 G |
| Farm | **Cucumble** | 6 | Day 13 | D26, D29 | Stays Planted | +2,400 G |
| Farm | **Strawbuddy** | 2 | Day 13 | D25 | Freed D25 | +260 G |
| Farm | **Cucumble** | 5 | Day 14 | D24, D27, D30 | Stays Planted | +3,000 G |
| Farm | **Strawbuddy** | 22 | Day 17 | D25, D27, D29 | Freed D29 | +8,580 G |
| Farm | **Strawbuddy** | 16 | Day 18 | D24, D26, D28, D30 | Freed D30 | +8,320 G |
| Farm | **Tingle Radish** | 23 | Day 22 | D26 | Freed D26 | +12,190 G |
| Farm | **Unionion** | 10 | Day 23 | D26 | Freed D26 | +1,950 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 24**

- **Morning Wallet**: **24,050 G**
- **Harvest & Ship** *(+5,880 G arriving D25)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 1/2)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 1/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,050 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **29,930 G** *(24,050 G carryover + 5,880 G payout)*
- **Harvest & Ship** *(+3,120 G arriving D26)*:
  - 24x Strawbuddy *(Farm)* → +3,120 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 2 | 190 G | D26 | +40 G |

- **Daily Seed Spent**: 190 G | **End-of-Day Wallet**: **29,740 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **32,860 G** *(29,740 G carryover + 3,120 G payout)*
- **Harvest & Ship** *(+17,650 G arriving D27)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 1/2)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 2/4)
  - 23x Tingle Radish *(Farm)* → +12,190 G (freed)
  - 10x Unionion *(Farm)* → +1,950 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 35 | 13,650 G | D30 | +4,900 G |

- **Daily Seed Spent**: 13,650 G | **End-of-Day Wallet**: **19,210 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **36,860 G** *(19,210 G carryover + 17,650 G payout)*
- **Harvest & Ship** *(+6,660 G arriving D28)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 2/2)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D30 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **36,545 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **43,205 G** *(36,545 G carryover + 6,660 G payout)*
- **Harvest & Ship** *(+2,080 G arriving D29)*:
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **43,205 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **45,285 G** *(43,205 G carryover + 2,080 G payout)*
- **Harvest & Ship** *(+4,060 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/2)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 22 | 2,090 G | D30 | +440 G |

- **Daily Seed Spent**: 2,090 G | **End-of-Day Wallet**: **43,195 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **47,255 G** *(43,195 G carryover + 4,060 G payout)*
- **Harvest & Ship** *(+26,945 G arriving D31)*:
  - 22x Carrop *(Farm)* → +2,530 G (freed)
  - 16x Cucumble *(Farm)* → +3,200 G (regrowth 3/3)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 4/4)
  - 35x Tingle Radish *(Farm)* → +18,550 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **47,255 G**
- **Plots Left**: Farm: 87

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **74,200 G** *(47,255 G carryover + 26,945 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 24–30)

- **Starting Wallet (Day 24)**: 24,050 G
- **Ending Wallet (Day 31 Quietus)**: **74,200 G**
- **Pre-planted Crop Sales**: **+44,500 G**
- **New Planting Net Profit**: **+5,650 G**
- **Net Profit (7 days)**: **+50,150 G**
- **Average Daily Profit**: **+7,164 G/day** *(over 7 active days)*
