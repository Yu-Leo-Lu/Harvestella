# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 20
- **Planning Timeline**: Day 20 -> Day 30 (11d Quietus window)
- **Capital Budget**: 99,185 G
- **Plot Capacities (Usable / Max)**: Farm: 234/245 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D20, D22 | Freed D22 | +15,400 G |
| Farm | **Bellhop** | 1 | Day 5 | D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +495 G |
| Farm | **Bellhop** | 1 | Day 6 | D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +495 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D20, D22, D24, D26, D28, D30 | Freed D30 | +1,980 G |
| Farm | **Seatide Garlic** | 24 | Day 14 | D20 | Freed D20 | +24,000 G |
| Farm | **Morrocorn** | 40 | Day 16 | D20 | Freed D20 | +16,000 G |
| Farm | **Eden Rice** | 15 | Day 17 | D20 | Freed D20 | +525 G |
| Farm | **Shatollan Paprika** | 37 | Day 17 | D22, D24, D26, D28, D30 | Stays Planted | +20,350 G |
| Farm | **Seatide Garlic** | 32 | Day 18 | D24 | Freed D24 | +32,000 G |
| Farm | **Carrop** | 11 | Day 19 | D20 | Freed D20 | +1,265 G |
| Waterside | **Islet Watermelon** | 3 | Day 13 | D25 | Freed D25 | +13,800 G |
| Waterside | **Islet Watermelon** | 3 | Day 15 | D27 | Freed D27 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 16 | D28 | Freed D28 | +9,200 G |
| Waterside | **Islet Watermelon** | 54 | Day 17 | D29 | Freed D29 | +248,400 G |
| Waterside | **Islet Watermelon** | 15 | Day 18 | D30 | Freed D30 | +69,000 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D20, D23, D26 | Freed D26 | +54,855 G |
| Cave | **Revol Pepper** | 12 | Day 17 | D21, D24, D27, D30 | Stays Planted | +12,720 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 20**

- **Morning Wallet**: **99,185 G**
- **Harvest & Ship** *(+68,195 G arriving D21)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/11)
  - 11x Carrop *(Farm)* → +1,265 G (freed)
  - 15x Eden Rice *(Farm)* → +525 G (freed)
  - 40x Morrocorn *(Farm)* → +16,000 G (freed)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 1/2)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 8 | 1,840 G | D24 | +1,360 G |
| Farm | **Morrocorn** | Shatolla | 45 | 9,000 G | D24 | +9,000 G |
| Farm | **Seatide Garlic** | Shatolla | 37 | 24,050 G | D26 | +12,950 G |

- **Daily Seed Spent**: 34,890 G | **End-of-Day Wallet**: **64,295 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **132,490 G** *(64,295 G carryover + 68,195 G payout)*
- **Harvest & Ship** *(+3,270 G arriving D22)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/11)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **132,490 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **135,760 G** *(132,490 G carryover + 3,270 G payout)*
- **Harvest & Ship** *(+12,190 G arriving D23)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/11)
  - 110x Shatollan Paprika *(Farm)* → +12,100 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 14 | 1,330 G | D23 | +280 G |
| Farm | **Morrocorn** | Shatolla | 56 | 11,200 G | D26 | +11,200 G |

- **Daily Seed Spent**: 12,530 G | **End-of-Day Wallet**: **123,230 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **135,420 G** *(123,230 G carryover + 12,190 G payout)*
- **Harvest & Ship** *(+19,985 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/11)
  - 14x Carrop *(Farm)* → +1,610 G (freed)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 14 | 1,330 G | D24 | +280 G |

- **Daily Seed Spent**: 1,330 G | **End-of-Day Wallet**: **134,090 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **154,075 G** *(134,090 G carryover + 19,985 G payout)*
- **Harvest & Ship** *(+62,480 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/11)
  - 14x Carrop *(Farm)* → +1,610 G (freed)
  - 53x Morrocorn *(Farm)* → +21,200 G (freed)
  - 32x Seatide Garlic *(Farm)* → +32,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 3/6)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **89,725 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **152,205 G** *(89,725 G carryover + 62,480 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/11)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **152,205 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **166,095 G** *(152,205 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+82,175 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/11)
  - 56x Morrocorn *(Farm)* → +22,400 G (freed)
  - 37x Seatide Garlic *(Farm)* → +37,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 4/6)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 43 | 8,600 G | D30 | +8,600 G |

- **Daily Seed Spent**: 20,100 G | **End-of-Day Wallet**: **145,995 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **228,170 G** *(145,995 G carryover + 82,175 G payout)*
- **Harvest & Ship** *(+17,070 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/11)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **228,170 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **245,240 G** *(228,170 G carryover + 17,070 G payout)*
- **Harvest & Ship** *(+13,690 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 9/11)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 5/6)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **245,240 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **258,930 G** *(245,240 G carryover + 13,690 G payout)*
- **Harvest & Ship** *(+248,490 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 10/11)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **258,930 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **507,420 G** *(258,930 G carryover + 248,490 G payout)*
- **Harvest & Ship** *(+212,870 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 11/11)
  - 93x Morrocorn *(Farm)* → +37,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 40x Shatollan Paprika *(Farm)* → +4,400 G (regrowth 6/6)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **507,420 G**
- **Plots Left**: Farm: 195 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **720,290 G** *(507,420 G carryover + 212,870 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 20–30)

- **Starting Wallet (Day 20)**: 99,185 G
- **Ending Wallet (Day 31 Quietus)**: **720,290 G**
- **Pre-planted Crop Sales**: **+534,285 G**
- **New Planting Net Profit**: **+86,820 G**
- **Net Profit (11 days)**: **+621,105 G**
- **Average Daily Profit**: **+56,464 G/day** *(over 11 active days)*
