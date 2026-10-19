# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 23
- **Planning Timeline**: Day 23 -> Day 30 (8d Quietus window)
- **Capital Budget**: 40,735 G
- **Plot Capacities (Usable / Max)**: Farm: 178/196 | Waterside: 81/81 | Cave: 73/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D24, D26, D28, D30 | Freed D30 | +6,600 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D23, D24, D25, D26, D27, D28 | Freed D28 | +10,140 G |
| Farm | **Seatide Garlic** | 45 | Day 17 | D23 | Freed D23 | +45,000 G |
| Farm | **Dress Lettuce** | 39 | Day 21 | D23 | Freed D23 | +3,315 G |
| Farm | **Seatide Garlic** | 24 | Day 21 | D27 | Freed D27 | +24,000 G |
| Farm | **Morrocorn** | 29 | Day 22 | D26 | Freed D26 | +11,600 G |
| Waterside | **Islet Watermelon** | 1 | Day 11 | D23 | Freed D23 | +4,600 G |
| Waterside | **Islet Watermelon** | 4 | Day 16 | D28 | Freed D28 | +18,400 G |
| Waterside | **Islet Watermelon** | 6 | Day 18 | D30 | Freed D30 | +27,600 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D25, D28 | Freed D28 | +16,500 G |
| Waterside | **Nectarcane** | 10 | Day 19 | D23, D26, D29 | Freed D29 | +7,500 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D24, D27, D30 | Freed D30 | +6,750 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D24, D27, D30 | Freed D30 | +7,155 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D24, D27 | Freed D27 | +22,000 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D24, D27, D30 | Freed D30 | +7,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 23**

- **Morning Wallet**: **40,735 G**
- **Harvest & Ship** *(+57,105 G arriving D24)*:
  - 39x Dress Lettuce *(Farm)* → +3,315 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 1/6)
  - 45x Seatide Garlic *(Farm)* → +45,000 G (freed)
  - 1x Islet Watermelon *(Waterside)* → +4,600 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 84 | 7,980 G | D24 | +1,680 G |
| Waterside | **Honey Flower** | Shatolla | 19 | 7,220 G | D29 | +4,750 G |

- **Daily Seed Spent**: 15,200 G | **End-of-Day Wallet**: **25,535 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 10

---

#### **Day 24**

- **Morning Wallet**: **82,640 G** *(25,535 G carryover + 57,105 G payout)*
- **Harvest & Ship** *(+31,135 G arriving D25)*:
  - 84x Carrop *(Farm)* → +9,660 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 2/6)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/4)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 1/3)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/3)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Curry Herbs** | Argene | 10 | 2,400 G | D30 | +1,100 G |
| Farm | **Seatide Garlic** | Shatolla | 84 | 54,600 G | D30 | +29,400 G |

- **Daily Seed Spent**: 57,000 G | **End-of-Day Wallet**: **25,640 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **56,775 G** *(25,640 G carryover + 31,135 G payout)*
- **Harvest & Ship** *(+9,940 G arriving D26)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 3/6)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 1/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **56,775 G**

---

#### **Day 26**

- **Morning Wallet**: **66,715 G** *(56,775 G carryover + 9,940 G payout)*
- **Harvest & Ship** *(+17,440 G arriving D27)*:
  - 29x Morrocorn *(Farm)* → +11,600 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 4/6)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 2/4)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 29 | 5,800 G | D30 | +5,800 G |

- **Daily Seed Spent**: 5,800 G | **End-of-Day Wallet**: **60,915 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **78,355 G** *(60,915 G carryover + 17,440 G payout)*
- **Harvest & Ship** *(+43,825 G arriving D28)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 5/6)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 2/3)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 2/3)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 9 | 945 G | D28 | +90 G |
| Farm | **Carrop** | Nemea | 15 | 1,425 G | D28 | +300 G |

- **Daily Seed Spent**: 2,370 G | **End-of-Day Wallet**: **75,985 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 44

---

#### **Day 28**

- **Morning Wallet**: **119,810 G** *(75,985 G carryover + 43,825 G payout)*
- **Harvest & Ship** *(+32,750 G arriving D29)*:
  - 24x Carrop *(Farm)* → +2,760 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 6/6)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 3/4)
  - 4x Islet Watermelon *(Waterside)* → +18,400 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 50 | 2,750 G | D30 | +1,500 G |

- **Daily Seed Spent**: 2,750 G | **End-of-Day Wallet**: **117,060 G**
- **Plots Left**: Farm: 0 | Waterside: 37 | Cave: 44

---

#### **Day 29**

- **Morning Wallet**: **149,810 G** *(117,060 G carryover + 32,750 G payout)*
- **Harvest & Ship** *(+14,470 G arriving D30)*:
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **149,810 G**

---

#### **Day 30**

- **Morning Wallet**: **164,280 G** *(149,810 G carryover + 14,470 G payout)*
- **Harvest & Ship** *(+139,735 G arriving D31)*:
  - 50x Dress Lettuce *(Farm)* → +4,250 G (freed)
  - 29x Morrocorn *(Farm)* → +11,600 G (freed)
  - 84x Seatide Garlic *(Farm)* → +84,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 4/4)
  - 6x Islet Watermelon *(Waterside)* → +27,600 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 3/3)
  - 10x Curry Herbs *(Cave)* → +3,500 G (freed)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 3/3)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **164,280 G**

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **304,015 G** *(164,280 G carryover + 139,735 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary

- **Starting Budget**: 40,735 G
- **Pre-planted Crop Sales**: **+218,660 G**
- **New Planting Net Profit**: **+44,620 G**
- **Total Season Net Profit**: **+263,280 G**
- **Final Quietus Wallet**: **304,015 G**
