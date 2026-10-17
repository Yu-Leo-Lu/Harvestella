# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 19
- **Planning Timeline**: Day 19 -> Day 30 (12d Quietus window)
- **Capital Budget**: 24,415 G
- **Plot Capacities**: Farm 0 -> 129 | Waterside 19 -> 48 | Cave 13

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Seatide Garlic** | 45 | Day 16 | D22 | Freed D22 | +45,000 G |
| Farm | **Carrop** | 37 | Day 19 | D20 | Freed D20 | +4,255 G |
| Farm | **Stellar Wheat** | 47 | Day 19 | D21 | Freed D21 | +2,585 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D23, D24, D25, D26, D27, D28 | Stays Planted *(Regrowth)* | +10,140 G |
| Farm | **Nemean Tomato** | 6 | Day 10 | D19, D20 | Stays Planted *(Regrowth)* | +780 G |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D20, D22, D24, D26, D28, D30 | Stays Planted *(Regrowth)* | +9,900 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D22, D25, D28 | Stays Planted *(Regrowth)* | +24,750 G |
| Waterside | **Honey Flower** | 18 | Day 17 | D23 | Freed D23 | +11,340 G |
| Waterside | **Islet Watermelon** | 6 | Day 18 | D30 | Freed D30 | +27,600 G |
| Waterside | **Islet Watermelon** | 4 | Day 16 | D28 | Freed D28 | +18,400 G |
| Waterside | **Islet Watermelon** | 1 | Day 12 | D24 | Freed D24 | +4,600 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D21, D24, D27 | Stays Planted *(Regrowth)* | +33,000 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D21, D24, D27, D30 | Stays Planted *(Regrowth)* | +9,540 G |
| Cave | **Sudor Pepper** | 9 | Day 15 | D21, D24 | Stays Planted *(Regrowth)* | +4,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 19**

- **Morning Wallet**: **24,415 G**
- 🌾 **Harvest & Ship**: 6x Nemean Tomato *(Farm)* — regrowth 1/2 (stays planted) → +390 G *(arrives morning D20)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **24,415 G**

---

#### **Day 20**

- 📬 **Payout**: **+390 G** *(from 6x Nemean Tomato (pre-planted) on Day 19)*
- **Morning Wallet**: **24,805 G** *(24,415 G carryover + 390 G)*
- 🌾 **Harvest & Ship**:
  - 37x Carrop *(Farm)* — single harvest (soil freed) → +4,255 G *(arrives morning D21)*
  - 6x Nemean Tomato *(Farm)* — regrowth 2/2 (stays planted) → +390 G *(arrives morning D21)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 1/6 (stays planted) → +1,650 G *(arrives morning D21)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 2 | 800 G | D23, D26, D29 | +700 G |
| Farm | **Stellar Wheat** | Lethe | 12 | 480 G | D22 | +180 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D24, D27, D30 | +3,800 G |
| Farm | **Seatide Garlic** | Shatolla | 25 | 16,250 G | D26 | +8,750 G |
| Waterside | **Nectarcane** | Shatolla | 9 | 3,330 G | D24, D27, D30 | +3,420 G |

- **Daily Seed Spent**: 24,560 G | **End-of-Day Wallet**: **245 G**

---

#### **Day 21**

- 📬 **Payout**: **+6,295 G** *(from 37x Carrop (pre-planted) on Day 20, 6x Nemean Tomato (pre-planted) on Day 20, 15x Shatollan Paprika (pre-planted) on Day 20)*
- **Morning Wallet**: **6,540 G** *(245 G carryover + 6,295 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 1/4 (stays planted) → +2,385 G *(arrives morning D22)*
  - 53x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +13,250 G *(arrives morning D22)*
  - 47x Stellar Wheat *(Farm)* — single harvest (soil freed) → +2,585 G *(arrives morning D22)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 11 | 4,400 G | D24, D27, D30 | +3,850 G |
| Farm | **Dress Lettuce** | Lethe | 35 | 1,925 G | D23 | +1,050 G |

- **Daily Seed Spent**: 6,325 G | **End-of-Day Wallet**: **215 G**

---

#### **Day 22**

- 📬 **Payout**: **+18,220 G** *(from 47x Stellar Wheat (pre-planted) on Day 21, 53x Sudor Pepper (pre-planted) on Day 21, 9x Revol Pepper (pre-planted) on Day 21)*
- **Morning Wallet**: **18,435 G** *(215 G carryover + 18,220 G)*
- 🌾 **Harvest & Ship**:
  - 45x Seatide Garlic *(Farm)* — single harvest (soil freed) → +45,000 G *(arrives morning D23)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 2/6 (stays planted) → +1,650 G *(arrives morning D23)*
  - 12x Stellar Wheat *(Farm)* — single harvest (soil freed) → +660 G *(arrives morning D23)*
  - 33x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +8,250 G *(arrives morning D23)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 32 | 3,040 G | D23 | +640 G |
| Farm | **Morrocorn** | Shatolla | 37 | 7,400 G | D26 | +7,400 G |

- **Daily Seed Spent**: 10,440 G | **End-of-Day Wallet**: **7,995 G**

---

#### **Day 23**

- 📬 **Payout**: **+55,560 G** *(from 45x Seatide Garlic (pre-planted) on Day 22, 15x Shatollan Paprika (pre-planted) on Day 22, 33x Nectarcane (pre-planted) on Day 22, 12x Stellar Wheat on Day 22)*
- **Morning Wallet**: **63,555 G** *(7,995 G carryover + 55,560 G)*
- 🌾 **Harvest & Ship**:
  - 2x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +500 G *(arrives morning D24)*
  - 32x Carrop *(Farm)* — single harvest (soil freed) → +3,680 G *(arrives morning D24)*
  - 35x Dress Lettuce *(Farm)* — single harvest (soil freed) → +2,975 G *(arrives morning D24)*
  - 26x Nemean Tomato *(Farm)* — regrowth 1/6 (stays planted) → +1,690 G *(arrives morning D24)*
  - 18x Honey Flower *(Waterside)* — single harvest (soil freed) → +11,340 G *(arrives morning D24)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 67 | 43,550 G | D29 | +23,450 G |

- **Daily Seed Spent**: 43,550 G | **End-of-Day Wallet**: **20,005 G**

---

#### **Day 24**

- 📬 **Payout**: **+20,185 G** *(from 26x Nemean Tomato (pre-planted) on Day 23, 18x Honey Flower (pre-planted) on Day 23, 2x Sudor Pepper on Day 23, 32x Carrop on Day 23, 35x Dress Lettuce on Day 23)*
- **Morning Wallet**: **40,190 G** *(20,005 G carryover + 20,185 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 2/4 (stays planted) → +2,385 G *(arrives morning D25)*
  - 64x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +16,000 G *(arrives morning D25)*
  - 26x Nemean Tomato *(Farm)* — regrowth 2/6 (stays planted) → +1,690 G *(arrives morning D25)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 3/6 (stays planted) → +1,650 G *(arrives morning D25)*
  - 1x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +4,600 G *(arrives morning D25)*
  - 19x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +4,750 G *(arrives morning D25)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Honey Flower** | Shatolla | 19 | 7,220 G | D30 | +4,750 G |

- **Daily Seed Spent**: 7,220 G | **End-of-Day Wallet**: **32,970 G**

---

#### **Day 25**

- 📬 **Payout**: **+31,075 G** *(from 26x Nemean Tomato (pre-planted) on Day 24, 15x Shatollan Paprika (pre-planted) on Day 24, 1x Islet Watermelon (pre-planted) on Day 24, 64x Sudor Pepper (pre-planted) on Day 24, 9x Revol Pepper (pre-planted) on Day 24, 19x Nectarcane on Day 24)*
- **Morning Wallet**: **64,045 G** *(32,970 G carryover + 31,075 G)*
- 🌾 **Harvest & Ship**:
  - 26x Nemean Tomato *(Farm)* — regrowth 3/6 (stays planted) → +1,690 G *(arrives morning D26)*
  - 33x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +8,250 G *(arrives morning D26)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **64,045 G**

---

#### **Day 26**

- 📬 **Payout**: **+9,940 G** *(from 26x Nemean Tomato (pre-planted) on Day 25, 33x Nectarcane (pre-planted) on Day 25)*
- **Morning Wallet**: **73,985 G** *(64,045 G carryover + 9,940 G)*
- 🌾 **Harvest & Ship**:
  - 2x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +500 G *(arrives morning D27)*
  - 37x Morrocorn *(Farm)* — single harvest (soil freed) → +14,800 G *(arrives morning D27)*
  - 26x Nemean Tomato *(Farm)* — regrowth 4/6 (stays planted) → +1,690 G *(arrives morning D27)*
  - 25x Seatide Garlic *(Farm)* — single harvest (soil freed) → +25,000 G *(arrives morning D27)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 4/6 (stays planted) → +1,650 G *(arrives morning D27)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 62 | 12,400 G | D30 | +12,400 G |

- **Daily Seed Spent**: 12,400 G | **End-of-Day Wallet**: **61,585 G**

---

#### **Day 27**

- 📬 **Payout**: **+43,640 G** *(from 26x Nemean Tomato (pre-planted) on Day 26, 15x Shatollan Paprika (pre-planted) on Day 26, 25x Seatide Garlic on Day 26, 37x Morrocorn on Day 26, 2x Sudor Pepper on Day 26)*
- **Morning Wallet**: **105,225 G** *(61,585 G carryover + 43,640 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 3/4 (stays planted) → +2,385 G *(arrives morning D28)*
  - 55x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +13,750 G *(arrives morning D28)*
  - 26x Nemean Tomato *(Farm)* — regrowth 5/6 (stays planted) → +1,690 G *(arrives morning D28)*
  - 19x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +4,750 G *(arrives morning D28)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **105,225 G**

---

#### **Day 28**

- 📬 **Payout**: **+22,575 G** *(from 26x Nemean Tomato (pre-planted) on Day 27, 55x Sudor Pepper (pre-planted) on Day 27, 9x Revol Pepper (pre-planted) on Day 27, 19x Nectarcane on Day 27)*
- **Morning Wallet**: **127,800 G** *(105,225 G carryover + 22,575 G)*
- 🌾 **Harvest & Ship**:
  - 26x Nemean Tomato *(Farm)* — regrowth 6/6 (stays planted) → +1,690 G *(arrives morning D29)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 5/6 (stays planted) → +1,650 G *(arrives morning D29)*
  - 4x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +18,400 G *(arrives morning D29)*
  - 33x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +8,250 G *(arrives morning D29)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **127,800 G**

---

#### **Day 29**

- 📬 **Payout**: **+29,990 G** *(from 26x Nemean Tomato (pre-planted) on Day 28, 15x Shatollan Paprika (pre-planted) on Day 28, 33x Nectarcane (pre-planted) on Day 28, 4x Islet Watermelon (pre-planted) on Day 28)*
- **Morning Wallet**: **157,790 G** *(127,800 G carryover + 29,990 G)*
- 🌾 **Harvest & Ship**:
  - 2x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +500 G *(arrives morning D30)*
  - 67x Seatide Garlic *(Farm)* — single harvest (soil freed) → +67,000 G *(arrives morning D30)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 67 | 6,365 G | D30 | +1,340 G |

- **Daily Seed Spent**: 6,365 G | **End-of-Day Wallet**: **151,425 G**

---

#### **Day 30**

- 📬 **Payout**: **+67,500 G** *(from 67x Seatide Garlic on Day 29, 2x Sudor Pepper on Day 29)*
- **Morning Wallet**: **218,925 G** *(151,425 G carryover + 67,500 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 4/4 (stays planted) → +2,385 G *(arrives morning D31)*
  - 11x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +2,750 G *(arrives morning D31)*
  - 67x Carrop *(Farm)* — single harvest (soil freed) → +7,705 G *(arrives morning D31)*
  - 62x Morrocorn *(Farm)* — single harvest (soil freed) → +24,800 G *(arrives morning D31)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 6/6 (stays planted) → +1,650 G *(arrives morning D31)*
  - 19x Honey Flower *(Waterside)* — single harvest (soil freed) → +11,970 G *(arrives morning D31)*
  - 6x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +27,600 G *(arrives morning D31)*
  - 19x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +4,750 G *(arrives morning D31)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **218,925 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+83,610 G** *(from Day 30 final harvest: 15x Shatollan Paprika, 6x Islet Watermelon, 9x Revol Pepper, 62x Morrocorn, 19x Honey Flower, 11x Sudor Pepper, 19x Nectarcane, 67x Carrop)*
- **Starting Budget**: 24,415 G
- **Total Season Net Profit**: **+278,120 G**
- 🏆 **Final Quietus Wallet**: **302,535 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 0 / 0 (expands to 129) (0.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 0 / 19 (expands to 48) (0.0% utilized, 19 idle)
- **Cave Plots Used (Init)**: 0 / 13 (0.0% utilized, 13 idle)
- **Initial Capital Spent**: 0 G / 24,415 G (0.0% spent, 24,415 G leftover)
- **Pre-planted Crop Sales**: **+206,390 G**
- **New Planting Net Profit**: **+71,730 G**
- **Total Cumulative Season Net Profit**: **+278,120 G** across all restock stages
- **Final Projected Wallet**: **302,535 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
