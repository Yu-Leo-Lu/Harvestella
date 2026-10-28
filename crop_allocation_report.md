# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 83,060 G
- **Plot Capacities (Usable / Max)**: Farm: 191/196 | Waterside: 81/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Dress Lettuce** | 9 | Day 1 | D3 | Freed D3 | +765 G |
| Farm | **Morrocorn** | 15 | Day 1 | D5 | Freed D5 | +6,000 G |
| Waterside | **Honey Flower** | 10 | Day 1 | D7 | Freed D7 | +6,300 G |
| Waterside | **Nectarcane** | 6 | Day 1 | D5, D8, D11 | Freed D11 | +4,500 G |
| Farm | **Shatollan Paprika** | 18 | Day 1 | D6, D8, D10, D12, D14, D16, D18, D20, D22 | Freed D22 | +17,820 G |
| Farm | **Seatide Garlic** | 3 | Day 1 | D7 | Freed D7 | +3,000 G |
| Cave | **Sudor Pepper** | 6 | Day 1 | D4, D7, D10 | Freed D10 | +4,500 G |
| Cave | **Revol Pepper** | 6 | Day 1 | D5, D8, D11, D14, D17 | Freed D17 | +7,950 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 1**

- **Morning Wallet**: **83,060 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 6 | 3,360 G | D5..D17 (5x) | +4,590 G |
| Cave | **Sudor Pepper** | Argene | 63 | 25,200 G | D4, D7, D10 | +22,050 G |
| Farm | **Morrocorn** | Lethe | 2 | 460 G | D5 | +340 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D5, D8, D11 | +3,800 G |
| Farm | **Morrocorn** | Shatolla | 92 | 18,400 G | D5 | +18,400 G |
| Farm | **Shatollan Paprika** | Shatolla | 52 | 13,000 G | D6..D22 (9x) | +38,480 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D13 | +6,300 G |
| Waterside | **Nectarcane** | Shatolla | 27 | 9,990 G | D5, D8, D11 | +10,260 G |

- **Daily Seed Spent**: 81,610 G | **End-of-Day Wallet**: **1,450 G**
- **Plots Left**: Farm: 0 | Waterside: 25 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **1,450 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **1,450 G**
- **Plots Left**: Farm: 0 | Waterside: 25 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **1,450 G**
- **Harvest & Ship** *(+765 G arriving D4)*:
  - 9x Dress Lettuce *(Farm)* → +765 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D4 | +120 G |

- **Daily Seed Spent**: 570 G | **End-of-Day Wallet**: **880 G**
- **Plots Left**: Farm: 3 | Waterside: 25 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **1,645 G** *(880 G carryover + 765 G payout)*
- **Harvest & Ship** *(+17,940 G arriving D5)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 1 | 230 G | D8 | +170 G |
| Farm | **Morrocorn** | Shatolla | 6 | 1,200 G | D8 | +1,200 G |

- **Daily Seed Spent**: 1,430 G | **End-of-Day Wallet**: **215 G**
- **Plots Left**: Farm: 2 | Waterside: 25 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **18,155 G** *(215 G carryover + 17,940 G payout)*
- **Harvest & Ship** *(+57,530 G arriving D6)*:
  - 109x Morrocorn *(Farm)* → +43,600 G (freed)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 1/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 15 | 825 G | D7 | +450 G |
| Farm | **Morrocorn** | Lethe | 9 | 2,070 G | D9 | +1,530 G |
| Farm | **Morrocorn** | Shatolla | 1 | 200 G | D9 | +200 G |
| Waterside | **Islet Watermelon** | Shatolla | 6 | 15,000 G | D17 | +12,600 G |

- **Daily Seed Spent**: 18,095 G | **End-of-Day Wallet**: **60 G**
- **Plots Left**: Farm: 86 | Waterside: 19 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **57,590 G** *(60 G carryover + 57,530 G payout)*
- **Harvest & Ship** *(+7,700 G arriving D7)*:
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 1/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 65 | 3,575 G | D8 | +1,950 G |
| Farm | **Morrocorn** | Lethe | 17 | 3,910 G | D10 | +2,890 G |
| Farm | **Seatide Garlic** | Shatolla | 4 | 2,600 G | D12 | +1,400 G |
| Waterside | **Islet Watermelon** | Shatolla | 19 | 47,500 G | D18 | +39,900 G |

- **Daily Seed Spent**: 57,585 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **7,705 G** *(5 G carryover + 7,700 G payout)*
- **Harvest & Ship** *(+27,825 G arriving D8)*:
  - 15x Dress Lettuce *(Farm)* → +1,275 G (freed)
  - 3x Seatide Garlic *(Farm)* → +3,000 G (freed)
  - 10x Honey Flower *(Waterside)* → +6,300 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 17 | 3,910 G | D11 | +2,890 G |
| Waterside | **Nectarcane** | Shatolla | 10 | 3,700 G | D11, D14, D17 | +3,800 G |

- **Daily Seed Spent**: 7,610 G | **End-of-Day Wallet**: **95 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **27,920 G** *(95 G carryover + 27,825 G payout)*
- **Harvest & Ship** *(+29,955 G arriving D9)*:
  - 65x Dress Lettuce *(Farm)* → +5,525 G (freed)
  - 7x Morrocorn *(Farm)* → +2,800 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 2/9)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 2/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 2 | 460 G | D12 | +340 G |
| Farm | **Carrop** | Nemea | 63 | 5,985 G | D9 | +1,260 G |
| Farm | **Seatide Garlic** | Shatolla | 8 | 5,200 G | D14 | +2,800 G |

- **Daily Seed Spent**: 11,645 G | **End-of-Day Wallet**: **16,275 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **46,230 G** *(16,275 G carryover + 29,955 G payout)*
- **Harvest & Ship** *(+11,245 G arriving D10)*:
  - 63x Carrop *(Farm)* → +7,245 G (freed)
  - 10x Morrocorn *(Farm)* → +4,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 71 | 46,150 G | D15 | +24,850 G |

- **Daily Seed Spent**: 46,150 G | **End-of-Day Wallet**: **80 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **11,325 G** *(80 G carryover + 11,245 G payout)*
- **Harvest & Ship** *(+31,750 G arriving D11)*:
  - 17x Morrocorn *(Farm)* → +6,800 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 3/9)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 16 | 10,400 G | D16 | +5,600 G |

- **Daily Seed Spent**: 10,400 G | **End-of-Day Wallet**: **925 G**
- **Plots Left**: Farm: 3 | Waterside: 0 | Cave: 69

---

#### **Day 11**

- **Morning Wallet**: **32,675 G** *(925 G carryover + 31,750 G payout)*
- **Harvest & Ship** *(+23,230 G arriving D12)*:
  - 17x Morrocorn *(Farm)* → +6,800 G (freed)
  - 53x Nectarcane *(Waterside)* → +13,250 G (regrowth 3/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 6 | 2,400 G | D14, D17, D20 | +2,100 G |
| Farm | **Seatide Garlic** | Shatolla | 20 | 13,000 G | D17 | +7,000 G |
| Waterside | **Honey Flower** | Shatolla | 43 | 16,340 G | D17 | +10,750 G |

- **Daily Seed Spent**: 31,740 G | **End-of-Day Wallet**: **935 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 63

---

#### **Day 12**

- **Morning Wallet**: **24,165 G** *(935 G carryover + 23,230 G payout)*
- **Harvest & Ship** *(+12,500 G arriving D13)*:
  - 2x Morrocorn *(Farm)* → +800 G (freed)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 4/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 41 | 22,960 G | D16..D28 (5x) | +31,365 G |
| Farm | **Morrocorn** | Shatolla | 6 | 1,200 G | D16 | +1,200 G |

- **Daily Seed Spent**: 24,160 G | **End-of-Day Wallet**: **5 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 22

---

#### **Day 13**

- **Morning Wallet**: **12,505 G** *(5 G carryover + 12,500 G payout)*
- **Harvest & Ship** *(+13,800 G arriving D14)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 22 | 12,320 G | D17..D29 (5x) | +16,830 G |

- **Daily Seed Spent**: 12,320 G | **End-of-Day Wallet**: **185 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **13,985 G** *(185 G carryover + 13,800 G payout)*
- **Harvest & Ship** *(+22,880 G arriving D15)*:
  - 8x Seatide Garlic *(Farm)* → +8,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 5/9)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 2/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/5)
  - 6x Sudor Pepper *(Cave)* → +1,500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 8 | 5,200 G | D20 | +2,800 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D26 | +6,300 G |

- **Daily Seed Spent**: 12,700 G | **End-of-Day Wallet**: **1,285 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **24,165 G** *(1,285 G carryover + 22,880 G payout)*
- **Harvest & Ship** *(+71,000 G arriving D16)*:
  - 71x Seatide Garlic *(Farm)* → +71,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 71 | 6,745 G | D16 | +1,420 G |

- **Daily Seed Spent**: 6,745 G | **End-of-Day Wallet**: **17,420 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **88,420 G** *(17,420 G carryover + 71,000 G payout)*
- **Harvest & Ship** *(+45,130 G arriving D17)*:
  - 71x Carrop *(Farm)* → +8,165 G (freed)
  - 6x Morrocorn *(Farm)* → +2,400 G (freed)
  - 16x Seatide Garlic *(Farm)* → +16,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 6/9)
  - 41x Revol Pepper *(Cave)* → +10,865 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 93 | 18,600 G | D20 | +18,600 G |

- **Daily Seed Spent**: 18,600 G | **End-of-Day Wallet**: **69,820 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **114,950 G** *(69,820 G carryover + 45,130 G payout)*
- **Harvest & Ship** *(+87,700 G arriving D18)*:
  - 20x Seatide Garlic *(Farm)* → +20,000 G (freed)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 6x Islet Watermelon *(Waterside)* → +27,600 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 3/3)
  - 34x Revol Pepper *(Cave)* → +9,010 G (regrowth 5/5)
  - 6x Sudor Pepper *(Cave)* → +1,500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Farm | **Dress Lettuce** | Lethe | 13 | 715 G | D19 | +390 G |
| Waterside | **Islet Watermelon** | Shatolla | 43 | 107,500 G | D29 | +90,300 G |

- **Daily Seed Spent**: 114,935 G | **End-of-Day Wallet**: **15 G**
- **Plots Left**: Farm: 7 | Waterside: 16 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **87,715 G** *(15 G carryover + 87,700 G payout)*
- **Harvest & Ship** *(+95,100 G arriving D19)*:
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 7/9)
  - 19x Islet Watermelon *(Waterside)* → +87,400 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 35 | 87,500 G | D30 | +73,500 G |

- **Daily Seed Spent**: 87,500 G | **End-of-Day Wallet**: **215 G**
- **Plots Left**: Farm: 7 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **95,315 G** *(215 G carryover + 95,100 G payout)*
- **Harvest & Ship** *(+11,970 G arriving D20)*:
  - 13x Dress Lettuce *(Farm)* → +1,105 G (freed)
  - 41x Revol Pepper *(Cave)* → +10,865 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 20 | 1,900 G | D20 | +400 G |

- **Daily Seed Spent**: 1,900 G | **End-of-Day Wallet**: **93,415 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **105,385 G** *(93,415 G carryover + 11,970 G payout)*
- **Harvest & Ship** *(+62,530 G arriving D21)*:
  - 20x Carrop *(Farm)* → +2,300 G (freed)
  - 93x Morrocorn *(Farm)* → +37,200 G (freed)
  - 8x Seatide Garlic *(Farm)* → +8,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 8/9)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 2/5)
  - 6x Sudor Pepper *(Cave)* → +1,500 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 6 | 2,400 G | D23, D26, D29 | +2,100 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D24 | +8,500 G |
| Farm | **Seatide Garlic** | Shatolla | 71 | 46,150 G | D26 | +24,850 G |

- **Daily Seed Spent**: 60,050 G | **End-of-Day Wallet**: **45,335 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **107,865 G** *(45,335 G carryover + 62,530 G payout)*
- **Harvest & Ship** *(+3,180 G arriving D22)*:
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **107,865 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **111,045 G** *(107,865 G carryover + 3,180 G payout)*
- **Harvest & Ship** *(+18,565 G arriving D23)*:
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 9/9)
  - 41x Revol Pepper *(Cave)* → +10,865 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 14 | 3,220 G | D26 | +2,380 G |
| Farm | **Carrop** | Nemea | 49 | 4,655 G | D23 | +980 G |
| Farm | **Morrocorn** | Shatolla | 7 | 1,400 G | D26 | +1,400 G |

- **Daily Seed Spent**: 9,275 G | **End-of-Day Wallet**: **101,770 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **120,335 G** *(101,770 G carryover + 18,565 G payout)*
- **Harvest & Ship** *(+12,965 G arriving D24)*:
  - 49x Carrop *(Farm)* → +5,635 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 3/5)
  - 6x Sudor Pepper *(Cave)* → +1,500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 49 | 4,655 G | D24 | +980 G |

- **Daily Seed Spent**: 4,655 G | **End-of-Day Wallet**: **115,680 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **128,645 G** *(115,680 G carryover + 12,965 G payout)*
- **Harvest & Ship** *(+28,815 G arriving D25)*:
  - 49x Carrop *(Farm)* → +5,635 G (freed)
  - 50x Morrocorn *(Farm)* → +20,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **64,295 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **93,110 G** *(64,295 G carryover + 28,815 G payout)*
- **Harvest & Ship** *(+10,865 G arriving D26)*:
  - 41x Revol Pepper *(Cave)* → +10,865 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **93,110 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **103,975 G** *(93,110 G carryover + 10,865 G payout)*
- **Harvest & Ship** *(+100,530 G arriving D27)*:
  - 21x Morrocorn *(Farm)* → +8,400 G (freed)
  - 71x Seatide Garlic *(Farm)* → +71,000 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 4/5)
  - 6x Sudor Pepper *(Cave)* → +1,500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 92 | 18,400 G | D30 | +18,400 G |

- **Daily Seed Spent**: 18,400 G | **End-of-Day Wallet**: **85,575 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **186,105 G** *(85,575 G carryover + 100,530 G payout)*
- **Harvest & Ship** *(+3,180 G arriving D28)*:
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **186,105 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **189,285 G** *(186,105 G carryover + 3,180 G payout)*
- **Harvest & Ship** *(+10,865 G arriving D29)*:
  - 41x Revol Pepper *(Cave)* → +10,865 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **189,285 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 41

---

#### **Day 29**

- **Morning Wallet**: **200,150 G** *(189,285 G carryover + 10,865 G payout)*
- **Harvest & Ship** *(+205,130 G arriving D30)*:
  - 43x Islet Watermelon *(Waterside)* → +197,800 G (freed)
  - 22x Revol Pepper *(Cave)* → +5,830 G (regrowth 5/5)
  - 6x Sudor Pepper *(Cave)* → +1,500 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **200,150 G**
- **Plots Left**: Farm: 0 | Waterside: 46 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **405,280 G** *(200,150 G carryover + 205,130 G payout)*
- **Harvest & Ship** *(+299,980 G arriving D31)*:
  - 92x Morrocorn *(Farm)* → +36,800 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 35x Islet Watermelon *(Waterside)* → +161,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **405,280 G**
- **Plots Left**: Farm: 191 | Waterside: 81 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **705,260 G** *(405,280 G carryover + 299,980 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 83,060 G
- **Ending Wallet (Day 31 Quietus)**: **705,260 G**
- **Pre-planted Crop Sales**: **+50,835 G**
- **New Planting Net Profit**: **+571,365 G**
- **Net Profit (30 days)**: **+622,200 G**
- **Average Daily Profit**: **+20,740 G/day** *(over 30 active days)*
