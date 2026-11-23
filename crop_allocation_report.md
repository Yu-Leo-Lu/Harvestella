# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 13
- **Planning Timeline**: Day 13 -> Day 30 (18d Quietus window)
- **Capital Budget**: 239,240 G
- **Plot Capacities (Usable / Max)**: Farm: 391/441 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Rainbow Bean** | 29 | Day 1 | D13, D15 | Freed D15 | +2,320 G |
| Farm | **Rainbow Bean** | 1 | Day 3 | D13, D15, D17 | Freed D17 | +120 G |
| Farm | **Royal Eggplant** | 46 | Day 10 | D15, D17, D19 | Freed D19 | +66,240 G |
| Farm | **Grass** | 44 | Day 11 | D13 | Freed D13 | +1,540 G |
| Farm | **Royal Eggplant** | 79 | Day 11 | D16, D18, D20 | Freed D20 | +113,760 G |
| Farm | **Stellar Wheat** | 99 | Day 11 | D13 | Freed D13 | +5,445 G |
| Farm | **Dress Lettuce** | 19 | Day 12 | D14 | Freed D14 | +1,615 G |
| Farm | **Lumpotato** | 1 | Day 12 | D15 | Freed D15 | +120 G |
| Farm | **Royal Eggplant** | 29 | Day 12 | D17, D19, D21 | Freed D21 | +41,760 G |
| Farm | **Unionion** | 41 | Day 12 | D15 | Freed D15 | +7,995 G |
| Waterside | **Honey Flower** | 55 | Day 7 | D13 | Freed D13 | +34,650 G |
| Waterside | **Honey Flower** | 22 | Day 11 | D17 | Freed D17 | +13,860 G |
| Cave | **Revol Pepper** | 22 | Day 1 | D14, D17 | Freed D17 | +11,660 G |
| Cave | **Curry Herbs** | 57 | Day 7 | D13 | Freed D13 | +19,950 G |
| Cave | **Sudor Pepper** | 2 | Day 10 | D13, D16, D19 | Freed D19 | +1,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 13**

- **Morning Wallet**: **239,240 G**
- **Harvest & Ship** *(+63,285 G arriving D14)*:
  - 44x Grass *(Farm)* → +1,540 G (freed)
  - 30x Rainbow Bean *(Farm)* → +1,200 G (regrowth 1/2)
  - 99x Stellar Wheat *(Farm)* → +5,445 G (freed)
  - 55x Honey Flower *(Waterside)* → +34,650 G (freed)
  - 57x Curry Herbs *(Cave)* → +19,950 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 57 | 31,920 G | D17..D29 (5x) | +43,605 G |
| Farm | **Grass** | Lethe | 25 | 750 G | D15 | +125 G |
| Farm | **Rainbow Bean** | Lethe | 15 | 2,700 G | D19..D27 (5x) | +300 G |
| Farm | **Unionion** | Lethe | 41 | 5,330 G | D16 | +2,665 G |
| Farm | **Morrocorn** | Shatolla | 64 | 12,800 G | D17 | +12,800 G |
| Waterside | **Honey Flower** | Shatolla | 55 | 20,900 G | D19 | +13,750 G |

- **Daily Seed Spent**: 74,400 G | **End-of-Day Wallet**: **164,840 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **228,125 G** *(164,840 G carryover + 63,285 G payout)*
- **Harvest & Ship** *(+7,445 G arriving D15)*:
  - 19x Dress Lettuce *(Farm)* → +1,615 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 10 | 800 G | D17 | +400 G |
| Farm | **Unionion** | Lethe | 9 | 1,170 G | D17 | +585 G |

- **Daily Seed Spent**: 1,970 G | **End-of-Day Wallet**: **226,155 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **233,600 G** *(226,155 G carryover + 7,445 G payout)*
- **Harvest & Ship** *(+32,270 G arriving D16)*:
  - 25x Grass *(Farm)* → +875 G (freed)
  - 1x Lumpotato *(Farm)* → +120 G (freed)
  - 30x Rainbow Bean *(Farm)* → +1,200 G (regrowth 2/2)
  - 46x Royal Eggplant *(Farm)* → +22,080 G (regrowth 1/3)
  - 41x Unionion *(Farm)* → +7,995 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 46 | 3,680 G | D18 | +1,840 G |
| Farm | **Lumpotato** | Lethe | 50 | 4,500 G | D18 | +1,500 G |

- **Daily Seed Spent**: 8,180 G | **End-of-Day Wallet**: **225,420 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **257,690 G** *(225,420 G carryover + 32,270 G payout)*
- **Harvest & Ship** *(+46,415 G arriving D17)*:
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 1/3)
  - 41x Unionion *(Farm)* → +7,995 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Rainbow Bean** | Lethe | 41 | 7,380 G | D22..D30 (5x) | +820 G |

- **Daily Seed Spent**: 7,380 G | **End-of-Day Wallet**: **250,310 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **296,725 G** *(250,310 G carryover + 46,415 G payout)*
- **Harvest & Ship** *(+99,390 G arriving D18)*:
  - 10x Lumpotato *(Farm)* → +1,200 G (freed)
  - 64x Morrocorn *(Farm)* → +25,600 G (freed)
  - 1x Rainbow Bean *(Farm)* → +40 G (regrowth 3/3)
  - 75x Royal Eggplant *(Farm)* → +36,000 G (regrowth 2/3)
  - 9x Unionion *(Farm)* → +1,755 G (freed)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 79x Revol Pepper *(Cave)* → +20,935 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 22 | 12,320 G | D21..D30 (4x) | +11,000 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D21 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 35 | 7,000 G | D21 | +7,000 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D23 | +5,500 G |

- **Daily Seed Spent**: 39,180 G | **End-of-Day Wallet**: **257,545 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **356,935 G** *(257,545 G carryover + 99,390 G payout)*
- **Harvest & Ship** *(+49,440 G arriving D19)*:
  - 96x Lumpotato *(Farm)* → +11,520 G (freed)
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 38 | 3,040 G | D21 | +1,520 G |
| Farm | **Unionion** | Nemea | 58 | 6,090 G | D21 | +5,220 G |

- **Daily Seed Spent**: 9,130 G | **End-of-Day Wallet**: **347,805 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **397,245 G** *(347,805 G carryover + 49,440 G payout)*
- **Harvest & Ship** *(+71,750 G arriving D20)*:
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 1/5)
  - 75x Royal Eggplant *(Farm)* → +36,000 G (regrowth 3/3)
  - 55x Honey Flower *(Waterside)* → +34,650 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 2 | 800 G | D22, D25, D28 | +700 G |
| Farm | **Dress Lettuce** | Lethe | 46 | 2,530 G | D21 | +1,380 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D23, D26, D29 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 45 | 16,650 G | D23, D26, D29 | +17,100 G |

- **Daily Seed Spent**: 23,680 G | **End-of-Day Wallet**: **373,565 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **445,315 G** *(373,565 G carryover + 71,750 G payout)*
- **Harvest & Ship** *(+53,025 G arriving D21)*:
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 3/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 2 | 160 G | D23 | +80 G |
| Farm | **Dress Lettuce** | Lethe | 34 | 1,870 G | D22 | +1,020 G |
| Farm | **Grass** | Lethe | 43 | 1,290 G | D22 | +215 G |

- **Daily Seed Spent**: 3,320 G | **End-of-Day Wallet**: **441,995 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **495,020 G** *(441,995 G carryover + 53,025 G payout)*
- **Harvest & Ship** *(+74,130 G arriving D22)*:
  - 46x Dress Lettuce *(Farm)* → +3,910 G (freed)
  - 38x Lumpotato *(Farm)* → +4,560 G (freed)
  - 85x Morrocorn *(Farm)* → +34,000 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 2/5)
  - 29x Royal Eggplant *(Farm)* → +13,920 G (regrowth 3/3)
  - 58x Unionion *(Farm)* → +11,310 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 59 | 1,770 G | D23 | +295 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D26, D28, D30 | +65,340 G |
| Farm | **Stellar Wheat** | Lethe | 96 | 3,840 G | D23 | +1,440 G |

- **Daily Seed Spent**: 82,830 G | **End-of-Day Wallet**: **412,190 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **486,320 G** *(412,190 G carryover + 74,130 G payout)*
- **Harvest & Ship** *(+6,535 G arriving D23)*:
  - 34x Dress Lettuce *(Farm)* → +2,890 G (freed)
  - 43x Grass *(Farm)* → +1,505 G (freed)
  - 41x Rainbow Bean *(Farm)* → +1,640 G (regrowth 1/5)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 75 | 4,125 G | D24 | +2,250 G |
| Farm | **Stellar Wheat** | Lethe | 3 | 120 G | D24 | +45 G |

- **Daily Seed Spent**: 4,245 G | **End-of-Day Wallet**: **482,075 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **488,610 G** *(482,075 G carryover + 6,535 G payout)*
- **Harvest & Ship** *(+50,900 G arriving D24)*:
  - 59x Grass *(Farm)* → +2,065 G (freed)
  - 2x Lumpotato *(Farm)* → +240 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 3/5)
  - 96x Stellar Wheat *(Farm)* → +5,280 G (freed)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 1/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 35 | 2,800 G | D26 | +1,400 G |
| Farm | **Dress Lettuce** | Lethe | 24 | 1,320 G | D25 | +720 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D26 | +8,910 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D29 | +5,500 G |

- **Daily Seed Spent**: 22,875 G | **End-of-Day Wallet**: **465,735 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **516,635 G** *(465,735 G carryover + 50,900 G payout)*
- **Harvest & Ship** *(+14,010 G arriving D25)*:
  - 75x Dress Lettuce *(Farm)* → +6,375 G (freed)
  - 41x Rainbow Bean *(Farm)* → +1,640 G (regrowth 2/5)
  - 3x Stellar Wheat *(Farm)* → +165 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 62 | 4,960 G | D27 | +2,480 G |
| Farm | **Grass** | Lethe | 15 | 450 G | D26 | +75 G |

- **Daily Seed Spent**: 5,410 G | **End-of-Day Wallet**: **511,225 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **525,235 G** *(511,225 G carryover + 14,010 G payout)*
- **Harvest & Ship** *(+3,140 G arriving D26)*:
  - 24x Dress Lettuce *(Farm)* → +2,040 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 4/5)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 24 | 720 G | D27 | +120 G |

- **Daily Seed Spent**: 720 G | **End-of-Day Wallet**: **524,515 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **527,655 G** *(524,515 G carryover + 3,140 G payout)*
- **Harvest & Ship** *(+102,045 G arriving D27)*:
  - 15x Grass *(Farm)* → +525 G (freed)
  - 35x Lumpotato *(Farm)* → +4,200 G (freed)
  - 41x Rainbow Bean *(Farm)* → +1,640 G (regrowth 3/5)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 2/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 31,300 G | **End-of-Day Wallet**: **496,355 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **598,400 G** *(496,355 G carryover + 102,045 G payout)*
- **Harvest & Ship** *(+14,710 G arriving D28)*:
  - 24x Grass *(Farm)* → +840 G (freed)
  - 62x Lumpotato *(Farm)* → +7,440 G (freed)
  - 15x Rainbow Bean *(Farm)* → +600 G (regrowth 5/5)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 2 | 160 G | D30 | +80 G |
| Farm | **Lumpotato** | Lethe | 50 | 4,500 G | D30 | +1,500 G |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D30 | +3,250 G |

- **Daily Seed Spent**: 11,160 G | **End-of-Day Wallet**: **587,240 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **601,950 G** *(587,240 G carryover + 14,710 G payout)*
- **Harvest & Ship** *(+49,660 G arriving D29)*:
  - 41x Rainbow Bean *(Farm)* → +1,640 G (regrowth 4/5)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **601,950 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 2

---

#### **Day 29**

- **Morning Wallet**: **651,610 G** *(601,950 G carryover + 49,660 G payout)*
- **Harvest & Ship** *(+42,715 G arriving D30)*:
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 3/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **651,610 G**
- **Plots Left**: Farm: 0 | Waterside: 77 | Cave: 59

---

#### **Day 30**

- **Morning Wallet**: **694,325 G** *(651,610 G carryover + 42,715 G payout)*
- **Harvest & Ship** *(+130,580 G arriving D31)*:
  - 52x Lumpotato *(Farm)* → +6,240 G (freed)
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 41x Rainbow Bean *(Farm)* → +1,640 G (regrowth 5/5)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)
  - 50x Unionion *(Farm)* → +9,750 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **694,325 G**
- **Plots Left**: Farm: 391 | Waterside: 77 | Cave: 59

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **824,905 G** *(694,325 G carryover + 130,580 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 13–30)

- **Starting Wallet (Day 13)**: 239,240 G
- **Ending Wallet (Day 31 Quietus)**: **824,905 G**
- **Pre-planted Crop Sales**: **+322,535 G**
- **New Planting Net Profit**: **+263,130 G**
- **Net Profit (18 days)**: **+585,665 G**
- **Average Daily Profit**: **+32,537 G/day** *(over 18 active days)*
