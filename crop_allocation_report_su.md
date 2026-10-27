# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 63,000 G
- **Plot Capacities (Usable / Max)**: Farm: 188/196 | Waterside: 81/81 | Cave: 81/81

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 1**

- **Morning Wallet**: **63,000 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 61 | 24,400 G | D4, D7, D10 | +21,350 G |
| Farm | **Dress Lettuce** | Lethe | 93 | 5,115 G | D3 | +2,790 G |
| Farm | **Morrocorn** | Shatolla | 28 | 5,600 G | D5 | +5,600 G |
| Farm | **Shatollan Paprika** | Shatolla | 67 | 16,750 G | D6..D22 (9x) | +49,580 G |
| Waterside | **Nectarcane** | Shatolla | 30 | 11,100 G | D5, D8, D11 | +11,400 G |

- **Daily Seed Spent**: 62,965 G | **End-of-Day Wallet**: **35 G**
- **Plots Left**: Farm: 0 | Waterside: 51 | Cave: 20

---

#### **Day 2**

- **Morning Wallet**: **35 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **35 G**
- **Plots Left**: Farm: 0 | Waterside: 51 | Cave: 20

---

#### **Day 3**

- **Morning Wallet**: **35 G**
- **Harvest & Ship** *(+7,905 G arriving D4)*:
  - 93x Dress Lettuce *(Farm)* → +7,905 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **35 G**
- **Plots Left**: Farm: 93 | Waterside: 51 | Cave: 20

---

#### **Day 4**

- **Morning Wallet**: **7,940 G** *(35 G carryover + 7,905 G payout)*
- **Harvest & Ship** *(+15,250 G arriving D5)*:
  - 61x Sudor Pepper *(Cave)* → +15,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 19 | 7,600 G | D7, D10, D13 | +6,650 G |
| Farm | **Dress Lettuce** | Lethe | 6 | 330 G | D6 | +180 G |

- **Daily Seed Spent**: 7,930 G | **End-of-Day Wallet**: **10 G**
- **Plots Left**: Farm: 87 | Waterside: 51 | Cave: 1

---

#### **Day 5**

- **Morning Wallet**: **15,260 G** *(10 G carryover + 15,250 G payout)*
- **Harvest & Ship** *(+18,700 G arriving D6)*:
  - 28x Morrocorn *(Farm)* → +11,200 G (freed)
  - 30x Nectarcane *(Waterside)* → +7,500 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 1 | 560 G | D9..D21 (5x) | +765 G |
| Farm | **Morrocorn** | Shatolla | 35 | 7,000 G | D9 | +7,000 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D17 | +6,300 G |

- **Daily Seed Spent**: 15,060 G | **End-of-Day Wallet**: **200 G**
- **Plots Left**: Farm: 80 | Waterside: 48 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **18,900 G** *(200 G carryover + 18,700 G payout)*
- **Harvest & Ship** *(+7,880 G arriving D7)*:
  - 6x Dress Lettuce *(Farm)* → +510 G (freed)
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 1/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D10 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 36 | 7,200 G | D10 | +7,200 G |

- **Daily Seed Spent**: 18,700 G | **End-of-Day Wallet**: **200 G**
- **Plots Left**: Farm: 0 | Waterside: 48 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **8,080 G** *(200 G carryover + 7,880 G payout)*
- **Harvest & Ship** *(+20,000 G arriving D8)*:
  - 80x Sudor Pepper *(Cave)* → +20,000 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Shatolla | 21 | 7,770 G | D11, D14, D17 | +7,980 G |

- **Daily Seed Spent**: 7,770 G | **End-of-Day Wallet**: **310 G**
- **Plots Left**: Farm: 0 | Waterside: 27 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **20,310 G** *(310 G carryover + 20,000 G payout)*
- **Harvest & Ship** *(+14,870 G arriving D9)*:
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 2/9)
  - 30x Nectarcane *(Waterside)* → +7,500 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D12, D15, D18 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 17 | 6,290 G | D12, D15, D18 | +6,460 G |

- **Daily Seed Spent**: 9,990 G | **End-of-Day Wallet**: **10,320 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **25,190 G** *(10,320 G carryover + 14,870 G payout)*
- **Harvest & Ship** *(+14,265 G arriving D10)*:
  - 35x Morrocorn *(Farm)* → +14,000 G (freed)
  - 1x Revol Pepper *(Cave)* → +265 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 35 | 22,750 G | D15 | +12,250 G |

- **Daily Seed Spent**: 22,750 G | **End-of-Day Wallet**: **2,440 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **16,705 G** *(2,440 G carryover + 14,265 G payout)*
- **Harvest & Ship** *(+61,770 G arriving D11)*:
  - 86x Morrocorn *(Farm)* → +34,400 G (freed)
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 3/9)
  - 80x Sudor Pepper *(Cave)* → +20,000 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 71 | 6,745 G | D11 | +1,420 G |
| Farm | **Seatide Garlic** | Shatolla | 15 | 9,750 G | D16 | +5,250 G |

- **Daily Seed Spent**: 16,495 G | **End-of-Day Wallet**: **210 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 61

---

#### **Day 11**

- **Morning Wallet**: **61,980 G** *(210 G carryover + 61,770 G payout)*
- **Harvest & Ship** *(+20,915 G arriving D12)*:
  - 71x Carrop *(Farm)* → +8,165 G (freed)
  - 51x Nectarcane *(Waterside)* → +12,750 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 11 | 4,400 G | D14, D17, D20 | +3,850 G |
| Farm | **Seatide Garlic** | Shatolla | 71 | 46,150 G | D17 | +24,850 G |
| Waterside | **Honey Flower** | Shatolla | 29 | 11,020 G | D17 | +7,250 G |

- **Daily Seed Spent**: 61,570 G | **End-of-Day Wallet**: **410 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 50

---

#### **Day 12**

- **Morning Wallet**: **21,325 G** *(410 G carryover + 20,915 G payout)*
- **Harvest & Ship** *(+14,385 G arriving D13)*:
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 4/9)
  - 27x Nectarcane *(Waterside)* → +6,750 G (regrowth 1/3)
  - 1x Revol Pepper *(Cave)* → +265 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 20 | 11,200 G | D16..D28 (5x) | +15,300 G |
| Cave | **Sudor Pepper** | Argene | 24 | 9,600 G | D15, D18, D21 | +8,400 G |

- **Daily Seed Spent**: 20,800 G | **End-of-Day Wallet**: **525 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 6

---

#### **Day 13**

- **Morning Wallet**: **14,910 G** *(525 G carryover + 14,385 G payout)*
- **Harvest & Ship** *(+4,750 G arriving D14)*:
  - 19x Sudor Pepper *(Cave)* → +4,750 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 25 | 14,000 G | D17..D29 (5x) | +19,125 G |
| Waterside | **Nectarcane** | Shatolla | 1 | 370 G | D17, D20, D23 | +380 G |

- **Daily Seed Spent**: 14,370 G | **End-of-Day Wallet**: **540 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **5,290 G** *(540 G carryover + 4,750 G payout)*
- **Harvest & Ship** *(+15,370 G arriving D15)*:
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 5/9)
  - 21x Nectarcane *(Waterside)* → +5,250 G (regrowth 2/3)
  - 11x Sudor Pepper *(Cave)* → +2,750 G (regrowth 1/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **5,290 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **20,660 G** *(5,290 G carryover + 15,370 G payout)*
- **Harvest & Ship** *(+48,015 G arriving D16)*:
  - 35x Seatide Garlic *(Farm)* → +35,000 G (freed)
  - 27x Nectarcane *(Waterside)* → +6,750 G (regrowth 2/3)
  - 1x Revol Pepper *(Cave)* → +265 G (regrowth 3/5)
  - 24x Sudor Pepper *(Cave)* → +6,000 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 11 | 1,045 G | D16 | +220 G |
| Farm | **Morrocorn** | Shatolla | 24 | 4,800 G | D19 | +4,800 G |

- **Daily Seed Spent**: 5,845 G | **End-of-Day Wallet**: **14,815 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **62,830 G** *(14,815 G carryover + 48,015 G payout)*
- **Harvest & Ship** *(+28,935 G arriving D17)*:
  - 11x Carrop *(Farm)* → +1,265 G (freed)
  - 15x Seatide Garlic *(Farm)* → +15,000 G (freed)
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 6/9)
  - 20x Revol Pepper *(Cave)* → +5,300 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 26 | 5,200 G | D20 | +5,200 G |

- **Daily Seed Spent**: 5,200 G | **End-of-Day Wallet**: **57,630 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **86,565 G** *(57,630 G carryover + 28,935 G payout)*
- **Harvest & Ship** *(+117,945 G arriving D18)*:
  - 71x Seatide Garlic *(Farm)* → +71,000 G (freed)
  - 29x Honey Flower *(Waterside)* → +18,270 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 22x Nectarcane *(Waterside)* → +5,500 G (regrowth 3/3)
  - 25x Revol Pepper *(Cave)* → +6,625 G (regrowth 1/5)
  - 11x Sudor Pepper *(Cave)* → +2,750 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 71 | 3,905 G | D19 | +2,130 G |
| Waterside | **Islet Watermelon** | Shatolla | 33 | 82,500 G | D29 | +69,300 G |

- **Daily Seed Spent**: 86,405 G | **End-of-Day Wallet**: **160 G**
- **Plots Left**: Farm: 0 | Waterside: 20 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **118,105 G** *(160 G carryover + 117,945 G payout)*
- **Harvest & Ship** *(+20,385 G arriving D19)*:
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 7/9)
  - 27x Nectarcane *(Waterside)* → +6,750 G (regrowth 3/3)
  - 1x Revol Pepper *(Cave)* → +265 G (regrowth 4/5)
  - 24x Sudor Pepper *(Cave)* → +6,000 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 47 | 117,500 G | D30 | +98,700 G |

- **Daily Seed Spent**: 117,500 G | **End-of-Day Wallet**: **605 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **20,990 G** *(605 G carryover + 20,385 G payout)*
- **Harvest & Ship** *(+20,935 G arriving D20)*:
  - 71x Dress Lettuce *(Farm)* → +6,035 G (freed)
  - 24x Morrocorn *(Farm)* → +9,600 G (freed)
  - 20x Revol Pepper *(Cave)* → +5,300 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 46 | 10,580 G | D23 | +7,820 G |
| Farm | **Morrocorn** | Shatolla | 49 | 9,800 G | D23 | +9,800 G |

- **Daily Seed Spent**: 20,380 G | **End-of-Day Wallet**: **610 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **21,545 G** *(610 G carryover + 20,935 G payout)*
- **Harvest & Ship** *(+27,395 G arriving D21)*:
  - 26x Morrocorn *(Farm)* → +10,400 G (freed)
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 8/9)
  - 1x Nectarcane *(Waterside)* → +250 G (regrowth 2/3)
  - 25x Revol Pepper *(Cave)* → +6,625 G (regrowth 2/5)
  - 11x Sudor Pepper *(Cave)* → +2,750 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 11 | 4,400 G | D23, D26, D29 | +3,850 G |
| Farm | **Seatide Garlic** | Shatolla | 26 | 16,900 G | D26 | +9,100 G |

- **Daily Seed Spent**: 21,300 G | **End-of-Day Wallet**: **245 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **27,640 G** *(245 G carryover + 27,395 G payout)*
- **Harvest & Ship** *(+6,265 G arriving D22)*:
  - 1x Revol Pepper *(Cave)* → +265 G (regrowth 5/5)
  - 24x Sudor Pepper *(Cave)* → +6,000 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Sudor Pepper** | Argene | 25 | 10,000 G | D24, D27, D30 | +8,750 G |

- **Daily Seed Spent**: 10,000 G | **End-of-Day Wallet**: **17,640 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **23,905 G** *(17,640 G carryover + 6,265 G payout)*
- **Harvest & Ship** *(+12,670 G arriving D23)*:
  - 67x Shatollan Paprika *(Farm)* → +7,370 G (regrowth 9/9)
  - 20x Revol Pepper *(Cave)* → +5,300 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 5 | 275 G | D24 | +150 G |
| Farm | **Carrop** | Nemea | 2 | 190 G | D23 | +40 G |
| Farm | **Morrocorn** | Shatolla | 60 | 12,000 G | D26 | +12,000 G |

- **Daily Seed Spent**: 12,465 G | **End-of-Day Wallet**: **11,440 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **24,110 G** *(11,440 G carryover + 12,670 G payout)*
- **Harvest & Ship** *(+47,855 G arriving D24)*:
  - 2x Carrop *(Farm)* → +230 G (freed)
  - 95x Morrocorn *(Farm)* → +38,000 G (freed)
  - 1x Nectarcane *(Waterside)* → +250 G (regrowth 3/3)
  - 25x Revol Pepper *(Cave)* → +6,625 G (regrowth 3/5)
  - 11x Sudor Pepper *(Cave)* → +2,750 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 3 | 165 G | D25 | +90 G |
| Farm | **Carrop** | Nemea | 68 | 6,460 G | D24 | +1,360 G |
| Farm | **Seatide Garlic** | Shatolla | 26 | 16,900 G | D29 | +9,100 G |

- **Daily Seed Spent**: 23,525 G | **End-of-Day Wallet**: **585 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **48,440 G** *(585 G carryover + 47,855 G payout)*
- **Harvest & Ship** *(+14,495 G arriving D25)*:
  - 68x Carrop *(Farm)* → +7,820 G (freed)
  - 5x Dress Lettuce *(Farm)* → +425 G (freed)
  - 25x Sudor Pepper *(Cave)* → +6,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 73 | 47,450 G | D30 | +25,550 G |
| Waterside | **Honey Flower** | Shatolla | 1 | 380 G | D30 | +250 G |

- **Daily Seed Spent**: 47,830 G | **End-of-Day Wallet**: **610 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **15,105 G** *(610 G carryover + 14,495 G payout)*
- **Harvest & Ship** *(+5,555 G arriving D26)*:
  - 3x Dress Lettuce *(Farm)* → +255 G (freed)
  - 20x Revol Pepper *(Cave)* → +5,300 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 3 | 285 G | D26 | +60 G |

- **Daily Seed Spent**: 285 G | **End-of-Day Wallet**: **14,820 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **20,375 G** *(14,820 G carryover + 5,555 G payout)*
- **Harvest & Ship** *(+59,720 G arriving D27)*:
  - 3x Carrop *(Farm)* → +345 G (freed)
  - 60x Morrocorn *(Farm)* → +24,000 G (freed)
  - 26x Seatide Garlic *(Farm)* → +26,000 G (freed)
  - 25x Revol Pepper *(Cave)* → +6,625 G (regrowth 4/5)
  - 11x Sudor Pepper *(Cave)* → +2,750 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D30 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 39 | 7,800 G | D30 | +7,800 G |

- **Daily Seed Spent**: 19,300 G | **End-of-Day Wallet**: **1,075 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **60,795 G** *(1,075 G carryover + 59,720 G payout)*
- **Harvest & Ship** *(+6,250 G arriving D28)*:
  - 25x Sudor Pepper *(Cave)* → +6,250 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **60,795 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **67,045 G** *(60,795 G carryover + 6,250 G payout)*
- **Harvest & Ship** *(+5,300 G arriving D29)*:
  - 20x Revol Pepper *(Cave)* → +5,300 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **67,045 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 20

---

#### **Day 29**

- **Morning Wallet**: **72,345 G** *(67,045 G carryover + 5,300 G payout)*
- **Harvest & Ship** *(+187,175 G arriving D30)*:
  - 26x Seatide Garlic *(Farm)* → +26,000 G (freed)
  - 33x Islet Watermelon *(Waterside)* → +151,800 G (freed)
  - 25x Revol Pepper *(Cave)* → +6,625 G (regrowth 5/5)
  - 11x Sudor Pepper *(Cave)* → +2,750 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 26 | 2,470 G | D30 | +520 G |

- **Daily Seed Spent**: 2,470 G | **End-of-Day Wallet**: **69,875 G**
- **Plots Left**: Farm: 0 | Waterside: 33 | Cave: 56

---

#### **Day 30**

- **Morning Wallet**: **257,050 G** *(69,875 G carryover + 187,175 G payout)*
- **Harvest & Ship** *(+334,670 G arriving D31)*:
  - 26x Carrop *(Farm)* → +2,990 G (freed)
  - 89x Morrocorn *(Farm)* → +35,600 G (freed)
  - 73x Seatide Garlic *(Farm)* → +73,000 G (freed)
  - 1x Honey Flower *(Waterside)* → +630 G (freed)
  - 47x Islet Watermelon *(Waterside)* → +216,200 G (freed)
  - 25x Sudor Pepper *(Cave)* → +6,250 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **257,050 G**
- **Plots Left**: Farm: 188 | Waterside: 81 | Cave: 81

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **591,720 G** *(257,050 G carryover + 334,670 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 63,000 G
- **Ending Wallet (Day 31 Quietus)**: **591,720 G**
- **Net Profit (30 days)**: **+528,720 G**
- **Average Daily Profit**: **+17,624 G/day** *(over 30 active days)*
