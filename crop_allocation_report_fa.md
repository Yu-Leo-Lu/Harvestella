# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 236,090 G
- **Plot Capacities (Usable / Max)**: Farm: 294/294 | Waterside: 81/81 | Cave: 81/81

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 1**

- **Morning Wallet**: **236,090 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D5..D17 (5x) | +61,965 G |
| Farm | **Grass** | Lethe | 99 | 2,970 G | D3 | +495 G |
| Farm | **Lumpotato** | Lethe | 13 | 1,170 G | D4 | +390 G |
| Farm | **Rainbow Bean** | Lethe | 15 | 2,700 G | D7..D15 (5x) | +300 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D8, D10, D12 | +65,340 G |
| Farm | **Stellar Wheat** | Lethe | 50 | 2,000 G | D3 | +750 G |
| Farm | **Unionion** | Lethe | 18 | 2,340 G | D4 | +1,170 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D5, D8, D11 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 71 | 26,270 G | D5, D8, D11 | +26,980 G |

- **Daily Seed Spent**: 163,730 G | **End-of-Day Wallet**: **72,360 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **72,360 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **72,360 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **72,360 G**
- **Harvest & Ship** *(+6,215 G arriving D4)*:
  - 99x Grass *(Farm)* → +3,465 G (freed)
  - 50x Stellar Wheat *(Farm)* → +2,750 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 99 | 5,445 G | D5 | +2,970 G |
| Farm | **Stellar Wheat** | Lethe | 49 | 1,960 G | D5 | +735 G |

- **Daily Seed Spent**: 7,405 G | **End-of-Day Wallet**: **64,955 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **71,170 G** *(64,955 G carryover + 6,215 G payout)*
- **Harvest & Ship** *(+5,070 G arriving D5)*:
  - 13x Lumpotato *(Farm)* → +1,560 G (freed)
  - 18x Unionion *(Farm)* → +3,510 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 31 | 2,790 G | D7 | +930 G |

- **Daily Seed Spent**: 2,790 G | **End-of-Day Wallet**: **68,380 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **73,450 G** *(68,380 G carryover + 5,070 G payout)*
- **Harvest & Ship** *(+52,825 G arriving D6)*:
  - 99x Dress Lettuce *(Farm)* → +8,415 G (freed)
  - 49x Stellar Wheat *(Farm)* → +2,695 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D8 | +3,960 G |
| Farm | **Unionion** | Lethe | 49 | 6,370 G | D8 | +3,185 G |

- **Daily Seed Spent**: 14,290 G | **End-of-Day Wallet**: **59,160 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **111,985 G** *(59,160 G carryover + 52,825 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **111,985 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **111,985 G**
- **Harvest & Ship** *(+4,320 G arriving D8)*:
  - 31x Lumpotato *(Farm)* → +3,720 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 32 | 4,160 G | D10 | +2,080 G |

- **Daily Seed Spent**: 4,160 G | **End-of-Day Wallet**: **107,825 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **112,145 G** *(107,825 G carryover + 4,320 G payout)*
- **Harvest & Ship** *(+110,670 G arriving D9)*:
  - 99x Lumpotato *(Farm)* → +11,880 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)
  - 49x Unionion *(Farm)* → +9,555 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 49 | 4,410 G | D11 | +1,470 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D11 | +8,910 G |

- **Daily Seed Spent**: 14,805 G | **End-of-Day Wallet**: **97,340 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **208,010 G** *(97,340 G carryover + 110,670 G payout)*
- **Harvest & Ship** *(+600 G arriving D10)*:
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **208,010 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **208,610 G** *(208,010 G carryover + 600 G payout)*
- **Harvest & Ship** *(+53,760 G arriving D11)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)
  - 32x Unionion *(Farm)* → +6,240 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 4 | 360 G | D13 | +120 G |

- **Daily Seed Spent**: 360 G | **End-of-Day Wallet**: **208,250 G**
- **Plots Left**: Farm: 28 | Waterside: 0 | Cave: 0

---

#### **Day 11**

- **Morning Wallet**: **262,010 G** *(208,250 G carryover + 53,760 G payout)*
- **Harvest & Ship** *(+67,500 G arriving D12)*:
  - 49x Lumpotato *(Farm)* → +5,880 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 3/5)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 53 | 2,915 G | D13 | +1,590 G |
| Farm | **Grass** | Lethe | 6 | 180 G | D13 | +30 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D18, D20, D22 | +65,340 G |
| Farm | **Stellar Wheat** | Lethe | 18 | 720 G | D13 | +270 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D15, D18, D21 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 71 | 26,270 G | D15, D18, D21 | +26,980 G |

- **Daily Seed Spent**: 111,005 G | **End-of-Day Wallet**: **151,005 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **218,505 G** *(151,005 G carryover + 67,500 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D13)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 46 | 1,380 G | D14 | +230 G |
| Farm | **Unionion** | Nemea | 53 | 5,565 G | D15 | +4,770 G |

- **Daily Seed Spent**: 6,945 G | **End-of-Day Wallet**: **211,560 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **259,080 G** *(211,560 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+6,785 G arriving D14)*:
  - 53x Dress Lettuce *(Farm)* → +4,505 G (freed)
  - 6x Grass *(Farm)* → +210 G (freed)
  - 4x Lumpotato *(Farm)* → +480 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 4/5)
  - 18x Stellar Wheat *(Farm)* → +990 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Stellar Wheat** | Lethe | 81 | 3,240 G | D15 | +1,215 G |

- **Daily Seed Spent**: 3,240 G | **End-of-Day Wallet**: **255,840 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **262,625 G** *(255,840 G carryover + 6,785 G payout)*
- **Harvest & Ship** *(+23,075 G arriving D15)*:
  - 46x Grass *(Farm)* → +1,610 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 46 | 1,380 G | D16 | +230 G |

- **Daily Seed Spent**: 1,380 G | **End-of-Day Wallet**: **261,245 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **284,320 G** *(261,245 G carryover + 23,075 G payout)*
- **Harvest & Ship** *(+35,640 G arriving D16)*:
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 5/5)
  - 81x Stellar Wheat *(Farm)* → +4,455 G (freed)
  - 53x Unionion *(Farm)* → +10,335 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D18 | +3,960 G |
| Farm | **Lumpotato** | Lethe | 50 | 4,500 G | D18 | +1,500 G |

- **Daily Seed Spent**: 12,420 G | **End-of-Day Wallet**: **271,900 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **307,540 G** *(271,900 G carryover + 35,640 G payout)*
- **Harvest & Ship** *(+1,610 G arriving D17)*:
  - 46x Grass *(Farm)* → +1,610 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 46 | 2,530 G | D18 | +1,380 G |

- **Daily Seed Spent**: 2,530 G | **End-of-Day Wallet**: **305,010 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **306,620 G** *(305,010 G carryover + 1,610 G payout)*
- **Harvest & Ship** *(+21,465 G arriving D18)*:
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D21..D30 (4x) | +40,500 G |

- **Daily Seed Spent**: 45,360 G | **End-of-Day Wallet**: **261,260 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **282,725 G** *(261,260 G carryover + 21,465 G payout)*
- **Harvest & Ship** *(+89,560 G arriving D19)*:
  - 46x Dress Lettuce *(Farm)* → +3,910 G (freed)
  - 149x Lumpotato *(Farm)* → +17,880 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 49 | 4,410 G | D21 | +1,470 G |
| Farm | **Unionion** | Lethe | 99 | 12,870 G | D21 | +6,435 G |
| Farm | **Unionion** | Nemea | 46 | 4,830 G | D21 | +4,140 G |

- **Daily Seed Spent**: 22,110 G | **End-of-Day Wallet**: **260,615 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **350,175 G** *(260,615 G carryover + 89,560 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **350,175 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **350,175 G**
- **Harvest & Ship** *(+47,520 G arriving D21)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **350,175 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **397,695 G** *(350,175 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+75,870 G arriving D22)*:
  - 49x Lumpotato *(Farm)* → +5,880 G (freed)
  - 145x Unionion *(Farm)* → +28,275 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Stellar Wheat** | Lethe | 45 | 1,800 G | D23 | +675 G |
| Farm | **Unionion** | Lethe | 51 | 6,630 G | D24 | +3,315 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D25, D28 | +1,300 G |
| Waterside | **Nectarcane** | Shatolla | 71 | 26,270 G | D25, D28 | +9,230 G |

- **Daily Seed Spent**: 115,620 G | **End-of-Day Wallet**: **282,075 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **357,945 G** *(282,075 G carryover + 75,870 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D23)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 90 | 4,950 G | D24 | +2,700 G |
| Farm | **Stellar Wheat** | Lethe | 9 | 360 G | D24 | +135 G |

- **Daily Seed Spent**: 5,310 G | **End-of-Day Wallet**: **352,635 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **400,155 G** *(352,635 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+2,475 G arriving D24)*:
  - 45x Stellar Wheat *(Farm)* → +2,475 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 9 | 495 G | D25 | +270 G |
| Farm | **Grass** | Lethe | 36 | 1,080 G | D25 | +180 G |

- **Daily Seed Spent**: 1,575 G | **End-of-Day Wallet**: **398,580 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **401,055 G** *(398,580 G carryover + 2,475 G payout)*
- **Harvest & Ship** *(+39,555 G arriving D25)*:
  - 90x Dress Lettuce *(Farm)* → +7,650 G (freed)
  - 9x Stellar Wheat *(Farm)* → +495 G (freed)
  - 51x Unionion *(Farm)* → +9,945 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 3 | 240 G | D27 | +120 G |
| Farm | **Lumpotato** | Lethe | 99 | 8,910 G | D27 | +2,970 G |
| Farm | **Unionion** | Lethe | 48 | 6,240 G | D27 | +3,120 G |

- **Daily Seed Spent**: 15,390 G | **End-of-Day Wallet**: **385,665 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **425,220 G** *(385,665 G carryover + 39,555 G payout)*
- **Harvest & Ship** *(+22,275 G arriving D26)*:
  - 9x Dress Lettuce *(Farm)* → +765 G (freed)
  - 36x Grass *(Farm)* → +1,260 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Stellar Wheat** | Lethe | 45 | 1,800 G | D27 | +675 G |

- **Daily Seed Spent**: 1,800 G | **End-of-Day Wallet**: **423,420 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **445,695 G** *(423,420 G carryover + 22,275 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **445,695 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **445,695 G**
- **Harvest & Ship** *(+45,540 G arriving D28)*:
  - 102x Lumpotato *(Farm)* → +12,240 G (freed)
  - 45x Stellar Wheat *(Farm)* → +2,475 G (freed)
  - 48x Unionion *(Farm)* → +9,360 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 96 | 7,680 G | D30 | +3,840 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D30 | +8,910 G |

- **Daily Seed Spent**: 18,075 G | **End-of-Day Wallet**: **427,620 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **473,160 G** *(427,620 G carryover + 45,540 G payout)*
- **Harvest & Ship** *(+67,770 G arriving D29)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/2)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **473,160 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 29**

- **Morning Wallet**: **540,930 G** *(473,160 G carryover + 67,770 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **540,930 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 30**

- **Morning Wallet**: **540,930 G**
- **Harvest & Ship** *(+99,810 G arriving D31)*:
  - 96x Lumpotato *(Farm)* → +11,520 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/2)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **540,930 G**
- **Plots Left**: Farm: 195 | Waterside: 0 | Cave: 0

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **640,740 G** *(540,930 G carryover + 99,810 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 236,090 G
- **Ending Wallet (Day 31 Quietus)**: **640,740 G**
- **Net Profit (30 days)**: **+404,650 G**
- **Average Daily Profit**: **+13,488 G/day** *(over 30 active days)*
