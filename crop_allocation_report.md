# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 8
- **Planning Timeline**: Day 8 -> Day 30 (23d Quietus window)
- **Capital Budget**: 1,265 G
- **Plot Capacities (Usable / Max)**: Farm: 29/49

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Stellar Wheat** | 6 | Day 6 | D8 | Freed D8 | +330 G |
| Farm | **Unionion** | 2 | Day 6 | D9 | Freed D9 | +390 G |
| Farm | **Dress Lettuce** | 5 | Day 7 | D9 | Freed D9 | +425 G |
| Farm | **Unionion** | 6 | Day 7 | D10 | Freed D10 | +1,170 G |
| Farm | **Stellar Wheat** | 3 | Day 7 | D9 | Freed D9 | +165 G |
| Farm | **Dress Lettuce** | 6 | Day 7 | D9 | Freed D9 | +510 G |
| Farm | **Unionion** | 1 | Day 7 | D10 | Freed D10 | +195 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 8**

- **Morning Wallet**: **1,265 G**
- **Harvest & Ship** *(+330 G arriving D9)*:
  - 6x Stellar Wheat *(Farm)* → +330 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D10 | +180 G |

- **Daily Seed Spent**: 330 G | **End-of-Day Wallet**: **935 G**
- **Plots Left**: Farm: 0

---

#### **Day 9**

- **Morning Wallet**: **1,265 G** *(935 G carryover + 330 G payout)*
- **Harvest & Ship** *(+1,490 G arriving D10)*:
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)
  - 3x Stellar Wheat *(Farm)* → +165 G (freed)
  - 2x Unionion *(Farm)* → +390 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 1 | 370 G | D13..D28 (6x) | +830 G |
| Farm | **Dress Lettuce** | Lethe | 15 | 825 G | D11 | +450 G |

- **Daily Seed Spent**: 1,195 G | **End-of-Day Wallet**: **70 G**
- **Plots Left**: Farm: 0

---

#### **Day 10**

- **Morning Wallet**: **1,560 G** *(70 G carryover + 1,490 G payout)*
- **Harvest & Ship** *(+1,875 G arriving D11)*:
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)
  - 7x Unionion *(Farm)* → +1,365 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 2 | 740 G | D14..D29 (6x) | +1,660 G |
| Farm | **Dress Lettuce** | Lethe | 11 | 605 G | D12 | +330 G |

- **Daily Seed Spent**: 1,345 G | **End-of-Day Wallet**: **215 G**
- **Plots Left**: Farm: 0

---

#### **Day 11**

- **Morning Wallet**: **2,090 G** *(215 G carryover + 1,875 G payout)*
- **Harvest & Ship** *(+1,275 G arriving D12)*:
  - 15x Dress Lettuce *(Farm)* → +1,275 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 4 | 1,480 G | D15..D30 (6x) | +3,320 G |
| Farm | **Dress Lettuce** | Lethe | 11 | 605 G | D13 | +330 G |

- **Daily Seed Spent**: 2,085 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 0

---

#### **Day 12**

- **Morning Wallet**: **1,280 G** *(5 G carryover + 1,275 G payout)*
- **Harvest & Ship** *(+935 G arriving D13)*:
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 2 | 740 G | D16..D28 (5x) | +1,260 G |
| Farm | **Dress Lettuce** | Lethe | 9 | 495 G | D14 | +270 G |

- **Daily Seed Spent**: 1,235 G | **End-of-Day Wallet**: **45 G**
- **Plots Left**: Farm: 0

---

#### **Day 13**

- **Morning Wallet**: **980 G** *(45 G carryover + 935 G payout)*
- **Harvest & Ship** *(+1,135 G arriving D14)*:
  - 1x Cucumble *(Farm)* → +200 G (regrowth 1/6)
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D15 | +180 G |
| Farm | **Unionion** | Lethe | 5 | 650 G | D16 | +325 G |

- **Daily Seed Spent**: 980 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 0

---

#### **Day 14**

- **Morning Wallet**: **1,135 G** *(0 G carryover + 1,135 G payout)*
- **Harvest & Ship** *(+1,165 G arriving D15)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 1/6)
  - 9x Dress Lettuce *(Farm)* → +765 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 2 | 740 G | D18..D30 (5x) | +1,260 G |
| Farm | **Dress Lettuce** | Lethe | 7 | 385 G | D16 | +210 G |

- **Daily Seed Spent**: 1,125 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 0

---

#### **Day 15**

- **Morning Wallet**: **1,175 G** *(10 G carryover + 1,165 G payout)*
- **Harvest & Ship** *(+1,310 G arriving D16)*:
  - 4x Cucumble *(Farm)* → +800 G (regrowth 1/6)
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 6 | 630 G | D16 | +60 G |

- **Daily Seed Spent**: 630 G | **End-of-Day Wallet**: **545 G**
- **Plots Left**: Farm: 0

---

#### **Day 16**

- **Morning Wallet**: **1,855 G** *(545 G carryover + 1,310 G payout)*
- **Harvest & Ship** *(+2,860 G arriving D17)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 3x Cucumble *(Farm)* → +600 G (regrowth 2/6)
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)
  - 5x Unionion *(Farm)* → +975 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 4 | 1,480 G | D20..D29 (4x) | +1,720 G |
| Farm | **Dress Lettuce** | Lethe | 5 | 275 G | D18 | +150 G |

- **Daily Seed Spent**: 1,755 G | **End-of-Day Wallet**: **100 G**
- **Plots Left**: Farm: 9

---

#### **Day 17**

- **Morning Wallet**: **2,960 G** *(100 G carryover + 2,860 G payout)*
- **Harvest & Ship** *(+400 G arriving D18)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 2/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 8 | 2,960 G | D21..D30 (4x) | +3,440 G |

- **Daily Seed Spent**: 2,960 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 1

---

#### **Day 18**

- **Morning Wallet**: **400 G** *(0 G carryover + 400 G payout)*
- **Harvest & Ship** *(+1,625 G arriving D19)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/6)
  - 5x Dress Lettuce *(Farm)* → +425 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D20 | +180 G |

- **Daily Seed Spent**: 330 G | **End-of-Day Wallet**: **70 G**
- **Plots Left**: Farm: 0

---

#### **Day 19**

- **Morning Wallet**: **1,695 G** *(70 G carryover + 1,625 G payout)*
- **Harvest & Ship** *(+600 G arriving D20)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **1,695 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **2,295 G** *(1,695 G carryover + 600 G payout)*
- **Harvest & Ship** *(+1,710 G arriving D21)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 3/6)
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 6 | 2,220 G | D24, D27, D30 | +1,380 G |

- **Daily Seed Spent**: 2,220 G | **End-of-Day Wallet**: **75 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **1,785 G** *(75 G carryover + 1,710 G payout)*
- **Harvest & Ship** *(+2,800 G arriving D22)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **1,785 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **4,585 G** *(1,785 G carryover + 2,800 G payout)*
- **Harvest & Ship** *(+600 G arriving D23)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **4,585 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **5,185 G** *(4,585 G carryover + 600 G payout)*
- **Harvest & Ship** *(+1,200 G arriving D24)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,185 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **6,385 G** *(5,185 G carryover + 1,200 G payout)*
- **Harvest & Ship** *(+4,000 G arriving D25)*:
  - 20x Cucumble *(Farm)* → +4,000 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **6,385 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **10,385 G** *(6,385 G carryover + 4,000 G payout)*
- **Harvest & Ship** *(+600 G arriving D26)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **10,385 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **10,985 G** *(10,385 G carryover + 600 G payout)*
- **Harvest & Ship** *(+1,200 G arriving D27)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **10,985 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **12,185 G** *(10,985 G carryover + 1,200 G payout)*
- **Harvest & Ship** *(+4,000 G arriving D28)*:
  - 20x Cucumble *(Farm)* → +4,000 G (regrowth 5/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **12,185 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **16,185 G** *(12,185 G carryover + 4,000 G payout)*
- **Harvest & Ship** *(+600 G arriving D29)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 1 | 55 G | D30 | +30 G |

- **Daily Seed Spent**: 55 G | **End-of-Day Wallet**: **16,130 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **16,730 G** *(16,130 G carryover + 600 G payout)*
- **Harvest & Ship** *(+1,200 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 2 | 210 G | D30 | +20 G |

- **Daily Seed Spent**: 210 G | **End-of-Day Wallet**: **16,520 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **17,720 G** *(16,520 G carryover + 1,200 G payout)*
- **Harvest & Ship** *(+4,315 G arriving D31)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 20x Cucumble *(Farm)* → +4,000 G (regrowth 6/6)
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **17,720 G**
- **Plots Left**: Farm: 7

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **22,035 G** *(17,720 G carryover + 4,315 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 8–30)

- **Starting Wallet (Day 8)**: 1,265 G
- **Ending Wallet (Day 31 Quietus)**: **22,035 G**
- **Pre-planted Crop Sales**: **+3,185 G**
- **New Planting Net Profit**: **+17,585 G**
- **Net Profit (23 days)**: **+20,770 G**
- **Average Daily Profit**: **+903 G/day** *(over 23 active days)*
