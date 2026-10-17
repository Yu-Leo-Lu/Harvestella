# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 19
- **Planning Timeline**: Day 19 -> Day 30 (12d Quietus window)
- **Capital Budget**: 5,380 G
- **Plot Capacities**: Farm 0 -> 129 | Waterside 19 -> 48 | Cave 13

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Seatide Garlic** | 45 | Day 16 | D22 | Freed D22 | +45,000 G |
| Farm | **Carrop** | 37 | Day 19 | D20 | Freed D20 | +4,255 G |
| Farm | **Stellar Wheat** | 47 | Day 19 | D21 | Freed D21 | +2,585 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D23, D24, D25, D26, D27, D28 | Stays Planted *(Regrowth)* | +10,140 G |
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

- **Morning Wallet**: **5,380 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,380 G**

---

#### **Day 20**

- **Morning Wallet**: **5,380 G**
- 🌾 **Harvest & Ship**:
  - 37x Carrop *(Farm)* — single harvest (soil freed) → +4,255 G *(arrives morning D21)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 1/6 (stays planted) → +1,650 G *(arrives morning D21)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Stellar Wheat** | Lethe | 32 | 1,280 G | D22 | +480 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D24, D27, D30 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 1 | 370 G | D24, D27, D30 | +380 G |

- **Daily Seed Spent**: 5,350 G | **End-of-Day Wallet**: **30 G**

---

#### **Day 21**

- 📬 **Payout**: **+5,905 G** *(from 37x Carrop (pre-planted) on Day 20, 15x Shatollan Paprika (pre-planted) on Day 20)*
- **Morning Wallet**: **5,935 G** *(30 G carryover + 5,905 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 1/4 (stays planted) → +2,385 G *(arrives morning D22)*
  - 53x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +13,250 G *(arrives morning D22)*
  - 47x Stellar Wheat *(Farm)* — single harvest (soil freed) → +2,585 G *(arrives morning D22)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 13 | 5,200 G | D24, D27, D30 | +4,550 G |
| Farm | **Dress Lettuce** | Lethe | 13 | 715 G | D23 | +390 G |

- **Daily Seed Spent**: 5,915 G | **End-of-Day Wallet**: **20 G**

---

#### **Day 22**

- 📬 **Payout**: **+18,220 G** *(from 47x Stellar Wheat (pre-planted) on Day 21, 53x Sudor Pepper (pre-planted) on Day 21, 9x Revol Pepper (pre-planted) on Day 21)*
- **Morning Wallet**: **18,240 G** *(20 G carryover + 18,220 G)*
- 🌾 **Harvest & Ship**:
  - 45x Seatide Garlic *(Farm)* — single harvest (soil freed) → +45,000 G *(arrives morning D23)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 2/6 (stays planted) → +1,650 G *(arrives morning D23)*
  - 32x Stellar Wheat *(Farm)* — single harvest (soil freed) → +1,760 G *(arrives morning D23)*
  - 33x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +8,250 G *(arrives morning D23)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 23 | 1,265 G | D24 | +690 G |
| Farm | **Carrop** | Nemea | 43 | 4,085 G | D23 | +860 G |
| Farm | **Morrocorn** | Shatolla | 49 | 9,800 G | D26 | +9,800 G |

- **Daily Seed Spent**: 15,150 G | **End-of-Day Wallet**: **3,090 G**

---

#### **Day 23**

- 📬 **Payout**: **+56,660 G** *(from 45x Seatide Garlic (pre-planted) on Day 22, 15x Shatollan Paprika (pre-planted) on Day 22, 33x Nectarcane (pre-planted) on Day 22, 32x Stellar Wheat on Day 22)*
- **Morning Wallet**: **59,750 G** *(3,090 G carryover + 56,660 G)*
- 🌾 **Harvest & Ship**:
  - 43x Carrop *(Farm)* — single harvest (soil freed) → +4,945 G *(arrives morning D24)*
  - 13x Dress Lettuce *(Farm)* — single harvest (soil freed) → +1,105 G *(arrives morning D24)*
  - 26x Nemean Tomato *(Farm)* — regrowth 1/6 (stays planted) → +1,690 G *(arrives morning D24)*
  - 18x Honey Flower *(Waterside)* — single harvest (soil freed) → +11,340 G *(arrives morning D24)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 56 | 36,400 G | D29 | +19,600 G |

- **Daily Seed Spent**: 36,400 G | **End-of-Day Wallet**: **23,350 G**

---

#### **Day 24**

- 📬 **Payout**: **+19,080 G** *(from 26x Nemean Tomato (pre-planted) on Day 23, 18x Honey Flower (pre-planted) on Day 23, 43x Carrop on Day 23, 13x Dress Lettuce on Day 23)*
- **Morning Wallet**: **42,430 G** *(23,350 G carryover + 19,080 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 2/4 (stays planted) → +2,385 G *(arrives morning D25)*
  - 66x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +16,500 G *(arrives morning D25)*
  - 23x Dress Lettuce *(Farm)* — single harvest (soil freed) → +1,955 G *(arrives morning D25)*
  - 26x Nemean Tomato *(Farm)* — regrowth 2/6 (stays planted) → +1,690 G *(arrives morning D25)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 3/6 (stays planted) → +1,650 G *(arrives morning D25)*
  - 1x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +4,600 G *(arrives morning D25)*
  - 11x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +2,750 G *(arrives morning D25)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 23 | 14,950 G | D30 | +8,050 G |
| Waterside | **Honey Flower** | Shatolla | 27 | 10,260 G | D30 | +6,750 G |

- **Daily Seed Spent**: 25,210 G | **End-of-Day Wallet**: **17,220 G**

---

#### **Day 25**

- 📬 **Payout**: **+31,530 G** *(from 26x Nemean Tomato (pre-planted) on Day 24, 15x Shatollan Paprika (pre-planted) on Day 24, 1x Islet Watermelon (pre-planted) on Day 24, 66x Sudor Pepper (pre-planted) on Day 24, 9x Revol Pepper (pre-planted) on Day 24, 11x Nectarcane on Day 24, 23x Dress Lettuce on Day 24)*
- **Morning Wallet**: **48,750 G** *(17,220 G carryover + 31,530 G)*
- 🌾 **Harvest & Ship**:
  - 26x Nemean Tomato *(Farm)* — regrowth 3/6 (stays planted) → +1,690 G *(arrives morning D26)*
  - 33x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +8,250 G *(arrives morning D26)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **48,750 G**

---

#### **Day 26**

- 📬 **Payout**: **+9,940 G** *(from 26x Nemean Tomato (pre-planted) on Day 25, 33x Nectarcane (pre-planted) on Day 25)*
- **Morning Wallet**: **58,690 G** *(48,750 G carryover + 9,940 G)*
- 🌾 **Harvest & Ship**:
  - 49x Morrocorn *(Farm)* — single harvest (soil freed) → +19,600 G *(arrives morning D27)*
  - 26x Nemean Tomato *(Farm)* — regrowth 4/6 (stays planted) → +1,690 G *(arrives morning D27)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 4/6 (stays planted) → +1,650 G *(arrives morning D27)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 50 | 10,000 G | D30 | +10,000 G |

- **Daily Seed Spent**: 10,000 G | **End-of-Day Wallet**: **48,690 G**

---

#### **Day 27**

- 📬 **Payout**: **+22,940 G** *(from 26x Nemean Tomato (pre-planted) on Day 26, 15x Shatollan Paprika (pre-planted) on Day 26, 49x Morrocorn on Day 26)*
- **Morning Wallet**: **71,630 G** *(48,690 G carryover + 22,940 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 3/4 (stays planted) → +2,385 G *(arrives morning D28)*
  - 57x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +14,250 G *(arrives morning D28)*
  - 26x Nemean Tomato *(Farm)* — regrowth 5/6 (stays planted) → +1,690 G *(arrives morning D28)*
  - 11x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +2,750 G *(arrives morning D28)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **71,630 G**

---

#### **Day 28**

- 📬 **Payout**: **+21,075 G** *(from 26x Nemean Tomato (pre-planted) on Day 27, 57x Sudor Pepper (pre-planted) on Day 27, 9x Revol Pepper (pre-planted) on Day 27, 11x Nectarcane on Day 27)*
- **Morning Wallet**: **92,705 G** *(71,630 G carryover + 21,075 G)*
- 🌾 **Harvest & Ship**:
  - 26x Nemean Tomato *(Farm)* — regrowth 6/6 (stays planted) → +1,690 G *(arrives morning D29)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 5/6 (stays planted) → +1,650 G *(arrives morning D29)*
  - 4x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +18,400 G *(arrives morning D29)*
  - 33x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +8,250 G *(arrives morning D29)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **92,705 G**

---

#### **Day 29**

- 📬 **Payout**: **+29,990 G** *(from 26x Nemean Tomato (pre-planted) on Day 28, 15x Shatollan Paprika (pre-planted) on Day 28, 33x Nectarcane (pre-planted) on Day 28, 4x Islet Watermelon (pre-planted) on Day 28)*
- **Morning Wallet**: **122,695 G** *(92,705 G carryover + 29,990 G)*
- 🌾 **Harvest & Ship**: 56x Seatide Garlic *(Farm)* — single harvest (soil freed) → +56,000 G *(arrives morning D30)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 56 | 5,320 G | D30 | +1,120 G |

- **Daily Seed Spent**: 5,320 G | **End-of-Day Wallet**: **117,375 G**

---

#### **Day 30**

- 📬 **Payout**: **+56,000 G** *(from 56x Seatide Garlic on Day 29)*
- **Morning Wallet**: **173,375 G** *(117,375 G carryover + 56,000 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 4/4 (stays planted) → +2,385 G *(arrives morning D31)*
  - 13x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +3,250 G *(arrives morning D31)*
  - 56x Carrop *(Farm)* — single harvest (soil freed) → +6,440 G *(arrives morning D31)*
  - 50x Morrocorn *(Farm)* — single harvest (soil freed) → +20,000 G *(arrives morning D31)*
  - 23x Seatide Garlic *(Farm)* — single harvest (soil freed) → +23,000 G *(arrives morning D31)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 6/6 (stays planted) → +1,650 G *(arrives morning D31)*
  - 27x Honey Flower *(Waterside)* — single harvest (soil freed) → +17,010 G *(arrives morning D31)*
  - 6x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +27,600 G *(arrives morning D31)*
  - 11x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +2,750 G *(arrives morning D31)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **173,375 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+104,085 G** *(from Day 30 final harvest: 15x Shatollan Paprika, 6x Islet Watermelon, 9x Revol Pepper, 23x Seatide Garlic, 50x Morrocorn, 27x Honey Flower, 13x Sudor Pepper, 11x Nectarcane, 56x Carrop)*
- **Starting Budget**: 5,380 G
- **Total Season Net Profit**: **+272,080 G**
- 🏆 **Final Quietus Wallet**: **277,460 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 0 / 0 (expands to 129) (0.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 0 / 19 (expands to 48) (0.0% utilized, 19 idle)
- **Cave Plots Used (Init)**: 0 / 13 (0.0% utilized, 13 idle)
- **Initial Capital Spent**: 0 G / 5,380 G (0.0% spent, 5,380 G leftover)
- **Pre-planted Crop Sales**: **+205,610 G**
- **New Planting Net Profit**: **+66,470 G**
- **Total Cumulative Season Net Profit**: **+272,080 G** across all restock stages
- **Final Projected Wallet**: **277,460 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
