# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 5
- **Planning Timeline**: Day 5 -> Day 30 (26d Quietus window)
- **Capital Budget**: 21,565 G
- **Plot Capacities (Usable / Max)**: Farm: 190/196 | Waterside: 81/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Morrocorn** | 107 | Day 1 | D5 | Freed D5 | +42,800 G |
| Farm | **Seatide Garlic** | 4 | Day 1 | D7 | Freed D7 | +4,000 G |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D6, D8, D10, D12, D14, D16, D18, D20, D22 | Freed D22 | +69,300 G |
| Farm | **Seatide Garlic** | 5 | Day 3 | D9 | Freed D9 | +5,000 G |
| Farm | **Morrocorn** | 4 | Day 4 | D8 | Freed D8 | +1,600 G |
| Waterside | **Honey Flower** | 10 | Day 1 | D7 | Freed D7 | +6,300 G |
| Waterside | **Islet Watermelon** | 3 | Day 1 | D13 | Freed D13 | +13,800 G |
| Waterside | **Nectarcane** | 43 | Day 1 | D5, D8, D11 | Freed D11 | +32,250 G |
| Waterside | **Islet Watermelon** | 3 | Day 3 | D15 | Freed D15 | +13,800 G |
| Waterside | **Islet Watermelon** | 2 | Day 4 | D16 | Freed D16 | +9,200 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D5, D8, D11, D14, D17 | Freed D17 | +15,900 G |
| Cave | **Sudor Pepper** | 69 | Day 1 | D7, D10 | Freed D10 | +34,500 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 5**

- **Morning Wallet**: **21,565 G**
- **Harvest & Ship** *(+56,730 G arriving D6)*:
  - 107x Morrocorn *(Farm)* → +42,800 G (freed)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 1/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 44 | 2,420 G | D7 | +1,320 G |
| Farm | **Morrocorn** | Lethe | 35 | 8,050 G | D9 | +5,950 G |
| Farm | **Carrop** | Nemea | 10 | 950 G | D6 | +200 G |
| Farm | **Morrocorn** | Shatolla | 3 | 600 G | D9 | +600 G |
| Farm | **Seatide Garlic** | Shatolla | 14 | 9,100 G | D11 | +4,900 G |

- **Daily Seed Spent**: 21,120 G | **End-of-Day Wallet**: **445 G**
- **Plots Left**: Farm: 1 | Waterside: 20 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **57,175 G** *(445 G carryover + 56,730 G payout)*
- **Harvest & Ship** *(+8,850 G arriving D7)*:
  - 10x Carrop *(Farm)* → +1,150 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 1/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 11 | 7,150 G | D12 | +3,850 G |
| Waterside | **Islet Watermelon** | Shatolla | 20 | 50,000 G | D18 | +42,000 G |

- **Daily Seed Spent**: 57,150 G | **End-of-Day Wallet**: **25 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **8,875 G** *(25 G carryover + 8,850 G payout)*
- **Harvest & Ship** *(+31,290 G arriving D8)*:
  - 44x Dress Lettuce *(Farm)* → +3,740 G (freed)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 10x Honey Flower *(Waterside)* → +6,300 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 1/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 5 | 1,150 G | D11 | +850 G |
| Farm | **Carrop** | Nemea | 42 | 3,990 G | D8 | +840 G |
| Waterside | **Nectarcane** | Shatolla | 10 | 3,700 G | D11, D14, D17 | +3,800 G |

- **Daily Seed Spent**: 8,840 G | **End-of-Day Wallet**: **35 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **31,325 G** *(35 G carryover + 31,290 G payout)*
- **Harvest & Ship** *(+28,060 G arriving D9)*:
  - 42x Carrop *(Farm)* → +4,830 G (freed)
  - 4x Morrocorn *(Farm)* → +1,600 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 2/9)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 2/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 9 | 2,070 G | D12 | +1,530 G |
| Farm | **Seatide Garlic** | Shatolla | 38 | 24,700 G | D14 | +13,300 G |

- **Daily Seed Spent**: 26,770 G | **End-of-Day Wallet**: **4,555 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **32,615 G** *(4,555 G carryover + 28,060 G payout)*
- **Harvest & Ship** *(+20,200 G arriving D10)*:
  - 38x Morrocorn *(Farm)* → +15,200 G (freed)
  - 5x Seatide Garlic *(Farm)* → +5,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 37 | 3,515 G | D10 | +740 G |
| Farm | **Shatollan Paprika** | Shatolla | 5 | 1,250 G | D14..D30 (9x) | +3,700 G |

- **Daily Seed Spent**: 4,765 G | **End-of-Day Wallet**: **27,850 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **48,050 G** *(27,850 G carryover + 20,200 G payout)*
- **Harvest & Ship** *(+29,205 G arriving D11)*:
  - 37x Carrop *(Farm)* → +4,255 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 3/9)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 2/2)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 43 | 24,080 G | D14..D26 (5x) | +32,895 G |
| Farm | **Morrocorn** | Lethe | 1 | 230 G | D14 | +170 G |
| Farm | **Seatide Garlic** | Shatolla | 36 | 23,400 G | D16 | +12,600 G |

- **Daily Seed Spent**: 47,710 G | **End-of-Day Wallet**: **340 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 26

---

#### **Day 11**

- **Morning Wallet**: **29,545 G** *(340 G carryover + 29,205 G payout)*
- **Harvest & Ship** *(+32,430 G arriving D12)*:
  - 5x Morrocorn *(Farm)* → +2,000 G (freed)
  - 14x Seatide Garlic *(Farm)* → +14,000 G (freed)
  - 53x Nectarcane *(Waterside)* → +13,250 G (regrowth 3/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 20 | 13,000 G | D17 | +7,000 G |
| Waterside | **Honey Flower** | Shatolla | 43 | 16,340 G | D17 | +10,750 G |

- **Daily Seed Spent**: 29,340 G | **End-of-Day Wallet**: **205 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 26

---

#### **Day 12**

- **Morning Wallet**: **32,635 G** *(205 G carryover + 32,430 G payout)*
- **Harvest & Ship** *(+22,300 G arriving D13)*:
  - 9x Morrocorn *(Farm)* → +3,600 G (freed)
  - 11x Seatide Garlic *(Farm)* → +11,000 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 4/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 26 | 14,560 G | D16..D28 (5x) | +19,890 G |
| Farm | **Morrocorn** | Shatolla | 20 | 4,000 G | D16 | +4,000 G |

- **Daily Seed Spent**: 18,560 G | **End-of-Day Wallet**: **14,075 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **36,375 G** *(14,075 G carryover + 22,300 G payout)*
- **Harvest & Ship** *(+13,800 G arriving D14)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D25 | +6,300 G |

- **Daily Seed Spent**: 7,500 G | **End-of-Day Wallet**: **28,875 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **42,675 G** *(28,875 G carryover + 13,800 G payout)*
- **Harvest & Ship** *(+63,725 G arriving D15)*:
  - 1x Morrocorn *(Farm)* → +400 G (freed)
  - 38x Seatide Garlic *(Farm)* → +38,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 5/9)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 2/3)
  - 55x Revol Pepper *(Cave)* → +14,575 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 39 | 25,350 G | D20 | +13,650 G |

- **Daily Seed Spent**: 25,350 G | **End-of-Day Wallet**: **17,325 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **81,050 G** *(17,325 G carryover + 63,725 G payout)*
- **Harvest & Ship** *(+13,800 G arriving D16)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D27 | +6,300 G |

- **Daily Seed Spent**: 7,500 G | **End-of-Day Wallet**: **73,550 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **87,350 G** *(73,550 G carryover + 13,800 G payout)*
- **Harvest & Ship** *(+68,340 G arriving D17)*:
  - 20x Morrocorn *(Farm)* → +8,000 G (freed)
  - 36x Seatide Garlic *(Farm)* → +36,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 6/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 26x Revol Pepper *(Cave)* → +6,890 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 56 | 11,200 G | D20 | +11,200 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D28 | +4,200 G |

- **Daily Seed Spent**: 16,200 G | **End-of-Day Wallet**: **71,150 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **139,490 G** *(71,150 G carryover + 68,340 G payout)*
- **Harvest & Ship** *(+64,165 G arriving D18)*:
  - 20x Seatide Garlic *(Farm)* → +20,000 G (freed)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 3/3)
  - 55x Revol Pepper *(Cave)* → +14,575 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Farm | **Carrop** | Nemea | 2 | 190 G | D18 | +40 G |
| Waterside | **Islet Watermelon** | Shatolla | 53 | 132,500 G | D29 | +111,300 G |

- **Daily Seed Spent**: 139,410 G | **End-of-Day Wallet**: **80 G**
- **Plots Left**: Farm: 18 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **64,245 G** *(80 G carryover + 64,165 G payout)*
- **Harvest & Ship** *(+100,480 G arriving D19)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 7/9)
  - 20x Islet Watermelon *(Waterside)* → +92,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 20 | 13,000 G | D24 | +7,000 G |
| Waterside | **Islet Watermelon** | Shatolla | 20 | 50,000 G | D30 | +42,000 G |

- **Daily Seed Spent**: 63,000 G | **End-of-Day Wallet**: **1,245 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **101,725 G** *(1,245 G carryover + 100,480 G payout)*
- **Harvest & Ship** *(+6,890 G arriving D20)*:
  - 26x Revol Pepper *(Cave)* → +6,890 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **101,725 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **108,615 G** *(101,725 G carryover + 6,890 G payout)*
- **Harvest & Ship** *(+81,045 G arriving D21)*:
  - 56x Morrocorn *(Farm)* → +22,400 G (freed)
  - 39x Seatide Garlic *(Farm)* → +39,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 8/9)
  - 43x Revol Pepper *(Cave)* → +11,395 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D24 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 23 | 4,600 G | D24 | +4,600 G |
| Farm | **Seatide Garlic** | Shatolla | 20 | 13,000 G | D26 | +7,000 G |

- **Daily Seed Spent**: 29,100 G | **End-of-Day Wallet**: **79,515 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **160,560 G** *(79,515 G carryover + 81,045 G payout)*
- **Harvest & Ship** *(+3,180 G arriving D22)*:
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **160,560 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **163,740 G** *(160,560 G carryover + 3,180 G payout)*
- **Harvest & Ship** *(+15,140 G arriving D23)*:
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 9/9)
  - 26x Revol Pepper *(Cave)* → +6,890 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D23 | +120 G |
| Farm | **Morrocorn** | Shatolla | 64 | 12,800 G | D26 | +12,800 G |

- **Daily Seed Spent**: 13,370 G | **End-of-Day Wallet**: **150,370 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **165,510 G** *(150,370 G carryover + 15,140 G payout)*
- **Harvest & Ship** *(+12,085 G arriving D24)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 43x Revol Pepper *(Cave)* → +11,395 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D24 | +120 G |

- **Daily Seed Spent**: 570 G | **End-of-Day Wallet**: **164,940 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **177,025 G** *(164,940 G carryover + 12,085 G payout)*
- **Harvest & Ship** *(+53,620 G arriving D25)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 73x Morrocorn *(Farm)* → +29,200 G (freed)
  - 20x Seatide Garlic *(Farm)* → +20,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 6/9)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **112,675 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **166,295 G** *(112,675 G carryover + 53,620 G payout)*
- **Harvest & Ship** *(+20,690 G arriving D26)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 26x Revol Pepper *(Cave)* → +6,890 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **166,295 G**
- **Plots Left**: Farm: 2 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **186,985 G** *(166,295 G carryover + 20,690 G payout)*
- **Harvest & Ship** *(+57,545 G arriving D27)*:
  - 64x Morrocorn *(Farm)* → +25,600 G (freed)
  - 20x Seatide Garlic *(Farm)* → +20,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 7/9)
  - 43x Revol Pepper *(Cave)* → +11,395 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 35 | 7,000 G | D30 | +7,000 G |

- **Daily Seed Spent**: 18,500 G | **End-of-Day Wallet**: **168,485 G**
- **Plots Left**: Farm: 1 | Waterside: 3 | Cave: 43

---

#### **Day 27**

- **Morning Wallet**: **226,030 G** *(168,485 G carryover + 57,545 G payout)*
- **Harvest & Ship** *(+16,980 G arriving D28)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **226,030 G**
- **Plots Left**: Farm: 1 | Waterside: 6 | Cave: 43

---

#### **Day 28**

- **Morning Wallet**: **243,010 G** *(226,030 G carryover + 16,980 G payout)*
- **Harvest & Ship** *(+16,640 G arriving D29)*:
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 8/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 26x Revol Pepper *(Cave)* → +6,890 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **243,010 G**
- **Plots Left**: Farm: 1 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **259,650 G** *(243,010 G carryover + 16,640 G payout)*
- **Harvest & Ship** *(+243,800 G arriving D30)*:
  - 53x Islet Watermelon *(Waterside)* → +243,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **259,650 G**
- **Plots Left**: Farm: 1 | Waterside: 61 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **503,450 G** *(259,650 G carryover + 243,800 G payout)*
- **Harvest & Ship** *(+228,730 G arriving D31)*:
  - 85x Morrocorn *(Farm)* → +34,000 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 9/9)
  - 20x Islet Watermelon *(Waterside)* → +92,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **503,450 G**
- **Plots Left**: Farm: 190 | Waterside: 81 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **732,180 G** *(503,450 G carryover + 228,730 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 5–30)

- **Starting Wallet (Day 5)**: 21,565 G
- **Ending Wallet (Day 31 Quietus)**: **732,180 G**
- **Pre-planted Crop Sales**: **+248,450 G**
- **New Planting Net Profit**: **+462,165 G**
- **Net Profit (26 days)**: **+710,615 G**
- **Average Daily Profit**: **+27,331 G/day** *(over 26 active days)*
