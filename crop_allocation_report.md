# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 236,090 G
- **Plot Capacities (Usable / Max)**: Farm: 264/294 | Waterside: 81/81 | Cave: 81/81

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
| Waterside | **Honey Flower** | Shatolla | 63 | 23,940 G | D7 | +15,750 G |
| Waterside | **Nectarcane** | Shatolla | 18 | 6,660 G | D5, D8, D11 | +6,840 G |

- **Daily Seed Spent**: 156,850 G | **End-of-Day Wallet**: **79,240 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **79,240 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **79,240 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **79,240 G**
- **Harvest & Ship** *(+5,610 G arriving D4)*:
  - 66x Dress Lettuce *(Farm)* → +5,610 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 33 | 1,815 G | D5 | +990 G |
| Farm | **Morrocorn** | Lethe | 16 | 3,680 G | D7 | +2,720 G |
| Farm | **Royal Eggplant** | Lethe | 17 | 13,260 G | D10, D12, D14 | +11,220 G |

- **Daily Seed Spent**: 18,755 G | **End-of-Day Wallet**: **60,485 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **66,095 G** *(60,485 G carryover + 5,610 G payout)*
- **Harvest & Ship** *(+22,425 G arriving D5)*:
  - 115x Unionion *(Farm)* → +22,425 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D7 | +3,960 G |
| Farm | **Unionion** | Lethe | 17 | 2,210 G | D7 | +1,105 G |

- **Daily Seed Spent**: 10,130 G | **End-of-Day Wallet**: **55,965 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **78,390 G** *(55,965 G carryover + 22,425 G payout)*
- **Harvest & Ship** *(+28,770 G arriving D6)*:
  - 33x Dress Lettuce *(Farm)* → +2,805 G (freed)
  - 18x Nectarcane *(Waterside)* → +4,500 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 32 | 4,160 G | D8 | +2,080 G |

- **Daily Seed Spent**: 4,160 G | **End-of-Day Wallet**: **74,230 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **103,000 G** *(74,230 G carryover + 28,770 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **103,000 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **103,000 G**
- **Harvest & Ship** *(+61,285 G arriving D8)*:
  - 99x Lumpotato *(Farm)* → +11,880 G (freed)
  - 16x Morrocorn *(Farm)* → +6,400 G (freed)
  - 17x Unionion *(Farm)* → +3,315 G (freed)
  - 63x Honey Flower *(Waterside)* → +39,690 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 34 | 7,820 G | D11 | +5,780 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D11 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 36 | 13,680 G | D13 | +9,000 G |
| Waterside | **Nectarcane** | Shatolla | 27 | 9,990 G | D11, D14, D17 | +10,260 G |

- **Daily Seed Spent**: 51,290 G | **End-of-Day Wallet**: **51,710 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **112,995 G** *(51,710 G carryover + 61,285 G payout)*
- **Harvest & Ship** *(+71,565 G arriving D9)*:
  - 82x Royal Eggplant *(Farm)* → +39,360 G (regrowth 1/3)
  - 32x Unionion *(Farm)* → +6,240 G (freed)
  - 18x Nectarcane *(Waterside)* → +4,500 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 32 | 3,360 G | D11 | +2,880 G |

- **Daily Seed Spent**: 3,360 G | **End-of-Day Wallet**: **109,635 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **181,200 G** *(109,635 G carryover + 71,565 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **181,200 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **181,200 G**
- **Harvest & Ship** *(+47,520 G arriving D11)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **181,200 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 11**

- **Morning Wallet**: **228,720 G** *(181,200 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+92,155 G arriving D12)*:
  - 133x Morrocorn *(Farm)* → +53,200 G (freed)
  - 32x Unionion *(Farm)* → +6,240 G (freed)
  - 45x Nectarcane *(Waterside)* → +11,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 27 | 2,160 G | D14 | +1,080 G |
| Farm | **Dress Lettuce** | Lethe | 11 | 605 G | D13 | +330 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D18, D20, D22 | +65,340 G |
| Farm | **Unionion** | Lethe | 28 | 3,640 G | D14 | +1,820 G |
| Waterside | **Honey Flower** | Shatolla | 18 | 6,840 G | D17 | +4,500 G |

- **Daily Seed Spent**: 90,465 G | **End-of-Day Wallet**: **138,255 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **230,410 G** *(138,255 G carryover + 92,155 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D13)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 76 | 4,180 G | D14 | +2,280 G |
| Farm | **Unionion** | Lethe | 5 | 650 G | D15 | +325 G |

- **Daily Seed Spent**: 4,830 G | **End-of-Day Wallet**: **225,580 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **273,100 G** *(225,580 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+23,615 G arriving D14)*:
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)
  - 36x Honey Flower *(Waterside)* → +22,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 11 | 605 G | D15 | +330 G |
| Waterside | **Honey Flower** | Shatolla | 36 | 13,680 G | D19 | +9,000 G |

- **Daily Seed Spent**: 14,285 G | **End-of-Day Wallet**: **258,815 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **282,430 G** *(258,815 G carryover + 23,615 G payout)*
- **Harvest & Ship** *(+51,535 G arriving D15)*:
  - 76x Dress Lettuce *(Farm)* → +6,460 G (freed)
  - 27x Lumpotato *(Farm)* → +3,240 G (freed)
  - 17x Royal Eggplant *(Farm)* → +8,160 G (regrowth 3/3)
  - 28x Unionion *(Farm)* → +5,460 G (freed)
  - 27x Nectarcane *(Waterside)* → +6,750 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D17 | +3,250 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D17 | +8,910 G |

- **Daily Seed Spent**: 16,895 G | **End-of-Day Wallet**: **265,535 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **317,070 G** *(265,535 G carryover + 51,535 G payout)*
- **Harvest & Ship** *(+1,910 G arriving D16)*:
  - 11x Dress Lettuce *(Farm)* → +935 G (freed)
  - 5x Unionion *(Farm)* → +975 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 16 | 1,280 G | D18 | +640 G |

- **Daily Seed Spent**: 1,280 G | **End-of-Day Wallet**: **315,790 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **317,700 G** *(315,790 G carryover + 1,910 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **317,700 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **317,700 G**
- **Harvest & Ship** *(+68,610 G arriving D18)*:
  - 149x Unionion *(Farm)* → +29,055 G (freed)
  - 18x Honey Flower *(Waterside)* → +11,340 G (freed)
  - 27x Nectarcane *(Waterside)* → +6,750 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D21..D30 (4x) | +40,500 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D21 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D21 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 45 | 17,100 G | D23 | +11,250 G |

- **Daily Seed Spent**: 93,760 G | **End-of-Day Wallet**: **223,940 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **292,550 G** *(223,940 G carryover + 68,610 G payout)*
- **Harvest & Ship** *(+49,440 G arriving D19)*:
  - 16x Lumpotato *(Farm)* → +1,920 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 16 | 2,080 G | D21 | +1,040 G |

- **Daily Seed Spent**: 2,080 G | **End-of-Day Wallet**: **290,470 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **339,910 G** *(290,470 G carryover + 49,440 G payout)*
- **Harvest & Ship** *(+22,680 G arriving D20)*:
  - 36x Honey Flower *(Waterside)* → +22,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D23, D26, D29 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 26 | 9,620 G | D23, D26, D29 | +9,880 G |

- **Daily Seed Spent**: 13,320 G | **End-of-Day Wallet**: **326,590 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **349,270 G** *(326,590 G carryover + 22,680 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D21)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **349,270 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **396,790 G** *(349,270 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+84,185 G arriving D22)*:
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 16x Unionion *(Farm)* → +3,120 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 49 | 2,695 G | D23 | +1,470 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Unionion** | Nemea | 17 | 1,785 G | D24 | +1,530 G |

- **Daily Seed Spent**: 81,700 G | **End-of-Day Wallet**: **315,090 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **399,275 G** *(315,090 G carryover + 84,185 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D23)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 49 | 2,695 G | D24 | +1,470 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D26 | +8,500 G |

- **Daily Seed Spent**: 14,195 G | **End-of-Day Wallet**: **385,080 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **432,600 G** *(385,080 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+41,515 G arriving D24)*:
  - 49x Dress Lettuce *(Farm)* → +4,165 G (freed)
  - 45x Honey Flower *(Waterside)* → +28,350 G (freed)
  - 36x Nectarcane *(Waterside)* → +9,000 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 33 | 4,290 G | D26 | +2,145 G |
| Farm | **Unionion** | Nemea | 16 | 1,680 G | D26 | +1,440 G |
| Waterside | **Honey Flower** | Shatolla | 45 | 17,100 G | D29 | +11,250 G |

- **Daily Seed Spent**: 23,070 G | **End-of-Day Wallet**: **409,530 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **451,045 G** *(409,530 G carryover + 41,515 G payout)*
- **Harvest & Ship** *(+28,945 G arriving D25)*:
  - 49x Dress Lettuce *(Farm)* → +4,165 G (freed)
  - 17x Unionion *(Farm)* → +3,315 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 66 | 8,580 G | D27 | +4,290 G |

- **Daily Seed Spent**: 8,580 G | **End-of-Day Wallet**: **442,465 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **471,410 G** *(442,465 G carryover + 28,945 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **471,410 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **471,410 G**
- **Harvest & Ship** *(+38,555 G arriving D27)*:
  - 50x Morrocorn *(Farm)* → +20,000 G (freed)
  - 49x Unionion *(Farm)* → +9,555 G (freed)
  - 36x Nectarcane *(Waterside)* → +9,000 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 19,800 G | **End-of-Day Wallet**: **451,610 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **490,165 G** *(451,610 G carryover + 38,555 G payout)*
- **Harvest & Ship** *(+34,335 G arriving D28)*:
  - 66x Unionion *(Farm)* → +12,870 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 66 | 6,930 G | D30 | +5,940 G |

- **Daily Seed Spent**: 6,930 G | **End-of-Day Wallet**: **483,235 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **517,570 G** *(483,235 G carryover + 34,335 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D29)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **517,570 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 29**

- **Morning Wallet**: **565,090 G** *(517,570 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+37,350 G arriving D30)*:
  - 45x Honey Flower *(Waterside)* → +28,350 G (freed)
  - 36x Nectarcane *(Waterside)* → +9,000 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **565,090 G**
- **Plots Left**: Farm: 0 | Waterside: 81 | Cave: 0

---

#### **Day 30**

- **Morning Wallet**: **602,440 G** *(565,090 G carryover + 37,350 G payout)*
- **Harvest & Ship** *(+121,455 G arriving D31)*:
  - 99x Morrocorn *(Farm)* → +39,600 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/2)
  - 66x Unionion *(Farm)* → +12,870 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **602,440 G**
- **Plots Left**: Farm: 165 | Waterside: 81 | Cave: 0

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **723,895 G** *(602,440 G carryover + 121,455 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 236,090 G
- **Ending Wallet (Day 31 Quietus)**: **723,895 G**
- **Net Profit (30 days)**: **+487,805 G**
- **Average Daily Profit**: **+16,260 G/day** *(over 30 active days)*
