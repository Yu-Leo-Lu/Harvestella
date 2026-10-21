# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 236,090 G
- **Plot Capacities (Usable / Max)**: Farm: 294/294 | Waterside: 81/81 | Cave: 81/81

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 1**

- **Morning Wallet**: **236,090 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D5..D17 (5x) | +61,965 G |
| Farm | **Dress Lettuce** | Lethe | 53 | 2,915 G | D3 | +1,590 G |
| Farm | **Royal Eggplant** | Lethe | 91 | 70,980 G | D8, D10, D12 | +60,060 G |
| Farm | **Unionion** | Lethe | 51 | 6,630 G | D4 | +3,315 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D4 | +8,910 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D5, D8, D11 | +3,800 G |
| Waterside | **Honey Flower** | Shatolla | 63 | 23,940 G | D7 | +15,750 G |
| Waterside | **Nectarcane** | Shatolla | 8 | 2,960 G | D5, D8, D11 | +3,040 G |

- **Daily Seed Spent**: 166,880 G | **End-of-Day Wallet**: **69,210 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **69,210 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **69,210 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **69,210 G**
- **Harvest & Ship** *(+4,505 G arriving D4)*:
  - 53x Dress Lettuce *(Farm)* → +4,505 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 46 | 2,530 G | D5 | +1,380 G |
| Farm | **Royal Eggplant** | Lethe | 5 | 3,900 G | D10, D12, D14 | +3,300 G |
| Farm | **Unionion** | Lethe | 1 | 130 G | D6 | +65 G |

- **Daily Seed Spent**: 6,560 G | **End-of-Day Wallet**: **62,650 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **67,155 G** *(62,650 G carryover + 4,505 G payout)*
- **Harvest & Ship** *(+29,250 G arriving D5)*:
  - 150x Unionion *(Farm)* → +29,250 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 98 | 7,840 G | D7 | +3,920 G |
| Farm | **Lumpotato** | Lethe | 53 | 4,770 G | D7 | +1,590 G |

- **Daily Seed Spent**: 12,610 G | **End-of-Day Wallet**: **54,545 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **83,795 G** *(54,545 G carryover + 29,250 G payout)*
- **Harvest & Ship** *(+29,875 G arriving D6)*:
  - 46x Dress Lettuce *(Farm)* → +3,910 G (freed)
  - 18x Nectarcane *(Waterside)* → +4,500 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 45 | 4,050 G | D8 | +1,350 G |

- **Daily Seed Spent**: 4,050 G | **End-of-Day Wallet**: **79,745 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **109,620 G** *(79,745 G carryover + 29,875 G payout)*
- **Harvest & Ship** *(+195 G arriving D7)*:
  - 1x Unionion *(Farm)* → +195 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Royal Eggplant** | Lethe | 2 | 1,560 G | D13, D15, D17 | +1,320 G |

- **Daily Seed Spent**: 1,560 G | **End-of-Day Wallet**: **108,060 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **108,255 G** *(108,060 G carryover + 195 G payout)*
- **Harvest & Ship** *(+57,810 G arriving D8)*:
  - 151x Lumpotato *(Farm)* → +18,120 G (freed)
  - 63x Honey Flower *(Waterside)* → +39,690 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 1 | 80 G | D10 | +40 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D11 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D11 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 36 | 13,680 G | D13 | +9,000 G |
| Waterside | **Nectarcane** | Shatolla | 27 | 9,990 G | D11, D14, D17 | +10,260 G |

- **Daily Seed Spent**: 55,050 G | **End-of-Day Wallet**: **53,205 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **111,015 G** *(53,205 G carryover + 57,810 G payout)*
- **Harvest & Ship** *(+75,045 G arriving D9)*:
  - 45x Lumpotato *(Farm)* → +5,400 G (freed)
  - 91x Royal Eggplant *(Farm)* → +43,680 G (regrowth 1/3)
  - 18x Nectarcane *(Waterside)* → +4,500 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 46 | 5,980 G | D11 | +2,990 G |

- **Daily Seed Spent**: 5,980 G | **End-of-Day Wallet**: **105,035 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **180,080 G** *(105,035 G carryover + 75,045 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **180,080 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **180,080 G**
- **Harvest & Ship** *(+46,200 G arriving D11)*:
  - 1x Lumpotato *(Farm)* → +120 G (freed)
  - 96x Royal Eggplant *(Farm)* → +46,080 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Royal Eggplant** | Lethe | 1 | 780 G | D17, D19, D21 | +660 G |

- **Daily Seed Spent**: 780 G | **End-of-Day Wallet**: **179,300 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 11**

- **Morning Wallet**: **225,500 G** *(179,300 G carryover + 46,200 G payout)*
- **Harvest & Ship** *(+101,285 G arriving D12)*:
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 46x Unionion *(Farm)* → +8,970 G (freed)
  - 45x Nectarcane *(Waterside)* → +11,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 17 | 935 G | D13 | +510 G |
| Farm | **Lumpotato** | Lethe | 7 | 630 G | D14 | +210 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D18, D20, D22 | +65,340 G |
| Farm | **Unionion** | Lethe | 72 | 9,360 G | D14 | +4,680 G |
| Waterside | **Honey Flower** | Shatolla | 18 | 6,840 G | D17 | +4,500 G |

- **Daily Seed Spent**: 94,985 G | **End-of-Day Wallet**: **130,515 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **231,800 G** *(130,515 G carryover + 101,285 G payout)*
- **Harvest & Ship** *(+46,080 G arriving D13)*:
  - 96x Royal Eggplant *(Farm)* → +46,080 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 63 | 3,465 G | D14 | +1,890 G |
| Farm | **Unionion** | Lethe | 27 | 3,510 G | D15 | +1,755 G |

- **Daily Seed Spent**: 6,975 G | **End-of-Day Wallet**: **224,825 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **270,905 G** *(224,825 G carryover + 46,080 G payout)*
- **Harvest & Ship** *(+25,085 G arriving D14)*:
  - 17x Dress Lettuce *(Farm)* → +1,445 G (freed)
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 1/3)
  - 36x Honey Flower *(Waterside)* → +22,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 17 | 935 G | D15 | +510 G |
| Waterside | **Honey Flower** | Shatolla | 36 | 13,680 G | D19 | +9,000 G |

- **Daily Seed Spent**: 14,615 G | **End-of-Day Wallet**: **256,290 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **281,375 G** *(256,290 G carryover + 25,085 G payout)*
- **Harvest & Ship** *(+50,850 G arriving D15)*:
  - 63x Dress Lettuce *(Farm)* → +5,355 G (freed)
  - 7x Lumpotato *(Farm)* → +840 G (freed)
  - 5x Royal Eggplant *(Farm)* → +2,400 G (regrowth 3/3)
  - 72x Unionion *(Farm)* → +14,040 G (freed)
  - 27x Nectarcane *(Waterside)* → +6,750 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 10 | 800 G | D17 | +400 G |
| Farm | **Lumpotato** | Lethe | 39 | 3,510 G | D17 | +1,170 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D17 | +8,910 G |

- **Daily Seed Spent**: 14,705 G | **End-of-Day Wallet**: **266,670 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **317,520 G** *(266,670 G carryover + 50,850 G payout)*
- **Harvest & Ship** *(+7,670 G arriving D16)*:
  - 17x Dress Lettuce *(Farm)* → +1,445 G (freed)
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 2/3)
  - 27x Unionion *(Farm)* → +5,265 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 44 | 3,520 G | D18 | +1,760 G |

- **Daily Seed Spent**: 3,520 G | **End-of-Day Wallet**: **314,000 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **321,670 G** *(314,000 G carryover + 7,670 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **321,670 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **321,670 G**
- **Harvest & Ship** *(+66,180 G arriving D18)*:
  - 49x Lumpotato *(Farm)* → +5,880 G (freed)
  - 3x Royal Eggplant *(Farm)* → +1,440 G (regrowth 3/3)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
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

- **Daily Seed Spent**: 93,760 G | **End-of-Day Wallet**: **227,910 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **294,090 G** *(227,910 G carryover + 66,180 G payout)*
- **Harvest & Ship** *(+52,800 G arriving D19)*:
  - 44x Lumpotato *(Farm)* → +5,280 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 45 | 3,600 G | D21 | +1,800 G |

- **Daily Seed Spent**: 3,600 G | **End-of-Day Wallet**: **290,490 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **343,290 G** *(290,490 G carryover + 52,800 G payout)*
- **Harvest & Ship** *(+23,160 G arriving D20)*:
  - 1x Royal Eggplant *(Farm)* → +480 G (regrowth 2/3)
  - 36x Honey Flower *(Waterside)* → +22,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D23, D26, D29 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 26 | 9,620 G | D23, D26, D29 | +9,880 G |

- **Daily Seed Spent**: 13,320 G | **End-of-Day Wallet**: **329,970 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **353,130 G** *(329,970 G carryover + 23,160 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D21)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **353,130 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **400,650 G** *(353,130 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+86,945 G arriving D22)*:
  - 45x Lumpotato *(Farm)* → +5,400 G (freed)
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 1x Royal Eggplant *(Farm)* → +480 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 49 | 2,695 G | D23 | +1,470 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Unionion** | Nemea | 47 | 4,935 G | D24 | +4,230 G |

- **Daily Seed Spent**: 84,850 G | **End-of-Day Wallet**: **315,800 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **402,745 G** *(315,800 G carryover + 86,945 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D23)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 49 | 2,695 G | D24 | +1,470 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D26 | +8,500 G |

- **Daily Seed Spent**: 14,195 G | **End-of-Day Wallet**: **388,550 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **436,070 G** *(388,550 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+41,515 G arriving D24)*:
  - 49x Dress Lettuce *(Farm)* → +4,165 G (freed)
  - 45x Honey Flower *(Waterside)* → +28,350 G (freed)
  - 36x Nectarcane *(Waterside)* → +9,000 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 49 | 6,370 G | D26 | +3,185 G |
| Waterside | **Honey Flower** | Shatolla | 45 | 17,100 G | D29 | +11,250 G |

- **Daily Seed Spent**: 23,470 G | **End-of-Day Wallet**: **412,600 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **454,115 G** *(412,600 G carryover + 41,515 G payout)*
- **Harvest & Ship** *(+34,795 G arriving D25)*:
  - 49x Dress Lettuce *(Farm)* → +4,165 G (freed)
  - 47x Unionion *(Farm)* → +9,165 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 47 | 3,760 G | D27 | +1,880 G |
| Farm | **Unionion** | Lethe | 49 | 6,370 G | D27 | +3,185 G |

- **Daily Seed Spent**: 10,130 G | **End-of-Day Wallet**: **443,985 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **478,780 G** *(443,985 G carryover + 34,795 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **478,780 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **478,780 G**
- **Harvest & Ship** *(+38,555 G arriving D27)*:
  - 50x Morrocorn *(Farm)* → +20,000 G (freed)
  - 49x Unionion *(Farm)* → +9,555 G (freed)
  - 36x Nectarcane *(Waterside)* → +9,000 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 19,800 G | **End-of-Day Wallet**: **458,980 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **497,535 G** *(458,980 G carryover + 38,555 G payout)*
- **Harvest & Ship** *(+36,660 G arriving D28)*:
  - 47x Lumpotato *(Farm)* → +5,640 G (freed)
  - 49x Unionion *(Farm)* → +9,555 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 43 | 3,440 G | D30 | +1,720 G |
| Farm | **Unionion** | Nemea | 52 | 5,460 G | D30 | +4,680 G |

- **Daily Seed Spent**: 8,900 G | **End-of-Day Wallet**: **488,635 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **525,295 G** *(488,635 G carryover + 36,660 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D29)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **525,295 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 29**

- **Morning Wallet**: **572,815 G** *(525,295 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+37,350 G arriving D30)*:
  - 45x Honey Flower *(Waterside)* → +28,350 G (freed)
  - 36x Nectarcane *(Waterside)* → +9,000 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **572,815 G**
- **Plots Left**: Farm: 1 | Waterside: 81 | Cave: 0

---

#### **Day 30**

- **Morning Wallet**: **610,165 G** *(572,815 G carryover + 37,350 G payout)*
- **Harvest & Ship** *(+123,885 G arriving D31)*:
  - 43x Lumpotato *(Farm)* → +5,160 G (freed)
  - 99x Morrocorn *(Farm)* → +39,600 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/2)
  - 52x Unionion *(Farm)* → +10,140 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **610,165 G**
- **Plots Left**: Farm: 195 | Waterside: 81 | Cave: 0

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **734,050 G** *(610,165 G carryover + 123,885 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 236,090 G
- **Ending Wallet (Day 31 Quietus)**: **734,050 G**
- **Net Profit (30 days)**: **+497,960 G**
- **Average Daily Profit**: **+16,599 G/day** *(over 30 active days)*
