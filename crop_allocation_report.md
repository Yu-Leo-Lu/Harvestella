# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 12
- **Planning Timeline**: Day 12 -> Day 30 (19d Quietus window)
- **Capital Budget**: 230,485 G
- **Plot Capacities (Usable / Max)**: Farm: 394/441 | Waterside: 77/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Lantern Pumpkin** | 2 | Day 1 | D12 | Freed D12 | +7,500 G |
| Farm | **Rainbow Bean** | 29 | Day 1 | D13, D15 | Freed D15 | +2,320 G |
| Farm | **Royal Eggplant** | 6 | Day 1 | D12 | Freed D12 | +2,880 G |
| Farm | **Rainbow Bean** | 1 | Day 3 | D13, D15, D17 | Freed D17 | +120 G |
| Farm | **Royal Eggplant** | 43 | Day 3 | D12, D14 | Freed D14 | +41,280 G |
| Farm | **Morrocorn** | 14 | Day 8 | D12 | Freed D12 | +5,600 G |
| Farm | **Unionion** | 24 | Day 9 | D12 | Freed D12 | +4,680 G |
| Farm | **Royal Eggplant** | 47 | Day 10 | D17, D19, D21 | Freed D21 | +67,680 G |
| Farm | **Grass** | 41 | Day 11 | D13 | Freed D13 | +1,435 G |
| Farm | **Royal Eggplant** | 79 | Day 11 | D18, D20, D22 | Freed D22 | +113,760 G |
| Farm | **Stellar Wheat** | 99 | Day 11 | D13 | Freed D13 | +5,445 G |
| Waterside | **Honey Flower** | 55 | Day 7 | D13 | Freed D13 | +34,650 G |
| Waterside | **Honey Flower** | 22 | Day 11 | D17 | Freed D17 | +13,860 G |
| Cave | **Revol Pepper** | 22 | Day 1 | D14, D17 | Freed D17 | +11,660 G |
| Cave | **Curry Herbs** | 57 | Day 7 | D13 | Freed D13 | +19,950 G |
| Cave | **Sudor Pepper** | 2 | Day 10 | D13, D16, D19 | Freed D19 | +1,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 12**

- **Morning Wallet**: **230,485 G**
- **Harvest & Ship** *(+41,300 G arriving D13)*:
  - 2x Lantern Pumpkin *(Farm)* → +7,500 G (freed)
  - 14x Morrocorn *(Farm)* → +5,600 G (freed)
  - 49x Royal Eggplant *(Farm)* → +23,520 G (regrowth 1/1)
  - 24x Unionion *(Farm)* → +4,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 55 | 1,650 G | D14 | +275 G |

- **Daily Seed Spent**: 1,650 G | **End-of-Day Wallet**: **228,835 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **270,135 G** *(228,835 G carryover + 41,300 G payout)*
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
| Cave | **Revol Pepper** | Argene | 57 | 31,920 G | D17..D29 (5x) | +43,605 G |
| Farm | **Dress Lettuce** | Lethe | 76 | 4,180 G | D15 | +2,280 G |
| Farm | **Grass** | Lethe | 13 | 390 G | D15 | +65 G |
| Farm | **Lumpotato** | Lethe | 41 | 3,690 G | D16 | +1,230 G |
| Farm | **Morrocorn** | Lethe | 10 | 2,300 G | D17 | +1,700 G |
| Waterside | **Honey Flower** | Shatolla | 55 | 20,900 G | D19 | +13,750 G |

- **Daily Seed Spent**: 63,380 G | **End-of-Day Wallet**: **206,755 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **269,935 G** *(206,755 G carryover + 63,180 G payout)*
- **Harvest & Ship** *(+28,395 G arriving D15)*:
  - 55x Grass *(Farm)* → +1,925 G (freed)
  - 43x Royal Eggplant *(Farm)* → +20,640 G (regrowth 2/2)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D17 | +3,250 G |
| Farm | **Unionion** | Nemea | 48 | 5,040 G | D17 | +4,320 G |

- **Daily Seed Spent**: 11,540 G | **End-of-Day Wallet**: **258,395 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **286,790 G** *(258,395 G carryover + 28,395 G payout)*
- **Harvest & Ship** *(+8,115 G arriving D16)*:
  - 76x Dress Lettuce *(Farm)* → +6,460 G (freed)
  - 13x Grass *(Farm)* → +455 G (freed)
  - 30x Rainbow Bean *(Farm)* → +1,200 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 75 | 6,000 G | D18 | +3,000 G |
| Farm | **Dress Lettuce** | Lethe | 23 | 1,265 G | D17 | +690 G |
| Farm | **Morrocorn** | Lethe | 6 | 1,380 G | D19 | +1,020 G |
| Farm | **Royal Eggplant** | Lethe | 14 | 10,920 G | D22, D24, D26 | +9,240 G |

- **Daily Seed Spent**: 19,565 G | **End-of-Day Wallet**: **267,225 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **275,340 G** *(267,225 G carryover + 8,115 G payout)*
- **Harvest & Ship** *(+5,420 G arriving D17)*:
  - 41x Lumpotato *(Farm)* → +4,920 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 9 | 810 G | D19 | +270 G |
| Farm | **Rainbow Bean** | Lethe | 31 | 5,580 G | D22..D30 (5x) | +620 G |

- **Daily Seed Spent**: 6,390 G | **End-of-Day Wallet**: **268,950 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **274,370 G** *(268,950 G carryover + 5,420 G payout)*
- **Harvest & Ship** *(+82,460 G arriving D18)*:
  - 23x Dress Lettuce *(Farm)* → +1,955 G (freed)
  - 10x Morrocorn *(Farm)* → +4,000 G (freed)
  - 1x Rainbow Bean *(Farm)* → +40 G (regrowth 3/3)
  - 47x Royal Eggplant *(Farm)* → +22,560 G (regrowth 1/3)
  - 98x Unionion *(Farm)* → +19,110 G (freed)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 79x Revol Pepper *(Cave)* → +20,935 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 22 | 12,320 G | D21..D30 (4x) | +11,000 G |
| Farm | **Morrocorn** | Lethe | 33 | 7,590 G | D21 | +5,610 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D21 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D23 | +5,500 G |

- **Daily Seed Spent**: 48,070 G | **End-of-Day Wallet**: **226,300 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **308,760 G** *(226,300 G carryover + 82,460 G payout)*
- **Harvest & Ship** *(+46,920 G arriving D19)*:
  - 75x Lumpotato *(Farm)* → +9,000 G (freed)
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 24 | 1,920 G | D21 | +960 G |
| Farm | **Unionion** | Nemea | 51 | 5,355 G | D21 | +4,590 G |

- **Daily Seed Spent**: 7,275 G | **End-of-Day Wallet**: **301,485 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **348,405 G** *(301,485 G carryover + 46,920 G payout)*
- **Harvest & Ship** *(+61,190 G arriving D20)*:
  - 9x Lumpotato *(Farm)* → +1,080 G (freed)
  - 6x Morrocorn *(Farm)* → +2,400 G (freed)
  - 47x Royal Eggplant *(Farm)* → +22,560 G (regrowth 2/3)
  - 55x Honey Flower *(Waterside)* → +34,650 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 2 | 800 G | D22, D25, D28 | +700 G |
| Farm | **Royal Eggplant** | Lethe | 15 | 11,700 G | D26, D28, D30 | +9,900 G |
| Waterside | **Nectarcane** | Shatolla | 55 | 20,350 G | D23, D26, D29 | +20,900 G |

- **Daily Seed Spent**: 32,850 G | **End-of-Day Wallet**: **315,555 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **376,745 G** *(315,555 G carryover + 61,190 G payout)*
- **Harvest & Ship** *(+53,025 G arriving D21)*:
  - 79x Royal Eggplant *(Farm)* → +37,920 G (regrowth 2/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **376,745 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **429,770 G** *(376,745 G carryover + 53,025 G payout)*
- **Harvest & Ship** *(+94,015 G arriving D22)*:
  - 24x Lumpotato *(Farm)* → +2,880 G (freed)
  - 132x Morrocorn *(Farm)* → +52,800 G (freed)
  - 47x Royal Eggplant *(Farm)* → +22,560 G (regrowth 3/3)
  - 51x Unionion *(Farm)* → +9,945 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 84 | 2,520 G | D23 | +420 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Stellar Wheat** | Lethe | 71 | 2,840 G | D23 | +1,065 G |

- **Daily Seed Spent**: 82,580 G | **End-of-Day Wallet**: **347,190 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **441,205 G** *(347,190 G carryover + 94,015 G payout)*
- **Harvest & Ship** *(+46,380 G arriving D23)*:
  - 31x Rainbow Bean *(Farm)* → +1,240 G (regrowth 1/5)
  - 93x Royal Eggplant *(Farm)* → +44,640 G (regrowth 3/3)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 79 | 4,345 G | D24 | +2,370 G |

- **Daily Seed Spent**: 4,345 G | **End-of-Day Wallet**: **436,860 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **483,240 G** *(436,860 G carryover + 46,380 G payout)*
- **Harvest & Ship** *(+49,560 G arriving D24)*:
  - 84x Grass *(Farm)* → +2,940 G (freed)
  - 71x Stellar Wheat *(Farm)* → +3,905 G (freed)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 1/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 20 | 1,100 G | D25 | +600 G |
| Farm | **Grass** | Lethe | 7 | 210 G | D25 | +35 G |
| Farm | **Lumpotato** | Lethe | 29 | 2,610 G | D26 | +870 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D26 | +8,910 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D29 | +5,500 G |

- **Daily Seed Spent**: 22,675 G | **End-of-Day Wallet**: **460,565 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **510,125 G** *(460,565 G carryover + 49,560 G payout)*
- **Harvest & Ship** *(+20,505 G arriving D25)*:
  - 79x Dress Lettuce *(Farm)* → +6,715 G (freed)
  - 31x Rainbow Bean *(Farm)* → +1,240 G (regrowth 2/5)
  - 14x Royal Eggplant *(Farm)* → +6,720 G (regrowth 2/3)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 22 | 1,760 G | D27 | +880 G |
| Farm | **Grass** | Lethe | 8 | 240 G | D26 | +40 G |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D27 | +3,250 G |

- **Daily Seed Spent**: 8,500 G | **End-of-Day Wallet**: **501,625 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **522,130 G** *(501,625 G carryover + 20,505 G payout)*
- **Harvest & Ship** *(+2,445 G arriving D26)*:
  - 20x Dress Lettuce *(Farm)* → +1,700 G (freed)
  - 7x Grass *(Farm)* → +245 G (freed)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Stellar Wheat** | Lethe | 27 | 1,080 G | D27 | +405 G |

- **Daily Seed Spent**: 1,080 G | **End-of-Day Wallet**: **521,050 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **523,495 G** *(521,050 G carryover + 2,445 G payout)*
- **Harvest & Ship** *(+67,080 G arriving D27)*:
  - 8x Grass *(Farm)* → +280 G (freed)
  - 29x Lumpotato *(Farm)* → +3,480 G (freed)
  - 31x Rainbow Bean *(Farm)* → +1,240 G (regrowth 3/5)
  - 29x Royal Eggplant *(Farm)* → +13,920 G (regrowth 3/3)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 2/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 31,300 G | **End-of-Day Wallet**: **492,195 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **559,275 G** *(492,195 G carryover + 67,080 G payout)*
- **Harvest & Ship** *(+19,705 G arriving D28)*:
  - 22x Lumpotato *(Farm)* → +2,640 G (freed)
  - 27x Stellar Wheat *(Farm)* → +1,485 G (freed)
  - 50x Unionion *(Farm)* → +9,750 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 77 | 6,160 G | D30 | +3,080 G |
| Farm | **Lumpotato** | Lethe | 21 | 1,890 G | D30 | +630 G |

- **Daily Seed Spent**: 8,050 G | **End-of-Day Wallet**: **551,225 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **570,930 G** *(551,225 G carryover + 19,705 G payout)*
- **Harvest & Ship** *(+56,460 G arriving D29)*:
  - 31x Rainbow Bean *(Farm)* → +1,240 G (regrowth 4/5)
  - 114x Royal Eggplant *(Farm)* → +54,720 G (regrowth 2/3)
  - 2x Sudor Pepper *(Cave)* → +500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **570,930 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 2

---

#### **Day 29**

- **Morning Wallet**: **627,390 G** *(570,930 G carryover + 56,460 G payout)*
- **Harvest & Ship** *(+42,715 G arriving D30)*:
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 55x Nectarcane *(Waterside)* → +13,750 G (regrowth 3/3)
  - 57x Revol Pepper *(Cave)* → +15,105 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **627,390 G**
- **Plots Left**: Farm: 2 | Waterside: 77 | Cave: 59

---

#### **Day 30**

- **Morning Wallet**: **670,105 G** *(627,390 G carryover + 42,715 G payout)*
- **Harvest & Ship** *(+133,150 G arriving D31)*:
  - 98x Lumpotato *(Farm)* → +11,760 G (freed)
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 31x Rainbow Bean *(Farm)* → +1,240 G (regrowth 5/5)
  - 114x Royal Eggplant *(Farm)* → +54,720 G (regrowth 3/3)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **670,105 G**
- **Plots Left**: Farm: 295 | Waterside: 77 | Cave: 59

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **803,255 G** *(670,105 G carryover + 133,150 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 12–30)

- **Starting Wallet (Day 12)**: 230,485 G
- **Ending Wallet (Day 31 Quietus)**: **803,255 G**
- **Pre-planted Crop Sales**: **+334,320 G**
- **New Planting Net Profit**: **+238,450 G**
- **Net Profit (19 days)**: **+572,770 G**
- **Average Daily Profit**: **+30,146 G/day** *(over 19 active days)*
