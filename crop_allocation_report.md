# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 18
- **Planning Timeline**: Day 18 -> Day 30 (13d Quietus window)
- **Capital Budget**: 51,600 G
- **Plot Capacities**: Farm 119 -> 170 | Waterside 78 -> 81 | Cave 81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Waterside | **Islet Watermelon** | 1 | Day 8 | D20 | Freed D20 | +4,600 G |
| Waterside | **Islet Watermelon** | 2 | Day 12 | D24 | Freed D24 | +9,200 G |
| Farm | **Nemean Tomato** | 20 | Day 10 | D18, D19, D20 | Stays Planted *(Regrowth)* | +3,900 G |
| Farm | **Morrocorn** | 51 | Day 15 | D19 | Freed D19 | +20,400 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 18**

- **Morning Wallet**: **51,600 G**
- 🌾 **Harvest & Ship**: 20x Nemean Tomato *(Farm)* — regrowth 1/3 (stays planted) → +1,300 G *(arrives morning D19)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 13 | 5,200 G | D21, D24, D27 | +4,550 G |
| Farm | **Carrop** | Lethe | 47 | 4,935 G | D19 | +470 G |
| Farm | **Stellar Wheat** | Lethe | 50 | 2,000 G | D20 | +750 G |
| Farm | **Carrop** | Nemea | 21 | 1,995 G | D19 | +420 G |
| Waterside | **Islet Watermelon** | Shatolla | 4 | 10,000 G | D30 | +8,400 G |
| Waterside | **Nectarcane** | Shatolla | 73 | 27,010 G | D22, D25, D28 | +27,740 G |

- **Daily Seed Spent**: 51,140 G | **End-of-Day Wallet**: **460 G**

---

#### **Day 19**

- 📬 **Payout**: **+1,300 G** *(from 20x Nemean Tomato (pre-planted) on Day 18)*
- **Morning Wallet**: **1,760 G** *(460 G carryover + 1,300 G)*
- 🌾 **Harvest & Ship**:
  - 68x Carrop *(Farm)* — single harvest (soil freed) → +7,820 G *(arrives morning D20)*
  - 51x Morrocorn *(Farm)* — single harvest (soil freed) → +20,400 G *(arrives morning D20)*
  - 20x Nemean Tomato *(Farm)* — regrowth 2/3 (stays planted) → +1,300 G *(arrives morning D20)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 43 | 1,290 G | D21 | +215 G |

- **Daily Seed Spent**: 1,290 G | **End-of-Day Wallet**: **470 G**

---

#### **Day 20**

- 📬 **Payout**: **+29,520 G** *(from 20x Nemean Tomato (pre-planted) on Day 19, 51x Morrocorn (pre-planted) on Day 19, 68x Carrop on Day 19)*
- **Morning Wallet**: **29,990 G** *(470 G carryover + 29,520 G)*
- 🌾 **Harvest & Ship**:
  - 20x Nemean Tomato *(Farm)* — regrowth 3/3 (stays planted) → +1,300 G *(arrives morning D21)*
  - 50x Stellar Wheat *(Farm)* — single harvest (soil freed) → +2,750 G *(arrives morning D21)*
  - 1x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +4,600 G *(arrives morning D21)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 67 | 26,800 G | D23, D26, D29 | +23,450 G |
| Farm | **Carrop** | Lethe | 20 | 2,100 G | D21 | +200 G |
| Waterside | **Nectarcane** | Nemea | 1 | 370 G | D24, D27, D30 | +380 G |

- **Daily Seed Spent**: 29,270 G | **End-of-Day Wallet**: **720 G**

---

#### **Day 21**

- 📬 **Payout**: **+8,650 G** *(from 1x Islet Watermelon (pre-planted) on Day 20, 20x Nemean Tomato (pre-planted) on Day 20, 50x Stellar Wheat on Day 20)*
- **Morning Wallet**: **9,370 G** *(720 G carryover + 8,650 G)*
- 🌾 **Harvest & Ship**:
  - 13x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +3,250 G *(arrives morning D22)*
  - 20x Carrop *(Farm)* — single harvest (soil freed) → +2,300 G *(arrives morning D22)*
  - 43x Grass *(Farm)* — single harvest (soil freed) → +1,505 G *(arrives morning D22)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 98 | 5,390 G | D23 | +2,940 G |
| Farm | **Stellar Wheat** | Lethe | 26 | 1,040 G | D23 | +390 G |
| Farm | **Carrop** | Nemea | 5 | 475 G | D22 | +100 G |
| Farm | **Morrocorn** | Shatolla | 9 | 1,800 G | D25 | +1,800 G |

- **Daily Seed Spent**: 8,705 G | **End-of-Day Wallet**: **665 G**

---

#### **Day 22**

- 📬 **Payout**: **+7,055 G** *(from 13x Sudor Pepper on Day 21, 20x Carrop on Day 21, 43x Grass on Day 21)*
- **Morning Wallet**: **7,720 G** *(665 G carryover + 7,055 G)*
- 🌾 **Harvest & Ship**:
  - 5x Carrop *(Farm)* — single harvest (soil freed) → +575 G *(arrives morning D23)*
  - 73x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +18,250 G *(arrives morning D23)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 36 | 7,200 G | D26 | +7,200 G |

- **Daily Seed Spent**: 7,200 G | **End-of-Day Wallet**: **520 G**

---

#### **Day 23**

- 📬 **Payout**: **+18,825 G** *(from 73x Nectarcane on Day 22, 5x Carrop on Day 22)*
- **Morning Wallet**: **19,345 G** *(520 G carryover + 18,825 G)*
- 🌾 **Harvest & Ship**:
  - 67x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +16,750 G *(arrives morning D24)*
  - 98x Dress Lettuce *(Farm)* — single harvest (soil freed) → +8,330 G *(arrives morning D24)*
  - 26x Stellar Wheat *(Farm)* — single harvest (soil freed) → +1,430 G *(arrives morning D24)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Stellar Wheat** | Lethe | 59 | 2,360 G | D25 | +885 G |
| Farm | **Seatide Garlic** | Shatolla | 25 | 16,250 G | D29 | +8,750 G |

- **Daily Seed Spent**: 18,610 G | **End-of-Day Wallet**: **735 G**

---

#### **Day 24**

- 📬 **Payout**: **+26,510 G** *(from 67x Sudor Pepper on Day 23, 98x Dress Lettuce on Day 23, 26x Stellar Wheat on Day 23)*
- **Morning Wallet**: **27,245 G** *(735 G carryover + 26,510 G)*
- 🌾 **Harvest & Ship**:
  - 13x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +3,250 G *(arrives morning D25)*
  - 2x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +9,200 G *(arrives morning D25)*
  - 1x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +250 G *(arrives morning D25)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 40 | 26,000 G | D30 | +14,000 G |
| Waterside | **Honey Flower** | Shatolla | 2 | 760 G | D30 | +500 G |

- **Daily Seed Spent**: 26,760 G | **End-of-Day Wallet**: **485 G**

---

#### **Day 25**

- 📬 **Payout**: **+12,700 G** *(from 2x Islet Watermelon (pre-planted) on Day 24, 13x Sudor Pepper on Day 24, 1x Nectarcane on Day 24)*
- **Morning Wallet**: **13,185 G** *(485 G carryover + 12,700 G)*
- 🌾 **Harvest & Ship**:
  - 9x Morrocorn *(Farm)* — single harvest (soil freed) → +3,600 G *(arrives morning D26)*
  - 59x Stellar Wheat *(Farm)* — single harvest (soil freed) → +3,245 G *(arrives morning D26)*
  - 73x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +18,250 G *(arrives morning D26)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 46 | 10,580 G | D29 | +7,820 G |
| Farm | **Carrop** | Nemea | 21 | 1,995 G | D26 | +420 G |

- **Daily Seed Spent**: 12,575 G | **End-of-Day Wallet**: **610 G**

---

#### **Day 26**

- 📬 **Payout**: **+25,095 G** *(from 9x Morrocorn on Day 25, 73x Nectarcane on Day 25, 59x Stellar Wheat on Day 25)*
- **Morning Wallet**: **25,705 G** *(610 G carryover + 25,095 G)*
- 🌾 **Harvest & Ship**:
  - 67x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +16,750 G *(arrives morning D27)*
  - 21x Carrop *(Farm)* — single harvest (soil freed) → +2,415 G *(arrives morning D27)*
  - 36x Morrocorn *(Farm)* — single harvest (soil freed) → +14,400 G *(arrives morning D27)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 3 | 690 G | D30 | +510 G |
| Farm | **Morrocorn** | Shatolla | 54 | 10,800 G | D30 | +10,800 G |

- **Daily Seed Spent**: 11,490 G | **End-of-Day Wallet**: **14,215 G**

---

#### **Day 27**

- 📬 **Payout**: **+33,565 G** *(from 36x Morrocorn on Day 26, 67x Sudor Pepper on Day 26, 21x Carrop on Day 26)*
- **Morning Wallet**: **47,780 G** *(14,215 G carryover + 33,565 G)*
- 🌾 **Harvest & Ship**:
  - 13x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +3,250 G *(arrives morning D28)*
  - 1x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +250 G *(arrives morning D28)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **47,780 G**

---

#### **Day 28**

- 📬 **Payout**: **+3,500 G** *(from 13x Sudor Pepper on Day 27, 1x Nectarcane on Day 27)*
- **Morning Wallet**: **51,280 G** *(47,780 G carryover + 3,500 G)*
- 🌾 **Harvest & Ship**: 73x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +18,250 G *(arrives morning D29)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **51,280 G**

---

#### **Day 29**

- 📬 **Payout**: **+18,250 G** *(from 73x Nectarcane on Day 28)*
- **Morning Wallet**: **69,530 G** *(51,280 G carryover + 18,250 G)*
- 🌾 **Harvest & Ship**:
  - 67x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +16,750 G *(arrives morning D30)*
  - 46x Morrocorn *(Farm)* — single harvest (soil freed) → +18,400 G *(arrives morning D30)*
  - 25x Seatide Garlic *(Farm)* — single harvest (soil freed) → +25,000 G *(arrives morning D30)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 72 | 6,840 G | D30 | +1,440 G |

- **Daily Seed Spent**: 6,840 G | **End-of-Day Wallet**: **62,690 G**

---

#### **Day 30**

- 📬 **Payout**: **+60,150 G** *(from 25x Seatide Garlic on Day 29, 46x Morrocorn on Day 29, 67x Sudor Pepper on Day 29)*
- **Morning Wallet**: **122,840 G** *(62,690 G carryover + 60,150 G)*
- 🌾 **Harvest & Ship**:
  - 72x Carrop *(Farm)* — single harvest (soil freed) → +8,280 G *(arrives morning D31)*
  - 57x Morrocorn *(Farm)* — single harvest (soil freed) → +22,800 G *(arrives morning D31)*
  - 40x Seatide Garlic *(Farm)* — single harvest (soil freed) → +40,000 G *(arrives morning D31)*
  - 2x Honey Flower *(Waterside)* — single harvest (soil freed) → +1,260 G *(arrives morning D31)*
  - 4x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +18,400 G *(arrives morning D31)*
  - 1x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +250 G *(arrives morning D31)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **122,840 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+90,990 G** *(from Day 30 final harvest: 4x Islet Watermelon, 40x Seatide Garlic, 57x Morrocorn, 2x Honey Flower, 1x Nectarcane, 72x Carrop)*
- **Starting Budget**: 51,600 G
- **Total Season Net Profit**: **+162,230 G**
- 🏆 **Final Quietus Wallet**: **213,830 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 118 / 119 (expands to 170) (99.2% utilized, 1 idle)
- **Waterside Plots (Init)**: 77 / 78 (expands to 81) (98.7% utilized, 1 idle)
- **Cave Plots Used (Init)**: 13 / 81 (16.0% utilized, 68 idle)
- **Initial Capital Spent**: 51,140 G / 51,600 G (99.1% spent, 460 G leftover)
- **Pre-planted Crop Sales**: **+38,100 G**
- **New Planting Net Profit**: **+124,130 G**
- **Total Cumulative Season Net Profit**: **+162,230 G** across all restock stages
- **Final Projected Wallet**: **213,830 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
