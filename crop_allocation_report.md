# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 6
- **Planning Timeline**: Day 6 -> Day 30 (25d Quietus window)
- **Capital Budget**: 57,095 G
- **Plot Capacities (Usable / Max)**: Farm: 191/196 | Waterside: 81/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Seatide Garlic** | 4 | Day 1 | D7 | Freed D7 | +4,000 G |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D6, D8, D10, D12, D14, D16, D18, D20, D22 | Freed D22 | +69,300 G |
| Farm | **Seatide Garlic** | 5 | Day 3 | D9 | Freed D9 | +5,000 G |
| Farm | **Morrocorn** | 4 | Day 4 | D8 | Freed D8 | +1,600 G |
| Farm | **Carrop** | 37 | Day 5 | D6 | Freed D6 | +4,255 G |
| Farm | **Dress Lettuce** | 1 | Day 5 | D7 | Freed D7 | +85 G |
| Farm | **Grass** | 6 | Day 5 | D7 | Freed D7 | +210 G |
| Farm | **Morrocorn** | 27 | Day 5 | D9 | Freed D9 | +10,800 G |
| Farm | **Seatide Garlic** | 4 | Day 5 | D11 | Freed D11 | +4,000 G |
| Farm | **Stellar Wheat** | 31 | Day 5 | D7 | Freed D7 | +1,705 G |
| Farm | **Dress Lettuce** | 1 | Day 6 | D8 | Freed D8 | +85 G |
| Farm | **Bellhop** | 1 | Day 3 | D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +945 G |
| Farm | **Bellhop** | 1 | Day 6 | D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24, D25, D26, D27, D28, D29, D30 | Stays Planted | +810 G |
| Waterside | **Honey Flower** | 10 | Day 1 | D7 | Freed D7 | +6,300 G |
| Waterside | **Islet Watermelon** | 3 | Day 1 | D13 | Freed D13 | +13,800 G |
| Waterside | **Nectarcane** | 43 | Day 1 | D8, D11 | Freed D11 | +21,500 G |
| Waterside | **Islet Watermelon** | 3 | Day 3 | D15 | Freed D15 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 4 | D16 | Freed D16 | +9,200 G |
| Waterside | **Islet Watermelon** | 5 | Day 5 | D17 | Freed D17 | +23,000 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D8, D11, D14, D17 | Freed D17 | +12,720 G |
| Cave | **Sudor Pepper** | 69 | Day 1 | D7, D10 | Freed D10 | +34,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 6**

- **Morning Wallet**: **57,095 G**
- **Harvest & Ship** *(+11,955 G arriving D7)*:
  - 37x Carrop *(Farm)* → +4,255 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 1/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 12 | 2,760 G | D10 | +2,040 G |
| Farm | **Seatide Garlic** | Shatolla | 24 | 15,600 G | D12 | +8,400 G |
| Waterside | **Islet Watermelon** | Shatolla | 15 | 37,500 G | D18 | +31,500 G |

- **Daily Seed Spent**: 55,860 G | **End-of-Day Wallet**: **1,235 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **13,190 G** *(1,235 G carryover + 11,955 G payout)*
- **Harvest & Ship** *(+29,550 G arriving D8)*:
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)
  - 6x Grass *(Farm)* → +210 G (freed)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 31x Stellar Wheat *(Farm)* → +1,705 G (freed)
  - 10x Honey Flower *(Waterside)* → +6,300 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 42 | 3,990 G | D8 | +840 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D11, D14, D17 | +3,800 G |

- **Daily Seed Spent**: 7,690 G | **End-of-Day Wallet**: **5,500 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **35,050 G** *(5,500 G carryover + 29,550 G payout)*
- **Harvest & Ship** *(+28,145 G arriving D9)*:
  - 42x Carrop *(Farm)* → +4,830 G (freed)
  - 1x Dress Lettuce *(Farm)* → +85 G (freed)
  - 4x Morrocorn *(Farm)* → +1,600 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 2/9)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 1/2)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 47 | 30,550 G | D14 | +16,450 G |

- **Daily Seed Spent**: 30,550 G | **End-of-Day Wallet**: **4,500 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **32,645 G** *(4,500 G carryover + 28,145 G payout)*
- **Harvest & Ship** *(+15,800 G arriving D10)*:
  - 27x Morrocorn *(Farm)* → +10,800 G (freed)
  - 5x Seatide Garlic *(Farm)* → +5,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 21 | 1,995 G | D10 | +420 G |
| Farm | **Morrocorn** | Shatolla | 2 | 400 G | D13 | +400 G |
| Farm | **Shatollan Paprika** | Shatolla | 5 | 1,250 G | D14..D30 (9x) | +3,700 G |

- **Daily Seed Spent**: 3,645 G | **End-of-Day Wallet**: **29,000 G**
- **Plots Left**: Farm: 4 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **44,800 G** *(29,000 G carryover + 15,800 G payout)*
- **Harvest & Ship** *(+32,210 G arriving D11)*:
  - 1x Bellhop *(Farm)* → +45 G (regrowth 1/21)
  - 21x Carrop *(Farm)* → +2,415 G (freed)
  - 12x Morrocorn *(Farm)* → +4,800 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 3/9)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 46 | 25,760 G | D14..D26 (5x) | +35,190 G |
| Farm | **Morrocorn** | Lethe | 11 | 2,530 G | D14 | +1,870 G |
| Farm | **Morrocorn** | Shatolla | 1 | 200 G | D14 | +200 G |
| Farm | **Seatide Garlic** | Shatolla | 25 | 16,250 G | D16 | +8,750 G |

- **Daily Seed Spent**: 44,740 G | **End-of-Day Wallet**: **60 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 23

---

#### **Day 11**

- **Morning Wallet**: **32,270 G** *(60 G carryover + 32,210 G payout)*
- **Harvest & Ship** *(+20,475 G arriving D12)*:
  - 1x Bellhop *(Farm)* → +45 G (regrowth 2/21)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 53x Nectarcane *(Waterside)* → +13,250 G (regrowth 2/2)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 23 | 12,880 G | D15..D27 (5x) | +17,595 G |
| Farm | **Carrop** | Nemea | 4 | 380 G | D12 | +80 G |
| Waterside | **Honey Flower** | Shatolla | 43 | 16,340 G | D17 | +10,750 G |

- **Daily Seed Spent**: 29,600 G | **End-of-Day Wallet**: **2,670 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **23,145 G** *(2,670 G carryover + 20,475 G payout)*
- **Harvest & Ship** *(+32,205 G arriving D13)*:
  - 1x Bellhop *(Farm)* → +45 G (regrowth 3/21)
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 24x Seatide Garlic *(Farm)* → +24,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 4/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 5 | 1,150 G | D16 | +850 G |
| Farm | **Morrocorn** | Shatolla | 14 | 2,800 G | D16 | +2,800 G |
| Farm | **Seatide Garlic** | Shatolla | 9 | 5,850 G | D18 | +3,150 G |

- **Daily Seed Spent**: 9,800 G | **End-of-Day Wallet**: **13,345 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **45,550 G** *(13,345 G carryover + 32,205 G payout)*
- **Harvest & Ship** *(+14,690 G arriving D14)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 4/21)
  - 2x Morrocorn *(Farm)* → +800 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 2 | 190 G | D14 | +40 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D25 | +6,300 G |

- **Daily Seed Spent**: 7,690 G | **End-of-Day Wallet**: **37,860 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **52,550 G** *(37,860 G carryover + 14,690 G payout)*
- **Harvest & Ship** *(+78,240 G arriving D15)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 5/21)
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 12x Morrocorn *(Farm)* → +4,800 G (freed)
  - 47x Seatide Garlic *(Farm)* → +47,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 5/9)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 2/3)
  - 58x Revol Pepper *(Cave)* → +15,370 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 61 | 12,200 G | D18 | +12,200 G |

- **Daily Seed Spent**: 12,200 G | **End-of-Day Wallet**: **40,350 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **118,590 G** *(40,350 G carryover + 78,240 G payout)*
- **Harvest & Ship** *(+19,985 G arriving D16)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 6/21)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 23x Revol Pepper *(Cave)* → +6,095 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D27 | +6,300 G |

- **Daily Seed Spent**: 7,500 G | **End-of-Day Wallet**: **111,090 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **131,075 G** *(111,090 G carryover + 19,985 G payout)*
- **Harvest & Ship** *(+50,140 G arriving D17)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 7/21)
  - 19x Morrocorn *(Farm)* → +7,600 G (freed)
  - 25x Seatide Garlic *(Farm)* → +25,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 6/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 44 | 10,120 G | D20 | +7,480 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D28 | +4,200 G |

- **Daily Seed Spent**: 15,120 G | **End-of-Day Wallet**: **115,955 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **166,095 G** *(115,955 G carryover + 50,140 G payout)*
- **Harvest & Ship** *(+68,050 G arriving D18)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 8/21)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 5x Islet Watermelon *(Waterside)* → +23,000 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 3/3)
  - 58x Revol Pepper *(Cave)* → +15,370 G (regrowth 4/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Waterside | **Islet Watermelon** | Shatolla | 58 | 145,000 G | D29 | +121,800 G |

- **Daily Seed Spent**: 151,720 G | **End-of-Day Wallet**: **14,375 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **82,425 G** *(14,375 G carryover + 68,050 G payout)*
- **Harvest & Ship** *(+116,835 G arriving D19)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 9/21)
  - 61x Morrocorn *(Farm)* → +24,400 G (freed)
  - 9x Seatide Garlic *(Farm)* → +9,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 7/9)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 23x Revol Pepper *(Cave)* → +6,095 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 69 | 44,850 G | D24 | +24,150 G |
| Waterside | **Islet Watermelon** | Shatolla | 15 | 37,500 G | D30 | +31,500 G |

- **Daily Seed Spent**: 82,350 G | **End-of-Day Wallet**: **75 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **116,910 G** *(75 G carryover + 116,835 G payout)*
- **Harvest & Ship** *(+90 G arriving D20)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 10/21)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **116,910 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **117,000 G** *(116,910 G carryover + 90 G payout)*
- **Harvest & Ship** *(+38,130 G arriving D21)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 11/21)
  - 44x Morrocorn *(Farm)* → +17,600 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 8/9)
  - 46x Revol Pepper *(Cave)* → +12,190 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 23 | 4,600 G | D24 | +4,600 G |
| Farm | **Seatide Garlic** | Shatolla | 21 | 13,650 G | D26 | +7,350 G |

- **Daily Seed Spent**: 18,250 G | **End-of-Day Wallet**: **98,750 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **136,880 G** *(98,750 G carryover + 38,130 G payout)*
- **Harvest & Ship** *(+9,365 G arriving D22)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 12/21)
  - 35x Revol Pepper *(Cave)* → +9,275 G (regrowth 3/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **136,880 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **146,245 G** *(136,880 G carryover + 9,365 G payout)*
- **Harvest & Ship** *(+8,340 G arriving D23)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 13/21)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 9/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D26 | +8,500 G |
| Farm | **Carrop** | Nemea | 6 | 570 G | D23 | +120 G |
| Farm | **Morrocorn** | Shatolla | 14 | 2,800 G | D26 | +2,800 G |

- **Daily Seed Spent**: 14,870 G | **End-of-Day Wallet**: **131,375 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **139,715 G** *(131,375 G carryover + 8,340 G payout)*
- **Harvest & Ship** *(+12,970 G arriving D24)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 14/21)
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 46x Revol Pepper *(Cave)* → +12,190 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D24 | +120 G |

- **Daily Seed Spent**: 570 G | **End-of-Day Wallet**: **139,145 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **152,115 G** *(139,145 G carryover + 12,970 G payout)*
- **Harvest & Ship** *(+88,805 G arriving D25)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 15/21)
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 23x Morrocorn *(Farm)* → +9,200 G (freed)
  - 69x Seatide Garlic *(Farm)* → +69,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 6/9)
  - 35x Revol Pepper *(Cave)* → +9,275 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **87,765 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **176,570 G** *(87,765 G carryover + 88,805 G payout)*
- **Harvest & Ship** *(+13,890 G arriving D26)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 16/21)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **176,570 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **190,460 G** *(176,570 G carryover + 13,890 G payout)*
- **Harvest & Ship** *(+59,430 G arriving D27)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 17/21)
  - 64x Morrocorn *(Farm)* → +25,600 G (freed)
  - 21x Seatide Garlic *(Farm)* → +21,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 7/9)
  - 46x Revol Pepper *(Cave)* → +12,190 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 85 | 17,000 G | D30 | +17,000 G |

- **Daily Seed Spent**: 17,000 G | **End-of-Day Wallet**: **173,460 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 46

---

#### **Day 27**

- **Morning Wallet**: **232,890 G** *(173,460 G carryover + 59,430 G payout)*
- **Harvest & Ship** *(+23,165 G arriving D28)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 18/21)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 35x Revol Pepper *(Cave)* → +9,275 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **232,890 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 69

---

#### **Day 28**

- **Morning Wallet**: **256,055 G** *(232,890 G carryover + 23,165 G payout)*
- **Harvest & Ship** *(+9,840 G arriving D29)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 19/21)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 8/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **256,055 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **265,895 G** *(256,055 G carryover + 9,840 G payout)*
- **Harvest & Ship** *(+266,890 G arriving D30)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 20/21)
  - 58x Islet Watermelon *(Waterside)* → +266,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **265,895 G**
- **Plots Left**: Farm: 0 | Waterside: 66 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **532,785 G** *(265,895 G carryover + 266,890 G payout)*
- **Harvest & Ship** *(+205,820 G arriving D31)*:
  - 2x Bellhop *(Farm)* → +90 G (regrowth 21/21)
  - 85x Morrocorn *(Farm)* → +34,000 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 9/9)
  - 15x Islet Watermelon *(Waterside)* → +69,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **532,785 G**
- **Plots Left**: Farm: 189 | Waterside: 81 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **738,605 G** *(532,785 G carryover + 205,820 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 6–30)

- **Starting Wallet (Day 6)**: 57,095 G
- **Ending Wallet (Day 31 Quietus)**: **738,605 G**
- **Pre-planted Crop Sales**: **+237,615 G**
- **New Planting Net Profit**: **+443,895 G**
- **Net Profit (25 days)**: **+681,510 G**
- **Average Daily Profit**: **+27,260 G/day** *(over 25 active days)*
