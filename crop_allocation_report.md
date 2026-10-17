# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 18
- **Planning Timeline**: Day 18 -> Day 30 (13d Quietus window)
- **Capital Budget**: 51,600 G
- **Plot Capacities**: Farm 60 -> 196 | Waterside 36 -> 81 | Cave 54 -> 81

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 18**

- **Morning Wallet**: **51,600 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 44 | 17,600 G | D21, D24, D27 | +15,400 G |
| Farm | **Carrop** | Lethe | 34 | 3,570 G | D19 | +340 G |
| Farm | **Nemean Tomato** | Nemea | 26 | 4,420 G | D23..D28 (6x) | +5,720 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D30 | +6,300 G |
| Waterside | **Nectarcane** | Shatolla | 33 | 12,210 G | D22, D25, D28 | +12,540 G |

- **Daily Seed Spent**: 45,300 G | **End-of-Day Wallet**: **6,300 G**

---

#### **Day 19**

- **Morning Wallet**: **6,300 G**
- 🌾 **Harvest & Ship**: 34x Carrop *(Farm)* — single harvest (soil freed) → +3,910 G *(arrives morning D20)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 19 | 1,995 G | D20 | +190 G |
| Farm | **Stellar Wheat** | Lethe | 48 | 1,920 G | D21 | +720 G |
| Farm | **Carrop** | Nemea | 21 | 1,995 G | D20 | +420 G |

- **Daily Seed Spent**: 5,910 G | **End-of-Day Wallet**: **390 G**

---

#### **Day 20**

- 📬 **Payout**: **+3,910 G** *(from 34x Carrop on Day 19)*
- **Morning Wallet**: **4,300 G** *(390 G carryover + 3,910 G)*
- 🌾 **Harvest & Ship**: 40x Carrop *(Farm)* — single harvest (soil freed) → +4,600 G *(arrives morning D21)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 9 | 3,600 G | D23, D26, D29 | +3,150 G |
| Farm | **Stellar Wheat** | Lethe | 3 | 120 G | D22 | +45 G |

- **Daily Seed Spent**: 3,720 G | **End-of-Day Wallet**: **580 G**

---

#### **Day 21**

- 📬 **Payout**: **+4,600 G** *(from 40x Carrop on Day 20)*
- **Morning Wallet**: **5,180 G** *(580 G carryover + 4,600 G)*
- 🌾 **Harvest & Ship**:
  - 44x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +11,000 G *(arrives morning D22)*
  - 48x Stellar Wheat *(Farm)* — single harvest (soil freed) → +2,640 G *(arrives morning D22)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 84 | 4,620 G | D23 | +2,520 G |

- **Daily Seed Spent**: 4,620 G | **End-of-Day Wallet**: **560 G**

---

#### **Day 22**

- 📬 **Payout**: **+13,640 G** *(from 44x Sudor Pepper on Day 21, 48x Stellar Wheat on Day 21)*
- **Morning Wallet**: **14,200 G** *(560 G carryover + 13,640 G)*
- 🌾 **Harvest & Ship**:
  - 3x Stellar Wheat *(Farm)* — single harvest (soil freed) → +165 G *(arrives morning D23)*
  - 33x Nectarcane *(Waterside)* — regrowth 1/3 (stays planted) → +8,250 G *(arrives morning D23)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 11 | 1,045 G | D23 | +220 G |
| Farm | **Morrocorn** | Shatolla | 34 | 6,800 G | D26 | +6,800 G |

- **Daily Seed Spent**: 7,845 G | **End-of-Day Wallet**: **6,355 G**

---

#### **Day 23**

- 📬 **Payout**: **+8,415 G** *(from 33x Nectarcane on Day 22, 3x Stellar Wheat on Day 22)*
- **Morning Wallet**: **14,770 G** *(6,355 G carryover + 8,415 G)*
- 🌾 **Harvest & Ship**:
  - 9x Sudor Pepper *(Cave)* — regrowth 1/3 (stays planted) → +2,250 G *(arrives morning D24)*
  - 11x Carrop *(Farm)* — single harvest (soil freed) → +1,265 G *(arrives morning D24)*
  - 84x Dress Lettuce *(Farm)* — single harvest (soil freed) → +7,140 G *(arrives morning D24)*
  - 26x Nemean Tomato *(Farm)* — regrowth 1/6 (stays planted) → +1,690 G *(arrives morning D24)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 14 | 770 G | D25 | +420 G |
| Farm | **Stellar Wheat** | Lethe | 67 | 2,680 G | D25 | +1,005 G |
| Farm | **Seatide Garlic** | Shatolla | 15 | 9,750 G | D29 | +5,250 G |

- **Daily Seed Spent**: 13,200 G | **End-of-Day Wallet**: **1,570 G**

---

#### **Day 24**

- 📬 **Payout**: **+12,345 G** *(from 9x Sudor Pepper on Day 23, 26x Nemean Tomato on Day 23, 11x Carrop on Day 23, 84x Dress Lettuce on Day 23)*
- **Morning Wallet**: **13,915 G** *(1,570 G carryover + 12,345 G)*
- 🌾 **Harvest & Ship**:
  - 44x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +11,000 G *(arrives morning D25)*
  - 26x Nemean Tomato *(Farm)* — regrowth 2/6 (stays planted) → +1,690 G *(arrives morning D25)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Honey Flower** | Shatolla | 36 | 13,680 G | D30 | +9,000 G |

- **Daily Seed Spent**: 13,680 G | **End-of-Day Wallet**: **235 G**

---

#### **Day 25**

- 📬 **Payout**: **+12,690 G** *(from 44x Sudor Pepper on Day 24, 26x Nemean Tomato on Day 24)*
- **Morning Wallet**: **12,925 G** *(235 G carryover + 12,690 G)*
- 🌾 **Harvest & Ship**:
  - 14x Dress Lettuce *(Farm)* — single harvest (soil freed) → +1,190 G *(arrives morning D26)*
  - 26x Nemean Tomato *(Farm)* — regrowth 3/6 (stays planted) → +1,690 G *(arrives morning D26)*
  - 67x Stellar Wheat *(Farm)* — single harvest (soil freed) → +3,685 G *(arrives morning D26)*
  - 33x Nectarcane *(Waterside)* — regrowth 2/3 (stays planted) → +8,250 G *(arrives morning D26)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 33 | 3,135 G | D26 | +660 G |
| Farm | **Morrocorn** | Shatolla | 48 | 9,600 G | D29 | +9,600 G |

- **Daily Seed Spent**: 12,735 G | **End-of-Day Wallet**: **190 G**

---

#### **Day 26**

- 📬 **Payout**: **+14,815 G** *(from 33x Nectarcane on Day 25, 26x Nemean Tomato on Day 25, 14x Dress Lettuce on Day 25, 67x Stellar Wheat on Day 25)*
- **Morning Wallet**: **15,005 G** *(190 G carryover + 14,815 G)*
- 🌾 **Harvest & Ship**:
  - 9x Sudor Pepper *(Cave)* — regrowth 2/3 (stays planted) → +2,250 G *(arrives morning D27)*
  - 33x Carrop *(Farm)* — single harvest (soil freed) → +3,795 G *(arrives morning D27)*
  - 34x Morrocorn *(Farm)* — single harvest (soil freed) → +13,600 G *(arrives morning D27)*
  - 26x Nemean Tomato *(Farm)* — regrowth 4/6 (stays planted) → +1,690 G *(arrives morning D27)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 17 | 3,400 G | D30 | +3,400 G |

- **Daily Seed Spent**: 14,900 G | **End-of-Day Wallet**: **105 G**

---

#### **Day 27**

- 📬 **Payout**: **+21,335 G** *(from 34x Morrocorn on Day 26, 9x Sudor Pepper on Day 26, 26x Nemean Tomato on Day 26, 33x Carrop on Day 26)*
- **Morning Wallet**: **21,440 G** *(105 G carryover + 21,335 G)*
- 🌾 **Harvest & Ship**:
  - 44x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +11,000 G *(arrives morning D28)*
  - 26x Nemean Tomato *(Farm)* — regrowth 5/6 (stays planted) → +1,690 G *(arrives morning D28)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **21,440 G**

---

#### **Day 28**

- 📬 **Payout**: **+12,690 G** *(from 44x Sudor Pepper on Day 27, 26x Nemean Tomato on Day 27)*
- **Morning Wallet**: **34,130 G** *(21,440 G carryover + 12,690 G)*
- 🌾 **Harvest & Ship**:
  - 26x Nemean Tomato *(Farm)* — regrowth 6/6 (stays planted) → +1,690 G *(arrives morning D29)*
  - 33x Nectarcane *(Waterside)* — regrowth 3/3 (stays planted) → +8,250 G *(arrives morning D29)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **34,130 G**

---

#### **Day 29**

- 📬 **Payout**: **+9,940 G** *(from 33x Nectarcane on Day 28, 26x Nemean Tomato on Day 28)*
- **Morning Wallet**: **44,070 G** *(34,130 G carryover + 9,940 G)*
- 🌾 **Harvest & Ship**:
  - 9x Sudor Pepper *(Cave)* — regrowth 3/3 (stays planted) → +2,250 G *(arrives morning D30)*
  - 48x Morrocorn *(Farm)* — single harvest (soil freed) → +19,200 G *(arrives morning D30)*
  - 15x Seatide Garlic *(Farm)* — single harvest (soil freed) → +15,000 G *(arrives morning D30)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 34 | 3,570 G | D30 | +340 G |
| Farm | **Carrop** | Nemea | 55 | 5,225 G | D30 | +1,100 G |

- **Daily Seed Spent**: 8,795 G | **End-of-Day Wallet**: **35,275 G**

---

#### **Day 30**

- 📬 **Payout**: **+36,450 G** *(from 15x Seatide Garlic on Day 29, 48x Morrocorn on Day 29, 9x Sudor Pepper on Day 29)*
- **Morning Wallet**: **71,725 G** *(35,275 G carryover + 36,450 G)*
- 🌾 **Harvest & Ship**:
  - 89x Carrop *(Farm)* — single harvest (soil freed) → +10,235 G *(arrives morning D31)*
  - 67x Morrocorn *(Farm)* — single harvest (soil freed) → +26,800 G *(arrives morning D31)*
  - 36x Honey Flower *(Waterside)* — single harvest (soil freed) → +22,680 G *(arrives morning D31)*
  - 3x Islet Watermelon *(Waterside)* — single harvest (soil freed) → +13,800 G *(arrives morning D31)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **71,725 G**

---

### ❄️ Quietus Morning (Day 31 Finale & Summary)

- 📬 **Final Shipping Payout**: **+73,515 G** *(from Day 30 final harvest: 3x Islet Watermelon, 67x Morrocorn, 36x Honey Flower, 89x Carrop)*
- **Starting Budget**: 51,600 G
- **Total Season Net Profit**: **+93,640 G**
- 🏆 **Final Quietus Wallet**: **145,240 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 60 / 60 (expands to 196) (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 36 / 36 (expands to 81) (100.0% utilized, 0 idle)
- **Cave Plots Used (Init)**: 44 / 54 (expands to 81) (81.5% utilized, 10 idle)
- **Initial Capital Spent**: 45,300 G / 51,600 G (87.8% spent, 6,300 G leftover)
- **Total Cumulative Season Net Profit**: **+93,640 G** across all restock stages
- **Final Projected Wallet**: **145,240 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
