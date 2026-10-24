# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 15
- **Planning Timeline**: Day 15 -> Day 30 (16d Quietus window)
- **Capital Budget**: 3,120 G
- **Plot Capacities (Usable / Max)**: Farm: 61/98

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D15, D18, D21, D24, D27 | Freed D27 | +3,000 G |
| Farm | **Nemean Tomato** | 6 | Day 9 | D15, D16, D17, D18, D19 | Freed D19 | +1,950 G |
| Farm | **Cucumble** | 11 | Day 11 | D15, D18, D21, D24, D27, D30 | Freed D30 | +13,200 G |
| Farm | **Nemean Tomato** | 3 | Day 12 | D17, D18, D19, D20, D21, D22 | Freed D22 | +1,170 G |
| Farm | **Cucumble** | 6 | Day 13 | D17, D20, D23, D26, D29 | Stays Planted | +6,000 G |
| Farm | **Dress Lettuce** | 11 | Day 13 | D15 | Freed D15 | +935 G |
| Farm | **Nemean Tomato** | 10 | Day 13 | D18, D19, D20, D21, D22, D23 | Freed D23 | +3,900 G |
| Farm | **Stellar Wheat** | 4 | Day 13 | D15 | Freed D15 | +220 G |
| Farm | **Strawbuddy** | 2 | Day 13 | D17, D19, D21, D23, D25 | Freed D25 | +1,300 G |
| Farm | **Cucumble** | 5 | Day 14 | D18, D21, D24, D27, D30 | Stays Planted | +5,000 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 15**

- **Morning Wallet**: **3,120 G**
- **Harvest & Ship** *(+4,345 G arriving D16)*:
  - 14x Cucumble *(Farm)* → +2,800 G (regrowth 1/5)
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 1/5)
  - 4x Stellar Wheat *(Farm)* → +220 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 15 | 1,575 G | D18 | +1,350 G |

- **Daily Seed Spent**: 1,575 G | **End-of-Day Wallet**: **1,545 G**
- **Plots Left**: Farm: 0

---

#### **Day 16**

- **Morning Wallet**: **5,890 G** *(1,545 G carryover + 4,345 G payout)*
- **Harvest & Ship** *(+390 G arriving D17)*:
  - 6x Nemean Tomato *(Farm)* → +390 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,890 G**
- **Plots Left**: Farm: 0

---

#### **Day 17**

- **Morning Wallet**: **6,280 G** *(5,890 G carryover + 390 G payout)*
- **Harvest & Ship** *(+2,045 G arriving D18)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 1/5)
  - 9x Nemean Tomato *(Farm)* → +585 G (regrowth 3/5)
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 1/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **6,280 G**
- **Plots Left**: Farm: 0

---

#### **Day 18**

- **Morning Wallet**: **8,325 G** *(6,280 G carryover + 2,045 G payout)*
- **Harvest & Ship** *(+7,960 G arriving D19)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 2/5)
  - 19x Nemean Tomato *(Farm)* → +1,235 G (regrowth 4/5)
  - 15x Unionion *(Farm)* → +2,925 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Strawbuddy** | Nemea | 15 | 3,300 G | D22..D30 (5x) | +6,450 G |

- **Daily Seed Spent**: 3,300 G | **End-of-Day Wallet**: **5,025 G**
- **Plots Left**: Farm: 0

---

#### **Day 19**

- **Morning Wallet**: **12,985 G** *(5,025 G carryover + 7,960 G payout)*
- **Harvest & Ship** *(+1,495 G arriving D20)*:
  - 19x Nemean Tomato *(Farm)* → +1,235 G (regrowth 5/5)
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 6 | 630 G | D22 | +540 G |

- **Daily Seed Spent**: 630 G | **End-of-Day Wallet**: **12,355 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **13,850 G** *(12,355 G carryover + 1,495 G payout)*
- **Harvest & Ship** *(+2,045 G arriving D21)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/5)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 4/6)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **13,850 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **15,895 G** *(13,850 G carryover + 2,045 G payout)*
- **Harvest & Ship** *(+4,905 G arriving D22)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 3/5)
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 5/6)
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 3/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **15,895 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **20,800 G** *(15,895 G carryover + 4,905 G payout)*
- **Harvest & Ship** *(+3,965 G arriving D23)*:
  - 13x Nemean Tomato *(Farm)* → +845 G (regrowth 6/6)
  - 15x Strawbuddy *(Farm)* → +1,950 G (regrowth 1/5)
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 9 | 3,510 G | D26 | +1,260 G |

- **Daily Seed Spent**: 3,510 G | **End-of-Day Wallet**: **17,290 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **21,255 G** *(17,290 G carryover + 3,965 G payout)*
- **Harvest & Ship** *(+2,110 G arriving D24)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 3/5)
  - 10x Nemean Tomato *(Farm)* → +650 G (regrowth 6/6)
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 10 | 1,050 G | D26 | +900 G |

- **Daily Seed Spent**: 1,050 G | **End-of-Day Wallet**: **20,205 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **22,315 G** *(20,205 G carryover + 2,110 G payout)*
- **Harvest & Ship** *(+5,750 G arriving D25)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 4/5)
  - 15x Strawbuddy *(Farm)* → +1,950 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **22,315 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **28,065 G** *(22,315 G carryover + 5,750 G payout)*
- **Harvest & Ship** *(+260 G arriving D26)*:
  - 2x Strawbuddy *(Farm)* → +260 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 2 | 190 G | D26 | +40 G |

- **Daily Seed Spent**: 190 G | **End-of-Day Wallet**: **27,875 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **28,135 G** *(27,875 G carryover + 260 G payout)*
- **Harvest & Ship** *(+10,100 G arriving D27)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 4/5)
  - 15x Strawbuddy *(Farm)* → +1,950 G (regrowth 3/5)
  - 9x Tingle Radish *(Farm)* → +4,770 G (freed)
  - 10x Unionion *(Farm)* → +1,950 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Tingle Radish** | Nemea | 21 | 8,190 G | D30 | +2,940 G |

- **Daily Seed Spent**: 8,190 G | **End-of-Day Wallet**: **19,945 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **30,045 G** *(19,945 G carryover + 10,100 G payout)*
- **Harvest & Ship** *(+3,800 G arriving D28)*:
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 3 | 315 G | D30 | +270 G |

- **Daily Seed Spent**: 315 G | **End-of-Day Wallet**: **29,730 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **33,530 G** *(29,730 G carryover + 3,800 G payout)*
- **Harvest & Ship** *(+1,950 G arriving D29)*:
  - 15x Strawbuddy *(Farm)* → +1,950 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **33,530 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **35,480 G** *(33,530 G carryover + 1,950 G payout)*
- **Harvest & Ship** *(+1,200 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **35,480 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **36,680 G** *(35,480 G carryover + 1,200 G payout)*
- **Harvest & Ship** *(+16,865 G arriving D31)*:
  - 16x Cucumble *(Farm)* → +3,200 G (regrowth 6/6)
  - 15x Strawbuddy *(Farm)* → +1,950 G (regrowth 5/5)
  - 21x Tingle Radish *(Farm)* → +11,130 G (freed)
  - 3x Unionion *(Farm)* → +585 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **36,680 G**
- **Plots Left**: Farm: 50

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **53,545 G** *(36,680 G carryover + 16,865 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 15–30)

- **Starting Wallet (Day 15)**: 3,120 G
- **Ending Wallet (Day 31 Quietus)**: **53,545 G**
- **Pre-planted Crop Sales**: **+36,675 G**
- **New Planting Net Profit**: **+13,750 G**
- **Net Profit (16 days)**: **+50,425 G**
- **Average Daily Profit**: **+3,152 G/day** *(over 16 active days)*
