# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 25
- **Planning Timeline**: Day 25 -> Day 30 (6d Quietus window)
- **Capital Budget**: 940 G
- **Plot Capacities (Usable / Max)**: Farm: 134/196

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D27 | Freed D27 | +600 G |
| Farm | **Cucumble** | 11 | Day 11 | D27, D30 | Freed D30 | +4,400 G |
| Farm | **Cucumble** | 6 | Day 13 | D26, D29 | Stays Planted | +2,400 G |
| Farm | **Strawbuddy** | 2 | Day 13 | D25 | Freed D25 | +260 G |
| Farm | **Cucumble** | 5 | Day 14 | D27, D30 | Stays Planted | +2,000 G |
| Farm | **Strawbuddy** | 22 | Day 17 | D25, D27, D29 | Freed D29 | +8,580 G |
| Farm | **Strawbuddy** | 16 | Day 18 | D26, D28, D30 | Freed D30 | +6,240 G |
| Farm | **Tingle Radish** | 23 | Day 22 | D26 | Freed D26 | +12,190 G |
| Farm | **Unionion** | 10 | Day 23 | D26 | Freed D26 | +1,950 G |
| Farm | **Tingle Radish** | 28 | Day 25 | D29 | Freed D29 | +14,840 G |
| Farm | **Dress Lettuce** | 8 | Day 25 | D27 | Freed D27 | +680 G |
| Farm | **Carrop** | 2 | Day 25 | D26 | Freed D26 | +230 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 25**

- **Morning Wallet**: **940 G**
- **Harvest & Ship** *(+3,120 G arriving D26)*:
  - 24x Strawbuddy *(Farm)* → +3,120 G (regrowth 1/1)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **940 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **4,060 G** *(940 G carryover + 3,120 G payout)*
- **Harvest & Ship** *(+17,650 G arriving D27)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 1/2)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 1/3)
  - 23x Tingle Radish *(Farm)* → +12,190 G (freed)
  - 10x Unionion *(Farm)* → +1,950 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 33 | 3,135 G | D27 | +660 G |
| Farm | **Tingle Radish** | Nemea | 2 | 780 G | D30 | +280 G |

- **Daily Seed Spent**: 3,915 G | **End-of-Day Wallet**: **145 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **17,795 G** *(145 G carryover + 17,650 G payout)*
- **Harvest & Ship** *(+11,135 G arriving D28)*:
  - 33x Carrop *(Farm)* → +3,795 G (freed)
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 1/1)
  - 8x Dress Lettuce *(Farm)* → +680 G (freed)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 44 | 4,620 G | D30 | +3,960 G |

- **Daily Seed Spent**: 4,620 G | **End-of-Day Wallet**: **13,175 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **24,310 G** *(13,175 G carryover + 11,135 G payout)*
- **Harvest & Ship** *(+2,080 G arriving D29)*:
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,310 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **26,390 G** *(24,310 G carryover + 2,080 G payout)*
- **Harvest & Ship** *(+18,900 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/2)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 3/3)
  - 28x Tingle Radish *(Farm)* → +14,840 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 50 | 4,750 G | D30 | +1,000 G |

- **Daily Seed Spent**: 4,750 G | **End-of-Day Wallet**: **21,640 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **40,540 G** *(21,640 G carryover + 18,900 G payout)*
- **Harvest & Ship** *(+20,670 G arriving D31)*:
  - 50x Carrop *(Farm)* → +5,750 G (freed)
  - 16x Cucumble *(Farm)* → +3,200 G (regrowth 2/2)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 3/3)
  - 2x Tingle Radish *(Farm)* → +1,060 G (freed)
  - 44x Unionion *(Farm)* → +8,580 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **40,540 G**
- **Plots Left**: Farm: 123

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **61,210 G** *(40,540 G carryover + 20,670 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 25–30)

- **Starting Wallet (Day 25)**: 940 G
- **Ending Wallet (Day 31 Quietus)**: **61,210 G**
- **Pre-planted Crop Sales**: **+54,370 G**
- **New Planting Net Profit**: **+5,900 G**
- **Net Profit (6 days)**: **+60,270 G**
- **Average Daily Profit**: **+10,045 G/day** *(over 6 active days)*
