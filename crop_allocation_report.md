# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 19
- **Planning Timeline**: Day 19 -> Day 30 (12d Quietus window)
- **Capital Budget**: 51,104 G
- **Plot Capacities**: Farm 0 -> 129 | Waterside 19 -> 48 | Cave 16

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
| Cave | **Revol Pepper** | 6 | Day 14 | D21, D24, D27, D30 | Stays Planted *(Regrowth)* | +6,360 G |
| Cave | **Sudor Pepper** | 9 | Day 15 | D21, D24 | Stays Planted *(Regrowth)* | +4,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 19**

- **Morning Wallet**: **51,104 G**
- 🌾 **Harvest & Ship**: 6x Nemean Tomato *(Farm)* — regrowth 1/2 (stays planted) → +390 G *(arrives morning D20)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D23, D26, D29 | +3,800 G |

- **Daily Seed Spent**: 3,700 G | **End-of-Day Wallet**: **47,404 G**

---

#### **Day 20**

- 📬 **Payout**: **+390 G** *(from 6x Nemean Tomato (pre-planted) on Day 19)*
- **Morning Wallet**: **47,794 G** *(47,404 G carryover + 390 G)*
- 🌾 **Harvest & Ship**:
  - 37x Carrop *(Farm)* — single harvest (soil freed) → +4,255 G *(arrives morning D21)*
  - 6x Nemean Tomato *(Farm)* — regrowth 2/2 (stays planted) → +390 G *(arrives morning D21)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 1/6 (stays planted) → +1,650 G *(arrives morning D21)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 37 | 24,050 G | D26 | +12,950 G |
| Waterside | **Nectarcane** | Shatolla | 9 | 3,330 G | D24, D27, D30 | +3,420 G |

- **Daily Seed Spent**: 27,380 G | **End-of-Day Wallet**: **20,414 G**

---

#### **Day 21**

- 📬 **Payout**: **+6,295 G** *(from 37x Carrop (pre-planted) on Day 20, 6x Nemean Tomato (pre-planted) on Day 20, 15x Shatollan Paprika (pre-planted) on Day 20)*
- **Morning Wallet**: **26,709 G** *(20,414 G carryover + 6,295 G)*
- 🌾 **Harvest & Ship**:
  - 6x Revol Pepper *(Cave)* — regrowth 1/4 (stays planted) → +1,590 G *(arrives morning D22)*
  - 53x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +13,250 G *(arrives morning D22)*
  - 47x Stellar Wheat *(Farm)* — single harvest (soil freed) → +2,585 G *(arrives morning D22)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 16 | 6,400 G | D24, D27, D30 | +5,600 G |
| Farm | **Morrocorn** | Shatolla | 23 | 4,600 G | D25 | +4,600 G |
| Farm | **Seatide Garlic** | Shatolla | 24 | 15,600 G | D27 | +8,400 G |

- **Daily Seed Spent**: 26,600 G | **End-of-Day Wallet**: **109 G**

---

#### **Day 22**

- 📬 **Payout**: **+17,425 G** *(from 47x Stellar Wheat (pre-planted) on Day 21, 53x Sudor Pepper (pre-planted) on Day 21, 6x Revol Pepper (pre-planted) on Day 21)*
- **Morning Wallet**: **17,534 G** *(109 G carryover + 17,425 G)*
- 🌾 **Harvest & Ship**:
  - 45x Seatide Garlic *(Farm)* — single harvest (soil freed) → +45,000 G *(arrives morning D23)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 2/6 (stays planted) → +1,650 G *(arrives morning D23)*
  - 33x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +8,250 G *(arrives morning D23)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 11 | 605 G | D24 | +330 G |
| Farm | **Carrop** | Nemea | 3 | 285 G | D23 | +60 G |
| Farm | **Morrocorn** | Shatolla | 8 | 1,600 G | D26 | +1,600 G |
| Farm | **Seatide Garlic** | Shatolla | 23 | 14,950 G | D28 | +8,050 G |

- **Daily Seed Spent**: 17,440 G | **End-of-Day Wallet**: **94 G**

---

#### **Day 23**

- 📬 **Payout**: **+54,900 G** *(from 45x Seatide Garlic (pre-planted) on Day 22, 15x Shatollan Paprika (pre-planted) on Day 22, 33x Nectarcane (pre-planted) on Day 22)*
- **Morning Wallet**: **54,994 G** *(94 G carryover + 54,900 G)*
- 🌾 **Harvest & Ship**:
  - 3x Carrop *(Farm)* — single harvest (soil freed) → +345 G *(arrives morning D24)*
  - 26x Nemean Tomato *(Farm)* — regrowth 1/6 (stays planted) → +1,690 G *(arrives morning D24)*
  - 18x Honey Flower *(Waterside)* — single harvest (soil freed) → +11,340 G *(arrives morning D24)*
  - 10x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +2,500 G *(arrives morning D24)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 3 | 285 G | D24 | +60 G |
| Waterside | **Honey Flower** | Shatolla | 18 | 6,840 G | D29 | +4,500 G |

- **Daily Seed Spent**: 7,125 G | **End-of-Day Wallet**: **47,869 G**

---

#### **Day 24**

- 📬 **Payout**: **+15,875 G** *(from 26x Nemean Tomato (pre-planted) on Day 23, 18x Honey Flower (pre-planted) on Day 23, 10x Nectarcane on Day 23, 3x Carrop on Day 23)*
- **Morning Wallet**: **63,744 G** *(47,869 G carryover + 15,875 G)*
- 🌾 **Harvest & Ship**:
  - 6x Revol Pepper *(Cave)* — regrowth 2/4 (stays planted) → +1,590 G *(arrives morning D25)*
  - 69x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +17,250 G *(arrives morning D25)*
  - 3x Carrop *(Farm)* — single harvest (soil freed) → +345 G *(arrives morning D25)*
  - 11x Dress Lettuce *(Farm)* — single harvest (soil freed) → +935 G *(arrives morning D25)*
  - 26x Nemean Tomato *(Farm)* — regrowth 2/6 (stays planted) → +1,690 G *(arrives morning D25)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 3/6 (stays planted) → +1,650 G *(arrives morning D25)*
  - 1x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +4,600 G *(arrives morning D25)*
  - 9x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +2,250 G *(arrives morning D25)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 14 | 9,100 G | D30 | +4,900 G |
| Waterside | **Honey Flower** | Shatolla | 1 | 380 G | D30 | +250 G |

- **Daily Seed Spent**: 9,480 G | **End-of-Day Wallet**: **54,264 G**

---

#### **Day 25**

- 📬 **Payout**: **+30,310 G** *(from 26x Nemean Tomato (pre-planted) on Day 24, 15x Shatollan Paprika (pre-planted) on Day 24, 1x Islet Watermelon (pre-planted) on Day 24, 69x Sudor Pepper (pre-planted) on Day 24, 6x Revol Pepper (pre-planted) on Day 24, 9x Nectarcane on Day 24, 3x Carrop on Day 24, 11x Dress Lettuce on Day 24)*
- **Morning Wallet**: **84,574 G** *(54,264 G carryover + 30,310 G)*
- 🌾 **Harvest & Ship**:
  - 23x Morrocorn *(Farm)* — single harvest (soil freed) → +9,200 G *(arrives morning D26)*
  - 26x Nemean Tomato *(Farm)* — regrowth 3/6 (stays planted) → +1,690 G *(arrives morning D26)*
  - 33x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +8,250 G *(arrives morning D26)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 23 | 4,600 G | D29 | +4,600 G |

- **Daily Seed Spent**: 4,600 G | **End-of-Day Wallet**: **79,974 G**

---

#### **Day 26**

- 📬 **Payout**: **+19,140 G** *(from 26x Nemean Tomato (pre-planted) on Day 25, 33x Nectarcane (pre-planted) on Day 25, 23x Morrocorn on Day 25)*
- **Morning Wallet**: **99,114 G** *(79,974 G carryover + 19,140 G)*
- 🌾 **Harvest & Ship**:
  - 8x Morrocorn *(Farm)* — single harvest (soil freed) → +3,200 G *(arrives morning D27)*
  - 26x Nemean Tomato *(Farm)* — regrowth 4/6 (stays planted) → +1,690 G *(arrives morning D27)*
  - 37x Seatide Garlic *(Farm)* — single harvest (soil freed) → +37,000 G *(arrives morning D27)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 4/6 (stays planted) → +1,650 G *(arrives morning D27)*
  - 10x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +2,500 G *(arrives morning D27)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 45 | 9,000 G | D30 | +9,000 G |

- **Daily Seed Spent**: 9,000 G | **End-of-Day Wallet**: **90,114 G**

---

#### **Day 27**

- 📬 **Payout**: **+46,040 G** *(from 26x Nemean Tomato (pre-planted) on Day 26, 15x Shatollan Paprika (pre-planted) on Day 26, 37x Seatide Garlic on Day 26, 8x Morrocorn on Day 26, 10x Nectarcane on Day 26)*
- **Morning Wallet**: **136,154 G** *(90,114 G carryover + 46,040 G)*
- 🌾 **Harvest & Ship**:
  - 6x Revol Pepper *(Cave)* — regrowth 3/4 (stays planted) → +1,590 G *(arrives morning D28)*
  - 60x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +15,000 G *(arrives morning D28)*
  - 26x Nemean Tomato *(Farm)* — regrowth 5/6 (stays planted) → +1,690 G *(arrives morning D28)*
  - 24x Seatide Garlic *(Farm)* — single harvest (soil freed) → +24,000 G *(arrives morning D28)*
  - 9x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +2,250 G *(arrives morning D28)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 24 | 1,320 G | D29 | +720 G |

- **Daily Seed Spent**: 1,320 G | **End-of-Day Wallet**: **134,834 G**

---

#### **Day 28**

- 📬 **Payout**: **+44,530 G** *(from 26x Nemean Tomato (pre-planted) on Day 27, 60x Sudor Pepper (pre-planted) on Day 27, 6x Revol Pepper (pre-planted) on Day 27, 24x Seatide Garlic on Day 27, 9x Nectarcane on Day 27)*
- **Morning Wallet**: **179,364 G** *(134,834 G carryover + 44,530 G)*
- 🌾 **Harvest & Ship**:
  - 26x Nemean Tomato *(Farm)* — regrowth 6/6 (stays planted) → +1,690 G *(arrives morning D29)*
  - 23x Seatide Garlic *(Farm)* — single harvest (soil freed) → +23,000 G *(arrives morning D29)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 5/6 (stays planted) → +1,650 G *(arrives morning D29)*
  - 4x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +18,400 G *(arrives morning D29)*
  - 33x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +8,250 G *(arrives morning D29)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 23 | 2,185 G | D29 | +460 G |

- **Daily Seed Spent**: 2,185 G | **End-of-Day Wallet**: **177,179 G**

---

#### **Day 29**

- 📬 **Payout**: **+52,990 G** *(from 26x Nemean Tomato (pre-planted) on Day 28, 15x Shatollan Paprika (pre-planted) on Day 28, 33x Nectarcane (pre-planted) on Day 28, 4x Islet Watermelon (pre-planted) on Day 28, 23x Seatide Garlic on Day 28)*
- **Morning Wallet**: **230,169 G** *(177,179 G carryover + 52,990 G)*
- 🌾 **Harvest & Ship**:
  - 23x Carrop *(Farm)* — single harvest (soil freed) → +2,645 G *(arrives morning D30)*
  - 24x Dress Lettuce *(Farm)* — single harvest (soil freed) → +2,040 G *(arrives morning D30)*
  - 23x Morrocorn *(Farm)* — single harvest (soil freed) → +9,200 G *(arrives morning D30)*
  - 18x Honey Flower *(Waterside)* — single harvest (soil freed) → +11,340 G *(arrives morning D30)*
  - 10x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +2,500 G *(arrives morning D30)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 70 | 6,650 G | D30 | +1,400 G |

- **Daily Seed Spent**: 6,650 G | **End-of-Day Wallet**: **223,519 G**

---

#### **Day 30**

- 📬 **Payout**: **+27,725 G** *(from 23x Morrocorn on Day 29, 18x Honey Flower on Day 29, 10x Nectarcane on Day 29, 23x Carrop on Day 29, 24x Dress Lettuce on Day 29)*
- **Morning Wallet**: **251,244 G** *(223,519 G carryover + 27,725 G)*
- 🌾 **Harvest & Ship**:
  - 6x Revol Pepper *(Cave)* — regrowth 4/4 (stays planted) → +1,590 G *(arrives morning D31)*
  - 16x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +4,000 G *(arrives morning D31)*
  - 70x Carrop *(Farm)* — single harvest (soil freed) → +8,050 G *(arrives morning D31)*
  - 45x Morrocorn *(Farm)* — single harvest (soil freed) → +18,000 G *(arrives morning D31)*
  - 14x Seatide Garlic *(Farm)* — single harvest (soil freed) → +14,000 G *(arrives morning D31)*
  - 15x Shatollan Paprika *(Farm)* — regrowth 6/6 (stays planted) → +1,650 G *(arrives morning D31)*
  - 1x Honey Flower *(Waterside)* — single harvest (soil freed) → +630 G *(arrives morning D31)*
  - 6x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +27,600 G *(arrives morning D31)*
  - 9x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +2,250 G *(arrives morning D31)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **251,244 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+77,770 G** *(from Day 30 final harvest: 15x Shatollan Paprika, 6x Islet Watermelon, 6x Revol Pepper, 14x Seatide Garlic, 45x Morrocorn, 1x Honey Flower, 16x Sudor Pepper, 9x Nectarcane, 70x Carrop)*
- **Starting Budget**: 51,104 G
- **Total Season Net Profit**: **+277,910 G**
- 🏆 **Final Quietus Wallet**: **329,014 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 0 / 0 (expands to 129) (0.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 10 / 19 (expands to 48) (52.6% utilized, 9 idle)
- **Cave Plots Used (Init)**: 0 / 16 (0.0% utilized, 16 idle)
- **Initial Capital Spent**: 3,700 G / 51,104 G (7.2% spent, 47,404 G leftover)
- **Pre-planted Crop Sales**: **+203,210 G**
- **New Planting Net Profit**: **+74,700 G**
- **Total Cumulative Season Net Profit**: **+277,910 G** across all restock stages
- **Final Projected Wallet**: **329,014 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
