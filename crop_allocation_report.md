# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 11
- **Planning Timeline**: Day 11 -> Day 30 (20d Quietus window)
- **Capital Budget**: 5,460 G
- **Plot Capacities (Usable / Max)**: Farm: 29/49

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D12, D15, D18, D21, D24, D27 | Freed D27 | +3,600 G |
| Farm | **Unionion** | 1 | Day 8 | D11 | Freed D11 | +195 G |
| Farm | **Dress Lettuce** | 7 | Day 9 | D11 | Freed D11 | +595 G |
| Farm | **Nemean Tomato** | 6 | Day 9 | D14, D15, D16, D17, D18, D19 | Freed D19 | +2,340 G |
| Farm | **Stellar Wheat** | 6 | Day 9 | D11 | Freed D11 | +330 G |
| Farm | **Dress Lettuce** | 6 | Day 10 | D12 | Freed D12 | +510 G |
| Farm | **Tingle Radish** | 2 | Day 10 | D14 | Freed D14 | +1,060 G |
| Farm | **Unionion** | 1 | Day 10 | D13 | Freed D13 | +195 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 11**

- **Morning Wallet**: **5,460 G**
- **Harvest & Ship** *(+1,120 G arriving D12)*:
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)
  - 6x Stellar Wheat *(Farm)* → +330 G (freed)
  - 1x Unionion *(Farm)* → +195 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 11 | 4,070 G | D15..D30 (6x) | +9,130 G |

- **Daily Seed Spent**: 4,070 G | **End-of-Day Wallet**: **1,390 G**
- **Plots Left**: Farm: 0

---

#### **Day 12**

- **Morning Wallet**: **2,510 G** *(1,390 G carryover + 1,120 G payout)*
- **Harvest & Ship** *(+1,110 G arriving D13)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 1/6)
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D13 | +120 G |

- **Daily Seed Spent**: 570 G | **End-of-Day Wallet**: **1,940 G**
- **Plots Left**: Farm: 0

---

#### **Day 13**

- **Morning Wallet**: **3,050 G** *(1,940 G carryover + 1,110 G payout)*
- **Harvest & Ship** *(+885 G arriving D14)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 1x Unionion *(Farm)* → +195 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D14 | +120 G |

- **Daily Seed Spent**: 570 G | **End-of-Day Wallet**: **2,480 G**
- **Plots Left**: Farm: 1

---

#### **Day 14**

- **Morning Wallet**: **3,365 G** *(2,480 G carryover + 885 G payout)*
- **Harvest & Ship** *(+2,140 G arriving D15)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 1/6)
  - 2x Tingle Radish *(Farm)* → +1,060 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 9 | 3,330 G | D18..D30 (5x) | +5,670 G |

- **Daily Seed Spent**: 3,330 G | **End-of-Day Wallet**: **35 G**
- **Plots Left**: Farm: 0

---

#### **Day 15**

- **Morning Wallet**: **2,175 G** *(35 G carryover + 2,140 G payout)*
- **Harvest & Ship** *(+3,190 G arriving D16)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 2/6)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 2/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **2,175 G**
- **Plots Left**: Farm: 0

---

#### **Day 16**

- **Morning Wallet**: **5,365 G** *(2,175 G carryover + 3,190 G payout)*
- **Harvest & Ship** *(+390 G arriving D17)*:
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,365 G**
- **Plots Left**: Farm: 0

---

#### **Day 17**

- **Morning Wallet**: **5,755 G** *(5,365 G carryover + 390 G payout)*
- **Harvest & Ship** *(+390 G arriving D18)*:
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,755 G**
- **Plots Left**: Farm: 0

---

#### **Day 18**

- **Morning Wallet**: **6,145 G** *(5,755 G carryover + 390 G payout)*
- **Harvest & Ship** *(+4,990 G arriving D19)*:
  - 23x Cucumble *(Farm)* → +4,600 G (regrowth 3/6)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **6,145 G**
- **Plots Left**: Farm: 0

---

#### **Day 19**

- **Morning Wallet**: **11,135 G** *(6,145 G carryover + 4,990 G payout)*
- **Harvest & Ship** *(+390 G arriving D20)*:
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 6 | 630 G | D22 | +540 G |

- **Daily Seed Spent**: 630 G | **End-of-Day Wallet**: **10,505 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **10,895 G** *(10,505 G carryover + 390 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **10,895 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **10,895 G**
- **Harvest & Ship** *(+4,600 G arriving D22)*:
  - 23x Cucumble *(Farm)* → +4,600 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **10,895 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **15,495 G** *(10,895 G carryover + 4,600 G payout)*
- **Harvest & Ship** *(+1,170 G arriving D23)*:
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 6 | 2,340 G | D26 | +840 G |

- **Daily Seed Spent**: 2,340 G | **End-of-Day Wallet**: **13,155 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **14,325 G** *(13,155 G carryover + 1,170 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **14,325 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **14,325 G**
- **Harvest & Ship** *(+4,600 G arriving D25)*:
  - 23x Cucumble *(Farm)* → +4,600 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **14,325 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **18,925 G** *(14,325 G carryover + 4,600 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **18,925 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **18,925 G**
- **Harvest & Ship** *(+3,180 G arriving D27)*:
  - 6x Tingle Radish *(Farm)* → +3,180 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 6 | 2,340 G | D30 | +840 G |

- **Daily Seed Spent**: 2,340 G | **End-of-Day Wallet**: **16,585 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **19,765 G** *(16,585 G carryover + 3,180 G payout)*
- **Harvest & Ship** *(+4,600 G arriving D28)*:
  - 23x Cucumble *(Farm)* → +4,600 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D30 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **19,450 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **24,050 G** *(19,450 G carryover + 4,600 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,050 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **24,050 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,050 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **24,050 G**
- **Harvest & Ship** *(+7,765 G arriving D31)*:
  - 20x Cucumble *(Farm)* → +4,000 G (regrowth 6/6)
  - 6x Tingle Radish *(Farm)* → +3,180 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,050 G**
- **Plots Left**: Farm: 20

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **31,815 G** *(24,050 G carryover + 7,765 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 11–30)

- **Starting Wallet (Day 11)**: 5,460 G
- **Ending Wallet (Day 31 Quietus)**: **31,815 G**
- **Pre-planted Crop Sales**: **+8,825 G**
- **New Planting Net Profit**: **+17,530 G**
- **Net Profit (20 days)**: **+26,355 G**
- **Average Daily Profit**: **+1,318 G/day** *(over 20 active days)*
