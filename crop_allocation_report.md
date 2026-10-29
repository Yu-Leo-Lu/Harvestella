# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 4
- **Planning Timeline**: Day 4 -> Day 30 (27d Quietus window)
- **Capital Budget**: 6,020 G
- **Plot Capacities (Usable / Max)**: Farm: 190/196 | Waterside: 81/81 | Cave: 81/81

### 🌾 Pre-Planted Crop Field Status

| Biome | Crop Name | Quantity | Planted | Expected Harvests | Soil Status | Est. Revenue |
| :--- | :--- | :---: | :---: | :--- | :--- | :---: |
| Farm | **Morrocorn** | 107 | Day 1 | D5 | Freed D5 | +42,800 G |
| Farm | **Seatide Garlic** | 4 | Day 1 | D7 | Freed D7 | +4,000 G |
| Farm | **Shatollan Paprika** | 70 | Day 1 | D6, D8, D10, D12, D14, D16, D18, D20, D22 | Freed D22 | +69,300 G |
| Farm | **Carrop** | 4 | Day 3 | D4 | Freed D4 | +460 G |
| Farm | **Seatide Garlic** | 5 | Day 3 | D9 | Freed D9 | +5,000 G |
| Waterside | **Honey Flower** | 10 | Day 1 | D7 | Freed D7 | +6,300 G |
| Waterside | **Islet Watermelon** | 3 | Day 1 | D13 | Freed D13 | +13,800 G |
| Waterside | **Nectarcane** | 43 | Day 1 | D5, D8, D11 | Freed D11 | +32,250 G |
| Waterside | **Islet Watermelon** | 3 | Day 3 | D15 | Freed D15 | +13,800 G |
| Cave | **Revol Pepper** | 12 | Day 1 | D5, D8, D11, D14, D17 | Freed D17 | +15,900 G |
| Cave | **Sudor Pepper** | 69 | Day 1 | D4, D7, D10 | Freed D10 | +51,750 G |

### Optimal Daily Action Plan (Day-by-Day Timeline)

#### **Day 4**

- **Morning Wallet**: **6,020 G**
- **Harvest & Ship** *(+17,710 G arriving D5)*:
  - 4x Carrop *(Farm)* → +460 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 1/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 4 | 800 G | D8 | +800 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D16 | +4,200 G |

- **Daily Seed Spent**: 5,800 G | **End-of-Day Wallet**: **220 G**
- **Plots Left**: Farm: 0 | Waterside: 20 | Cave: 0

---

#### **Day 5**

- **Morning Wallet**: **17,930 G** *(220 G carryover + 17,710 G payout)*
- **Harvest & Ship** *(+56,730 G arriving D6)*:
  - 107x Morrocorn *(Farm)* → +42,800 G (freed)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 1/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Dress Lettuce** | Lethe | 43 | 2,365 G | D7 | +1,290 G |
| Farm | **Morrocorn** | Lethe | 34 | 7,820 G | D9 | +5,780 G |
| Farm | **Carrop** | Nemea | 22 | 2,090 G | D6 | +440 G |
| Farm | **Morrocorn** | Shatolla | 3 | 600 G | D9 | +600 G |
| Farm | **Seatide Garlic** | Shatolla | 3 | 1,950 G | D11 | +1,050 G |
| Farm | **Shatollan Paprika** | Shatolla | 2 | 500 G | D10..D26 (9x) | +1,480 G |
| Waterside | **Islet Watermelon** | Shatolla | 1 | 2,500 G | D17 | +2,100 G |

- **Daily Seed Spent**: 17,825 G | **End-of-Day Wallet**: **105 G**
- **Plots Left**: Farm: 0 | Waterside: 19 | Cave: 0

---

#### **Day 6**

- **Morning Wallet**: **56,835 G** *(105 G carryover + 56,730 G payout)*
- **Harvest & Ship** *(+10,230 G arriving D7)*:
  - 22x Carrop *(Farm)* → +2,530 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 1/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 9 | 855 G | D7 | +180 G |
| Farm | **Seatide Garlic** | Shatolla | 13 | 8,450 G | D12 | +4,550 G |
| Waterside | **Islet Watermelon** | Shatolla | 19 | 47,500 G | D18 | +39,900 G |

- **Daily Seed Spent**: 56,805 G | **End-of-Day Wallet**: **30 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 7**

- **Morning Wallet**: **10,260 G** *(30 G carryover + 10,230 G payout)*
- **Harvest & Ship** *(+32,240 G arriving D8)*:
  - 9x Carrop *(Farm)* → +1,035 G (freed)
  - 43x Dress Lettuce *(Farm)* → +3,655 G (freed)
  - 4x Seatide Garlic *(Farm)* → +4,000 G (freed)
  - 10x Honey Flower *(Waterside)* → +6,300 G (freed)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 2/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 12 | 2,760 G | D11 | +2,040 G |
| Farm | **Carrop** | Nemea | 40 | 3,800 G | D8 | +800 G |
| Waterside | **Nectarcane** | Nemea | 10 | 3,700 G | D11, D14, D17 | +3,800 G |

- **Daily Seed Spent**: 10,260 G | **End-of-Day Wallet**: **0 G**
- **Plots Left**: Farm: 4 | Waterside: 0 | Cave: 0

---

#### **Day 8**

- **Morning Wallet**: **32,240 G** *(0 G carryover + 32,240 G payout)*
- **Harvest & Ship** *(+27,830 G arriving D9)*:
  - 40x Carrop *(Farm)* → +4,600 G (freed)
  - 4x Morrocorn *(Farm)* → +1,600 G (freed)
  - 70x Shatollan Paprika *(Farm)* → +7,700 G (regrowth 2/9)
  - 43x Nectarcane *(Waterside)* → +10,750 G (regrowth 2/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 4 | 920 G | D12 | +680 G |
| Farm | **Seatide Garlic** | Shatolla | 44 | 28,600 G | D14 | +15,400 G |

- **Daily Seed Spent**: 29,520 G | **End-of-Day Wallet**: **2,720 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 9**

- **Morning Wallet**: **30,550 G** *(2,720 G carryover + 27,830 G payout)*
- **Harvest & Ship** *(+19,800 G arriving D10)*:
  - 37x Morrocorn *(Farm)* → +14,800 G (freed)
  - 5x Seatide Garlic *(Farm)* → +5,000 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 39 | 25,350 G | D15 | +13,650 G |
| Farm | **Shatollan Paprika** | Shatolla | 3 | 750 G | D14..D30 (9x) | +2,220 G |

- **Daily Seed Spent**: 26,100 G | **End-of-Day Wallet**: **4,450 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 10**

- **Morning Wallet**: **24,250 G** *(4,450 G carryover + 19,800 G payout)*
- **Harvest & Ship** *(+25,170 G arriving D11)*:
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 3/9)
  - 69x Sudor Pepper *(Cave)* → +17,250 G (regrowth 3/3)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 38 | 21,280 G | D14..D26 (5x) | +29,070 G |

- **Daily Seed Spent**: 21,280 G | **End-of-Day Wallet**: **2,970 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 31

---

#### **Day 11**

- **Morning Wallet**: **28,140 G** *(2,970 G carryover + 25,170 G payout)*
- **Harvest & Ship** *(+24,230 G arriving D12)*:
  - 12x Morrocorn *(Farm)* → +4,800 G (freed)
  - 3x Seatide Garlic *(Farm)* → +3,000 G (freed)
  - 53x Nectarcane *(Waterside)* → +13,250 G (regrowth 3/3)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 15 | 9,750 G | D17 | +5,250 G |
| Waterside | **Honey Flower** | Shatolla | 43 | 16,340 G | D17 | +10,750 G |

- **Daily Seed Spent**: 26,090 G | **End-of-Day Wallet**: **2,050 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 31

---

#### **Day 12**

- **Morning Wallet**: **26,280 G** *(2,050 G carryover + 24,230 G payout)*
- **Harvest & Ship** *(+22,520 G arriving D13)*:
  - 4x Morrocorn *(Farm)* → +1,600 G (freed)
  - 13x Seatide Garlic *(Farm)* → +13,000 G (freed)
  - 72x Shatollan Paprika *(Farm)* → +7,920 G (regrowth 4/9)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 31 | 17,360 G | D16..D28 (5x) | +23,715 G |
| Farm | **Morrocorn** | Shatolla | 17 | 3,400 G | D16 | +3,400 G |

- **Daily Seed Spent**: 20,760 G | **End-of-Day Wallet**: **5,520 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 13**

- **Morning Wallet**: **28,040 G** *(5,520 G carryover + 22,520 G payout)*
- **Harvest & Ship** *(+13,800 G arriving D14)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D25 | +6,300 G |

- **Daily Seed Spent**: 7,500 G | **End-of-Day Wallet**: **20,540 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 14**

- **Morning Wallet**: **34,340 G** *(20,540 G carryover + 13,800 G payout)*
- **Harvest & Ship** *(+68,000 G arriving D15)*:
  - 44x Seatide Garlic *(Farm)* → +44,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 5/9)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 2/3)
  - 50x Revol Pepper *(Cave)* → +13,250 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 43 | 27,950 G | D20 | +15,050 G |

- **Daily Seed Spent**: 27,950 G | **End-of-Day Wallet**: **6,390 G**
- **Plots Left**: Farm: 1 | Waterside: 0 | Cave: 0

---

#### **Day 15**

- **Morning Wallet**: **74,390 G** *(6,390 G carryover + 68,000 G payout)*
- **Harvest & Ship** *(+52,800 G arriving D16)*:
  - 39x Seatide Garlic *(Farm)* → +39,000 G (freed)
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 40 | 3,800 G | D16 | +800 G |
| Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | D27 | +6,300 G |

- **Daily Seed Spent**: 11,300 G | **End-of-Day Wallet**: **63,090 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 16**

- **Morning Wallet**: **115,890 G** *(63,090 G carryover + 52,800 G payout)*
- **Harvest & Ship** *(+37,065 G arriving D17)*:
  - 40x Carrop *(Farm)* → +4,600 G (freed)
  - 17x Morrocorn *(Farm)* → +6,800 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 6/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 1/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 57 | 11,400 G | D20 | +11,400 G |
| Waterside | **Islet Watermelon** | Shatolla | 2 | 5,000 G | D28 | +4,200 G |

- **Daily Seed Spent**: 16,400 G | **End-of-Day Wallet**: **99,490 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 17**

- **Morning Wallet**: **136,555 G** *(99,490 G carryover + 37,065 G payout)*
- **Harvest & Ship** *(+62,440 G arriving D18)*:
  - 15x Seatide Garlic *(Farm)* → +15,000 G (freed)
  - 43x Honey Flower *(Waterside)* → +27,090 G (freed)
  - 1x Islet Watermelon *(Waterside)* → +4,600 G (freed)
  - 10x Nectarcane *(Waterside)* → +2,500 G (regrowth 3/3)
  - 50x Revol Pepper *(Cave)* → +13,250 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cave | **Revol Pepper** | Argene | 12 | 6,720 G | D21..D30 (4x) | +6,000 G |
| Farm | **Seatide Garlic** | Shatolla | 15 | 9,750 G | D23 | +5,250 G |
| Waterside | **Islet Watermelon** | Shatolla | 48 | 120,000 G | D29 | +100,800 G |

- **Daily Seed Spent**: 136,470 G | **End-of-Day Wallet**: **85 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 0

---

#### **Day 18**

- **Morning Wallet**: **62,525 G** *(85 G carryover + 62,440 G payout)*
- **Harvest & Ship** *(+95,650 G arriving D19)*:
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 7/9)
  - 19x Islet Watermelon *(Waterside)* → +87,400 G (freed)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Waterside | **Islet Watermelon** | Shatolla | 25 | 62,500 G | D30 | +52,500 G |

- **Daily Seed Spent**: 62,500 G | **End-of-Day Wallet**: **25 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 19**

- **Morning Wallet**: **95,675 G** *(25 G carryover + 95,650 G payout)*
- **Harvest & Ship** *(+8,215 G arriving D20)*:
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 2/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **95,675 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 20**

- **Morning Wallet**: **103,890 G** *(95,675 G carryover + 8,215 G payout)*
- **Harvest & Ship** *(+84,120 G arriving D21)*:
  - 57x Morrocorn *(Farm)* → +22,800 G (freed)
  - 43x Seatide Garlic *(Farm)* → +43,000 G (freed)
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 8/9)
  - 38x Revol Pepper *(Cave)* → +10,070 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D24 | +8,500 G |
| Farm | **Morrocorn** | Shatolla | 25 | 5,000 G | D24 | +5,000 G |
| Farm | **Seatide Garlic** | Shatolla | 25 | 16,250 G | D26 | +8,750 G |

- **Daily Seed Spent**: 32,750 G | **End-of-Day Wallet**: **71,140 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 21**

- **Morning Wallet**: **155,260 G** *(71,140 G carryover + 84,120 G payout)*
- **Harvest & Ship** *(+3,180 G arriving D22)*:
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 1/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **155,260 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 22**

- **Morning Wallet**: **158,440 G** *(155,260 G carryover + 3,180 G payout)*
- **Harvest & Ship** *(+16,465 G arriving D23)*:
  - 75x Shatollan Paprika *(Farm)* → +8,250 G (regrowth 9/9)
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 3/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Lethe | 50 | 11,500 G | D26 | +8,500 G |
| Farm | **Carrop** | Nemea | 9 | 855 G | D23 | +180 G |
| Farm | **Morrocorn** | Shatolla | 11 | 2,200 G | D26 | +2,200 G |

- **Daily Seed Spent**: 14,555 G | **End-of-Day Wallet**: **143,885 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 23**

- **Morning Wallet**: **160,350 G** *(143,885 G carryover + 16,465 G payout)*
- **Harvest & Ship** *(+26,105 G arriving D24)*:
  - 9x Carrop *(Farm)* → +1,035 G (freed)
  - 15x Seatide Garlic *(Farm)* → +15,000 G (freed)
  - 38x Revol Pepper *(Cave)* → +10,070 G (regrowth 4/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Carrop** | Nemea | 24 | 2,280 G | D24 | +480 G |

- **Daily Seed Spent**: 2,280 G | **End-of-Day Wallet**: **158,070 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 24**

- **Morning Wallet**: **184,175 G** *(158,070 G carryover + 26,105 G payout)*
- **Harvest & Ship** *(+36,490 G arriving D25)*:
  - 24x Carrop *(Farm)* → +2,760 G (freed)
  - 75x Morrocorn *(Farm)* → +30,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 8/9)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 2/4)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Seatide Garlic** | Shatolla | 99 | 64,350 G | D30 | +34,650 G |

- **Daily Seed Spent**: 64,350 G | **End-of-Day Wallet**: **119,825 G**
- **Plots Left**: Farm: 0 | Waterside: 0 | Cave: 0

---

#### **Day 25**

- **Morning Wallet**: **156,315 G** *(119,825 G carryover + 36,490 G payout)*
- **Harvest & Ship** *(+22,015 G arriving D26)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 4/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **156,315 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 0

---

#### **Day 26**

- **Morning Wallet**: **178,330 G** *(156,315 G carryover + 22,015 G payout)*
- **Harvest & Ship** *(+60,020 G arriving D27)*:
  - 61x Morrocorn *(Farm)* → +24,400 G (freed)
  - 25x Seatide Garlic *(Farm)* → +25,000 G (freed)
  - 5x Shatollan Paprika *(Farm)* → +550 G (regrowth 9/9)
  - 38x Revol Pepper *(Cave)* → +10,070 G (regrowth 5/5)

##### 🌱 Seed Purchases & Planting

| Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Farm | **Morrocorn** | Shatolla | 88 | 17,600 G | D30 | +17,600 G |

- **Daily Seed Spent**: 17,600 G | **End-of-Day Wallet**: **160,730 G**
- **Plots Left**: Farm: 0 | Waterside: 3 | Cave: 38

---

#### **Day 27**

- **Morning Wallet**: **220,750 G** *(160,730 G carryover + 60,020 G payout)*
- **Harvest & Ship** *(+16,980 G arriving D28)*:
  - 3x Islet Watermelon *(Waterside)* → +13,800 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 3/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **220,750 G**
- **Plots Left**: Farm: 0 | Waterside: 6 | Cave: 38

---

#### **Day 28**

- **Morning Wallet**: **237,730 G** *(220,750 G carryover + 16,980 G payout)*
- **Harvest & Ship** *(+17,745 G arriving D29)*:
  - 3x Shatollan Paprika *(Farm)* → +330 G (regrowth 8/9)
  - 2x Islet Watermelon *(Waterside)* → +9,200 G (freed)
  - 31x Revol Pepper *(Cave)* → +8,215 G (regrowth 5/5)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **237,730 G**
- **Plots Left**: Farm: 0 | Waterside: 8 | Cave: 69

---

#### **Day 29**

- **Morning Wallet**: **255,475 G** *(237,730 G carryover + 17,745 G payout)*
- **Harvest & Ship** *(+220,800 G arriving D30)*:
  - 48x Islet Watermelon *(Waterside)* → +220,800 G (freed)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **255,475 G**
- **Plots Left**: Farm: 0 | Waterside: 56 | Cave: 69

---

#### **Day 30**

- **Morning Wallet**: **476,275 G** *(255,475 G carryover + 220,800 G payout)*
- **Harvest & Ship** *(+252,710 G arriving D31)*:
  - 88x Morrocorn *(Farm)* → +35,200 G (freed)
  - 99x Seatide Garlic *(Farm)* → +99,000 G (freed)
  - 3x Shatollan Paprika *(Farm)* → +330 G (regrowth 9/9)
  - 25x Islet Watermelon *(Waterside)* → +115,000 G (freed)
  - 12x Revol Pepper *(Cave)* → +3,180 G (regrowth 4/4)

- *No seed purchases or planting scheduled today.*
- **End-of-Day Wallet**: **476,275 G**
- **Plots Left**: Farm: 190 | Waterside: 81 | Cave: 69

---

#### **Day 31 (Quietus Morning)**

- **Morning Wallet**: **728,985 G** *(476,275 G carryover + 252,710 G payout)*
- ❄️ *Quietus has arrived. All unharvested field crops wither.*

---

### 🏆 Season Financial Summary (Days 4–30)

- **Starting Wallet (Day 4)**: 6,020 G
- **Ending Wallet (Day 31 Quietus)**: **728,985 G**
- **Pre-planted Crop Sales**: **+255,360 G**
- **New Planting Net Profit**: **+467,605 G**
- **Net Profit (27 days)**: **+722,965 G**
- **Average Daily Profit**: **+26,776 G/day** *(over 27 active days)*
