# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 3
- **Planning Timeline**: Day 3 -> Day 30 (28d Quietus window)
- **Capital Budget**: 8,760 G
- **Plot Capacities (Usable / Max)**: Farm: 190/196 | Waterside: 81/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Dress Lettuce** | 9 | Day 1 | D3 | Freed D3 | +765 G |
| Farm | **Morrocorn** | 107 | Day 1 | D5 | Freed D5 | +42,800 G |
| Farm | **Seatide Garlic** | 4 | Day 1 | D7 | Freed D7 | +4,000 G |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D6, D8, D10, D12, D14, D16, D18, D20, D22 | Freed D22 | +69,300 G |
| Waterside | **Honey Flower** | 10 | Day 1 | D7 | Freed D7 | +6,300 G |
| Waterside | **Islet Watermelon** | 3 | Day 1 | D13 | Freed D13 | +13,800 G |
| Waterside | **Nectarcane** | 43 | Day 1 | D5, D8, D11 | Freed D11 | +32,250 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D5, D8, D11, D14, D17 | Freed D17 | +15,900 G |
| Cave | **Sudor Pepper** | 69 | Day 1 | D4, D7, D10 | Freed D10 | +51,750 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 3**

- **Morning Wallet**: **8,760 G**
- **Harvest & Ship** *(+765 G arriving D4)*:
  - 9x Dress Lettuce *(Farm)* → +765 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 7 | 665 G | D4 | +140 G |
| Farm | **Shatollan Paprika** | Shatolla | 2 | 500 G | D8..D24 (9x) | +1,480 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D15 | +6,300 G |

- **Daily Seed Spent**: 8,665 G | **End-of-Day Wallet**: **95 G**
- **Plots Left**: Farm: 0 | Waterside: 22 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **860 G** *(95 G carryover + 765 G payout)*
- **Harvest & Ship** *(+18,055 G arriving D5)*:
  - 7x Carrop *(Farm)* → +805 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 7 | 385 G | D6 | +210 G |

- **Daily Seed Spent**: 385 G | **End-of-Day Wallet**: **475 G**
- **Plots Left**: Farm: 0 | Waterside: 22 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **18,530 G** *(475 G carryover + 18,055 G payout)*
- **Harvest & Ship** *(+56,730 G arriving D6)*:
  - 107x Morrocorn *(Farm)* → +42,800 G (freed)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 1/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 46 | 2,530 G | D7 | +1,380 G |
| Farm | **Carrop** | Nemea | 4 | 380 G | D6 | +80 G |
| Farm | **Morrocorn** | Shatolla | 3 | 600 G | D9 | +600 G |
| Waterside | **Islet Watermelon** | Shatolla | 6 | 15,000 G | D17 | +12,600 G |

- **Daily Seed Spent**: 18,510 G | **End-of-Day Wallet**: **20 G**
- **Plots Left**: Farm: 54 | Waterside: 16 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **56,750 G** *(20 G carryover + 56,730 G payout)*
- **Harvest & Ship** *(+8,755 G arriving D7)*:
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 7x Dress Lettuce *(Farm)* → +595 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 1/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 17 | 935 G | D8 | +510 G |
| Farm | **Morrocorn** | Lethe | 31 | 7,130 G | D10 | +5,270 G |
| Farm | **Morrocorn** | Shatolla | 4 | 800 G | D10 | +800 G |
| Farm | **Seatide Garlic** | Shatolla | 12 | 7,800 G | D12 | +4,200 G |
| Waterside | **Islet Watermelon** | Shatolla | 16 | 40,000 G | D18 | +33,600 G |

- **Daily Seed Spent**: 56,665 G | **End-of-Day Wallet**: **85 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **8,840 G** *(85 G carryover + 8,755 G payout)*
- **Harvest & Ship** *(+31,460 G arriving D8)*:
  - 46x Dress Lettuce *(Farm)* → +3,910 G (freed)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 10x Honey Flower *(Waterside)* → +6,300 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 19 | 4,370 G | D11 | +3,230 G |
| Farm | **Carrop** | Nemea | 31 | 2,945 G | D8 | +620 G |
| Waterside | **Nectarcane** | Shatolla | 4 | 1,480 G | D11, D14, D17 | +1,520 G |

- **Daily Seed Spent**: 8,795 G | **End-of-Day Wallet**: **45 G**
- **Plots Left**: Farm: 1 | Waterside: 6 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **31,505 G** *(45 G carryover + 31,460 G payout)*
- **Harvest & Ship** *(+26,860 G arriving D9)*:
  - 31x Carrop *(Farm)* → +3,565 G (freed)
  - 17x Dress Lettuce *(Farm)* → +1,445 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 2/9)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 2/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 6 | 570 G | D9 | +120 G |
| Waterside | **Nectarcane** | Nemea | 6 | 2,220 G | D12, D15, D18 | +2,280 G |
| Farm | **Seatide Garlic** | Shatolla | 43 | 27,950 G | D14 | +15,050 G |

- **Daily Seed Spent**: 30,740 G | **End-of-Day Wallet**: **765 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **27,625 G** *(765 G carryover + 26,860 G payout)*
- **Harvest & Ship** *(+1,890 G arriving D10)*:
  - 6x Carrop *(Farm)* → +690 G (freed)
  - 3x Morrocorn *(Farm)* → +1,200 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 8 | 5,200 G | D15 | +2,800 G |

- **Daily Seed Spent**: 5,200 G | **End-of-Day Wallet**: **22,425 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **24,315 G** *(22,425 G carryover + 1,890 G payout)*
- **Harvest & Ship** *(+39,170 G arriving D11)*:
  - 35x Morrocorn *(Farm)* → +14,000 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 3/9)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 1 | 560 G | D14..D26 (5x) | +765 G |
| Farm | **Seatide Garlic** | Shatolla | 36 | 23,400 G | D16 | +12,600 G |

- **Daily Seed Spent**: 23,960 G | **End-of-Day Wallet**: **355 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 68

---

#### **Day 11**

- **Morning Wallet**: **39,525 G** *(355 G carryover + 39,170 G payout)*
- **Harvest & Ship** *(+22,530 G arriving D12)*:
  - 19x Morrocorn *(Farm)* → +7,600 G (freed)
  - 47x Nectarcane *(Waterside)* → +11,750 G (regrowth 3/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 19 | 10,640 G | D15..D27 (5x) | +14,535 G |
| Farm | **Seatide Garlic** | Shatolla | 19 | 12,350 G | D17 | +6,650 G |
| Waterside | **Honey Flower** | Shatolla | 43 | 16,340 G | D17 | +10,750 G |

- **Daily Seed Spent**: 39,330 G | **End-of-Day Wallet**: **195 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 49

---

#### **Day 12**

- **Morning Wallet**: **22,725 G** *(195 G carryover + 22,530 G payout)*
- **Harvest & Ship** *(+21,420 G arriving D13)*:
  - 12x Seatide Garlic *(Farm)* → +12,000 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 4/9)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 36 | 20,160 G | D16..D28 (5x) | +27,540 G |
| Farm | **Morrocorn** | Shatolla | 12 | 2,400 G | D16 | +2,400 G |

- **Daily Seed Spent**: 22,560 G | **End-of-Day Wallet**: **165 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 13

---

#### **Day 13**

- **Morning Wallet**: **21,585 G** *(165 G carryover + 21,420 G payout)*
- **Harvest & Ship** *(+13,800 G arriving D14)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 13 | 7,280 G | D17..D29 (5x) | +9,945 G |

- **Daily Seed Spent**: 7,280 G | **End-of-Day Wallet**: **14,305 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **28,105 G** *(14,305 G carryover + 13,800 G payout)*
- **Harvest & Ship** *(+55,365 G arriving D15)*:
  - 43x Seatide Garlic *(Farm)* → +43,000 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 5/9)
  - 4x Nectarcane *(Waterside)* → +1,000 G (regrowth 2/3)
  - 13x Revol Pepper *(Cave)* → +3,445 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 43 | 27,950 G | D20 | +15,050 G |

- **Daily Seed Spent**: 27,950 G | **End-of-Day Wallet**: **155 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **55,520 G** *(155 G carryover + 55,365 G payout)*
- **Harvest & Ship** *(+28,335 G arriving D16)*:
  - 8x Seatide Garlic *(Farm)* → +8,000 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 2/3)
  - 19x Revol Pepper *(Cave)* → +5,035 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 8 | 760 G | D16 | +160 G |
| Waterside | **Islet Watermelon** | Shatolla | 6 | 15,000 G | D27 | +12,600 G |

- **Daily Seed Spent**: 15,760 G | **End-of-Day Wallet**: **39,760 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **68,095 G** *(39,760 G carryover + 28,335 G payout)*
- **Harvest & Ship** *(+59,180 G arriving D17)*:
  - 8x Carrop *(Farm)* → +920 G (freed)
  - 12x Morrocorn *(Farm)* → +4,800 G (freed)
  - 36x Seatide Garlic *(Farm)* → +36,000 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 6/9)
  - 36x Revol Pepper *(Cave)* → +9,540 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 56 | 11,200 G | D20 | +11,200 G |

- **Daily Seed Spent**: 11,200 G | **End-of-Day Wallet**: **56,895 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **116,075 G** *(56,895 G carryover + 59,180 G payout)*
- **Harvest & Ship** *(+81,580 G arriving D18)*:
  - 19x Seatide Garlic *(Farm)* → +19,000 G (freed)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 6x Islet Watermelon *(Waterside)* → +27,600 G (freed)
  - 4x Nectarcane *(Waterside)* → +1,000 G (regrowth 3/3)
  - 26x Revol Pepper *(Cave)* → +6,890 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Farm | **Dress Lettuce** | Lethe | 15 | 825 G | D19 | +450 G |
| Farm | **Seatide Garlic** | Shatolla | 4 | 2,600 G | D23 | +1,400 G |
| Waterside | **Islet Watermelon** | Shatolla | 42 | 105,000 G | D29 | +88,200 G |

- **Daily Seed Spent**: 115,145 G | **End-of-Day Wallet**: **930 G**
- **Plots Left**: Farm: 0 | Waterside: 11 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **82,510 G** *(930 G carryover + 81,580 G payout)*
- **Harvest & Ship** *(+88,055 G arriving D19)*:
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 7/9)
  - 16x Islet Watermelon *(Waterside)* → +73,600 G (freed)
  - 6x Nectarcane *(Waterside)* → +1,500 G (regrowth 3/3)
  - 19x Revol Pepper *(Cave)* → +5,035 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 33 | 82,500 G | D30 | +69,300 G |

- **Daily Seed Spent**: 82,500 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **88,065 G** *(10 G carryover + 88,055 G payout)*
- **Harvest & Ship** *(+10,815 G arriving D20)*:
  - 15x Dress Lettuce *(Farm)* → +1,275 G (freed)
  - 36x Revol Pepper *(Cave)* → +9,540 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 15 | 1,425 G | D20 | +300 G |

- **Daily Seed Spent**: 1,425 G | **End-of-Day Wallet**: **86,640 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **97,455 G** *(86,640 G carryover + 10,815 G payout)*
- **Harvest & Ship** *(+78,755 G arriving D21)*:
  - 15x Carrop *(Farm)* → +1,725 G (freed)
  - 56x Morrocorn *(Farm)* → +22,400 G (freed)
  - 43x Seatide Garlic *(Farm)* → +43,000 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 8/9)
  - 14x Revol Pepper *(Cave)* → +3,710 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D24 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 31 | 6,200 G | D24 | +6,200 G |
| Farm | **Seatide Garlic** | Shatolla | 33 | 21,450 G | D26 | +11,550 G |

- **Daily Seed Spent**: 39,150 G | **End-of-Day Wallet**: **58,305 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **137,060 G** *(58,305 G carryover + 78,755 G payout)*
- **Harvest & Ship** *(+8,215 G arriving D22)*:
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 3/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **137,060 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **145,275 G** *(137,060 G carryover + 8,215 G payout)*
- **Harvest & Ship** *(+17,460 G arriving D23)*:
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 9/9)
  - 36x Revol Pepper *(Cave)* → +9,540 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D26 | +8,500 G |
| Farm | **Carrop** | Nemea | 12 | 1,140 G | D23 | +240 G |
| Farm | **Morrocorn** | Shatolla | 8 | 1,600 G | D26 | +1,600 G |

- **Daily Seed Spent**: 14,240 G | **End-of-Day Wallet**: **131,035 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **148,495 G** *(131,035 G carryover + 17,460 G payout)*
- **Harvest & Ship** *(+9,090 G arriving D24)*:
  - 12x Carrop *(Farm)* → +1,380 G (freed)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 14x Revol Pepper *(Cave)* → +3,710 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 16 | 1,520 G | D24 | +320 G |

- **Daily Seed Spent**: 1,520 G | **End-of-Day Wallet**: **146,975 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **156,065 G** *(146,975 G carryover + 9,090 G payout)*
- **Harvest & Ship** *(+42,675 G arriving D25)*:
  - 16x Carrop *(Farm)* → +1,840 G (freed)
  - 81x Morrocorn *(Farm)* → +32,400 G (freed)
  - 2x Shatollan Paprika *(Farm)* → +220 G (regrowth 9/9)
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **91,715 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **134,390 G** *(91,715 G carryover + 42,675 G payout)*
- **Harvest & Ship** *(+9,540 G arriving D26)*:
  - 36x Revol Pepper *(Cave)* → +9,540 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **134,390 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **143,930 G** *(134,390 G carryover + 9,540 G payout)*
- **Harvest & Ship** *(+59,910 G arriving D27)*:
  - 58x Morrocorn *(Farm)* → +23,200 G (freed)
  - 33x Seatide Garlic *(Farm)* → +33,000 G (freed)
  - 14x Revol Pepper *(Cave)* → +3,710 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 91 | 18,200 G | D30 | +18,200 G |

- **Daily Seed Spent**: 18,200 G | **End-of-Day Wallet**: **125,730 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 1

---

#### **Day 27**

- **Morning Wallet**: **185,640 G** *(125,730 G carryover + 59,910 G payout)*
- **Harvest & Ship** *(+35,815 G arriving D28)*:
  - 6x Islet Watermelon *(Waterside)* → +27,600 G (freed)
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **185,640 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 20

---

#### **Day 28**

- **Morning Wallet**: **221,455 G** *(185,640 G carryover + 35,815 G payout)*
- **Harvest & Ship** *(+9,540 G arriving D29)*:
  - 36x Revol Pepper *(Cave)* → +9,540 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **221,455 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 56

---

#### **Day 29**

- **Morning Wallet**: **230,995 G** *(221,455 G carryover + 9,540 G payout)*
- **Harvest & Ship** *(+196,645 G arriving D30)*:
  - 42x Islet Watermelon *(Waterside)* → +193,200 G (freed)
  - 13x Revol Pepper *(Cave)* → +3,445 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **230,995 G**
- **Plots Left**: Farm: 0 | Waterside: 48 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **427,640 G** *(230,995 G carryover + 196,645 G payout)*
- **Harvest & Ship** *(+290,380 G arriving D31)*:
  - 91x Morrocorn *(Farm)* → +36,400 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 33x Islet Watermelon *(Waterside)* → +151,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **427,640 G**
- **Plots Left**: Farm: 190 | Waterside: 81 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **718,020 G** *(427,640 G carryover + 290,380 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 3–30)

- **Starting Wallet (Day 3)**: 8,760 G
- **Ending Wallet (Day 31 Quietus)**: **718,020 G**
- **Pre-planted Crop Sales**: **+236,865 G**
- **New Planting Net Profit**: **+472,395 G**
- **Net Profit (28 days)**: **+709,260 G**
- **Average Daily Profit**: **+25,331 G/day** *(over 28 active days)*
