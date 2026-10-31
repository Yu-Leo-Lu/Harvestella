# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 15
- **Planning Timeline**: Day 15 -> Day 30 (16d Quietus window)
- **Capital Budget**: 99,690 G
- **Plot Capacities (Usable / Max)**: Farm: 240/245 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D16, D18, D20, D22 | Freed D22 | +30,800 G |
| Farm | **Bellhop** | 1 | Day 5 | D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +720 G |
| Farm | **Bellhop** | 1 | Day 6 | D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +720 G |
| Farm | **Nemean Tomato** | 5 | Day 9 | D15, D16, D17, D18, D19 | Freed D19 | +1,625 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D16, D18, D20, D22, D24, D26, D28, D30 | Freed D30 | +2,640 G |
| Farm | **Seatide Garlic** | 25 | Day 10 | D16 | Freed D16 | +25,000 G |
| Farm | **Morrocorn** | 18 | Day 12 | D16 | Freed D16 | +7,200 G |
| Farm | **Seatide Garlic** | 6 | Day 12 | D18 | Freed D18 | +6,000 G |
| Farm | **Carrop** | 52 | Day 14 | D15 | Freed D15 | +5,980 G |
| Farm | **Morrocorn** | 35 | Day 14 | D18 | Freed D18 | +14,000 G |
| Farm | **Seatide Garlic** | 24 | Day 14 | D20 | Freed D20 | +24,000 G |
| Farm | **Dress Lettuce** | 16 | Day 15 | D17 | Freed D17 | +1,360 G |
| Farm | **Stellar Wheat** | 33 | Day 15 | D17 | Freed D17 | +1,815 G |
| Farm | **Grass** | 3 | Day 15 | D17 | Freed D17 | +105 G |
| Waterside | **Islet Watermelon** | 3 | Day 3 | D15 | Freed D15 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 4 | D16 | Freed D16 | +9,200 G |
| Waterside | **Islet Watermelon** | 5 | Day 5 | D17 | Freed D17 | +23,000 G |
| Waterside | **Islet Watermelon** | 15 | Day 6 | D18 | Freed D18 | +69,000 G |
| Waterside | **Nectarcane** | 6 | Day 7 | D17 | Freed D17 | +1,500 G |
| Waterside | **Honey Flower** | 43 | Day 11 | D17 | Freed D17 | +27,090 G |
| Waterside | **Islet Watermelon** | 3 | Day 13 | D25 | Freed D25 | +13,800 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D17 | Freed D17 | +3,180 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D17, D20, D23, D26 | Freed D26 | +73,140 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 15**

- **Morning Wallet**: **99,690 G**
- **Harvest & Ship** *(+20,195 G arriving D16)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/16)
  - 52x Carrop *(Farm)* → +5,980 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 1/5)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D27 | +6,300 G |

- **Daily Seed Spent**: 7,500 G | **End-of-Day Wallet**: **92,190 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **112,385 G** *(92,190 G carryover + 20,195 G payout)*
- **Harvest & Ship** *(+49,845 G arriving D17)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/16)
  - 18x Morrocorn *(Farm)* → +7,200 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 2/5)
  - 25x Seatide Garlic *(Farm)* → +25,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 1/4)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 6 | 1,380 G | D20 | +1,020 G |
| Farm | **Morrocorn** | Shatolla | 37 | 7,400 G | D20 | +7,400 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D28 | +4,200 G |

- **Daily Seed Spent**: 13,780 G | **End-of-Day Wallet**: **98,605 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **148,450 G** *(98,605 G carryover + 49,845 G payout)*
- **Harvest & Ship** *(+76,750 G arriving D18)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/16)
  - 16x Dress Lettuce *(Farm)* → +1,360 G (freed)
  - 3x Grass *(Farm)* → +105 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 3/5)
  - 33x Stellar Wheat *(Farm)* → +1,815 G (freed)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 5x Islet Watermelon *(Waterside)* → +23,000 G (freed)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 1/1)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Farm | **Carrop** | Nemea | 8 | 760 G | D18 | +160 G |
| Farm | **Morrocorn** | Shatolla | 1 | 200 G | D21 | +200 G |
| Farm | **Shatollan Paprika** | Shatolla | 43 | 10,750 G | D22..D30 (5x) | +12,900 G |
| Waterside | **Islet Watermelon** | Shatolla | 52 | 130,000 G | D29 | +109,200 G |

- **Daily Seed Spent**: 148,430 G | **End-of-Day Wallet**: **20 G**
- **Plots Left**: Farm: 0 | Waterside: 2 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **76,770 G** *(20 G carryover + 76,750 G payout)*
- **Harvest & Ship** *(+98,365 G arriving D19)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/16)
  - 8x Carrop *(Farm)* → +920 G (freed)
  - 35x Morrocorn *(Farm)* → +14,000 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 4/5)
  - 6x Seatide Garlic *(Farm)* → +6,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 2/4)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 5 | 1,150 G | D22 | +850 G |
| Farm | **Carrop** | Nemea | 12 | 1,140 G | D19 | +240 G |
| Farm | **Seatide Garlic** | Shatolla | 32 | 20,800 G | D24 | +11,200 G |
| Waterside | **Islet Watermelon** | Shatolla | 17 | 42,500 G | D30 | +35,700 G |

- **Daily Seed Spent**: 65,590 G | **End-of-Day Wallet**: **11,180 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **109,545 G** *(11,180 G carryover + 98,365 G payout)*
- **Harvest & Ship** *(+1,795 G arriving D20)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/16)
  - 12x Carrop *(Farm)* → +1,380 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 17 | 1,615 G | D20 | +340 G |

- **Daily Seed Spent**: 1,615 G | **End-of-Day Wallet**: **107,930 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **109,725 G** *(107,930 G carryover + 1,795 G payout)*
- **Harvest & Ship** *(+69,560 G arriving D21)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/16)
  - 17x Carrop *(Farm)* → +1,955 G (freed)
  - 43x Morrocorn *(Farm)* → +17,200 G (freed)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 3/4)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 47 | 9,400 G | D24 | +9,400 G |
| Farm | **Seatide Garlic** | Shatolla | 37 | 24,050 G | D26 | +12,950 G |

- **Daily Seed Spent**: 33,450 G | **End-of-Day Wallet**: **76,275 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **145,835 G** *(76,275 G carryover + 69,560 G payout)*
- **Harvest & Ship** *(+3,670 G arriving D22)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/16)
  - 1x Morrocorn *(Farm)* → +400 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 1 | 95 G | D22 | +20 G |

- **Daily Seed Spent**: 95 G | **End-of-Day Wallet**: **145,740 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **149,410 G** *(145,740 G carryover + 3,670 G payout)*
- **Harvest & Ship** *(+14,965 G arriving D23)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/16)
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 5x Morrocorn *(Farm)* → +2,000 G (freed)
  - 116x Shatollan Paprika *(Farm)* → +12,760 G (regrowth 4/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 20 | 1,900 G | D23 | +400 G |
| Farm | **Morrocorn** | Shatolla | 56 | 11,200 G | D26 | +11,200 G |

- **Daily Seed Spent**: 13,100 G | **End-of-Day Wallet**: **136,310 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **151,275 G** *(136,310 G carryover + 14,965 G payout)*
- **Harvest & Ship** *(+20,675 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 9/16)
  - 20x Carrop *(Farm)* → +2,300 G (freed)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 20 | 1,900 G | D24 | +400 G |

- **Daily Seed Spent**: 1,900 G | **End-of-Day Wallet**: **149,375 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **170,050 G** *(149,375 G carryover + 20,675 G payout)*
- **Harvest & Ship** *(+61,430 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 10/16)
  - 20x Carrop *(Farm)* → +2,300 G (freed)
  - 47x Morrocorn *(Farm)* → +18,800 G (freed)
  - 32x Seatide Garlic *(Farm)* → +32,000 G (freed)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 5/8)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **105,700 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **167,130 G** *(105,700 G carryover + 61,430 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 11/16)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **167,130 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **181,020 G** *(167,130 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+82,835 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 12/16)
  - 56x Morrocorn *(Farm)* → +22,400 G (freed)
  - 37x Seatide Garlic *(Farm)* → +37,000 G (freed)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 6/8)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 4/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 43 | 8,600 G | D30 | +8,600 G |

- **Daily Seed Spent**: 20,100 G | **End-of-Day Wallet**: **160,920 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **243,755 G** *(160,920 G carryover + 82,835 G payout)*
- **Harvest & Ship** *(+17,070 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 13/16)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **243,755 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **260,825 G** *(243,755 G carryover + 17,070 G payout)*
- **Harvest & Ship** *(+14,350 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 14/16)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 7/8)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **260,825 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **275,175 G** *(260,825 G carryover + 14,350 G payout)*
- **Harvest & Ship** *(+239,290 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 15/16)
  - 52x Islet Watermelon *(Waterside)* → +239,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **275,175 G**
- **Plots Left**: Farm: 0 | Waterside: 60 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **514,465 G** *(275,175 G carryover + 239,290 G payout)*
- **Harvest & Ship** *(+222,730 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 16/16)
  - 93x Morrocorn *(Farm)* → +37,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 8/8)
  - 17x Islet Watermelon *(Waterside)* → +78,200 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **514,465 G**
- **Plots Left**: Farm: 195 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **737,195 G** *(514,465 G carryover + 222,730 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 15–30)

- **Starting Wallet (Day 15)**: 99,690 G
- **Ending Wallet (Day 31 Quietus)**: **737,195 G**
- **Pre-planted Crop Sales**: **+355,675 G**
- **New Planting Net Profit**: **+281,830 G**
- **Net Profit (16 days)**: **+637,505 G**
- **Average Daily Profit**: **+39,844 G/day** *(over 16 active days)*
