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
| Farm | **Lumpotato** | Argene | 5 | 400 G | D4 | +200 G |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D5..D17 (5x) | +61,965 G |
| Farm | **Dress Lettuce** | Lethe | 99 | 5,445 G | D3 | +2,970 G |
| Farm | **Royal Eggplant** | Lethe | 90 | 70,200 G | D8, D10, D12 | +59,400 G |
| Farm | **Stellar Wheat** | Lethe | 53 | 2,120 G | D3 | +795 G |
| Farm | **Unionion** | Nemea | 47 | 4,935 G | D4 | +4,230 G |
| Waterside | **Nectarcane** | Shatolla | 81 | 29,970 G | D5, D8, D11 | +30,780 G |

- **Daily Seed Spent**: 158,430 G | **End-of-Day Wallet**: **77,660 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 2**

- **Morning Wallet**: **77,660 G**

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **77,660 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 3**

- **Morning Wallet**: **77,660 G**
- **Harvest & Ship** *(+11,330 G arriving D4)*:
  - 99x Dress Lettuce *(Farm)* → +8,415 G (freed)
  - 53x Stellar Wheat *(Farm)* → +2,915 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Grass** | Lethe | 99 | 2,970 G | D5 | +495 G |
| Farm | **Royal Eggplant** | Lethe | 7 | 5,460 G | D10, D12, D14 | +4,620 G |
| Farm | **Stellar Wheat** | Lethe | 46 | 1,840 G | D5 | +690 G |

- **Daily Seed Spent**: 10,270 G | **End-of-Day Wallet**: **67,390 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 4**

- **Morning Wallet**: **78,720 G** *(67,390 G carryover + 11,330 G payout)*
- **Harvest & Ship** *(+9,765 G arriving D5)*:
  - 5x Lumpotato *(Farm)* → +600 G (freed)
  - 47x Unionion *(Farm)* → +9,165 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Nemea | 52 | 5,460 G | D7 | +4,680 G |

- **Daily Seed Spent**: 5,460 G | **End-of-Day Wallet**: **73,260 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **83,025 G** *(73,260 G carryover + 9,765 G payout)*
- **Harvest & Ship** *(+47,710 G arriving D6)*:
  - 99x Grass *(Farm)* → +3,465 G (freed)
  - 46x Stellar Wheat *(Farm)* → +2,530 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 1/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 46 | 3,680 G | D8 | +1,840 G |
| Farm | **Unionion** | Lethe | 99 | 12,870 G | D8 | +6,435 G |

- **Daily Seed Spent**: 16,550 G | **End-of-Day Wallet**: **66,475 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **114,185 G** *(66,475 G carryover + 47,710 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **114,185 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **114,185 G**
- **Harvest & Ship** *(+10,140 G arriving D8)*:
  - 52x Unionion *(Farm)* → +10,140 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 2 | 160 G | D10 | +80 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D11 | +8,500 G |

- **Daily Seed Spent**: 11,660 G | **End-of-Day Wallet**: **102,525 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **112,665 G** *(102,525 G carryover + 10,140 G payout)*
- **Harvest & Ship** *(+109,740 G arriving D9)*:
  - 46x Lumpotato *(Farm)* → +5,520 G (freed)
  - 90x Royal Eggplant *(Farm)* → +43,200 G (regrowth 1/3)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 2/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 46 | 3,680 G | D11 | +1,840 G |
| Farm | **Lumpotato** | Lethe | 99 | 8,910 G | D11 | +2,970 G |

- **Daily Seed Spent**: 12,590 G | **End-of-Day Wallet**: **100,075 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **209,815 G** *(100,075 G carryover + 109,740 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **209,815 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **209,815 G**
- **Harvest & Ship** *(+46,800 G arriving D11)*:
  - 2x Lumpotato *(Farm)* → +240 G (freed)
  - 97x Royal Eggplant *(Farm)* → +46,560 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Royal Eggplant** | Lethe | 2 | 1,560 G | D17, D19, D21 | +1,320 G |

- **Daily Seed Spent**: 1,560 G | **End-of-Day Wallet**: **208,255 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 11**

- **Morning Wallet**: **255,055 G** *(208,255 G carryover + 46,800 G payout)*
- **Harvest & Ship** *(+79,115 G arriving D12)*:
  - 145x Lumpotato *(Farm)* → +17,400 G (freed)
  - 50x Morrocorn *(Farm)* → +20,000 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 90 | 4,950 G | D13 | +2,700 G |
| Farm | **Lumpotato** | Lethe | 1 | 90 G | D14 | +30 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D18, D20, D22 | +65,340 G |
| Farm | **Unionion** | Lethe | 5 | 650 G | D14 | +325 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D15, D18, D21 | +3,800 G |
| Waterside | **Nectarcane** | Shatolla | 71 | 26,270 G | D15, D18, D21 | +26,980 G |

- **Daily Seed Spent**: 112,880 G | **End-of-Day Wallet**: **142,175 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 12**

- **Morning Wallet**: **221,290 G** *(142,175 G carryover + 79,115 G payout)*
- **Harvest & Ship** *(+46,560 G arriving D13)*:
  - 97x Royal Eggplant *(Farm)* → +46,560 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 53 | 4,770 G | D15 | +1,590 G |
| Farm | **Stellar Wheat** | Lethe | 36 | 1,440 G | D14 | +540 G |

- **Daily Seed Spent**: 6,210 G | **End-of-Day Wallet**: **215,080 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **261,640 G** *(215,080 G carryover + 46,560 G payout)*
- **Harvest & Ship** *(+7,650 G arriving D14)*:
  - 90x Dress Lettuce *(Farm)* → +7,650 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 9 | 495 G | D15 | +270 G |
| Farm | **Grass** | Lethe | 17 | 510 G | D15 | +85 G |
| Farm | **Stellar Wheat** | Lethe | 63 | 2,520 G | D15 | +945 G |

- **Daily Seed Spent**: 3,525 G | **End-of-Day Wallet**: **258,115 G**
- **Plots Left**: Farm: 2 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **265,765 G** *(258,115 G carryover + 7,650 G payout)*
- **Harvest & Ship** *(+27,900 G arriving D15)*:
  - 1x Lumpotato *(Farm)* → +120 G (freed)
  - 7x Royal Eggplant *(Farm)* → +3,360 G (regrowth 3/3)
  - 36x Stellar Wheat *(Farm)* → +1,980 G (freed)
  - 5x Unionion *(Farm)* → +975 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Unionion** | Lethe | 50 | 6,500 G | D17 | +3,250 G |

- **Daily Seed Spent**: 6,500 G | **End-of-Day Wallet**: **259,265 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **287,165 G** *(259,265 G carryover + 27,900 G payout)*
- **Harvest & Ship** *(+31,435 G arriving D16)*:
  - 9x Dress Lettuce *(Farm)* → +765 G (freed)
  - 17x Grass *(Farm)* → +595 G (freed)
  - 53x Lumpotato *(Farm)* → +6,360 G (freed)
  - 63x Stellar Wheat *(Farm)* → +3,465 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D18 | +3,960 G |
| Farm | **Unionion** | Lethe | 44 | 5,720 G | D18 | +2,860 G |

- **Daily Seed Spent**: 13,640 G | **End-of-Day Wallet**: **273,525 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **304,960 G** *(273,525 G carryover + 31,435 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **304,960 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **304,960 G**
- **Harvest & Ship** *(+32,175 G arriving D18)*:
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 1/3)
  - 50x Unionion *(Farm)* → +9,750 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 81 | 45,360 G | D21..D30 (4x) | +40,500 G |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D21 | +8,500 G |

- **Daily Seed Spent**: 56,860 G | **End-of-Day Wallet**: **248,100 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **280,275 G** *(248,100 G carryover + 32,175 G payout)*
- **Harvest & Ship** *(+88,230 G arriving D19)*:
  - 99x Lumpotato *(Farm)* → +11,880 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/3)
  - 44x Unionion *(Farm)* → +8,580 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 44 | 3,960 G | D21 | +1,320 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D21 | +8,910 G |

- **Daily Seed Spent**: 14,355 G | **End-of-Day Wallet**: **265,920 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **354,150 G** *(265,920 G carryover + 88,230 G payout)*
- **Harvest & Ship** *(+960 G arriving D20)*:
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **354,150 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **355,110 G** *(354,150 G carryover + 960 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D21)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/3)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **355,110 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **402,630 G** *(355,110 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+87,260 G arriving D22)*:
  - 44x Lumpotato *(Farm)* → +5,280 G (freed)
  - 50x Morrocorn *(Farm)* → +20,000 G (freed)
  - 2x Royal Eggplant *(Farm)* → +960 G (regrowth 3/3)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 3/3)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 1/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 5 | 275 G | D23 | +150 G |
| Farm | **Lumpotato** | Lethe | 8 | 720 G | D24 | +240 G |
| Farm | **Royal Eggplant** | Lethe | 99 | 77,220 G | D28, D30 | +17,820 G |
| Farm | **Stellar Wheat** | Lethe | 35 | 1,400 G | D23 | +525 G |
| Farm | **Unionion** | Lethe | 48 | 6,240 G | D24 | +3,120 G |
| Waterside | **Nectarcane** | Shatolla | 81 | 29,970 G | D25, D28 | +10,530 G |

- **Daily Seed Spent**: 115,825 G | **End-of-Day Wallet**: **286,805 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **374,065 G** *(286,805 G carryover + 87,260 G payout)*
- **Harvest & Ship** *(+47,520 G arriving D23)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 94 | 5,170 G | D24 | +2,820 G |
| Farm | **Morrocorn** | Lethe | 5 | 1,150 G | D26 | +850 G |

- **Daily Seed Spent**: 6,320 G | **End-of-Day Wallet**: **367,745 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **415,265 G** *(367,745 G carryover + 47,520 G payout)*
- **Harvest & Ship** *(+2,350 G arriving D24)*:
  - 5x Dress Lettuce *(Farm)* → +425 G (freed)
  - 35x Stellar Wheat *(Farm)* → +1,925 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 40 | 3,600 G | D26 | +1,200 G |

- **Daily Seed Spent**: 3,600 G | **End-of-Day Wallet**: **411,665 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **414,015 G** *(411,665 G carryover + 2,350 G payout)*
- **Harvest & Ship** *(+39,775 G arriving D25)*:
  - 94x Dress Lettuce *(Farm)* → +7,990 G (freed)
  - 8x Lumpotato *(Farm)* → +960 G (freed)
  - 48x Unionion *(Farm)* → +9,360 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Lethe | 51 | 4,590 G | D27 | +1,530 G |
| Farm | **Unionion** | Nemea | 99 | 10,395 G | D27 | +8,910 G |

- **Daily Seed Spent**: 14,985 G | **End-of-Day Wallet**: **399,030 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **438,805 G** *(399,030 G carryover + 39,775 G payout)*
- **Harvest & Ship** *(+20,250 G arriving D26)*:
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 1/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **438,805 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **459,055 G** *(438,805 G carryover + 20,250 G payout)*
- **Harvest & Ship** *(+6,800 G arriving D27)*:
  - 40x Lumpotato *(Farm)* → +4,800 G (freed)
  - 5x Morrocorn *(Farm)* → +2,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 45 | 10,350 G | D30 | +7,650 G |

- **Daily Seed Spent**: 10,350 G | **End-of-Day Wallet**: **448,705 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 27**

- **Morning Wallet**: **455,505 G** *(448,705 G carryover + 6,800 G payout)*
- **Harvest & Ship** *(+46,890 G arriving D28)*:
  - 51x Lumpotato *(Farm)* → +6,120 G (freed)
  - 99x Unionion *(Farm)* → +19,305 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 3/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Lumpotato** | Argene | 99 | 7,920 G | D30 | +3,960 G |
| Farm | **Unionion** | Lethe | 51 | 6,630 G | D30 | +3,315 G |

- **Daily Seed Spent**: 14,550 G | **End-of-Day Wallet**: **440,955 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 28**

- **Morning Wallet**: **487,845 G** *(440,955 G carryover + 46,890 G payout)*
- **Harvest & Ship** *(+67,770 G arriving D29)*:
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 1/2)
  - 81x Nectarcane *(Waterside)* → +20,250 G (regrowth 2/2)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **487,845 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 29**

- **Morning Wallet**: **555,615 G** *(487,845 G carryover + 67,770 G payout)*

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **555,615 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 30**

- **Morning Wallet**: **555,615 G**
- **Harvest & Ship** *(+108,810 G arriving D31)*:
  - 99x Lumpotato *(Farm)* → +11,880 G (freed)
  - 45x Morrocorn *(Farm)* → +18,000 G (freed)
  - 99x Royal Eggplant *(Farm)* → +47,520 G (regrowth 2/2)
  - 51x Unionion *(Farm)* → +9,945 G (freed)
  - 81x Revol Pepper *(Cave)* → +21,465 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **555,615 G**
- **Plots Left**: Farm: 195 | Waterside: 0 | Cave: 0

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **664,425 G** *(555,615 G carryover + 108,810 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 1–30)

- **Starting Wallet (Day 1)**: 236,090 G
- **Ending Wallet (Day 31 Quietus)**: **664,425 G**
- **Net Profit (30 days)**: **+428,335 G**
- **Average Daily Profit**: **+14,278 G/day** *(over 30 active days)*
