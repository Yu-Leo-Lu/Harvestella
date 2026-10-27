# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 26
- **Planning Timeline**: Day 26 -> Day 30 (5d Quietus window)
- **Capital Budget**: 150 G
- **Plot Capacities (Usable / Max)**: Farm: 134/196 | Waterside: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Cucumble** | 3 | Day 8 | D27 | Freed D27 | +600 G |
| Farm | **Cucumble** | 11 | Day 11 | D27, D30 | Freed D30 | +4,400 G |
| Farm | **Cucumble** | 6 | Day 13 | D26, D29 | Stays Planted | +2,400 G |
| Farm | **Cucumble** | 5 | Day 14 | D27, D30 | Stays Planted | +2,000 G |
| Farm | **Strawbuddy** | 22 | Day 17 | D27, D29 | Freed D29 | +5,720 G |
| Farm | **Strawbuddy** | 16 | Day 18 | D26, D28, D30 | Freed D30 | +6,240 G |
| Farm | **Tingle Radish** | 23 | Day 22 | D26 | Freed D26 | +12,190 G |
| Farm | **Unionion** | 10 | Day 23 | D26 | Freed D26 | +1,950 G |
| Farm | **Carrop** | 2 | Day 25 | D26 | Freed D26 | +230 G |
| Farm | **Dress Lettuce** | 8 | Day 25 | D27 | Freed D27 | +680 G |
| Farm | **Tingle Radish** | 28 | Day 25 | D29 | Freed D29 | +14,840 G |
| Farm | **Tingle Radish** | 23 | Day 26 | D30 | Freed D30 | +12,190 G |
| Farm | **Carrop** | 12 | Day 26 | D27 | Freed D27 | +1,380 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 26**

- **Morning Wallet**: **150 G**
- **Harvest & Ship** *(+17,650 G arriving D27)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 1/2)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 1/3)
  - 23x Tingle Radish *(Farm)* → +12,190 G (freed)
  - 10x Unionion *(Farm)* → +1,950 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **150 G**
- **Plots Left**: Farm: 0 | Waterside: 81

---

#### **Day 27**

- **Morning Wallet**: **17,800 G** *(150 G carryover + 17,650 G payout)*
- **Harvest & Ship** *(+8,720 G arriving D28)*:
  - 12x Carrop *(Farm)* → +1,380 G (freed)
  - 19x Cucumble *(Farm)* → +3,800 G (regrowth 1/1)
  - 8x Dress Lettuce *(Farm)* → +680 G (freed)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 23 | 2,415 G | D30 | +2,070 G |

- **Daily Seed Spent**: 2,415 G | **End-of-Day Wallet**: **15,385 G**
- **Plots Left**: Farm: 0 | Waterside: 81

---

#### **Day 28**

- **Morning Wallet**: **24,105 G** *(15,385 G carryover + 8,720 G payout)*
- **Harvest & Ship** *(+2,080 G arriving D29)*:
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,105 G**
- **Plots Left**: Farm: 0 | Waterside: 81

---

#### **Day 29**

- **Morning Wallet**: **26,185 G** *(24,105 G carryover + 2,080 G payout)*
- **Harvest & Ship** *(+18,900 G arriving D30)*:
  - 6x Cucumble *(Farm)* → +1,200 G (regrowth 2/2)
  - 22x Strawbuddy *(Farm)* → +2,860 G (regrowth 2/2)
  - 28x Tingle Radish *(Farm)* → +14,840 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 50 | 4,750 G | D30 | +1,000 G |

- **Daily Seed Spent**: 4,750 G | **End-of-Day Wallet**: **21,435 G**
- **Plots Left**: Farm: 0 | Waterside: 81

---

#### **Day 30**

- **Morning Wallet**: **40,335 G** *(21,435 G carryover + 18,900 G payout)*
- **Harvest & Ship** *(+27,705 G arriving D31)*:
  - 50x Carrop *(Farm)* → +5,750 G (freed)
  - 16x Cucumble *(Farm)* → +3,200 G (regrowth 2/2)
  - 16x Strawbuddy *(Farm)* → +2,080 G (regrowth 3/3)
  - 23x Tingle Radish *(Farm)* → +12,190 G (freed)
  - 23x Unionion *(Farm)* → +4,485 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **40,335 G**
- **Plots Left**: Farm: 123 | Waterside: 81

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **68,040 G** *(40,335 G carryover + 27,705 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 26–30)

- **Starting Wallet (Day 26)**: 150 G
- **Ending Wallet (Day 31 Quietus)**: **68,040 G**
- **Pre-planted Crop Sales**: **+64,820 G**
- **New Planting Net Profit**: **+3,070 G**
- **Net Profit (5 days)**: **+67,890 G**
- **Average Daily Profit**: **+13,578 G/day** *(over 5 active days)*
