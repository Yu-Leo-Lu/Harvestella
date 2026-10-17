# Harvestella Crop Allocation & Planting Report

> Mathematically optimal seed purchase and planting allocations generated via Day-to-Day Time-Indexed Mixed-Integer Linear Programming (MILP).

## SPRING Optimization Plan

- **Config Profile**: [`configs/spring.yaml`](configs/spring.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 1,000 G
- **Plot Capacities**: Farm 70 | Waterside 0 | Cave 0

### Optimal Planting Timeline

#### Stage 1: Day 1 → Day 10 (10-day window)

- **Starting Cash**: 1,000 G | **Stage Spent**: 6,510 G | **Farm (Peak)**: 32 / 70 (Seeds: 75)

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 1 | Farm | **Unionion** | Nemea | 6 | 630 G | 370 G | Day 4 | +540 G |
| Day 1 | Farm | **Dress Lettuce** | Lethe | 6 | 330 G | 40 G | Day 3 | +180 G |
| Day 1 | Farm | **Stellar Wheat** | Lethe | 1 | 40 G | 0 G | Day 3 | +15 G |
| Day 4 | Farm | **Unionion** | Nemea | 2 | 210 G | 355 G | Day 7 | +180 G |
| Day 4 | Farm | **Dress Lettuce** | Lethe | 6 | 330 G | 25 G | Day 6 | +180 G |
| Day 5 | Farm | **Unionion** | Nemea | 10 | 1,050 G | 145 G | Day 8 | +900 G |
| Day 5 | Farm | **Dress Lettuce** | Lethe | 2 | 110 G | 35 G | Day 7 | +60 G |
| Day 7 | Farm | **Dress Lettuce** | Lethe | 9 | 495 G | 50 G | Day 9 | +270 G |
| Day 8 | Farm | **Unionion** | Nemea | 5 | 525 G | 85 G | Day 11 | +450 G |
| Day 8 | Farm | **Dress Lettuce** | Lethe | 1 | 55 G | 30 G | Day 10 | +30 G |
| Day 9 | Farm | **Unionion** | Nemea | 17 | 1,785 G | 195 G | Day 12 | +1,530 G |
| Day 9 | Farm | **Dress Lettuce** | Lethe | 2 | 110 G | 85 G | Day 11 | +60 G |
| Day 10 | Farm | **Unionion** | Nemea | 8 | 840 G | 10 G | Day 13 | +720 G |

- **Stage Harvest Revenue Arrived**: +5,520 G | **Projected Cash at Stage End**: **10 G**

#### Stage 2: Day 11 → Day 20 (10-day window)

- **Starting Cash**: 10 G | **Stage Spent**: 22,795 G | **Farm (Peak)**: 70 / 70 (Seeds: 224)

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 11 | Farm | **Dress Lettuce** | Lethe | 1 | 55 G | 40 G | Day 13 | +30 G |
| Day 12 | Farm | **Dress Lettuce** | Lethe | 21 | 1,155 G | 30 G | Day 14 | +630 G |
| Day 13 | Farm | **Unionion** | Nemea | 22 | 2,310 G | 1,035 G | Day 16 | +1,980 G |
| Day 13 | Farm | **Dress Lettuce** | Lethe | 18 | 990 G | 45 G | Day 15 | +540 G |
| Day 14 | Farm | **Unionion** | Nemea | 16 | 1,680 G | 10 G | Day 17 | +1,440 G |
| Day 15 | Farm | **Dress Lettuce** | Lethe | 32 | 1,760 G | 35 G | Day 17 | +960 G |
| Day 16 | Farm | **Unionion** | Nemea | 9 | 945 G | 620 G | Day 19 | +810 G |
| Day 16 | Farm | **Dress Lettuce** | Lethe | 10 | 550 G | 70 G | Day 18 | +300 G |
| Day 17 | Farm | **Strawbuddy** | Nemea | 7 | 1,540 G | 2,820 G | Day 21..29 (5x) | +3,010 G |
| Day 17 | Farm | **Unionion** | Nemea | 21 | 2,205 G | 615 G | Day 20 | +1,890 G |
| Day 17 | Farm | **Carrop** | Nemea | 2 | 190 G | 425 G | Day 18 | +40 G |
| Day 17 | Farm | **Dress Lettuce** | Lethe | 4 | 220 G | 205 G | Day 19 | +120 G |
| Day 18 | Farm | **Strawbuddy** | Nemea | 26 | 5,720 G | 325 G | Day 22..30 (5x) | +11,180 G |
| Day 18 | Farm | **Unionion** | Nemea | 3 | 315 G | 10 G | Day 21 | +270 G |
| Day 19 | Farm | **Unionion** | Nemea | 8 | 840 G | 250 G | Day 22 | +720 G |
| Day 19 | Farm | **Dress Lettuce** | Lethe | 4 | 220 G | 30 G | Day 21 | +120 G |
| Day 20 | Farm | **Unionion** | Nemea | 20 | 2,100 G | 25 G | Day 23 | +1,800 G |

- **Stage Harvest Revenue Arrived**: +22,810 G | **Projected Cash at Stage End**: **25 G**

#### Stage 3: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 25 G | **Stage Spent**: 23,575 G | **Farm (Peak)**: 70 / 70 (Seeds: 85)

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 21 | Farm | **Tingle Radish** | Nemea | 8 | 3,120 G | 1,000 G | Day 25 | +1,120 G |
| Day 21 | Farm | **Dress Lettuce** | Lethe | 1 | 55 G | 945 G | Day 23 | +30 G |
| Day 22 | Farm | **Tingle Radish** | Nemea | 7 | 2,730 G | 50 G | Day 26 | +980 G |
| Day 23 | Farm | **Tingle Radish** | Nemea | 10 | 3,900 G | 1,090 G | Day 27 | +1,400 G |
| Day 23 | Farm | **Unionion** | Nemea | 10 | 1,050 G | 40 G | Day 26 | +900 G |
| Day 24 | Farm | **Carrop** | Nemea | 2 | 190 G | 4,745 G | Day 25 | +40 G |
| Day 25 | Farm | **Tingle Radish** | Nemea | 9 | 3,510 G | 4,615 G | Day 29 | +1,260 G |
| Day 25 | Farm | **Carrop** | Nemea | 1 | 95 G | 4,520 G | Day 26 | +20 G |
| Day 26 | Farm | **Tingle Radish** | Nemea | 18 | 7,020 G | 2,880 G | Day 30 | +2,520 G |
| Day 27 | Farm | **Unionion** | Nemea | 10 | 1,050 G | 10,985 G | Day 30 | +900 G |
| Day 29 | Farm | **Carrop** | Nemea | 9 | 855 G | 19,720 G | Day 30 | +180 G |

- **Stage Harvest Revenue Arrived**: +48,950 G | **Projected Cash at Stage End**: **25,400 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 13 / 70 (18.6% utilized, 57 idle)
- **Initial Capital Spent**: 1,000 G / 1,000 G (100.0% spent, 0 G leftover)
- **Total Cumulative Season Net Profit**: **+40,305 G** across all restock stages
- **Final Projected Wallet**: **41,305 G** on Day 30 (Quietus)

---

## SUMMER Optimization Plan

- **Config Profile**: [`configs/summer.yaml`](configs/summer.yaml)
- **Current Day**: Day 18
- **Planning Timeline**: Day 18 -> Day 30 (13d Quietus window)
- **Capital Budget**: 51,600 G
- **Plot Capacities**: Farm 60 -> 196 | Waterside 36 -> 81 | Cave 54 -> 81

### Optimal Planting Timeline

#### Stage 1: Day 18 → Day 20 (3-day window)

- **Starting Cash**: 51,600 G | **Stage Spent**: 54,930 G | **Farm (Peak)**: 114 / 114 (Seeds: 151) | **Waterside (Peak)**: 36 / 36 | **Cave (Peak)**: 53 / 54

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 18 | Farm | **Nemean Tomato** | Nemea | 26 | 4,420 G | 47,180 G | Day 23..28 (6x) | +5,720 G |
| Day 18 | Farm | **Carrop** | Lethe | 34 | 3,570 G | 43,610 G | Day 19 | +340 G |
| Day 18 | Waterside | **Islet Watermelon** | Shatolla | 3 | 7,500 G | 36,110 G | Day 30 | +6,300 G |
| Day 18 | Waterside | **Nectarcane** | Shatolla | 33 | 12,210 G | 23,900 G | Day 22, Day 25, Day 28 | +12,540 G |
| Day 18 | Cave | **Sudor Pepper** | Argene | 44 | 17,600 G | 6,300 G | Day 21, Day 24, Day 27 | +15,400 G |
| Day 19 | Farm | **Carrop** | Nemea | 21 | 1,995 G | 4,305 G | Day 20 | +420 G |
| Day 19 | Farm | **Carrop** | Lethe | 19 | 1,995 G | 2,310 G | Day 20 | +190 G |
| Day 19 | Farm | **Stellar Wheat** | Lethe | 48 | 1,920 G | 390 G | Day 21 | +720 G |
| Day 20 | Farm | **Stellar Wheat** | Lethe | 3 | 120 G | 4,180 G | Day 22 | +45 G |
| Day 20 | Cave | **Sudor Pepper** | Argene | 9 | 3,600 G | 580 G | Day 23, Day 26, Day 29 | +3,150 G |

- **Stage Harvest Revenue Arrived**: +3,910 G | **Projected Cash at Stage End**: **580 G**

#### Stage 2: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 580 G | **Stage Spent**: 75,775 G | **Farm (Peak)**: 156 / 196 (Seeds: 462) | **Waterside (Peak)**: 72 / 81 | **Cave (Peak)**: 53 / 81

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 21 | Farm | **Dress Lettuce** | Lethe | 84 | 4,620 G | 560 G | Day 23 | +2,520 G |
| Day 22 | Farm | **Morrocorn** | Shatolla | 34 | 6,800 G | 7,400 G | Day 26 | +6,800 G |
| Day 22 | Farm | **Carrop** | Nemea | 11 | 1,045 G | 6,355 G | Day 23 | +220 G |
| Day 23 | Farm | **Seatide Garlic** | Shatolla | 15 | 9,750 G | 5,020 G | Day 29 | +5,250 G |
| Day 23 | Farm | **Dress Lettuce** | Lethe | 14 | 770 G | 4,250 G | Day 25 | +420 G |
| Day 23 | Farm | **Stellar Wheat** | Lethe | 67 | 2,680 G | 1,570 G | Day 25 | +1,005 G |
| Day 24 | Waterside | **Honey Flower** | Shatolla | 36 | 13,680 G | 235 G | Day 30 | +9,000 G |
| Day 25 | Farm | **Morrocorn** | Shatolla | 48 | 9,600 G | 3,325 G | Day 29 | +9,600 G |
| Day 25 | Farm | **Carrop** | Nemea | 33 | 3,135 G | 190 G | Day 26 | +660 G |
| Day 26 | Farm | **Morrocorn** | Shatolla | 17 | 3,400 G | 11,605 G | Day 30 | +3,400 G |
| Day 26 | Farm | **Morrocorn** | Lethe | 50 | 11,500 G | 105 G | Day 30 | +8,500 G |
| Day 29 | Farm | **Carrop** | Nemea | 55 | 5,225 G | 38,845 G | Day 30 | +1,100 G |
| Day 29 | Farm | **Carrop** | Lethe | 34 | 3,570 G | 35,275 G | Day 30 | +340 G |

- **Stage Harvest Revenue Arrived**: +146,920 G | **Projected Cash at Stage End**: **71,725 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 60 / 60 (expands to 196) (100.0% utilized, 0 idle)
- **Waterside Plots (Init)**: 36 / 36 (expands to 81) (100.0% utilized, 0 idle)
- **Cave Plots Used (Init)**: 44 / 54 (expands to 81) (81.5% utilized, 10 idle)
- **Initial Capital Spent**: 45,300 G / 51,600 G (87.8% spent, 6,300 G leftover)
- **Total Cumulative Season Net Profit**: **+93,640 G** across all restock stages
- **Final Projected Wallet**: **145,240 G** on Day 30 (Quietus)

---

## FALL Optimization Plan

- **Config Profile**: [`configs/fall.yaml`](configs/fall.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 15,000 G
- **Plot Capacities**: Farm 70 | Waterside 12 | Cave 12

### Optimal Planting Timeline

#### Stage 1: Day 1 → Day 10 (10-day window)

- **Starting Cash**: 15,000 G | **Stage Spent**: 46,885 G | **Farm (Peak)**: 70 / 70 (Seeds: 264) | **Waterside (Peak)**: 12 / 12 | **Cave (Peak)**: 12 / 12

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 1 | Farm | **Unionion** | Nemea | 38 | 3,990 G | 11,010 G | Day 4 | +3,420 G |
| Day 1 | Farm | **Dress Lettuce** | Lethe | 31 | 1,705 G | 9,305 G | Day 3 | +930 G |
| Day 1 | Waterside | **Nectarcane** | Nemea | 3 | 1,110 G | 8,195 G | Day 5, Day 8, Day 11 | +1,140 G |
| Day 1 | Cave | **Sudor Pepper** | Argene | 12 | 4,800 G | 3,395 G | Day 4, Day 7, Day 10 | +4,200 G |
| Day 3 | Farm | **Unionion** | Nemea | 32 | 3,360 G | 35 G | Day 6 | +2,880 G |
| Day 4 | Farm | **Unionion** | Nemea | 13 | 1,365 G | 1,305 G | Day 7 | +1,170 G |
| Day 4 | Farm | **Dress Lettuce** | Lethe | 23 | 1,265 G | 40 G | Day 6 | +690 G |
| Day 6 | Farm | **Royal Eggplant** | Lethe | 7 | 5,460 G | 5,740 G | Day 13, Day 15, Day 17 | +4,620 G |
| Day 6 | Farm | **Unionion** | Nemea | 15 | 1,575 G | 4,165 G | Day 9 | +1,350 G |
| Day 6 | Farm | **Dress Lettuce** | Lethe | 34 | 1,870 G | 2,295 G | Day 8 | +1,020 G |
| Day 7 | Farm | **Royal Eggplant** | Lethe | 13 | 10,140 G | 350 G | Day 14, Day 16, Day 18 | +8,580 G |
| Day 8 | Farm | **Unionion** | Nemea | 1 | 105 G | 5,780 G | Day 11 | +90 G |
| Day 8 | Farm | **Unionion** | Lethe | 26 | 3,380 G | 2,400 G | Day 11 | +1,690 G |
| Day 8 | Farm | **Dress Lettuce** | Lethe | 8 | 440 G | 1,960 G | Day 10 | +240 G |
| Day 8 | Waterside | **Nectarcane** | Shatolla | 5 | 1,850 G | 110 G | Day 12, Day 15, Day 18 | +1,900 G |
| Day 9 | Farm | **Unionion** | Lethe | 15 | 1,950 G | 1,800 G | Day 12 | +975 G |
| Day 9 | Waterside | **Nectarcane** | Shatolla | 4 | 1,480 G | 320 G | Day 13, Day 16, Day 19 | +1,520 G |
| Day 10 | Farm | **Unionion** | Lethe | 8 | 1,040 G | 2,205 G | Day 13 | +520 G |

- **Stage Harvest Revenue Arrived**: +34,090 G | **Projected Cash at Stage End**: **2,205 G**

#### Stage 2: Day 11 → Day 20 (10-day window)

- **Starting Cash**: 2,205 G | **Stage Spent**: 77,420 G | **Farm (Peak)**: 70 / 70 (Seeds: 192) | **Waterside (Peak)**: 12 / 12 | **Cave (Peak)**: 12 / 12

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 11 | Farm | **Unionion** | Nemea | 27 | 2,835 G | 3,050 G | Day 14 | +2,430 G |
| Day 11 | Cave | **Revol Pepper** | Argene | 5 | 2,800 G | 250 G | Day 15..27 (5x) | +3,825 G |
| Day 12 | Farm | **Unionion** | Nemea | 15 | 1,575 G | 4,690 G | Day 15 | +1,350 G |
| Day 12 | Waterside | **Nectarcane** | Nemea | 3 | 1,110 G | 3,580 G | Day 16, Day 19, Day 22 | +1,140 G |
| Day 13 | Farm | **Unionion** | Nemea | 8 | 840 G | 6,915 G | Day 16 | +720 G |
| Day 13 | Cave | **Revol Pepper** | Argene | 7 | 3,920 G | 2,995 G | Day 17..29 (5x) | +5,355 G |
| Day 14 | Farm | **Unionion** | Nemea | 27 | 2,835 G | 6,080 G | Day 17 | +2,430 G |
| Day 15 | Farm | **Unionion** | Nemea | 15 | 1,575 G | 16,010 G | Day 18 | +1,350 G |
| Day 16 | Farm | **Unionion** | Nemea | 7 | 735 G | 24,135 G | Day 19 | +630 G |
| Day 17 | Farm | **Dress Lettuce** | Lethe | 23 | 1,265 G | 32,420 G | Day 19 | +690 G |
| Day 18 | Farm | **Royal Eggplant** | Lethe | 23 | 17,940 G | 24,960 G | Day 25, Day 27, Day 29 | +15,180 G |
| Day 19 | Farm | **Royal Eggplant** | Lethe | 47 | 36,660 G | 40 G | Day 26, Day 28, Day 30 | +31,020 G |
| Day 20 | Waterside | **Nectarcane** | Shatolla | 9 | 3,330 G | 1,780 G | Day 24, Day 27, Day 30 | +3,420 G |

- **Stage Harvest Revenue Arrived**: +76,995 G | **Projected Cash at Stage End**: **1,780 G**

#### Stage 3: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 1,780 G | **Stage Spent**: 1,110 G | **Farm (Peak)**: 70 / 70 (Seeds: 0) | **Waterside (Peak)**: 12 / 12 | **Cave (Peak)**: 12 / 12

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 23 | Waterside | **Nectarcane** | Shatolla | 3 | 1,110 G | 4,600 G | Day 27, Day 30 | +390 G |

- **Stage Harvest Revenue Arrived**: +95,635 G | **Projected Cash at Stage End**: **96,305 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 69 / 70 (98.6% utilized, 1 idle)
- **Waterside Plots (Init)**: 3 / 12 (25.0% utilized, 9 idle)
- **Cave Plots Used (Init)**: 12 / 12 (100.0% utilized, 0 idle)
- **Initial Capital Spent**: 11,605 G / 15,000 G (77.4% spent, 3,395 G leftover)
- **Total Cumulative Season Net Profit**: **+106,865 G** across all restock stages
- **Final Projected Wallet**: **121,865 G** on Day 30 (Quietus)

---

## WINTER Optimization Plan

- **Config Profile**: [`configs/winter.yaml`](configs/winter.yaml)
- **Current Day**: Day 1
- **Planning Timeline**: Day 1 -> Day 30 (30d Quietus window)
- **Capital Budget**: 20,000 G
- **Plot Capacities**: Farm 70 | Waterside 0 | Cave 0

### Optimal Planting Timeline

#### Stage 1: Day 1 → Day 10 (10-day window)

- **Starting Cash**: 20,000 G | **Stage Spent**: 43,500 G | **Farm (Peak)**: 70 / 70 (Seeds: 149)

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 1 | Farm | **Argene Cabbage** | Argene | 66 | 14,520 G | 5,480 G | Day 5 | +6,600 G |
| Day 1 | Farm | **Lumpotato** | Argene | 1 | 80 G | 5,400 G | Day 4 | +40 G |
| Day 2 | Farm | **Argene Cabbage** | Argene | 2 | 440 G | 4,960 G | Day 6 | +200 G |
| Day 4 | Farm | **Chilly Plant** | Argene | 1 | 800 G | 4,160 G | Day 11 | +500 G |
| Day 5 | Farm | **Chilly Plant** | Argene | 5 | 4,000 G | 280 G | Day 12 | +2,500 G |
| Day 5 | Farm | **Lumpotato** | Argene | 2 | 160 G | 120 G | Day 8 | +80 G |
| Day 6 | Farm | **Chilly Plant** | Argene | 19 | 15,200 G | 6,040 G | Day 13 | +9,500 G |
| Day 6 | Farm | **Argene Cabbage** | Argene | 22 | 4,840 G | 1,200 G | Day 10 | +2,200 G |
| Day 6 | Farm | **Lumpotato** | Argene | 12 | 960 G | 240 G | Day 9 | +480 G |
| Day 7 | Farm | **Lumpotato** | Argene | 9 | 720 G | 160 G | Day 10 | +360 G |
| Day 8 | Farm | **Lumpotato** | Argene | 2 | 160 G | 0 G | Day 11 | +80 G |
| Day 9 | Farm | **Lumpotato** | Argene | 1 | 80 G | 160 G | Day 12 | +40 G |
| Day 10 | Farm | **Argene Cabbage** | Argene | 7 | 1,540 G | 60 G | Day 14 | +700 G |

- **Stage Harvest Revenue Arrived**: +23,560 G | **Projected Cash at Stage End**: **60 G**

#### Stage 2: Day 11 → Day 20 (10-day window)

- **Starting Cash**: 60 G | **Stage Spent**: 59,780 G | **Farm (Peak)**: 70 / 70 (Seeds: 145)

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 11 | Farm | **Argene Cabbage** | Argene | 37 | 8,140 G | 40 G | Day 15 | +3,700 G |
| Day 12 | Farm | **Chilly Plant** | Argene | 1 | 800 G | 780 G | Day 19 | +500 G |
| Day 12 | Farm | **Lumpotato** | Argene | 4 | 320 G | 460 G | Day 15 | +160 G |
| Day 13 | Farm | **Chilly Plant** | Argene | 7 | 5,600 G | 1,480 G | Day 20 | +3,500 G |
| Day 13 | Farm | **Lumpotato** | Argene | 12 | 960 G | 520 G | Day 16 | +480 G |
| Day 14 | Farm | **Lumpotato** | Argene | 7 | 560 G | 24,660 G | Day 17 | +280 G |
| Day 15 | Farm | **Chilly Plant** | Argene | 33 | 26,400 G | 500 G | Day 22 | +16,500 G |
| Day 15 | Farm | **Lumpotato** | Argene | 6 | 480 G | 20 G | Day 18 | +240 G |
| Day 16 | Farm | **Chilly Plant** | Argene | 15 | 12,000 G | 340 G | Day 23 | +7,500 G |
| Day 16 | Farm | **Lumpotato** | Argene | 1 | 80 G | 260 G | Day 19 | +40 G |
| Day 17 | Farm | **Argene Cabbage** | Argene | 6 | 1,320 G | 380 G | Day 21 | +600 G |
| Day 17 | Farm | **Lumpotato** | Argene | 1 | 80 G | 300 G | Day 20 | +40 G |
| Day 18 | Farm | **Argene Cabbage** | Argene | 5 | 1,100 G | 40 G | Day 22 | +500 G |
| Day 19 | Farm | **Argene Cabbage** | Argene | 3 | 660 G | 100 G | Day 23 | +300 G |
| Day 20 | Farm | **Chilly Plant** | Argene | 1 | 800 G | 720 G | Day 27 | +500 G |
| Day 20 | Farm | **Lumpotato** | Argene | 6 | 480 G | 240 G | Day 23 | +240 G |

- **Stage Harvest Revenue Arrived**: +59,960 G | **Projected Cash at Stage End**: **240 G**

#### Stage 3: Day 21 → Day 30 (10-day window)

- **Starting Cash**: 240 G | **Stage Spent**: 55,280 G | **Farm (Peak)**: 70 / 70 (Seeds: 70)

| Plant Day | Biome | Crop Name | Vendor Town | Quantity | Seed Spent | Balance | Harvest Days | Net Profit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 22 | Farm | **Chilly Plant** | Argene | 14 | 11,200 G | 180 G | Day 29 | +7,000 G |
| Day 23 | Farm | **Chilly Plant** | Argene | 55 | 44,000 G | 680 G | Day 30 | +27,500 G |
| Day 27 | Farm | **Lumpotato** | Argene | 1 | 80 G | 21,780 G | Day 30 | +40 G |

- **Stage Harvest Revenue Arrived**: +96,320 G | **Projected Cash at Stage End**: **41,280 G**

### Resource Utilization & Financial Summary

- **Farm Plots Used (Init)**: 67 / 70 (95.7% utilized, 3 idle)
- **Initial Capital Spent**: 14,600 G / 20,000 G (73.0% spent, 5,400 G leftover)
- **Total Cumulative Season Net Profit**: **+92,900 G** across all restock stages
- **Final Projected Wallet**: **112,900 G** on Day 30 (Quietus)

---

## Key Optimization Principles

1. **Day-to-Day Rolling Capital Reinvestment**:
   - Rather than waiting for 10-day shop restocks to reinvest cash, the model dynamically redeploys proceeds the very morning after a harvest arrives (accounting for the 1-day overnight shipping turnaround).
2. **Soil Occupancy & Regrowth Dynamics**:
   - Single-harvest crops free up soil immediately on harvest day for replanting, while regrowth crops (such as Tomato, Peppers, and Nectarcane) remain rooted in soil across their full harvesting cycle without incurring additional seed costs.
3. **Biome Specialization & Plot Balancing**:
   - High-margin multi-biome crops (**Nectarcane** on Waterside and **Sudor/Revol Pepper** in Cave) run on independent plot constraints, providing pure additive revenue independent of main farm capacity.
