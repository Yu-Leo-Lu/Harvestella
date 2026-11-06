# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 662,825 G
- **Plot Capacities (Usable / Max)**: Farm: 275/294 | Waterside: 77/81 | Cave: 81/81

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 1**

- **Morning Wallet**: **662,825 G**

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D4 | +3,960 G |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D5..D17 (5x) | +61,965 G |
| Farm | **Dress Lettuce** | Lethe | 72 | 3,960 G | D3 | +2,160 G |
| Farm | **Royal Eggplant** | Lethe | 51 | 39,780 G | D8, D10, D12 | +33,660 G |
| Farm | **Unionion** | Lethe | 53 | 6,890 G | D4 | +3,445 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D5, D8, D11 | +3,800 G |
| Waterside | **Honey Flower** | Shatolla | 49 | 18,620 G | D7 | +12,250 G |
| Waterside | **Nectarcane** | Shatolla | 18 | 6,660 G | D5, D8, D11 | +6,840 G |

- **Daily Seed Spent**: 132,890 G | **End-of-Day Wallet**: **529,935 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **529,935 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **529,935 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **529,935 G**
- **Harvest & Ship** *(+6,120 G arriving D4)*:
  - 72x Dress Lettuce *(Farm)* → +6,120 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 27 | 1,485 G | D5 | +810 G |
| Farm | **Royal Eggplant** | Lethe | 43 | 33,540 G | D10, D12, D14 | +28,380 G |
| Farm | **Unionion** | Lethe | 2 | 260 G | D6 | +130 G |

- **Daily Seed Spent**: 35,285 G | **End-of-Day Wallet**: **494,650 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **500,770 G** *(494,650 G carryover + 6,120 G payout)*
- **Harvest & Ship** *(+22,215 G arriving D5)*:
  - 99x Lumpotato *(Farm)* → +11,880 G (freed)
  - 53x Unionion *(Farm)* → +10,335 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 36 | 3,240 G | D7 | +1,080 G |
| Farm | **Unionion** | Lethe | 17 | 2,210 G | D7 | +1,105 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D7 | +8,910 G |

- **Daily Seed Spent**: 15,845 G | **End-of-Day Wallet**: **484,925 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **507,140 G** *(484,925 G carryover + 22,215 G payout)*
- **Harvest & Ship** *(+30,760 G arriving D6)*:
  - 27x Dress Lettuce *(Farm)* → +2,295 G (freed)
  - 28x Nectarcane *(Waterside)* → +7,000 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 27 | 3,510 G | D8 | +1,755 G |

- **Daily Seed Spent**: 3,510 G | **End-of-Day Wallet**: **503,630 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **534,390 G** *(503,630 G carryover + 30,760 G payout)*
- **Harvest & Ship** *(+390 G arriving D7)*:
  - 2x Unionion *(Farm)* → +390 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Royal Eggplant** | Lethe | 2 | 1,560 G | D13, D15, D17 | +1,320 G |

- **Daily Seed Spent**: 1,560 G | **End-of-Day Wallet**: **532,830 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **533,220 G** *(532,830 G carryover + 390 G payout)*
- **Harvest & Ship** *(+57,810 G arriving D8)*:
  - 36x Lumpotato *(Farm)* → +4,320 G (freed)
  - 116x Unionion *(Farm)* → +22,620 G (freed)
  - 49x Honey Flower *(Waterside)* → +30,870 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 3 | 270 G | D10 | +90 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D11 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D11 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 49 | 18,620 G | D13 | +12,250 G |

- **Daily Seed Spent**: 50,190 G | **End-of-Day Wallet**: **483,030 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **540,840 G** *(483,030 G carryover + 57,810 G payout)*
- **Harvest & Ship** *(+58,210 G arriving D9)*:
  - 51x Royal Eggplant *(Farm)* → +24,480 G (regrowth 1/3)
  - 27x Unionion *(Farm)* → +5,265 G (freed)
  - 28x Nectarcane *(Waterside)* → +7,000 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 27 | 2,430 G | D11 | +810 G |

- **Daily Seed Spent**: 2,430 G | **End-of-Day Wallet**: **538,410 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **596,620 G** *(538,410 G carryover + 58,210 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **596,620 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **596,620 G**
- **Harvest & Ship** *(+45,480 G arriving D11)*:
  - 3x Lumpotato *(Farm)* → +360 G (freed)
  - 94x Royal Eggplant *(Farm)* → +45,120 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Royal Eggplant** | Lethe | 3 | 2,340 G | D17, D19, D21 | +1,980 G |

- **Daily Seed Spent**: 2,340 G | **End-of-Day Wallet**: **594,280 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 11**

- **Morning Wallet**: **639,760 G** *(594,280 G carryover + 45,480 G payout)*
- **Harvest & Ship** *(+91,305 G arriving D12)*:
  - 27x Lumpotato *(Farm)* → +3,240 G (freed)
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 28x Nectarcane *(Waterside)* → +7,000 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 3 | 240 G | D14 | +120 G |
| Farm | **Dress Lettuce** | Lethe | 24 | 1,320 G | D13 | +720 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D18, D20, D22 | +65,340 G |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D14 | +3,250 G |
| Waterside | **Honey Flower** | Shatolla | 27 | 10,260 G | D17 | +6,750 G |

- **Daily Seed Spent**: 95,540 G | **End-of-Day Wallet**: **544,220 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **635,525 G** *(544,220 G carryover + 91,305 G payout)*
- **Harvest & Ship** *(+45,120 G arriving D13)*:
  - 94x Royal Eggplant *(Farm)* → +45,120 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 51 | 2,805 G | D14 | +1,530 G |

- **Daily Seed Spent**: 2,805 G | **End-of-Day Wallet**: **632,720 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **677,840 G** *(632,720 G carryover + 45,120 G payout)*
- **Harvest & Ship** *(+33,870 G arriving D14)*:
  - 24x Dress Lettuce *(Farm)* → +2,040 G (freed)
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 1/3)
  - 49x Honey Flower *(Waterside)* → +30,870 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 24 | 1,320 G | D15 | +720 G |
| Waterside | **Nectarcane** | Nemea | 5 | 1,850 G | D17, D20, D23 | +1,900 G |
| Waterside | **Honey Flower** | Shatolla | 44 | 16,720 G | D19 | +11,000 G |

- **Daily Seed Spent**: 19,890 G | **End-of-Day Wallet**: **657,950 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **691,820 G** *(657,950 G carryover + 33,870 G payout)*
- **Harvest & Ship** *(+56,550 G arriving D15)*:
  - 51x Dress Lettuce *(Farm)* → +4,335 G (freed)
  - 3x Lumpotato *(Farm)* → +360 G (freed)
  - 43x Royal Eggplant *(Farm)* → +20,640 G (regrowth 3/3)
  - 50x Unionion *(Farm)* → +9,750 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 96 | 7,680 G | D17 | +3,840 G |
| Farm | **Unionion** | Nemea | 51 | 5,355 G | D17 | +4,590 G |

- **Daily Seed Spent**: 13,035 G | **End-of-Day Wallet**: **678,785 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **735,335 G** *(678,785 G carryover + 56,550 G payout)*
- **Harvest & Ship** *(+3,000 G arriving D16)*:
  - 24x Dress Lettuce *(Farm)* → +2,040 G (freed)
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 24 | 2,520 G | D18 | +2,160 G |

- **Daily Seed Spent**: 2,520 G | **End-of-Day Wallet**: **732,815 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **735,815 G** *(732,815 G carryover + 3,000 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **735,815 G**
- **Plots Left**: Farm: 0 | Waterside: 1 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **735,815 G**
- **Harvest & Ship** *(+63,590 G arriving D18)*:
  - 96x Lumpotato *(Farm)* → +11,520 G (freed)
  - 5x Royal Eggplant *(Farm)* → +2,400 G (regrowth 3/3)
  - 51x Unionion *(Farm)* → +9,945 G (freed)
  - 27x Honey Flower *(Waterside)* → +17,010 G (freed)
  - 5x Nectarcane *(Waterside)* → +1,250 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D21..D30 (4x) | +40,500 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D21 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D21 | +19,800 G |
| Waterside | **Honey Flower** | Shatolla | 28 | 10,640 G | D23 | +7,000 G |

- **Daily Seed Spent**: 87,300 G | **End-of-Day Wallet**: **648,515 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **712,105 G** *(648,515 G carryover + 63,590 G payout)*
- **Harvest & Ship** *(+52,200 G arriving D19)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)
  - 24x Unionion *(Farm)* → +4,680 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 24 | 2,520 G | D21 | +2,160 G |

- **Daily Seed Spent**: 2,520 G | **End-of-Day Wallet**: **709,585 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **761,785 G** *(709,585 G carryover + 52,200 G payout)*
- **Harvest & Ship** *(+29,160 G arriving D20)*:
  - 3x Royal Eggplant *(Farm)* → +1,440 G (regrowth 2/3)
  - 44x Honey Flower *(Waterside)* → +27,720 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Nectarcane** | Nemea | 4 | 1,480 G | D23, D26, D29 | +1,520 G |
| Waterside | **Nectarcane** | Shatolla | 40 | 14,800 G | D23, D26, D29 | +15,200 G |

- **Daily Seed Spent**: 16,280 G | **End-of-Day Wallet**: **745,505 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **774,665 G** *(745,505 G carryover + 29,160 G payout)*
- **Harvest & Ship** *(+48,770 G arriving D21)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)
  - 5x Nectarcane *(Waterside)* → +1,250 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **774,665 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **823,435 G** *(774,665 G carryover + 48,770 G payout)*
- **Harvest & Ship** *(+87,185 G arriving D22)*:
  - 149x Morrocorn *(Farm)* → +59,600 G (freed)
  - 3x Royal Eggplant *(Farm)* → +1,440 G (regrowth 3/3)
  - 24x Unionion *(Farm)* → +4,680 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 49 | 2,695 G | D23 | +1,470 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Unionion** | Lethe | 27 | 3,510 G | D24 | +1,755 G |

- **Daily Seed Spent**: 83,425 G | **End-of-Day Wallet**: **740,010 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **827,195 G** *(740,010 G carryover + 87,185 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D23)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 49 | 2,695 G | D24 | +1,470 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D26 | +8,500 G |

- **Daily Seed Spent**: 14,195 G | **End-of-Day Wallet**: **813,000 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **860,520 G** *(813,000 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+34,055 G arriving D24)*:
  - 49x Dress Lettuce *(Farm)* → +4,165 G (freed)
  - 28x Honey Flower *(Waterside)* → +17,640 G (freed)
  - 49x Nectarcane *(Waterside)* → +12,250 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 27 | 2,160 G | D26 | +1,080 G |
| Farm | **Unionion** | Lethe | 22 | 2,860 G | D26 | +1,430 G |
| Waterside | **Honey Flower** | Shatolla | 33 | 12,540 G | D29 | +8,250 G |

- **Daily Seed Spent**: 17,560 G | **End-of-Day Wallet**: **842,960 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **877,015 G** *(842,960 G carryover + 34,055 G payout)*
- **Harvest & Ship** *(+30,895 G arriving D25)*:
  - 49x Dress Lettuce *(Farm)* → +4,165 G (freed)
  - 27x Unionion *(Farm)* → +5,265 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 76 | 7,980 G | D27 | +6,840 G |

- **Daily Seed Spent**: 7,980 G | **End-of-Day Wallet**: **869,035 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **899,930 G** *(869,035 G carryover + 30,895 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **899,930 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **899,930 G**
- **Harvest & Ship** *(+38,530 G arriving D27)*:
  - 27x Lumpotato *(Farm)* → +3,240 G (freed)
  - 50x Morrocorn *(Farm)* → +20,000 G (freed)
  - 22x Unionion *(Farm)* → +4,290 G (freed)
  - 44x Nectarcane *(Waterside)* → +11,000 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 99 | 19,800 G | D30 | +19,800 G |

- **Daily Seed Spent**: 19,800 G | **End-of-Day Wallet**: **880,130 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **918,660 G** *(880,130 G carryover + 38,530 G payout)*
- **Harvest & Ship** *(+36,285 G arriving D28)*:
  - 76x Unionion *(Farm)* → +14,820 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 54 | 4,320 G | D30 | +2,160 G |
| Farm | **Unionion** | Nemea | 22 | 2,310 G | D30 | +1,980 G |

- **Daily Seed Spent**: 6,630 G | **End-of-Day Wallet**: **912,030 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **948,315 G** *(912,030 G carryover + 36,285 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D29)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **948,315 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 29**

- **Morning Wallet**: **995,835 G** *(948,315 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+31,790 G arriving D30)*:
  - 33x Honey Flower *(Waterside)* → +20,790 G (freed)
  - 44x Nectarcane *(Waterside)* → +11,000 G (regrowth 3/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **995,835 G**
- **Plots Left**: Farm: 1 | Waterside: 77 | Cave: 0

---

#### **Day 30**

- **Morning Wallet**: **1,027,625 G** *(995,835 G carryover + 31,790 G payout)*
- **Harvest & Ship** *(+119,355 G arriving D31)*:
  - 54x Lumpotato *(Farm)* → +6,480 G (freed)
  - 99x Morrocorn *(Farm)* → +39,600 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/2)
  - 22x Unionion *(Farm)* → +4,290 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **1,027,625 G**
- **Plots Left**: Farm: 176 | Waterside: 77 | Cave: 0

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **1,146,980 G** *(1,027,625 G carryover + 119,355 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 662,825 G
- **Ending Wallet (Day 31 Quietus)**: **1,146,980 G**
- **Net Profit (30 days)**: **+484,155 G**
- **Average Daily Profit**: **+16,138 G/day** *(over 30 active days)*
