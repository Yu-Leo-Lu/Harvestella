# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 12
- **Planning Timeline**: Day 12 -> Day 30 (19d Quietus window)
- **Capital Budget**: 230,485 G
- **Plot Capacities (Usable / Max)**: Farm: 379/441 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Lantern Pumpkin** | 2 | Day 1 | D12 | Freed D12 | +7,500 G |
| Farm | **Rainbow Bean** | 29 | Day 1 | D13, D15 | Freed D15 | +2,320 G |
| Farm | **Rainbow Bean** | 1 | Day 3 | D13, D15, D17 | Freed D17 | +120 G |
| Farm | **Royal Eggplant** | 42 | Day 3 | D12 | Freed D12 | +20,160 G |
| Farm | **Morrocorn** | 14 | Day 8 | D12 | Freed D12 | +5,600 G |
| Farm | **Unionion** | 24 | Day 9 | D12 | Freed D12 | +4,680 G |
| Farm | **Royal Eggplant** | 46 | Day 10 | D15, D17, D19 | Freed D19 | +66,240 G |
| Farm | **Grass** | 41 | Day 11 | D13 | Freed D13 | +1,435 G |
| Farm | **Royal Eggplant** | 79 | Day 11 | D16, D18, D20 | Freed D20 | +113,760 G |
| Farm | **Stellar Wheat** | 99 | Day 11 | D13 | Freed D13 | +5,445 G |
| Waterside | **Honey Flower** | 55 | Day 7 | D13 | Freed D13 | +34,650 G |
| Waterside | **Honey Flower** | 22 | Day 11 | D17 | Freed D17 | +13,860 G |
| Cave | **Revol Pepper** | 22 | Day 1 | D14, D17 | Freed D17 | +11,660 G |
| Cave | **Curry Herbs** | 57 | Day 7 | D13 | Freed D13 | +19,950 G |
| Cave | **Sudor Pepper** | 2 | Day 10 | D13, D16, D19 | Freed D19 | +1,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 12**

- **Morning Wallet**: **230,485 G**
- **Harvest & Ship** *(+37,940 G arriving D13)*:
  - 2x Lantern Pumpkin *(Farm)* → +7,500 G (freed)
  - 14x Morrocorn *(Farm)* → +5,600 G (freed)
  - 42x Royal Eggplant *(Farm)* → +20,160 G (regrowth 1/1)
  - 24x Unionion *(Farm)* → +4,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 11 | 330 G | D14 | +55 G |
| Farm | **Royal Eggplant** | Lethe | 29 | 22,620 G | D17, D19, D21 | +19,140 G |
| Farm | **Unionion** | Lethe | 44 | 5,720 G | D15 | +2,860 G |

- **Daily Seed Spent**: 28,670 G | **End-of-Day Wallet**: **201,815 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **239,755 G** *(201,815 G carryover + 37,940 G payout)*
- **Harvest & Ship** *(+63,180 G arriving D14)*:
  - 41x Grass *(Farm)* → +1,435 G (freed)
  - 30x Rainbow Bean *(Farm)* → +1,200 G (regrowth 1/2)
  - 99x Stellar Wheat *(Farm)* → +5,445 G (freed)
  - 55x Honey Flower *(Waterside)* → +34,650 G (freed)
  - 57x Curry Herbs *(Cave)* → +19,950 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 36 | 2,880 G | D16 | +1,440 G |
| Cave | **Revol Pepper** | Argene | 57 | 31,920 G | D17..D29 (5x) | +43,605 G |
| Farm | **Grass** | Lethe | 31 | 930 G | D15 | +155 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D17 | +8,500 G |
| Farm | **Rainbow Bean** | Lethe | 5 | 900 G | D19..D27 (5x) | +100 G |
| Farm | **Morrocorn** | Shatolla | 18 | 3,600 G | D17 | +3,600 G |
| Waterside | **Honey Flower** | Shatolla | 55 | 20,900 G | D19 | +13,750 G |

- **Daily Seed Spent**: 72,630 G | **End-of-Day Wallet**: **167,125 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **230,305 G** *(167,125 G carryover + 63,180 G payout)*
- **Harvest & Ship** *(+6,215 G arriving D15)*:
  - 11x Grass *(Farm)* → +385 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 11 | 880 G | D17 | +440 G |

- **Daily Seed Spent**: 880 G | **End-of-Day Wallet**: **229,425 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **235,640 G** *(229,425 G carryover + 6,215 G payout)*
- **Harvest & Ship** *(+32,945 G arriving D16)*:
  - 31x Grass *(Farm)* → +1,085 G (freed)
  - 30x Rainbow Bean *(Farm)* → +1,200 G (regrowth 2/2)
  - 46x Royal Eggplant *(Farm)* → +22,080 G (regrowth 1/3)
  - 44x Unionion *(Farm)* → +8,580 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 4 | 520 G | D18 | +260 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D18 | +8,910 G |

- **Daily Seed Spent**: 10,915 G | **End-of-Day Wallet**: **224,725 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **257,670 G** *(224,725 G carryover + 32,945 G payout)*
- **Harvest & Ship** *(+42,740 G arriving D17)*:
  - 36x Lumpotato *(Farm)* → +4,320 G (freed)
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 1/3)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Rainbow Bean** | Lethe | 36 | 6,480 G | D22..D30 (5x) | +720 G |

- **Daily Seed Spent**: 6,480 G | **End-of-Day Wallet**: **251,190 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **293,930 G** *(251,190 G carryover + 42,740 G payout)*
- **Harvest & Ship** *(+99,355 G arriving D18)*:
  - 11x Lumpotato *(Farm)* → +1,320 G (freed)
  - 68x Morrocorn *(Farm)* → +27,200 G (freed)
  - 1x Rainbow Bean *(Farm)* → +40 G (regrowth 3/3)
  - 75x Royal Eggplant *(Farm)* → +36,000 G (regrowth 2/3)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 79x Revol Pepper *(Cave)* → +20,935 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 22 | 12,320 G | D21..D30 (4x) | +11,000 G |
| Farm | **Morrocorn** | Shatolla | 81 | 16,200 G | D21 | +16,200 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D23 | +5,500 G |

- **Daily Seed Spent**: 36,880 G | **End-of-Day Wallet**: **257,050 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **356,405 G** *(257,050 G carryover + 99,355 G payout)*
- **Harvest & Ship** *(+58,005 G arriving D19)*:
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 2/3)
  - 103x Unionion *(Farm)* → +20,085 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 51 | 4,080 G | D21 | +2,040 G |
| Farm | **Lumpotato** | Lethe | 50 | 4,500 G | D21 | +1,500 G |
| Farm | **Unionion** | Lethe | 2 | 260 G | D21 | +130 G |

- **Daily Seed Spent**: 8,840 G | **End-of-Day Wallet**: **347,565 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **405,570 G** *(347,565 G carryover + 58,005 G payout)*
- **Harvest & Ship** *(+71,350 G arriving D20)*:
  - 5x Rainbow Bean *(Farm)* → +200 G (regrowth 1/5)
  - 75x Royal Eggplant *(Farm)* → +36,000 G (regrowth 3/3)
  - 55x Honey Flower *(Waterside)* → +34,650 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 2 | 800 G | D22, D25, D28 | +700 G |
| Farm | **Dress Lettuce** | Lethe | 20 | 1,100 G | D21 | +600 G |
| Farm | **Grass** | Lethe | 26 | 780 G | D21 | +130 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D23, D26, D29 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 45 | 16,650 G | D23, D26, D29 | +17,100 G |

- **Daily Seed Spent**: 23,030 G | **End-of-Day Wallet**: **382,540 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **453,890 G** *(382,540 G carryover + 71,350 G payout)*
- **Harvest & Ship** *(+53,025 G arriving D21)*:
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 3/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 79 | 4,345 G | D22 | +2,370 G |

- **Daily Seed Spent**: 4,345 G | **End-of-Day Wallet**: **449,545 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **502,570 G** *(449,545 G carryover + 53,025 G payout)*
- **Harvest & Ship** *(+67,470 G arriving D22)*:
  - 20x Dress Lettuce *(Farm)* → +1,700 G (freed)
  - 26x Grass *(Farm)* → +910 G (freed)
  - 101x Lumpotato *(Farm)* → +12,120 G (freed)
  - 81x Morrocorn *(Farm)* → +32,400 G (freed)
  - 5x Rainbow Bean *(Farm)* → +200 G (regrowth 2/5)
  - 29x Royal Eggplant *(Farm)* → +13,920 G (regrowth 3/3)
  - 2x Unionion *(Farm)* → +390 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 99 | 5,445 G | D23 | +2,970 G |
| Farm | **Grass** | Lethe | 41 | 1,230 G | D23 | +205 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D26, D28, D30 | +65,340 G |
| Farm | **Stellar Wheat** | Lethe | 20 | 800 G | D23 | +300 G |

- **Daily Seed Spent**: 84,695 G | **End-of-Day Wallet**: **417,875 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **485,345 G** *(417,875 G carryover + 67,470 G payout)*
- **Harvest & Ship** *(+8,655 G arriving D23)*:
  - 79x Dress Lettuce *(Farm)* → +6,715 G (freed)
  - 36x Rainbow Bean *(Farm)* → +1,440 G (regrowth 1/5)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Stellar Wheat** | Lethe | 79 | 3,160 G | D24 | +1,185 G |

- **Daily Seed Spent**: 3,160 G | **End-of-Day Wallet**: **482,185 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **490,840 G** *(482,185 G carryover + 8,655 G payout)*
- **Harvest & Ship** *(+53,865 G arriving D24)*:
  - 99x Dress Lettuce *(Farm)* → +8,415 G (freed)
  - 41x Grass *(Farm)* → +1,435 G (freed)
  - 5x Rainbow Bean *(Farm)* → +200 G (regrowth 3/5)
  - 20x Stellar Wheat *(Farm)* → +1,100 G (freed)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 1/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 87 | 6,960 G | D26 | +3,480 G |
| Farm | **Grass** | Lethe | 23 | 690 G | D25 | +115 G |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D26 | +3,250 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D29 | +5,500 G |

- **Daily Seed Spent**: 22,510 G | **End-of-Day Wallet**: **468,330 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **522,195 G** *(468,330 G carryover + 53,865 G payout)*
- **Harvest & Ship** *(+11,615 G arriving D25)*:
  - 36x Rainbow Bean *(Farm)* → +1,440 G (regrowth 2/5)
  - 79x Stellar Wheat *(Farm)* → +4,345 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 12 | 960 G | D27 | +480 G |
| Farm | **Grass** | Lethe | 12 | 360 G | D26 | +60 G |
| Farm | **Unionion** | Nemea | 55 | 5,775 G | D27 | +4,950 G |

- **Daily Seed Spent**: 7,095 G | **End-of-Day Wallet**: **515,100 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **526,715 G** *(515,100 G carryover + 11,615 G payout)*
- **Harvest & Ship** *(+1,505 G arriving D26)*:
  - 23x Grass *(Farm)* → +805 G (freed)
  - 5x Rainbow Bean *(Farm)* → +200 G (regrowth 4/5)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 23 | 690 G | D27 | +115 G |

- **Daily Seed Spent**: 690 G | **End-of-Day Wallet**: **526,025 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **527,530 G** *(526,025 G carryover + 1,505 G payout)*
- **Harvest & Ship** *(+98,425 G arriving D27)*:
  - 12x Grass *(Farm)* → +420 G (freed)
  - 87x Lumpotato *(Farm)* → +10,440 G (freed)
  - 36x Rainbow Bean *(Farm)* → +1,440 G (regrowth 3/5)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)
  - 50x Unionion *(Farm)* → +9,750 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 2/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 31,300 G | **End-of-Day Wallet**: **496,230 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **594,655 G** *(496,230 G carryover + 98,425 G payout)*
- **Harvest & Ship** *(+19,000 G arriving D28)*:
  - 23x Grass *(Farm)* → +805 G (freed)
  - 12x Lumpotato *(Farm)* → +1,440 G (freed)
  - 5x Rainbow Bean *(Farm)* → +200 G (regrowth 5/5)
  - 55x Unionion *(Farm)* → +10,725 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 50 | 4,500 G | D30 | +1,500 G |
| Farm | **Unionion** | Nemea | 44 | 4,620 G | D30 | +3,960 G |

- **Daily Seed Spent**: 9,120 G | **End-of-Day Wallet**: **585,535 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **604,535 G** *(585,535 G carryover + 19,000 G payout)*
- **Harvest & Ship** *(+49,460 G arriving D29)*:
  - 36x Rainbow Bean *(Farm)* → +1,440 G (regrowth 4/5)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **604,535 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 2

---

#### **Day 29**

- **Morning Wallet**: **653,995 G** *(604,535 G carryover + 49,460 G payout)*
- **Harvest & Ship** *(+42,715 G arriving D30)*:
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 3/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **653,995 G**
- **Plots Left**: Farm: 1 | Waterside: 77 | Cave: 59

---

#### **Day 30**

- **Morning Wallet**: **696,710 G** *(653,995 G carryover + 42,715 G payout)*
- **Harvest & Ship** *(+128,970 G arriving D31)*:
  - 50x Lumpotato *(Farm)* → +6,000 G (freed)
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 36x Rainbow Bean *(Farm)* → +1,440 G (regrowth 5/5)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)
  - 44x Unionion *(Farm)* → +8,580 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **696,710 G**
- **Plots Left**: Farm: 379 | Waterside: 77 | Cave: 59

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **825,680 G** *(696,710 G carryover + 128,970 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 12–30)

- **Starting Wallet (Day 12)**: 230,485 G
- **Ending Wallet (Day 31 Quietus)**: **825,680 G**
- **Pre-planted Crop Sales**: **+308,880 G**
- **New Planting Net Profit**: **+286,315 G**
- **Net Profit (19 days)**: **+595,195 G**
- **Average Daily Profit**: **+31,326 G/day** *(over 19 active days)*
