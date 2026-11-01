# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 16
- **Planning Timeline**: Day 16 -> Day 30 (15d Quietus window)
- **Capital Budget**: 116,290 G
- **Plot Capacities (Usable / Max)**: Farm: 240/245 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D16, D18, D20, D22 | Freed D22 | +30,800 G |
| Farm | **Bellhop** | 1 | Day 5 | D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +675 G |
| Farm | **Bellhop** | 1 | Day 6 | D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +675 G |
| Farm | **Nemean Tomato** | 5 | Day 9 | D16, D17, D18, D19 | Freed D19 | +1,300 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D16, D18, D20, D22, D24, D26, D28, D30 | Freed D30 | +2,640 G |
| Farm | **Seatide Garlic** | 25 | Day 10 | D16 | Freed D16 | +25,000 G |
| Farm | **Morrocorn** | 18 | Day 12 | D16 | Freed D16 | +7,200 G |
| Farm | **Seatide Garlic** | 6 | Day 12 | D18 | Freed D18 | +6,000 G |
| Farm | **Morrocorn** | 35 | Day 14 | D18 | Freed D18 | +14,000 G |
| Farm | **Seatide Garlic** | 24 | Day 14 | D20 | Freed D20 | +24,000 G |
| Farm | **Dress Lettuce** | 16 | Day 15 | D17 | Freed D17 | +1,360 G |
| Farm | **Grass** | 3 | Day 15 | D17 | Freed D17 | +105 G |
| Farm | **Stellar Wheat** | 33 | Day 15 | D17 | Freed D17 | +1,815 G |
| Waterside | **Islet Watermelon** | 2 | Day 4 | D16 | Freed D16 | +9,200 G |
| Waterside | **Islet Watermelon** | 5 | Day 5 | D17 | Freed D17 | +23,000 G |
| Waterside | **Islet Watermelon** | 15 | Day 6 | D18 | Freed D18 | +69,000 G |
| Waterside | **Nectarcane** | 6 | Day 7 | D17 | Freed D17 | +1,500 G |
| Waterside | **Honey Flower** | 43 | Day 11 | D17 | Freed D17 | +27,090 G |
| Waterside | **Islet Watermelon** | 3 | Day 13 | D25 | Freed D25 | +13,800 G |
| Waterside | **Islet Watermelon** | 3 | Day 15 | D27 | Freed D27 | +13,800 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D17 | Freed D17 | +3,180 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D17, D20, D23, D26 | Freed D26 | +73,140 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 16**

- **Morning Wallet**: **116,290 G**
- **Harvest & Ship** *(+49,845 G arriving D17)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 1/15)
  - 18x Morrocorn *(Farm)* → +7,200 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 1/4)
  - 25x Seatide Garlic *(Farm)* → +25,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 1/4)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 43 | 8,600 G | D20 | +8,600 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D28 | +4,200 G |

- **Daily Seed Spent**: 13,600 G | **End-of-Day Wallet**: **102,690 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **152,535 G** *(102,690 G carryover + 49,845 G payout)*
- **Harvest & Ship** *(+76,750 G arriving D18)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 2/15)
  - 16x Dress Lettuce *(Farm)* → +1,360 G (freed)
  - 3x Grass *(Farm)* → +105 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 2/4)
  - 33x Stellar Wheat *(Farm)* → +1,815 G (freed)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 5x Islet Watermelon *(Waterside)* → +23,000 G (freed)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 1/1)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/1)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Farm | **Shatollan Paprika** | Shatolla | 43 | 10,750 G | D22..D30 (5x) | +12,900 G |
| Waterside | **Islet Watermelon** | Shatolla | 54 | 135,000 G | D29 | +113,400 G |

- **Daily Seed Spent**: 152,470 G | **End-of-Day Wallet**: **65 G**
- **Plots Left**: Farm: 9 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **76,815 G** *(65 G carryover + 76,750 G payout)*
- **Harvest & Ship** *(+97,445 G arriving D19)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/15)
  - 35x Morrocorn *(Farm)* → +14,000 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 3/4)
  - 6x Seatide Garlic *(Farm)* → +6,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 2/4)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 17 | 1,615 G | D19 | +340 G |
| Farm | **Seatide Garlic** | Shatolla | 32 | 20,800 G | D24 | +11,200 G |
| Waterside | **Islet Watermelon** | Shatolla | 15 | 37,500 G | D30 | +31,500 G |

- **Daily Seed Spent**: 59,915 G | **End-of-Day Wallet**: **16,900 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **114,345 G** *(16,900 G carryover + 97,445 G payout)*
- **Harvest & Ship** *(+2,370 G arriving D20)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/15)
  - 17x Carrop *(Farm)* → +1,955 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 4/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 11 | 2,530 G | D23 | +1,870 G |
| Farm | **Carrop** | Nemea | 11 | 1,045 G | D20 | +220 G |

- **Daily Seed Spent**: 3,575 G | **End-of-Day Wallet**: **110,770 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **113,140 G** *(110,770 G carryover + 2,370 G payout)*
- **Harvest & Ship** *(+68,870 G arriving D21)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/15)
  - 11x Carrop *(Farm)* → +1,265 G (freed)
  - 43x Morrocorn *(Farm)* → +17,200 G (freed)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 3/4)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 41 | 8,200 G | D24 | +8,200 G |
| Farm | **Seatide Garlic** | Shatolla | 37 | 24,050 G | D26 | +12,950 G |

- **Daily Seed Spent**: 32,250 G | **End-of-Day Wallet**: **80,890 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **149,760 G** *(80,890 G carryover + 68,870 G payout)*
- **Harvest & Ship** *(+3,270 G arriving D22)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/15)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 1 | 95 G | D22 | +20 G |

- **Daily Seed Spent**: 95 G | **End-of-Day Wallet**: **149,665 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **152,935 G** *(149,665 G carryover + 3,270 G payout)*
- **Harvest & Ship** *(+12,965 G arriving D23)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/15)
  - 1x Carrop *(Farm)* → +115 G (freed)
  - 116x Shatollan Paprika *(Farm)* → +12,760 G (regrowth 4/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 14 | 1,330 G | D23 | +280 G |
| Farm | **Morrocorn** | Shatolla | 56 | 11,200 G | D26 | +11,200 G |

- **Daily Seed Spent**: 12,530 G | **End-of-Day Wallet**: **140,405 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **153,370 G** *(140,405 G carryover + 12,965 G payout)*
- **Harvest & Ship** *(+24,385 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/15)
  - 14x Carrop *(Farm)* → +1,610 G (freed)
  - 11x Morrocorn *(Farm)* → +4,400 G (freed)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 26 | 2,470 G | D24 | +520 G |

- **Daily Seed Spent**: 2,470 G | **End-of-Day Wallet**: **150,900 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **175,285 G** *(150,900 G carryover + 24,385 G payout)*
- **Harvest & Ship** *(+59,720 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 9/15)
  - 26x Carrop *(Farm)* → +2,990 G (freed)
  - 41x Morrocorn *(Farm)* → +16,400 G (freed)
  - 32x Seatide Garlic *(Farm)* → +32,000 G (freed)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 5/8)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **110,935 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **170,655 G** *(110,935 G carryover + 59,720 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 10/15)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **170,655 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **184,545 G** *(170,655 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+82,835 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 11/15)
  - 56x Morrocorn *(Farm)* → +22,400 G (freed)
  - 37x Seatide Garlic *(Farm)* → +37,000 G (freed)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 6/8)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 4/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 43 | 8,600 G | D30 | +8,600 G |

- **Daily Seed Spent**: 20,100 G | **End-of-Day Wallet**: **164,445 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **247,280 G** *(164,445 G carryover + 82,835 G payout)*
- **Harvest & Ship** *(+17,070 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 12/15)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **247,280 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **264,350 G** *(247,280 G carryover + 17,070 G payout)*
- **Harvest & Ship** *(+14,350 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 13/15)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 7/8)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **264,350 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **278,700 G** *(264,350 G carryover + 14,350 G payout)*
- **Harvest & Ship** *(+248,490 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 14/15)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **278,700 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **527,190 G** *(278,700 G carryover + 248,490 G payout)*
- **Harvest & Ship** *(+213,530 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 15/15)
  - 93x Morrocorn *(Farm)* → +37,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 46x Shatollan Paprika *(Farm)* → +5,060 G (regrowth 8/8)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **527,190 G**
- **Plots Left**: Farm: 195 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **740,720 G** *(527,190 G carryover + 213,530 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 16–30)

- **Starting Wallet (Day 16)**: 116,290 G
- **Ending Wallet (Day 31 Quietus)**: **740,720 G**
- **Pre-planted Crop Sales**: **+349,280 G**
- **New Planting Net Profit**: **+275,150 G**
- **Net Profit (15 days)**: **+624,430 G**
- **Average Daily Profit**: **+41,629 G/day** *(over 15 active days)*
