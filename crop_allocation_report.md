# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 2
- **Planning Timeline**: Day 2 -> Day 30 (29d Quietus window)
- **Capital Budget**: 0 G
- **Plot Capacities (Usable / Max)**: Farm: 29/49

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Carrop** | 6 | Day 2 | D3 | Freed D3 | +690 G |
| Farm | **Dress Lettuce** | 3 | Day 2 | D4 | Freed D4 | +255 G |
| Farm | **Stellar Wheat** | 7 | Day 2 | D4 | Freed D4 | +385 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 2**

- **Morning Wallet**: **0 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 13

---

#### **Day 3**

- **Morning Wallet**: **0 G**
- **Harvest & Ship** *(+690 G arriving D4)*:
  - 6x Carrop *(Farm)* → +690 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 19

---

#### **Day 4**

- **Morning Wallet**: **690 G** *(0 G carryover + 690 G payout)*
- **Harvest & Ship** *(+640 G arriving D5)*:
  - 3x Dress Lettuce *(Farm)* → +255 G (freed)
  - 7x Stellar Wheat *(Farm)* → +385 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D6 | +360 G |

- **Daily Seed Spent**: 660 G | **End-of-Day Wallet**: **30 G**
- **Plots Left**: Farm: 17

---

#### **Day 5**

- **Morning Wallet**: **670 G** *(30 G carryover + 640 G payout)*

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D7 | +360 G |

- **Daily Seed Spent**: 660 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 5

---

#### **Day 6**

- **Morning Wallet**: **10 G**
- **Harvest & Ship** *(+1,020 G arriving D7)*:
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 17

---

#### **Day 7**

- **Morning Wallet**: **1,030 G** *(10 G carryover + 1,020 G payout)*
- **Harvest & Ship** *(+1,020 G arriving D8)*:
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Lethe | 3 | 315 G | D8 | +30 G |
| Farm | **Dress Lettuce** | Lethe | 8 | 440 G | D9 | +240 G |
| Farm | **Unionion** | Lethe | 2 | 260 G | D10 | +130 G |

- **Daily Seed Spent**: 1,015 G | **End-of-Day Wallet**: **15 G**
- **Plots Left**: Farm: 16

---

#### **Day 8**

- **Morning Wallet**: **1,035 G** *(15 G carryover + 1,020 G payout)*
- **Harvest & Ship** *(+345 G arriving D9)*:
  - 3x Carrop *(Farm)* → +345 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 18 | 990 G | D10 | +540 G |

- **Daily Seed Spent**: 990 G | **End-of-Day Wallet**: **45 G**
- **Plots Left**: Farm: 1

---

#### **Day 9**

- **Morning Wallet**: **390 G** *(45 G carryover + 345 G payout)*
- **Harvest & Ship** *(+680 G arriving D10)*:
  - 8x Dress Lettuce *(Farm)* → +680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 7 | 385 G | D11 | +210 G |

- **Daily Seed Spent**: 385 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 2

---

#### **Day 10**

- **Morning Wallet**: **685 G** *(5 G carryover + 680 G payout)*
- **Harvest & Ship** *(+1,920 G arriving D11)*:
  - 18x Dress Lettuce *(Farm)* → +1,530 G (freed)
  - 2x Unionion *(Farm)* → +390 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D12 | +360 G |

- **Daily Seed Spent**: 660 G | **End-of-Day Wallet**: **25 G**
- **Plots Left**: Farm: 10

---

#### **Day 11**

- **Morning Wallet**: **1,945 G** *(25 G carryover + 1,920 G payout)*
- **Harvest & Ship** *(+595 G arriving D12)*:
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 3 | 1,110 G | D15..D30 (6x) | +2,490 G |
| Farm | **Dress Lettuce** | Lethe | 14 | 770 G | D13 | +420 G |

- **Daily Seed Spent**: 1,880 G | **End-of-Day Wallet**: **65 G**
- **Plots Left**: Farm: 0

---

#### **Day 12**

- **Morning Wallet**: **660 G** *(65 G carryover + 595 G payout)*
- **Harvest & Ship** *(+1,020 G arriving D13)*:
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D14 | +360 G |

- **Daily Seed Spent**: 660 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 0

---

#### **Day 13**

- **Morning Wallet**: **1,020 G** *(0 G carryover + 1,020 G payout)*
- **Harvest & Ship** *(+1,190 G arriving D14)*:
  - 14x Dress Lettuce *(Farm)* → +1,190 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D15 | +360 G |
| Farm | **Unionion** | Lethe | 2 | 260 G | D16 | +130 G |

- **Daily Seed Spent**: 920 G | **End-of-Day Wallet**: **100 G**
- **Plots Left**: Farm: 0

---

#### **Day 14**

- **Morning Wallet**: **1,290 G** *(100 G carryover + 1,190 G payout)*
- **Harvest & Ship** *(+1,020 G arriving D15)*:
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 2 | 740 G | D18..D30 (5x) | +1,260 G |
| Farm | **Dress Lettuce** | Lethe | 10 | 550 G | D16 | +300 G |

- **Daily Seed Spent**: 1,290 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 0

---

#### **Day 15**

- **Morning Wallet**: **1,020 G** *(0 G carryover + 1,020 G payout)*
- **Harvest & Ship** *(+1,620 G arriving D16)*:
  - 3x Cucumble *(Farm)* → +600 G (regrowth 1/6)
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 12 | 660 G | D17 | +360 G |

- **Daily Seed Spent**: 660 G | **End-of-Day Wallet**: **360 G**
- **Plots Left**: Farm: 0

---

#### **Day 16**

- **Morning Wallet**: **1,980 G** *(360 G carryover + 1,620 G payout)*
- **Harvest & Ship** *(+1,240 G arriving D17)*:
  - 10x Dress Lettuce *(Farm)* → +850 G (freed)
  - 2x Unionion *(Farm)* → +390 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 2 | 740 G | D20..D29 (4x) | +860 G |
| Farm | **Dress Lettuce** | Lethe | 10 | 550 G | D18 | +300 G |

- **Daily Seed Spent**: 1,290 G | **End-of-Day Wallet**: **690 G**
- **Plots Left**: Farm: 0

---

#### **Day 17**

- **Morning Wallet**: **1,930 G** *(690 G carryover + 1,240 G payout)*
- **Harvest & Ship** *(+1,020 G arriving D18)*:
  - 12x Dress Lettuce *(Farm)* → +1,020 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 4 | 1,480 G | D21..D30 (4x) | +1,720 G |
| Farm | **Dress Lettuce** | Lethe | 8 | 440 G | D19 | +240 G |

- **Daily Seed Spent**: 1,920 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 0

---

#### **Day 18**

- **Morning Wallet**: **1,030 G** *(10 G carryover + 1,020 G payout)*
- **Harvest & Ship** *(+1,850 G arriving D19)*:
  - 5x Cucumble *(Farm)* → +1,000 G (regrowth 2/6)
  - 10x Dress Lettuce *(Farm)* → +850 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 4 | 220 G | D20 | +120 G |
| Farm | **Unionion** | Lethe | 6 | 780 G | D21 | +390 G |

- **Daily Seed Spent**: 1,000 G | **End-of-Day Wallet**: **30 G**
- **Plots Left**: Farm: 0

---

#### **Day 19**

- **Morning Wallet**: **1,880 G** *(30 G carryover + 1,850 G payout)*
- **Harvest & Ship** *(+680 G arriving D20)*:
  - 8x Dress Lettuce *(Farm)* → +680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 8 | 1,040 G | D22 | +520 G |

- **Daily Seed Spent**: 1,040 G | **End-of-Day Wallet**: **840 G**
- **Plots Left**: Farm: 0

---

#### **Day 20**

- **Morning Wallet**: **1,520 G** *(840 G carryover + 680 G payout)*
- **Harvest & Ship** *(+740 G arriving D21)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 1/4)
  - 4x Dress Lettuce *(Farm)* → +340 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Cucumble** | Lethe | 4 | 1,480 G | D24, D27, D30 | +920 G |

- **Daily Seed Spent**: 1,480 G | **End-of-Day Wallet**: **40 G**
- **Plots Left**: Farm: 0

---

#### **Day 21**

- **Morning Wallet**: **780 G** *(40 G carryover + 740 G payout)*
- **Harvest & Ship** *(+2,970 G arriving D22)*:
  - 9x Cucumble *(Farm)* → +1,800 G (regrowth 3/6)
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 6 | 780 G | D24 | +390 G |

- **Daily Seed Spent**: 780 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 0

---

#### **Day 22**

- **Morning Wallet**: **2,970 G** *(0 G carryover + 2,970 G payout)*
- **Harvest & Ship** *(+1,560 G arriving D23)*:
  - 8x Unionion *(Farm)* → +1,560 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 8 | 440 G | D24 | +240 G |

- **Daily Seed Spent**: 440 G | **End-of-Day Wallet**: **2,530 G**
- **Plots Left**: Farm: 0

---

#### **Day 23**

- **Morning Wallet**: **4,090 G** *(2,530 G carryover + 1,560 G payout)*
- **Harvest & Ship** *(+400 G arriving D24)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 2/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **4,090 G**
- **Plots Left**: Farm: 0

---

#### **Day 24**

- **Morning Wallet**: **4,490 G** *(4,090 G carryover + 400 G payout)*
- **Harvest & Ship** *(+4,450 G arriving D25)*:
  - 13x Cucumble *(Farm)* → +2,600 G (regrowth 4/6)
  - 8x Dress Lettuce *(Farm)* → +680 G (freed)
  - 6x Unionion *(Farm)* → +1,170 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 14 | 1,820 G | D27 | +910 G |

- **Daily Seed Spent**: 1,820 G | **End-of-Day Wallet**: **2,670 G**
- **Plots Left**: Farm: 0

---

#### **Day 25**

- **Morning Wallet**: **7,120 G** *(2,670 G carryover + 4,450 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **7,120 G**
- **Plots Left**: Farm: 0

---

#### **Day 26**

- **Morning Wallet**: **7,120 G**
- **Harvest & Ship** *(+400 G arriving D27)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **7,120 G**
- **Plots Left**: Farm: 0

---

#### **Day 27**

- **Morning Wallet**: **7,520 G** *(7,120 G carryover + 400 G payout)*
- **Harvest & Ship** *(+5,330 G arriving D28)*:
  - 13x Cucumble *(Farm)* → +2,600 G (regrowth 5/6)
  - 14x Unionion *(Farm)* → +2,730 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 14 | 1,820 G | D30 | +910 G |

- **Daily Seed Spent**: 1,820 G | **End-of-Day Wallet**: **5,700 G**
- **Plots Left**: Farm: 0

---

#### **Day 28**

- **Morning Wallet**: **11,030 G** *(5,700 G carryover + 5,330 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **11,030 G**
- **Plots Left**: Farm: 0

---

#### **Day 29**

- **Morning Wallet**: **11,030 G**
- **Harvest & Ship** *(+400 G arriving D30)*:
  - 2x Cucumble *(Farm)* → +400 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **11,030 G**
- **Plots Left**: Farm: 0

---

#### **Day 30**

- **Morning Wallet**: **11,430 G** *(11,030 G carryover + 400 G payout)*
- **Harvest & Ship** *(+5,330 G arriving D31)*:
  - 13x Cucumble *(Farm)* → +2,600 G (regrowth 6/6)
  - 14x Unionion *(Farm)* → +2,730 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **11,430 G**
- **Plots Left**: Farm: 17

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **16,760 G** *(11,430 G carryover + 5,330 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 2–30)

- **Starting Wallet (Day 2)**: 0 G
- **Ending Wallet (Day 31 Quietus)**: **16,760 G**
- **Pre-planted Crop Sales**: **+1,330 G**
- **New Planting Net Profit**: **+15,430 G**
- **Net Profit (29 days)**: **+16,760 G**
- **Average Daily Profit**: **+578 G/day** *(over 29 active days)*
