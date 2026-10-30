# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 11
- **Planning Timeline**: Day 11 -> Day 30 (20d Quietus window)
- **Capital Budget**: 31,895 G
- **Plot Capacities (Usable / Max)**: Farm: 191/196 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D12, D14, D16, D18, D20, D22 | Freed D22 | +46,200 G |
| Farm | **Bellhop** | 1 | Day 4 | D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +900 G |
| Farm | **Seatide Garlic** | 4 | Day 5 | D11 | Freed D11 | +4,000 G |
| Farm | **Bellhop** | 1 | Day 6 | D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +810 G |
| Farm | **Seatide Garlic** | 24 | Day 6 | D12 | Freed D12 | +24,000 G |
| Farm | **Seatide Garlic** | 47 | Day 8 | D14 | Freed D14 | +47,000 G |
| Farm | **Morrocorn** | 6 | Day 9 | D13 | Freed D13 | +2,400 G |
| Farm | **Nemean Tomato** | 5 | Day 9 | D14, D15, D16, D17, D18, D19 | Freed D19 | +1,950 G |
| Farm | **Shatollan Paprika** | 3 | Day 9 | D14, D16, D18, D20, D22, D24, D26, D28, D30 | Freed D30 | +2,970 G |
| Farm | **Morrocorn** | 5 | Day 10 | D14 | Freed D14 | +2,000 G |
| Farm | **Seatide Garlic** | 25 | Day 10 | D16 | Freed D16 | +25,000 G |
| Waterside | **Islet Watermelon** | 3 | Day 1 | D13 | Freed D13 | +13,800 G |
| Waterside | **Nectarcane** | 43 | Day 1 | D11 | Freed D11 | +10,750 G |
| Waterside | **Islet Watermelon** | 3 | Day 3 | D15 | Freed D15 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 4 | D16 | Freed D16 | +9,200 G |
| Waterside | **Islet Watermelon** | 5 | Day 5 | D17 | Freed D17 | +23,000 G |
| Waterside | **Islet Watermelon** | 15 | Day 6 | D18 | Freed D18 | +69,000 G |
| Waterside | **Nectarcane** | 6 | Day 7 | D11, D14, D17 | Freed D17 | +4,500 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D11, D14, D17 | Freed D17 | +9,540 G |
| Cave | **Revol Pepper** | 69 | Day 10 | D14, D17, D20, D23, D26 | Freed D26 | +91,425 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 11**

- **Morning Wallet**: **31,895 G**
- **Harvest & Ship** *(+19,475 G arriving D12)*:
  - 1x Bellhop *(Farm)* → +45 G (regrowth 1/20)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 49x Nectarcane *(Waterside)* → +12,250 G (regrowth 1/1)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 4 | 380 G | D12 | +80 G |
| Waterside | **Honey Flower** | Shatolla | 43 | 16,340 G | D17 | +10,750 G |

- **Daily Seed Spent**: 16,720 G | **End-of-Day Wallet**: **15,175 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **34,650 G** *(15,175 G carryover + 19,475 G payout)*
- **Harvest & Ship** *(+32,205 G arriving D13)*:
  - 1x Bellhop *(Farm)* → +45 G (regrowth 2/20)
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 1/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 20 | 4,000 G | D16 | +4,000 G |
| Farm | **Seatide Garlic** | Shatolla | 8 | 5,200 G | D18 | +2,800 G |

- **Daily Seed Spent**: 9,200 G | **End-of-Day Wallet**: **25,450 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **57,655 G** *(25,450 G carryover + 32,205 G payout)*
- **Harvest & Ship** *(+16,290 G arriving D14)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 3/20)
  - 6x Morrocorn *(Farm)* → +2,400 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D14 | +120 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D25 | +6,300 G |

- **Daily Seed Spent**: 8,070 G | **End-of-Day Wallet**: **49,585 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **65,875 G** *(49,585 G carryover + 16,290 G payout)*
- **Harvest & Ship** *(+81,100 G arriving D15)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/20)
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 5x Morrocorn *(Farm)* → +2,000 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 1/6)
  - 47x Seatide Garlic *(Farm)* → +47,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 2/6)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 24 | 5,520 G | D18 | +4,080 G |
| Farm | **Morrocorn** | Shatolla | 34 | 6,800 G | D18 | +6,800 G |

- **Daily Seed Spent**: 12,320 G | **End-of-Day Wallet**: **53,555 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **134,655 G** *(53,555 G carryover + 81,100 G payout)*
- **Harvest & Ship** *(+14,215 G arriving D16)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/20)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 2/6)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D27 | +6,300 G |

- **Daily Seed Spent**: 7,500 G | **End-of-Day Wallet**: **127,155 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **141,370 G** *(127,155 G carryover + 14,215 G payout)*
- **Harvest & Ship** *(+50,645 G arriving D17)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/20)
  - 20x Morrocorn *(Farm)* → +8,000 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 3/6)
  - 25x Seatide Garlic *(Farm)* → +25,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 3/6)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 45 | 9,000 G | D20 | +9,000 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D28 | +4,200 G |

- **Daily Seed Spent**: 14,000 G | **End-of-Day Wallet**: **127,370 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **178,015 G** *(127,370 G carryover + 50,645 G payout)*
- **Harvest & Ship** *(+73,470 G arriving D18)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/20)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 4/6)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 5x Islet Watermelon *(Waterside)* → +23,000 G (freed)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Waterside | **Islet Watermelon** | Shatolla | 54 | 135,000 G | D29 | +113,400 G |

- **Daily Seed Spent**: 141,720 G | **End-of-Day Wallet**: **36,295 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **109,765 G** *(36,295 G carryover + 73,470 G payout)*
- **Harvest & Ship** *(+108,645 G arriving D19)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/20)
  - 58x Morrocorn *(Farm)* → +23,200 G (freed)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 5/6)
  - 8x Seatide Garlic *(Farm)* → +8,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 4/6)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 66 | 42,900 G | D24 | +23,100 G |
| Waterside | **Islet Watermelon** | Shatolla | 15 | 37,500 G | D30 | +31,500 G |

- **Daily Seed Spent**: 80,400 G | **End-of-Day Wallet**: **29,365 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **138,010 G** *(29,365 G carryover + 108,645 G payout)*
- **Harvest & Ship** *(+415 G arriving D20)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 9/20)
  - 5x Nemean Tomato *(Farm)* → +325 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 5 | 475 G | D20 | +100 G |

- **Daily Seed Spent**: 475 G | **End-of-Day Wallet**: **137,535 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **137,950 G** *(137,535 G carryover + 415 G payout)*
- **Harvest & Ship** *(+44,980 G arriving D21)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 10/20)
  - 5x Carrop *(Farm)* → +575 G (freed)
  - 45x Morrocorn *(Farm)* → +18,000 G (freed)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 5/6)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 25 | 5,750 G | D24 | +4,250 G |
| Farm | **Seatide Garlic** | Shatolla | 25 | 16,250 G | D26 | +8,750 G |

- **Daily Seed Spent**: 22,000 G | **End-of-Day Wallet**: **115,950 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **160,930 G** *(115,950 G carryover + 44,980 G payout)*
- **Harvest & Ship** *(+3,270 G arriving D22)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 11/20)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **160,930 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **164,200 G** *(160,930 G carryover + 3,270 G payout)*
- **Harvest & Ship** *(+8,120 G arriving D23)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 12/20)
  - 73x Shatollan Paprika *(Farm)* → +8,030 G (regrowth 6/6)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 8 | 760 G | D23 | +160 G |
| Farm | **Morrocorn** | Shatolla | 62 | 12,400 G | D26 | +12,400 G |

- **Daily Seed Spent**: 13,160 G | **End-of-Day Wallet**: **151,040 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **159,160 G** *(151,040 G carryover + 8,120 G payout)*
- **Harvest & Ship** *(+19,295 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 13/20)
  - 8x Carrop *(Farm)* → +920 G (freed)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 8 | 760 G | D24 | +160 G |

- **Daily Seed Spent**: 760 G | **End-of-Day Wallet**: **158,400 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **177,695 G** *(158,400 G carryover + 19,295 G payout)*
- **Harvest & Ship** *(+80,520 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 14/20)
  - 8x Carrop *(Farm)* → +920 G (freed)
  - 25x Morrocorn *(Farm)* → +10,000 G (freed)
  - 66x Seatide Garlic *(Farm)* → +66,000 G (freed)
  - 3x Shatollan Paprika *(Farm)* → +330 G (regrowth 6/9)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **113,345 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **193,865 G** *(113,345 G carryover + 80,520 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 15/20)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **193,865 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **207,755 G** *(193,865 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+68,505 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 16/20)
  - 62x Morrocorn *(Farm)* → +24,800 G (freed)
  - 25x Seatide Garlic *(Farm)* → +25,000 G (freed)
  - 3x Shatollan Paprika *(Farm)* → +330 G (regrowth 7/9)
  - 69x Revol Pepper *(Cave)* → +18,285 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 37 | 7,400 G | D30 | +7,400 G |

- **Daily Seed Spent**: 18,900 G | **End-of-Day Wallet**: **188,855 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 69

---

#### **Day 27**

- **Morning Wallet**: **257,360 G** *(188,855 G carryover + 68,505 G payout)*
- **Harvest & Ship** *(+17,070 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 17/20)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **257,360 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **274,430 G** *(257,360 G carryover + 17,070 G payout)*
- **Harvest & Ship** *(+9,620 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 18/20)
  - 3x Shatollan Paprika *(Farm)* → +330 G (regrowth 8/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **274,430 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **284,050 G** *(274,430 G carryover + 9,620 G payout)*
- **Harvest & Ship** *(+248,490 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 19/20)
  - 54x Islet Watermelon *(Waterside)* → +248,400 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **284,050 G**
- **Plots Left**: Farm: 0 | Waterside: 62 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **532,540 G** *(284,050 G carryover + 248,490 G payout)*
- **Harvest & Ship** *(+206,400 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 20/20)
  - 87x Morrocorn *(Farm)* → +34,800 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 3x Shatollan Paprika *(Farm)* → +330 G (regrowth 9/9)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **532,540 G**
- **Plots Left**: Farm: 189 | Waterside: 77 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **738,940 G** *(532,540 G carryover + 206,400 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 11–30)

- **Starting Wallet (Day 11)**: 31,895 G
- **Ending Wallet (Day 31 Quietus)**: **738,940 G**
- **Pre-planted Crop Sales**: **+402,245 G**
- **New Planting Net Profit**: **+304,800 G**
- **Net Profit (20 days)**: **+707,045 G**
- **Average Daily Profit**: **+35,352 G/day** *(over 20 active days)*
