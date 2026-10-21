# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 236,090 G
- **Plot Capacities (Usable / Max)**: Farm: 264/294 | Waterside: 77/81 | Cave: 81/81

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 1**

- **Morning Wallet**: **236,090 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D5..D17 (5x) | +61,965 G |
| Farm | **Dress Lettuce** | Lethe | 66 | 3,630 G | D3 | +1,980 G |
| Farm | **Royal Eggplant** | Lethe | 82 | 63,960 G | D8, D10, D12 | +54,120 G |
| Farm | **Unionion** | Lethe | 49 | 6,370 G | D4 | +3,185 G |
| Farm | **Unionion** | Nemea | 66 | 6,930 G | D4 | +5,940 G |
| Waterside | **Honey Flower** | Shatolla | 55 | 20,900 G | D7 | +13,750 G |
| Waterside | **Nectarcane** | Shatolla | 22 | 8,140 G | D5, D8, D11 | +8,360 G |

- **Daily Seed Spent**: 155,290 G | **End-of-Day Wallet**: **80,800 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **80,800 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **80,800 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **80,800 G**
- **Harvest & Ship** *(+5,610 G arriving D4)*:
  - 66x Dress Lettuce *(Farm)* → +5,610 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 33 | 1,815 G | D5 | +990 G |
| Farm | **Morrocorn** | Lethe | 16 | 3,680 G | D7 | +2,720 G |
| Farm | **Royal Eggplant** | Lethe | 17 | 13,260 G | D10, D12, D14 | +11,220 G |

- **Daily Seed Spent**: 18,755 G | **End-of-Day Wallet**: **62,045 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **67,655 G** *(62,045 G carryover + 5,610 G payout)*
- **Harvest & Ship** *(+22,425 G arriving D5)*:
  - 115x Unionion *(Farm)* → +22,425 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D7 | +3,960 G |
| Farm | **Unionion** | Lethe | 17 | 2,210 G | D7 | +1,105 G |

- **Daily Seed Spent**: 10,130 G | **End-of-Day Wallet**: **57,525 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **79,950 G** *(57,525 G carryover + 22,425 G payout)*
- **Harvest & Ship** *(+29,770 G arriving D6)*:
  - 33x Dress Lettuce *(Farm)* → +2,805 G (freed)
  - 22x Nectarcane *(Waterside)* → +5,500 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 32 | 4,160 G | D8 | +2,080 G |

- **Daily Seed Spent**: 4,160 G | **End-of-Day Wallet**: **75,790 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **105,560 G** *(75,790 G carryover + 29,770 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **105,560 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **105,560 G**
- **Harvest & Ship** *(+56,245 G arriving D8)*:
  - 99x Lumpotato *(Farm)* → +11,880 G (freed)
  - 16x Morrocorn *(Farm)* → +6,400 G (freed)
  - 17x Unionion *(Farm)* → +3,315 G (freed)
  - 55x Honey Flower *(Waterside)* → +34,650 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 34 | 7,820 G | D11 | +5,780 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D11 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 44 | 16,720 G | D13 | +11,000 G |
| Waterside | **Nectarcane** | Shatolla | 11 | 4,070 G | D11, D14, D17 | +4,180 G |

- **Daily Seed Spent**: 48,410 G | **End-of-Day Wallet**: **57,150 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **113,395 G** *(57,150 G carryover + 56,245 G payout)*
- **Harvest & Ship** *(+72,565 G arriving D9)*:
  - 82x Royal Eggplant *(Farm)* → +39,360 G (regrowth 1/3)
  - 32x Unionion *(Farm)* → +6,240 G (freed)
  - 22x Nectarcane *(Waterside)* → +5,500 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 32 | 3,360 G | D11 | +2,880 G |

- **Daily Seed Spent**: 3,360 G | **End-of-Day Wallet**: **110,035 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **182,600 G** *(110,035 G carryover + 72,565 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **182,600 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **182,600 G**
- **Harvest & Ship** *(+47,520 G arriving D11)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **182,600 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 11**

- **Morning Wallet**: **230,120 G** *(182,600 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+89,155 G arriving D12)*:
  - 133x Morrocorn *(Farm)* → +53,200 G (freed)
  - 32x Unionion *(Farm)* → +6,240 G (freed)
  - 33x Nectarcane *(Waterside)* → +8,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 67 | 5,360 G | D14 | +2,680 G |
| Farm | **Dress Lettuce** | Lethe | 18 | 990 G | D13 | +540 G |
| Farm | **Royal Eggplant** | Lethe | 80 | 62,400 G | D18, D20, D22 | +52,800 G |
| Waterside | **Honey Flower** | Shatolla | 22 | 8,360 G | D17 | +5,500 G |

- **Daily Seed Spent**: 77,110 G | **End-of-Day Wallet**: **153,010 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **242,165 G** *(153,010 G carryover + 89,155 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D13)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 64 | 3,520 G | D14 | +1,920 G |
| Farm | **Royal Eggplant** | Lethe | 17 | 13,260 G | D19, D21, D23 | +11,220 G |

- **Daily Seed Spent**: 16,780 G | **End-of-Day Wallet**: **225,385 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **272,905 G** *(225,385 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+29,250 G arriving D14)*:
  - 18x Dress Lettuce *(Farm)* → +1,530 G (freed)
  - 44x Honey Flower *(Waterside)* → +27,720 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 16 | 880 G | D15 | +480 G |
| Farm | **Royal Eggplant** | Lethe | 2 | 1,560 G | D20, D22, D24 | +1,320 G |
| Waterside | **Honey Flower** | Shatolla | 44 | 16,720 G | D19 | +11,000 G |

- **Daily Seed Spent**: 19,160 G | **End-of-Day Wallet**: **253,745 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **282,995 G** *(253,745 G carryover + 29,250 G payout)*
- **Harvest & Ship** *(+45,855 G arriving D15)*:
  - 64x Dress Lettuce *(Farm)* → +5,440 G (freed)
  - 67x Lumpotato *(Farm)* → +8,040 G (freed)
  - 17x Royal Eggplant *(Farm)* → +8,160 G (regrowth 3/3)
  - 11x Nectarcane *(Waterside)* → +2,750 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D17 | +3,250 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D17 | +8,910 G |

- **Daily Seed Spent**: 16,895 G | **End-of-Day Wallet**: **266,100 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **311,955 G** *(266,100 G carryover + 45,855 G payout)*
- **Harvest & Ship** *(+1,360 G arriving D16)*:
  - 16x Dress Lettuce *(Farm)* → +1,360 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 16 | 1,280 G | D18 | +640 G |

- **Daily Seed Spent**: 1,280 G | **End-of-Day Wallet**: **310,675 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **312,035 G** *(310,675 G carryover + 1,360 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **312,035 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **312,035 G**
- **Harvest & Ship** *(+67,130 G arriving D18)*:
  - 149x Unionion *(Farm)* → +29,055 G (freed)
  - 22x Honey Flower *(Waterside)* → +13,860 G (freed)
  - 11x Nectarcane *(Waterside)* → +2,750 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D21..D30 (4x) | +40,500 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D21 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D21 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 33 | 12,540 G | D23 | +8,250 G |

- **Daily Seed Spent**: 89,200 G | **End-of-Day Wallet**: **222,835 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **289,965 G** *(222,835 G carryover + 67,130 G payout)*
- **Harvest & Ship** *(+40,320 G arriving D19)*:
  - 16x Lumpotato *(Farm)* → +1,920 G (freed)
  - 80x Royal Eggplant *(Farm)* → +38,400 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 16 | 1,280 G | D21 | +640 G |

- **Daily Seed Spent**: 1,280 G | **End-of-Day Wallet**: **288,685 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **329,005 G** *(288,685 G carryover + 40,320 G payout)*
- **Harvest & Ship** *(+35,880 G arriving D20)*:
  - 17x Royal Eggplant *(Farm)* → +8,160 G (regrowth 1/3)
  - 44x Honey Flower *(Waterside)* → +27,720 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D23, D26, D29 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 34 | 12,580 G | D23, D26, D29 | +12,920 G |

- **Daily Seed Spent**: 16,280 G | **End-of-Day Wallet**: **312,725 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **348,605 G** *(312,725 G carryover + 35,880 G payout)*
- **Harvest & Ship** *(+39,360 G arriving D21)*:
  - 82x Royal Eggplant *(Farm)* → +39,360 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **348,605 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **387,965 G** *(348,605 G carryover + 39,360 G payout)*
- **Harvest & Ship** *(+91,145 G arriving D22)*:
  - 16x Lumpotato *(Farm)* → +1,920 G (freed)
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 17x Royal Eggplant *(Farm)* → +8,160 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 57 | 3,135 G | D23 | +1,710 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Unionion** | Nemea | 9 | 945 G | D24 | +810 G |

- **Daily Seed Spent**: 81,300 G | **End-of-Day Wallet**: **306,665 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **397,810 G** *(306,665 G carryover + 91,145 G payout)*
- **Harvest & Ship** *(+39,360 G arriving D23)*:
  - 82x Royal Eggplant *(Farm)* → +39,360 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 42 | 2,310 G | D24 | +1,260 G |
| Farm | **Morrocorn** | Lethe | 38 | 8,740 G | D26 | +6,460 G |

- **Daily Seed Spent**: 11,050 G | **End-of-Day Wallet**: **386,760 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **426,120 G** *(386,760 G carryover + 39,360 G payout)*
- **Harvest & Ship** *(+44,795 G arriving D24)*:
  - 57x Dress Lettuce *(Farm)* → +4,845 G (freed)
  - 17x Royal Eggplant *(Farm)* → +8,160 G (regrowth 3/3)
  - 33x Honey Flower *(Waterside)* → +20,790 G (freed)
  - 44x Nectarcane *(Waterside)* → +11,000 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 37 | 4,810 G | D26 | +2,405 G |
| Farm | **Unionion** | Nemea | 37 | 3,885 G | D26 | +3,330 G |
| Waterside | **Honey Flower** | Shatolla | 33 | 12,540 G | D29 | +8,250 G |

- **Daily Seed Spent**: 21,235 G | **End-of-Day Wallet**: **404,885 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **449,680 G** *(404,885 G carryover + 44,795 G payout)*
- **Harvest & Ship** *(+27,750 G arriving D25)*:
  - 42x Dress Lettuce *(Farm)* → +3,570 G (freed)
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 3/3)
  - 9x Unionion *(Farm)* → +1,755 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 41 | 3,280 G | D27 | +1,640 G |
| Farm | **Unionion** | Lethe | 12 | 1,560 G | D27 | +780 G |

- **Daily Seed Spent**: 4,840 G | **End-of-Day Wallet**: **444,840 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **472,590 G** *(444,840 G carryover + 27,750 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **472,590 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **472,590 G**
- **Harvest & Ship** *(+40,630 G arriving D27)*:
  - 38x Morrocorn *(Farm)* → +15,200 G (freed)
  - 74x Unionion *(Farm)* → +14,430 G (freed)
  - 44x Nectarcane *(Waterside)* → +11,000 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 12 | 2,760 G | D30 | +2,040 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 22,560 G | **End-of-Day Wallet**: **450,030 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **490,660 G** *(450,030 G carryover + 40,630 G payout)*
- **Harvest & Ship** *(+28,725 G arriving D28)*:
  - 41x Lumpotato *(Farm)* → +4,920 G (freed)
  - 12x Unionion *(Farm)* → +2,340 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 53 | 5,565 G | D30 | +4,770 G |

- **Daily Seed Spent**: 5,565 G | **End-of-Day Wallet**: **485,095 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **513,820 G** *(485,095 G carryover + 28,725 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D29)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **513,820 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 29**

- **Morning Wallet**: **561,340 G** *(513,820 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+31,790 G arriving D30)*:
  - 33x Honey Flower *(Waterside)* → +20,790 G (freed)
  - 44x Nectarcane *(Waterside)* → +11,000 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **561,340 G**
- **Plots Left**: Farm: 1 | Waterside: 77 | Cave: 0

---

#### **Day 30**

- **Morning Wallet**: **593,130 G** *(561,340 G carryover + 31,790 G payout)*
- **Harvest & Ship** *(+123,720 G arriving D31)*:
  - 111x Morrocorn *(Farm)* → +44,400 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/2)
  - 53x Unionion *(Farm)* → +10,335 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **593,130 G**
- **Plots Left**: Farm: 165 | Waterside: 77 | Cave: 0

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **716,850 G** *(593,130 G carryover + 123,720 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 236,090 G
- **Ending Wallet (Day 31 Quietus)**: **716,850 G**
- **Net Profit (30 days)**: **+480,760 G**
- **Average Daily Profit**: **+16,025 G/day** *(over 30 active days)*
