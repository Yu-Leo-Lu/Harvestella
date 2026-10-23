# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 9
- **Planning Timeline**: Day 9 -> Day 30 (22d Quietus window)
- **Capital Budget**: 1,525 G
- **Plot Capacities (Usable / Max)**: Farm: 29/49

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Unionion** | 2 | Day 6 | D9 | Freed D9 | +390 G |
| Farm | **Dress Lettuce** | 11 | Day 7 | D9 | Freed D9 | +935 G |
| Farm | **Stellar Wheat** | 3 | Day 7 | D9 | Freed D9 | +165 G |
| Farm | **Unionion** | 7 | Day 7 | D10 | Freed D10 | +1,365 G |
| Farm | **Cucumble** | 3 | Day 8 | D12, D15, D18, D21, D24, D27 | Freed D27 | +3,600 G |
| Farm | **Dress Lettuce** | 1 | Day 8 | D10 | Freed D10 | +85 G |
| Farm | **Stellar Wheat** | 1 | Day 8 | D10 | Freed D10 | +55 G |
| Farm | **Unionion** | 1 | Day 8 | D11 | Freed D11 | +195 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 9**

- **Morning Wallet**: **1,525 G**
- **Harvest & Ship** *(+1,490 G arriving D10)*:
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)
  - 3x Stellar Wheat *(Farm)* → +165 G (freed)
  - 2x Unionion *(Farm)* → +390 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 3 | 1,110 G | D13..D28 (6x) | +2,490 G |
| Farm | **Dress Lettuce** | Lethe | 7 | 385 G | D11 | +210 G |

- **Daily Seed Spent**: 1,495 G | **End-of-Day Wallet**: **30 G**
- **Plots Left**: Farm: 6

---

#### **Day 10**

- **Morning Wallet**: **1,520 G** *(30 G carryover + 1,490 G payout)*
- **Harvest & Ship** *(+1,505 G arriving D11)*:
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)
  - 1x Stellar Wheat *(Farm)* → +55 G (freed)
  - 7x Unionion *(Farm)* → +1,365 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 1 | 370 G | D14..D29 (6x) | +830 G |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D12 | +180 G |
| Farm | **Unionion** | Lethe | 6 | 780 G | D13 | +390 G |

- **Daily Seed Spent**: 1,480 G | **End-of-Day Wallet**: **40 G**
- **Plots Left**: Farm: 2

---

#### **Day 11**

- **Morning Wallet**: **1,545 G** *(40 G carryover + 1,505 G payout)*
- **Harvest & Ship** *(+790 G arriving D12)*:
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)
  - 1x Unionion *(Farm)* → +195 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 3 | 1,110 G | D15..D30 (6x) | +2,490 G |
| Farm | **Dress Lettuce** | Lethe | 7 | 385 G | D13 | +210 G |

- **Daily Seed Spent**: 1,495 G | **End-of-Day Wallet**: **50 G**
- **Plots Left**: Farm: 0

---

#### **Day 12**

- **Morning Wallet**: **840 G** *(50 G carryover + 790 G payout)*
- **Harvest & Ship** *(+1,110 G arriving D13)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 1/6)
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 1 | 105 G | D13 | +10 G |
| Farm | **Cucumble** | Lethe | 1 | 370 G | D16..D28 (5x) | +630 G |
| Farm | **Dress Lettuce** | Lethe | 4 | 220 G | D14 | +120 G |

- **Daily Seed Spent**: 695 G | **End-of-Day Wallet**: **145 G**
- **Plots Left**: Farm: 0

---

#### **Day 13**

- **Morning Wallet**: **1,255 G** *(145 G carryover + 1,110 G payout)*
- **Harvest & Ship** *(+2,480 G arriving D14)*:
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 3x Cucumble *(Farm)* → +600 G (regrowth 1/6)
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 1 | 370 G | D17..D29 (5x) | +630 G |
| Farm | **Dress Lettuce** | Lethe | 7 | 385 G | D15 | +210 G |
| Farm | **Unionion** | Lethe | 3 | 390 G | D16 | +195 G |

- **Daily Seed Spent**: 1,145 G | **End-of-Day Wallet**: **110 G**
- **Plots Left**: Farm: 3

---

#### **Day 14**

- **Morning Wallet**: **2,590 G** *(110 G carryover + 2,480 G payout)*
- **Harvest & Ship** *(+540 G arriving D15)*:
  - 1x Cucumble *(Farm)* → +200 G (regrowth 1/6)
  - 4x Dress Lettuce *(Farm)* → +340 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 7 | 2,590 G | D18..D30 (5x) | +4,410 G |

- **Daily Seed Spent**: 2,590 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 0

---

#### **Day 15**

- **Morning Wallet**: **540 G** *(0 G carryover + 540 G payout)*
- **Harvest & Ship** *(+1,795 G arriving D16)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/6)
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 4 | 420 G | D16 | +40 G |
| Farm | **Dress Lettuce** | Lethe | 1 | 55 G | D17 | +30 G |

- **Daily Seed Spent**: 475 G | **End-of-Day Wallet**: **65 G**
- **Plots Left**: Farm: 2

---

#### **Day 16**

- **Morning Wallet**: **1,860 G** *(65 G carryover + 1,795 G payout)*
- **Harvest & Ship** *(+1,845 G arriving D17)*:
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 4x Cucumble *(Farm)* → +800 G (regrowth 2/6)
  - 3x Unionion *(Farm)* → +585 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 5 | 1,850 G | D20..D29 (4x) | +2,150 G |

- **Daily Seed Spent**: 1,850 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 4

---

#### **Day 17**

- **Morning Wallet**: **1,855 G** *(10 G carryover + 1,845 G payout)*
- **Harvest & Ship** *(+485 G arriving D18)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 2/6)
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 5 | 1,850 G | D21..D30 (4x) | +2,150 G |

- **Daily Seed Spent**: 1,850 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 0

---

#### **Day 18**

- **Morning Wallet**: **490 G** *(5 G carryover + 485 G payout)*
- **Harvest & Ship** *(+2,600 G arriving D19)*:
  - 13x Cucumble *(Farm)* → +2,600 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **490 G**
- **Plots Left**: Farm: 0

---

#### **Day 19**

- **Morning Wallet**: **3,090 G** *(490 G carryover + 2,600 G payout)*
- **Harvest & Ship** *(+800 G arriving D20)*:
  - 4x Cucumble *(Farm)* → +800 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **3,090 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **3,890 G** *(3,090 G carryover + 800 G payout)*
- **Harvest & Ship** *(+1,400 G arriving D21)*:
  - 7x Cucumble *(Farm)* → +1,400 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **3,890 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **5,290 G** *(3,890 G carryover + 1,400 G payout)*
- **Harvest & Ship** *(+3,600 G arriving D22)*:
  - 18x Cucumble *(Farm)* → +3,600 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,290 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **8,890 G** *(5,290 G carryover + 3,600 G payout)*
- **Harvest & Ship** *(+800 G arriving D23)*:
  - 4x Cucumble *(Farm)* → +800 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **8,890 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **9,690 G** *(8,890 G carryover + 800 G payout)*
- **Harvest & Ship** *(+1,400 G arriving D24)*:
  - 7x Cucumble *(Farm)* → +1,400 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **9,690 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **11,090 G** *(9,690 G carryover + 1,400 G payout)*
- **Harvest & Ship** *(+3,600 G arriving D25)*:
  - 18x Cucumble *(Farm)* → +3,600 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **11,090 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **14,690 G** *(11,090 G carryover + 3,600 G payout)*
- **Harvest & Ship** *(+800 G arriving D26)*:
  - 4x Cucumble *(Farm)* → +800 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **14,690 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **15,490 G** *(14,690 G carryover + 800 G payout)*
- **Harvest & Ship** *(+1,400 G arriving D27)*:
  - 7x Cucumble *(Farm)* → +1,400 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **15,490 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **16,890 G** *(15,490 G carryover + 1,400 G payout)*
- **Harvest & Ship** *(+3,600 G arriving D28)*:
  - 18x Cucumble *(Farm)* → +3,600 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 3 | 390 G | D30 | +195 G |

- **Daily Seed Spent**: 390 G | **End-of-Day Wallet**: **16,500 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **20,100 G** *(16,500 G carryover + 3,600 G payout)*
- **Harvest & Ship** *(+800 G arriving D29)*:
  - 4x Cucumble *(Farm)* → +800 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 3 | 165 G | D30 | +90 G |

- **Daily Seed Spent**: 165 G | **End-of-Day Wallet**: **19,935 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **20,735 G** *(19,935 G carryover + 800 G payout)*
- **Harvest & Ship** *(+1,400 G arriving D30)*:
  - 7x Cucumble *(Farm)* → +1,400 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 1 | 105 G | D30 | +10 G |

- **Daily Seed Spent**: 105 G | **End-of-Day Wallet**: **20,630 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **22,030 G** *(20,630 G carryover + 1,400 G payout)*
- **Harvest & Ship** *(+3,955 G arriving D31)*:
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 15x Cucumble *(Farm)* → +3,000 G (regrowth 6/6)
  - 3x Dress Lettuce *(Farm)* → +255 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **22,030 G**
- **Plots Left**: Farm: 10

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **25,985 G** *(22,030 G carryover + 3,955 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 9–30)

- **Starting Wallet (Day 9)**: 1,525 G
- **Ending Wallet (Day 31 Quietus)**: **25,985 G**
- **Pre-planted Crop Sales**: **+6,790 G**
- **New Planting Net Profit**: **+17,670 G**
- **Net Profit (22 days)**: **+24,460 G**
- **Average Daily Profit**: **+1,112 G/day** *(over 22 active days)*
