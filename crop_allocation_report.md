# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 10
- **Planning Timeline**: Day 10 -> Day 30 (21d Quietus window)
- **Capital Budget**: 2,515 G
- **Plot Capacities (Usable / Max)**: Farm: 29/49

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Unionion** | 7 | Day 7 | D10 | Freed D10 | +1,365 G |
| Farm | **Cucumble** | 3 | Day 8 | D12, D15, D18, D21, D24, D27 | Freed D27 | +3,600 G |
| Farm | **Dress Lettuce** | 1 | Day 8 | D10 | Freed D10 | +85 G |
| Farm | **Stellar Wheat** | 1 | Day 8 | D10 | Freed D10 | +55 G |
| Farm | **Unionion** | 1 | Day 8 | D11 | Freed D11 | +195 G |
| Farm | **Dress Lettuce** | 7 | Day 9 | D11 | Freed D11 | +595 G |
| Farm | **Nemean Tomato** | 3 | Day 9 | D14, D15, D16, D17, D18, D19 | Freed D19 | +1,170 G |
| Farm | **Stellar Wheat** | 6 | Day 9 | D11 | Freed D11 | +330 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 10**

- **Morning Wallet**: **2,515 G**
- **Harvest & Ship** *(+1,505 G arriving D11)*:
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)
  - 1x Stellar Wheat *(Farm)* → +55 G (freed)
  - 7x Unionion *(Farm)* → +1,365 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 2 | 740 G | D14..D29 (6x) | +1,660 G |
| Farm | **Dress Lettuce** | Lethe | 1 | 55 G | D12 | +30 G |
| Farm | **Unionion** | Nemea | 6 | 630 G | D13 | +540 G |

- **Daily Seed Spent**: 1,425 G | **End-of-Day Wallet**: **1,090 G**
- **Plots Left**: Farm: 0

---

#### **Day 11**

- **Morning Wallet**: **2,595 G** *(1,090 G carryover + 1,505 G payout)*
- **Harvest & Ship** *(+1,120 G arriving D12)*:
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)
  - 6x Stellar Wheat *(Farm)* → +330 G (freed)
  - 1x Unionion *(Farm)* → +195 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 7 | 2,590 G | D15..D30 (6x) | +5,810 G |

- **Daily Seed Spent**: 2,590 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 7

---

#### **Day 12**

- **Morning Wallet**: **1,125 G** *(5 G carryover + 1,120 G payout)*
- **Harvest & Ship** *(+685 G arriving D13)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 1/6)
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 8 | 840 G | D15 | +720 G |

- **Daily Seed Spent**: 840 G | **End-of-Day Wallet**: **285 G**
- **Plots Left**: Farm: 0

---

#### **Day 13**

- **Morning Wallet**: **970 G** *(285 G carryover + 685 G payout)*
- **Harvest & Ship** *(+1,170 G arriving D14)*:
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 1 | 55 G | D15 | +30 G |
| Farm | **Carrop** | Nemea | 4 | 380 G | D14 | +80 G |
| Farm | **Strawbuddy** | Nemea | 1 | 220 G | D17..D25 (5x) | +430 G |

- **Daily Seed Spent**: 655 G | **End-of-Day Wallet**: **315 G**
- **Plots Left**: Farm: 0

---

#### **Day 14**

- **Morning Wallet**: **1,485 G** *(315 G carryover + 1,170 G payout)*
- **Harvest & Ship** *(+1,055 G arriving D15)*:
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 2x Cucumble *(Farm)* → +400 G (regrowth 1/6)
  - 3x Nemean Tomato *(Farm)* → +195 G (regrowth 1/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 4 | 1,480 G | D18..D30 (5x) | +2,520 G |

- **Daily Seed Spent**: 1,480 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 0

---

#### **Day 15**

- **Morning Wallet**: **1,060 G** *(5 G carryover + 1,055 G payout)*
- **Harvest & Ship** *(+3,840 G arriving D16)*:
  - 10x Cucumble *(Farm)* → +2,000 G (regrowth 2/6)
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)
  - 3x Nemean Tomato *(Farm)* → +195 G (regrowth 2/6)
  - 8x Unionion *(Farm)* → +1,560 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 9 | 945 G | D18 | +810 G |

- **Daily Seed Spent**: 945 G | **End-of-Day Wallet**: **115 G**
- **Plots Left**: Farm: 0

---

#### **Day 16**

- **Morning Wallet**: **3,955 G** *(115 G carryover + 3,840 G payout)*
- **Harvest & Ship** *(+195 G arriving D17)*:
  - 3x Nemean Tomato *(Farm)* → +195 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **3,955 G**
- **Plots Left**: Farm: 0

---

#### **Day 17**

- **Morning Wallet**: **4,150 G** *(3,955 G carryover + 195 G payout)*
- **Harvest & Ship** *(+725 G arriving D18)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 2/6)
  - 3x Nemean Tomato *(Farm)* → +195 G (regrowth 4/6)
  - 1x Strawbuddy *(Farm)* → +130 G (regrowth 1/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **4,150 G**
- **Plots Left**: Farm: 0

---

#### **Day 18**

- **Morning Wallet**: **4,875 G** *(4,150 G carryover + 725 G payout)*
- **Harvest & Ship** *(+4,750 G arriving D19)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 3/6)
  - 3x Nemean Tomato *(Farm)* → +195 G (regrowth 5/6)
  - 9x Unionion *(Farm)* → +1,755 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Strawbuddy** | Nemea | 9 | 1,980 G | D22..D30 (5x) | +3,870 G |

- **Daily Seed Spent**: 1,980 G | **End-of-Day Wallet**: **2,895 G**
- **Plots Left**: Farm: 0

---

#### **Day 19**

- **Morning Wallet**: **7,645 G** *(2,895 G carryover + 4,750 G payout)*
- **Harvest & Ship** *(+325 G arriving D20)*:
  - 3x Nemean Tomato *(Farm)* → +195 G (regrowth 6/6)
  - 1x Strawbuddy *(Farm)* → +130 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D22 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **7,330 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **7,655 G** *(7,330 G carryover + 325 G payout)*
- **Harvest & Ship** *(+400 G arriving D21)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 3/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **7,655 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **8,055 G** *(7,655 G carryover + 400 G payout)*
- **Harvest & Ship** *(+2,930 G arriving D22)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 4/6)
  - 1x Strawbuddy *(Farm)* → +130 G (regrowth 3/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **8,055 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **10,985 G** *(8,055 G carryover + 2,930 G payout)*
- **Harvest & Ship** *(+1,755 G arriving D23)*:
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 1/5)
  - 3x Unionion *(Farm)* → +585 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 3 | 1,170 G | D26 | +420 G |

- **Daily Seed Spent**: 1,170 G | **End-of-Day Wallet**: **9,815 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **11,570 G** *(9,815 G carryover + 1,755 G payout)*
- **Harvest & Ship** *(+530 G arriving D24)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 4/6)
  - 1x Strawbuddy *(Farm)* → +130 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **11,570 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **12,100 G** *(11,570 G carryover + 530 G payout)*
- **Harvest & Ship** *(+3,970 G arriving D25)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 5/6)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **12,100 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **16,070 G** *(12,100 G carryover + 3,970 G payout)*
- **Harvest & Ship** *(+130 G arriving D26)*:
  - 1x Strawbuddy *(Farm)* → +130 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 1 | 95 G | D26 | +20 G |

- **Daily Seed Spent**: 95 G | **End-of-Day Wallet**: **15,975 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **16,105 G** *(15,975 G carryover + 130 G payout)*
- **Harvest & Ship** *(+3,275 G arriving D27)*:
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 2x Cucumble *(Farm)* → +400 G (regrowth 5/6)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 3/5)
  - 3x Tingle Radish *(Farm)* → +1,590 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 4 | 1,560 G | D30 | +560 G |

- **Daily Seed Spent**: 1,560 G | **End-of-Day Wallet**: **14,545 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **17,820 G** *(14,545 G carryover + 3,275 G payout)*
- **Harvest & Ship** *(+2,800 G arriving D28)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D30 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **17,505 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **20,305 G** *(17,505 G carryover + 2,800 G payout)*
- **Harvest & Ship** *(+1,170 G arriving D29)*:
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **20,305 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **21,475 G** *(20,305 G carryover + 1,170 G payout)*
- **Harvest & Ship** *(+400 G arriving D30)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 2 | 190 G | D30 | +40 G |

- **Daily Seed Spent**: 190 G | **End-of-Day Wallet**: **21,285 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **21,685 G** *(21,285 G carryover + 400 G payout)*
- **Harvest & Ship** *(+6,305 G arriving D31)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 11x Cucumble *(Farm)* → +2,200 G (regrowth 6/6)
  - 9x Strawbuddy *(Farm)* → +1,170 G (regrowth 5/5)
  - 4x Tingle Radish *(Farm)* → +2,120 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **21,685 G**
- **Plots Left**: Farm: 25

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **27,990 G** *(21,685 G carryover + 6,305 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 10–30)

- **Starting Wallet (Day 10)**: 2,515 G
- **Ending Wallet (Day 31 Quietus)**: **27,990 G**
- **Pre-planted Crop Sales**: **+7,395 G**
- **New Planting Net Profit**: **+18,080 G**
- **Net Profit (21 days)**: **+25,475 G**
- **Average Daily Profit**: **+1,213 G/day** *(over 21 active days)*
