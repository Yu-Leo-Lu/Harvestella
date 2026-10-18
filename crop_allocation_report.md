# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 22
- **Planning Timeline**: Day 22 -> Day 30 (9d Quietus window)
- **Capital Budget**: 20,950 G
- **Plot Capacities**: Farm 29 -> 178 | Waterside 18 -> 81 | Cave 10 -> 73

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D22, D24, D26, D28, D30 | Freed D30 | +8,250 G |
| Farm | **Seatide Garlic** | 45 | Day 18 | D24 | Freed D24 | +45,000 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D23, D24, D25, D26, D27, D28 | Freed D28 | +10,140 G |
| Farm | **Dress Lettuce** | 39 | Day 21 | D23 | Freed D23 | +3,315 G |
| Farm | **Seatide Garlic** | 24 | Day 21 | D27 | Freed D27 | +24,000 G |
| Waterside | **Islet Watermelon** | 1 | Day 12 | D24 | Freed D24 | +4,600 G |
| Waterside | **Islet Watermelon** | 4 | Day 16 | D28 | Freed D28 | +18,400 G |
| Waterside | **Islet Watermelon** | 6 | Day 18 | D30 | Freed D30 | +27,600 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D22, D25, D28 | Freed D28 | +24,750 G |
| Waterside | **Nectarcane** | 10 | Day 19 | D23, D26, D29 | Freed D29 | +7,500 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D24, D27, D30 | Freed D30 | +6,750 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D24, D27, D30 | Freed D30 | +7,155 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D24, D27 | Freed D27 | +22,000 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D24, D27, D30 | Freed D30 | +7,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 22**

- **Morning Wallet**: **20,950 G**
- **Harvest & Ship** *(+9,900 G arriving D23)*:
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 1/5)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 29 | 5,800 G | D26 | +5,800 G |

- **Daily Seed Spent**: 5,800 G | **End-of-Day Wallet**: **15,150 G**
- **Plots Left**: Farm: 0 | Waterside: 18 | Cave: 10

---

#### **Day 23**

- **Morning Wallet**: **25,050 G** *(15,150 G carryover + 9,900 G payout)*
- **Harvest & Ship** *(+7,505 G arriving D24)*:
  - 39x Dress Lettuce *(Farm)* → +3,315 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 1/6)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Curry Herbs** | Argene | 8 | 1,920 G | D29 | +880 G |
| Farm | **Dress Lettuce** | Lethe | 10 | 550 G | D25 | +300 G |
| Farm | **Seatide Garlic** | Shatolla | 29 | 18,850 G | D29 | +10,150 G |

- **Daily Seed Spent**: 21,320 G | **End-of-Day Wallet**: **3,730 G**
- **Plots Left**: Farm: 0 | Waterside: 18 | Cave: 2

---

#### **Day 24**

- **Morning Wallet**: **11,235 G** *(3,730 G carryover + 7,505 G payout)*
- **Harvest & Ship** *(+71,075 G arriving D25)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 2/6)
  - 45x Seatide Garlic *(Farm)* → +45,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 2/5)
  - 1x Islet Watermelon *(Waterside)* → +4,600 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 1/3)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 1/3)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 6 | 3,900 G | D30 | +2,100 G |
| Waterside | **Honey Flower** | Shatolla | 19 | 7,220 G | D30 | +4,750 G |

- **Daily Seed Spent**: 11,120 G | **End-of-Day Wallet**: **115 G**
- **Plots Left**: Farm: 39 | Waterside: 0 | Cave: 2

---

#### **Day 25**

- **Morning Wallet**: **71,190 G** *(115 G carryover + 71,075 G payout)*
- **Harvest & Ship** *(+10,790 G arriving D26)*:
  - 10x Dress Lettuce *(Farm)* → +850 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 3/6)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 49 | 9,800 G | D29 | +9,800 G |

- **Daily Seed Spent**: 9,800 G | **End-of-Day Wallet**: **61,390 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 2

---

#### **Day 26**

- **Morning Wallet**: **72,180 G** *(61,390 G carryover + 10,790 G payout)*
- **Harvest & Ship** *(+17,440 G arriving D27)*:
  - 29x Morrocorn *(Farm)* → +11,600 G (freed)
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 4/6)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 3/5)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 8 | 1,840 G | D30 | +1,360 G |
| Farm | **Morrocorn** | Shatolla | 21 | 4,200 G | D30 | +4,200 G |

- **Daily Seed Spent**: 6,040 G | **End-of-Day Wallet**: **66,140 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 2

---

#### **Day 27**

- **Morning Wallet**: **83,580 G** *(66,140 G carryover + 17,440 G payout)*
- **Harvest & Ship** *(+43,825 G arriving D28)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 5/6)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 2/3)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 2/3)
  - 54x Sudor Pepper *(Cave)* → +13,500 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 24 | 1,320 G | D29 | +720 G |

- **Daily Seed Spent**: 1,320 G | **End-of-Day Wallet**: **82,260 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 46

---

#### **Day 28**

- **Morning Wallet**: **126,085 G** *(82,260 G carryover + 43,825 G payout)*
- **Harvest & Ship** *(+29,990 G arriving D29)*:
  - 26x Nemean Tomato *(Farm)* → +1,690 G (regrowth 6/6)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 4/5)
  - 4x Islet Watermelon *(Waterside)* → +18,400 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 26 | 1,430 G | D30 | +780 G |

- **Daily Seed Spent**: 1,430 G | **End-of-Day Wallet**: **124,655 G**
- **Plots Left**: Farm: 0 | Waterside: 37 | Cave: 46

---

#### **Day 29**

- **Morning Wallet**: **154,645 G** *(124,655 G carryover + 29,990 G payout)*
- **Harvest & Ship** *(+55,940 G arriving D30)*:
  - 24x Dress Lettuce *(Farm)* → +2,040 G (freed)
  - 49x Morrocorn *(Farm)* → +19,600 G (freed)
  - 29x Seatide Garlic *(Farm)* → +29,000 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 3/3)
  - 8x Curry Herbs *(Cave)* → +2,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 3 | 315 G | D30 | +30 G |
| Farm | **Carrop** | Nemea | 99 | 9,405 G | D30 | +1,980 G |

- **Daily Seed Spent**: 9,720 G | **End-of-Day Wallet**: **144,925 G**
- **Plots Left**: Farm: 0 | Waterside: 47 | Cave: 54

---

#### **Day 30**

- **Morning Wallet**: **200,865 G** *(144,925 G carryover + 55,940 G payout)*
- **Harvest & Ship** *(+79,895 G arriving D31)*:
  - 102x Carrop *(Farm)* → +11,730 G (freed)
  - 26x Dress Lettuce *(Farm)* → +2,210 G (freed)
  - 29x Morrocorn *(Farm)* → +11,600 G (freed)
  - 6x Seatide Garlic *(Farm)* → +6,000 G (freed)
  - 15x Shatollan Paprika *(Farm)* → +1,650 G (regrowth 5/5)
  - 19x Honey Flower *(Waterside)* → +11,970 G (freed)
  - 6x Islet Watermelon *(Waterside)* → +27,600 G (freed)
  - 9x Nectarcane *(Waterside)* → +2,250 G (regrowth 3/3)
  - 9x Revol Pepper *(Cave)* → +2,385 G (regrowth 3/3)
  - 10x Sudor Pepper *(Cave)* → +2,500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **200,865 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+79,895 G** *(from Day 30 final harvest: 15x Shatollan Paprika, 6x Islet Watermelon, 9x Nectarcane, 9x Revol Pepper, 10x Sudor Pepper, 6x Seatide Garlic, 29x Morrocorn, 19x Honey Flower, 102x Carrop, 26x Dress Lettuce)*
- **Starting Budget**: 20,950 G
- **Total Season Net Profit**: **+259,810 G**
- 🏆 **Final Quietus Wallet**: **280,760 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 29 / 29 (expands to 178) (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 0 / 18 (expands to 81) (0.0% utilized, 18 idle)
- **Cave Plots Used (Init)**: 0 / 10 (expands to 73) (0.0% utilized, 10 idle)
- **Initial Capital Spent**: 5,800 G / 20,950 G (27.7% spent, 15,150 G leftover)
- **Pre-planted Crop Sales**: **+216,960 G**
- **New Planting Net Profit**: **+42,850 G**
- **Total Cumulative Season Net Profit**: **+259,810 G** across all restock stages
- **Final Projected Wallet**: **280,760 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
