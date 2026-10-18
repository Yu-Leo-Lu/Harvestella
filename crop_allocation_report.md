# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 22
- **Planning Timeline**: Day 22 -> Day 30 (9d Quietus window)
- **Capital Budget**: 20,950 G
- **Plot Capacities**: Farm 29 -> 137 | Waterside 18 -> 29 | Cave 10

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 15 | Day 9 | D22, D24, D26, D28, D30 | Stays Planted *(Regrowth)* | +8,250 G |
| Farm | **Seatide Garlic** | 45 | Day 18 | D24 | Freed D24 | +45,000 G |
| Farm | **Nemean Tomato** | 26 | Day 18 | D23, D24, D25, D26, D27, D28 | Stays Planted *(Regrowth)* | +10,140 G |
| Farm | **Dress Lettuce** | 39 | Day 21 | D23 | Freed D23 | +3,315 G |
| Farm | **Seatide Garlic** | 24 | Day 21 | D27 | Freed D27 | +24,000 G |
| Waterside | **Islet Watermelon** | 1 | Day 12 | D24 | Freed D24 | +4,600 G |
| Waterside | **Islet Watermelon** | 4 | Day 16 | D28 | Freed D28 | +18,400 G |
| Waterside | **Islet Watermelon** | 6 | Day 18 | D30 | Freed D30 | +27,600 G |
| Waterside | **Nectarcane** | 33 | Day 18 | D22, D25, D28 | Stays Planted *(Regrowth)* | +24,750 G |
| Waterside | **Nectarcane** | 10 | Day 19 | D23, D26, D29 | Stays Planted *(Regrowth)* | +7,500 G |
| Waterside | **Nectarcane** | 9 | Day 20 | D24, D27, D30 | Stays Planted *(Regrowth)* | +6,750 G |
| Cave | **Revol Pepper** | 9 | Day 14 | D24, D27, D30 | Stays Planted *(Regrowth)* | +7,155 G |
| Cave | **Sudor Pepper** | 44 | Day 18 | D24, D27 | Stays Planted *(Regrowth)* | +22,000 G |
| Cave | **Sudor Pepper** | 10 | Day 21 | D24, D27, D30 | Stays Planted *(Regrowth)* | +7,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 22**

- **Morning Wallet**: **20,950 G**
- 🌾 **Harvest & Ship**:
  - 15x Shatollan Paprika *(Farm)* — regrowth 1/5 (stays planted) → +1,650 G *(arrives morning D23)*
  - 33x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +8,250 G *(arrives morning D23)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Curry Herbs** | Argene | 10 | 2,400 G | D28 | +1,100 G |
| Farm | **Morrocorn** | Shatolla | 29 | 5,800 G | D26 | +5,800 G |

- **Daily Seed Spent**: 8,200 G | **End-of-Day Wallet**: **12,750 G**
- **Plots Left**: Farm: 0 | Waterside: 18 | Cave: 0

---

#### **Day 23**

- 📬 **Payout**: **+9,900 G** *(from 15x Shatollan Paprika (pre-planted) on Day 22, 33x Nectarcane (pre-planted) on Day 22)*
- **Morning Wallet**: **22,650 G** *(12,750 G carryover + 9,900 G)*
- 🌾 **Harvest & Ship**:
  - 39x Dress Lettuce *(Farm)* — single harvest (soil freed) → +3,315 G *(arrives morning D24)*
  - 26x Nemean Tomato *(Farm)* — regrowth 1/6 (stays planted) → +1,690 G *(arrives morning D24)*
  - 10x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +2,500 G *(arrives morning D24)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 39 | 2,145 G | D25 | +1,170 G |

- **Daily Seed Spent**: 2,145 G | **End-of-Day Wallet**: **20,505 G**
- **Plots Left**: Farm: 0 | Waterside: 18 | Cave: 0

---

#### **Day 24**

- 📬 **Payout**: **+7,505 G** *(from 26x Nemean Tomato (pre-planted) on Day 23, 39x Dress Lettuce (pre-planted) on Day 23, 10x Nectarcane (pre-planted) on Day 23)*
- **Morning Wallet**: **28,010 G** *(20,505 G carryover + 7,505 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 1/3 (stays planted) → +2,385 G *(arrives morning D25)*
  - 54x Sudor Pepper *(Cave)* — regrowth 1/2 (stays planted) → +13,500 G *(arrives morning D25)*
  - 26x Nemean Tomato *(Farm)* — regrowth 2/6 (stays planted) → +1,690 G *(arrives morning D25)*
  - 45x Seatide Garlic *(Farm)* — single harvest (soil freed) → +45,000 G *(arrives morning D25)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 2/5 (stays planted) → +1,650 G *(arrives morning D25)*
  - 1x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +4,600 G *(arrives morning D25)*
  - 9x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +2,250 G *(arrives morning D25)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 14 | 770 G | D26 | +420 G |
| Farm | **Seatide Garlic** | Shatolla | 31 | 20,150 G | D30 | +10,850 G |
| Waterside | **Honey Flower** | Shatolla | 18 | 6,840 G | D30 | +4,500 G |

- **Daily Seed Spent**: 27,760 G | **End-of-Day Wallet**: **250 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 25**

- 📬 **Payout**: **+71,075 G** *(from 15x Shatollan Paprika (pre-planted) on Day 24, 45x Seatide Garlic (pre-planted) on Day 24, 26x Nemean Tomato (pre-planted) on Day 24, 1x Islet Watermelon (pre-planted) on Day 24, 9x Nectarcane (pre-planted) on Day 24, 9x Revol Pepper (pre-planted) on Day 24, 54x Sudor Pepper (pre-planted) on Day 24)*
- **Morning Wallet**: **71,325 G** *(250 G carryover + 71,075 G)*
- 🌾 **Harvest & Ship**:
  - 39x Dress Lettuce *(Farm)* — single harvest (soil freed) → +3,315 G *(arrives morning D26)*
  - 26x Nemean Tomato *(Farm)* — regrowth 3/6 (stays planted) → +1,690 G *(arrives morning D26)*
  - 33x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +8,250 G *(arrives morning D26)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 39 | 3,705 G | D26 | +780 G |

- **Daily Seed Spent**: 3,705 G | **End-of-Day Wallet**: **67,620 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 26**

- 📬 **Payout**: **+13,255 G** *(from 26x Nemean Tomato (pre-planted) on Day 25, 33x Nectarcane (pre-planted) on Day 25, 39x Dress Lettuce on Day 25)*
- **Morning Wallet**: **80,875 G** *(67,620 G carryover + 13,255 G)*
- 🌾 **Harvest & Ship**:
  - 39x Carrop *(Farm)* — single harvest (soil freed) → +4,485 G *(arrives morning D27)*
  - 14x Dress Lettuce *(Farm)* — single harvest (soil freed) → +1,190 G *(arrives morning D27)*
  - 29x Morrocorn *(Farm)* — single harvest (soil freed) → +11,600 G *(arrives morning D27)*
  - 26x Nemean Tomato *(Farm)* — regrowth 4/6 (stays planted) → +1,690 G *(arrives morning D27)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 3/5 (stays planted) → +1,650 G *(arrives morning D27)*
  - 10x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +2,500 G *(arrives morning D27)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 12 | 2,760 G | D30 | +2,040 G |
| Farm | **Morrocorn** | Shatolla | 70 | 14,000 G | D30 | +14,000 G |

- **Daily Seed Spent**: 16,760 G | **End-of-Day Wallet**: **64,115 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 27**

- 📬 **Payout**: **+23,115 G** *(from 15x Shatollan Paprika (pre-planted) on Day 26, 26x Nemean Tomato (pre-planted) on Day 26, 10x Nectarcane (pre-planted) on Day 26, 29x Morrocorn on Day 26, 39x Carrop on Day 26, 14x Dress Lettuce on Day 26)*
- **Morning Wallet**: **87,230 G** *(64,115 G carryover + 23,115 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 2/3 (stays planted) → +2,385 G *(arrives morning D28)*
  - 54x Sudor Pepper *(Cave)* — regrowth 2/2 (stays planted) → +13,500 G *(arrives morning D28)*
  - 26x Nemean Tomato *(Farm)* — regrowth 5/6 (stays planted) → +1,690 G *(arrives morning D28)*
  - 24x Seatide Garlic *(Farm)* — single harvest (soil freed) → +24,000 G *(arrives morning D28)*
  - 9x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +2,250 G *(arrives morning D28)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D29 | +180 G |
| Farm | **Carrop** | Nemea | 18 | 1,710 G | D28 | +360 G |

- **Daily Seed Spent**: 2,040 G | **End-of-Day Wallet**: **85,190 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 28**

- 📬 **Payout**: **+43,825 G** *(from 26x Nemean Tomato (pre-planted) on Day 27, 24x Seatide Garlic (pre-planted) on Day 27, 9x Nectarcane (pre-planted) on Day 27, 9x Revol Pepper (pre-planted) on Day 27, 54x Sudor Pepper (pre-planted) on Day 27)*
- **Morning Wallet**: **129,015 G** *(85,190 G carryover + 43,825 G)*
- 🌾 **Harvest & Ship**:
  - 10x Curry Herbs *(Cave)* — single harvest (soil freed) → +3,500 G *(arrives morning D29)*
  - 18x Carrop *(Farm)* — single harvest (soil freed) → +2,070 G *(arrives morning D29)*
  - 26x Nemean Tomato *(Farm)* — regrowth 6/6 (stays planted) → +1,690 G *(arrives morning D29)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 4/5 (stays planted) → +1,650 G *(arrives morning D29)*
  - 4x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +18,400 G *(arrives morning D29)*
  - 33x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +8,250 G *(arrives morning D29)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 18 | 1,710 G | D29 | +360 G |

- **Daily Seed Spent**: 1,710 G | **End-of-Day Wallet**: **127,305 G**
- **Plots Left**: Farm: 0 | Waterside: 5 | Cave: 10

---

#### **Day 29**

- 📬 **Payout**: **+35,560 G** *(from 15x Shatollan Paprika (pre-planted) on Day 28, 26x Nemean Tomato (pre-planted) on Day 28, 4x Islet Watermelon (pre-planted) on Day 28, 33x Nectarcane (pre-planted) on Day 28, 18x Carrop on Day 28, 10x Curry Herbs on Day 28)*
- **Morning Wallet**: **162,865 G** *(127,305 G carryover + 35,560 G)*
- 🌾 **Harvest & Ship**:
  - 18x Carrop *(Farm)* — single harvest (soil freed) → +2,070 G *(arrives morning D30)*
  - 6x Dress Lettuce *(Farm)* — single harvest (soil freed) → +510 G *(arrives morning D30)*
  - 10x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +2,500 G *(arrives morning D30)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 24 | 2,280 G | D30 | +480 G |

- **Daily Seed Spent**: 2,280 G | **End-of-Day Wallet**: **160,585 G**
- **Plots Left**: Farm: 0 | Waterside: 5 | Cave: 10

---

#### **Day 30**

- 📬 **Payout**: **+5,080 G** *(from 10x Nectarcane (pre-planted) on Day 29, 18x Carrop on Day 29, 6x Dress Lettuce on Day 29)*
- **Morning Wallet**: **165,665 G** *(160,585 G carryover + 5,080 G)*
- 🌾 **Harvest & Ship**:
  - 9x Revol Pepper *(Cave)* — regrowth 3/3 (stays planted) → +2,385 G *(arrives morning D31)*
  - 10x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +2,500 G *(arrives morning D31)*
  - 24x Carrop *(Farm)* — single harvest (soil freed) → +2,760 G *(arrives morning D31)*
  - 82x Morrocorn *(Farm)* — single harvest (soil freed) → +32,800 G *(arrives morning D31)*
  - 31x Seatide Garlic *(Farm)* — single harvest (soil freed) → +31,000 G *(arrives morning D31)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 5/5 (stays planted) → +1,650 G *(arrives morning D31)*
  - 18x Honey Flower *(Waterside)* — single harvest (soil freed) → +11,340 G *(arrives morning D31)*
  - 6x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +27,600 G *(arrives morning D31)*
  - 9x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +2,250 G *(arrives morning D31)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **165,665 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+114,285 G** *(from Day 30 final harvest: 15x Shatollan Paprika, 6x Islet Watermelon, 9x Nectarcane, 9x Revol Pepper, 10x Sudor Pepper, 31x Seatide Garlic, 82x Morrocorn, 18x Honey Flower, 24x Carrop)*
- **Starting Budget**: 20,950 G
- **Total Season Net Profit**: **+259,000 G**
- 🏆 **Final Quietus Wallet**: **279,950 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 29 / 29 (expands to 137) (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 0 / 18 (expands to 29) (0.0% utilized, 18 idle)
- **Cave Plots Used (Init)**: 10 / 10 (100.0% utilized, 0 idle)
- **Initial Capital Spent**: 8,200 G / 20,950 G (39.1% spent, 12,750 G leftover)
- **Pre-planted Crop Sales**: **+216,960 G**
- **New Planting Net Profit**: **+42,040 G**
- **Total Cumulative Season Net Profit**: **+259,000 G** across all restock stages
- **Final Projected Wallet**: **279,950 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
