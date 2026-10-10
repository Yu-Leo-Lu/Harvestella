# Harvestella Seed Catalog & Agricultural Database

A comprehensive, data-driven reference catalog compiled from in-game general store inventories, seasonal growth logs, and economic data sheets.

---

## 1. Town General Store Inventories (What Sells Where & At What Price)

### Lethe Village General Store
| Crop / Sapling Name | Item Category | Buy Price | Sell Price (Basic) | Sell Price (Prem.) | Growth / Cycle | Land Type | Season Availability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Grass Seeds** | Seeds | 30 G | 35 G | 45 G | 2 days | Farm | Spring, Summer, Fall |
| **Stellar Wheat Seeds** | Seeds | 40 G | 55 G | 70 G | 2 days | Farm | Spring, Summer, Fall |
| **Dress Lettuce Seeds** | Seeds | 55 G | 85 G | 105 G | 2 days | Farm | Spring, Summer, Fall |
| **Carrop Seeds** | Seeds | 105 G | 115 G | 145 G | 1 day | Farm | Spring, Summer |
| **Morrocorn Seeds** | Seeds | 200 G | 400 G | 500 G | 4 days | Farm | Summer |
| **Cucumble Seeds** | Seeds | 370 G | 200 G | 250 G | 4 days/repeat | Farm | Spring |
| **Grouply Grape Sapling** | Sapling | 2,000 G | 85 G | 105 G | 6 days/repeat | Farm | Fall (All Year) |
| **Princess Chestnut Sapling** | Sapling | 2,200 G | 60 G | 75 G | 7 days/repeat | Farm | Fall (All Year, No Water) |
| **SnowCap Mikan Sapling** | Sapling | 2,300 G | 65 G | 80 G | 7 days/repeat | Farm | Winter (All Year) |
| **Lantern Pumpkin Seeds** | Seeds | 3,750 G | 3,750 G | — | 11 days | Farm | Fall |

> **Store Note for Lethe:** Carrop seeds cost **105 G** in Lethe versus **95 G** in Nemea. Buying Carrops in Lethe cuts basic profit margin from +20 G (+21.1%) down to +10 G (+9.5%).

---

### Nemea Town General Store (Spring Region)
| Crop / Sapling Name | Item Category | Buy Price | Sell Price (Basic) | Sell Price (Prem.) | Growth / Cycle | Land Type | Season Availability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Carrop Seeds** | Seeds | 95 G | 115 G | 145 G | 1 day | Farm | Spring, Summer |
| **Unionion Seeds** | Seeds | 105 G | 195 G | 245 G | 3 days | Farm | Spring |
| **Nemean Tomato Seeds** | Seeds | 170 G | 65 G | 95 G | 5 days/repeat | Farm | Spring |
| **Strawbuddy Seeds** | Seeds | 220 G | 130 G | 160 G | 4 days/repeat | Farm | Spring |
| **Nectarcane Seeds** | Seeds | 370 G | 250 G | 310 G | 4 days/repeat | Waterside | Spring, Summer, Fall |
| **Tingle Radish Seeds** | Seeds | 390 G | 530 G | 660 G | 4 days | Farm | Spring |
| **Wisty Peach Sapling** | Sapling | 4,200 G | 115 G | 230 G | 10 days/repeat | Farm | Spring (All Year) |

---

### Shatolla Seaside General Store (Summer Region)
| Crop / Sapling Name | Item Category | Buy Price | Sell Price (Basic) | Sell Price (Prem.) | Growth / Cycle | Land Type | Season Availability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Morrocorn Seeds** | Seeds | 200 G | 400 G | 500 G | 4 days | Farm | Summer |
| **Shatollan Paprika Seeds** | Seeds | 250 G | 110 G | 135 G | 5 days/repeat | Farm | Summer |
| **Nectarcane Seeds** | Seeds | 370 G | 250 G | 310 G | 4 days/repeat | Waterside | Spring, Summer, Fall |
| **Honey Flower Seeds** | Seeds | 380 G | 630 G | 785 G | 6 days | Waterside | Summer |
| **Bellhop Seeds** | Seeds | 560 G | 45 G | 55 G | 7 days/repeat | Farm | Summer |
| **Seatide Garlic Seeds** | Seeds | 650 G | 1,000 G | 1,250 G | 6 days | Farm | Summer |
| **Islet Watermelon Seeds** | Seeds | 2,500 G | 4,600 G | 5,800 G | 12 days/repeat | Waterside | Summer |
| **Lococonut Sapling** | Sapling | 3,200 G | 35 G | 45 G | 7 days/repeat | Waterside | Summer (All Year) |

---

### Holy Capital Argene General Store (Winter Region)
| Crop / Sapling Name | Item Category | Buy Price | Sell Price (Basic) | Sell Price (Prem.) | Growth / Cycle | Land Type | Season Availability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Argene Cabbage Seeds** | Seeds | 220 G | 320 G | 400 G | 4 days | Farm | Winter |
| **Sudor Pepper Seeds** | Seeds | 400 G | 250 G | 310 G | 3 days/repeat | Cave | Winter (Biomes) |
| **Revol Pepper Seeds** | Seeds | 560 G | 265 G | 330 G | 4 days/repeat | Cave | Winter (Biomes) |
| **Chilly Plant Seeds** | Seeds | 800 G | 1,300 G | 1,625 G | 7 days | Farm | Winter |

---

## 2. Complete Cross-Town Price Arbitrage & Variance

Only one crop exhibits dual-pricing across general stores:

| Crop | Cheaper Store | Lower Price | Expensive Store | Higher Price | Price Difference | ROI Impact |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| **Carrop Seeds** | **Nemea** | **95 G** | Lethe | 105 G | +10 G (+10.5%) | Nemea yields **+21.1% ROI** vs Lethe's **+9.5% ROI** |

*All other cross-town seeds (e.g., Nectarcane sold in both Shatolla and Nemea at 370 G; Morrocorn sold in Lethe and Shatolla at 200 G) share identical wholesale pricing across all shops.*

---

## 3. Comprehensive Master Agricultural Database

Consolidated raw operational metrics sorted from lowest seed cost to highest seed cost:

* **M (Gross Multiplier):** $\frac{\text{Basic Sell Price}}{\text{Seed Cost}}$
* **Turnaround (+1d Delay):** Growth Days + 1 day overnight shipping bin clearing delay
* **Continuous Rate (%/day):** Single-crop immediate replanting velocity ($M^{1 / \text{Growth}} - 1$)
* **Realized Cash Compounded Rate (%/day):** Actual wallet growth accounting for shipping delay ($M^{1 / (\text{Growth} + 1)} - 1$)
* **Full Season Profit (30d):** Cumulative net profit per tile across 30 days starting Day 1

| Crop Name | Vendor Town | Land Req. | Seed Cost | Basic Sell | Prem. Sell | Harvest Cycle | Turnaround (+1d) | M Multiplier | Single Cycle Net Profit | 30-Day Net Profit (Basic) | Realized Daily Cash Rate |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Grass** | Lethe | Farm | 30 G | 35 G | 45 G | 2 days | 3 days | 1.167 | +5 G | +75 G | +5.27% |
| **Stellar Wheat** | Lethe | Farm | 40 G | 55 G | 70 G | 2 days | 3 days | 1.375 | +15 G | +225 G | +11.20% |
| **Dress Lettuce** | Lethe | Farm | 55 G | 85 G | 105 G | 2 days | 3 days | 1.545 | +30 G | +450 G | +15.62% |
| **Carrop (Nemea)** | Nemea | Farm | 95 G | 115 G | 145 G | 1 day | 2 days | 1.211 | +20 G | +600 G | +10.02% |
| **Carrop (Lethe)** | Lethe | Farm | 105 G | 115 G | 145 G | 1 day | 2 days | 1.095 | +10 G | +300 G | +4.65% |
| **Unionion** | Nemea | Farm | 105 G | 195 G | 245 G | 3 days | 4 days | 1.857 | +90 G | +900 G | +16.74% |
| **Nemean Tomato** | Nemea | Farm | 170 G | 65 G | 95 G | 5 days/repeat | 6 days | 0.382 | -105 G | +220 G | +2.81% |
| **Morrocorn** | Shatolla/Lethe | Farm | 200 G | 400 G | 500 G | 4 days | 5 days | 2.000 | +200 G | +1,400 G | +14.87% |
| **Strawbuddy** | Nemea | Farm | 220 G | 130 G | 160 G | 4 days/repeat | 5 days | 0.591 | -90 G | +690 G | +4.85% |
| **Argene Cabbage** | Argene | Farm | 220 G | 320 G | 400 G | 4 days | 5 days | 1.455 | +100 G | +700 G | +7.78% |
| **Shatollan Paprika**| Shatolla | Farm | 250 G | 110 G | 135 G | 5 days/repeat | 6 days | 0.440 | -140 G | +410 G | +3.70% |
| **Nectarcane** | Shatolla/Nemea | Waterside | 370 G | 250 G | 310 G | 4 days/repeat | 5 days | 0.676 | -120 G | +1,380 G | +5.32% |
| **Cucumble** | Lethe | Farm | 370 G | 200 G | 250 G | 4 days/repeat | 5 days | 0.541 | -170 G | +1,030 G | +4.54% |
| **Honey Flower** | Shatolla | Waterside | 380 G | 630 G | 785 G | 6 days | 7 days | 1.658 | +250 G | +1,250 G | +7.50% |
| **Tingle Radish** | Nemea | Farm | 390 G | 530 G | 660 G | 4 days | 5 days | 1.359 | +140 G | +980 G | +6.33% |
| **Sudor Pepper** | Argene | Cave | 400 G | 250 G | 310 G | 3 days/repeat | 4 days | 0.625 | -150 G | +2,100 G | +6.70% |
| **Revol Pepper** | Argene | Cave | 560 G | 265 G | 330 G | 4 days/repeat | 5 days | 0.473 | -295 G | +1,565 G | +4.61% |
| **Bellhop Seeds** | Shatolla | Farm | 560 G | 45 G | 55 G | 7 days/repeat | 8 days | 0.080 | -515 G | -380 G | Neg. |
| **Seatide Garlic** | Shatolla | Farm | 650 G | 1,000 G | 1,250 G | 6 days | 7 days | 1.538 | +350 G | +1,750 G | +6.35% |
| **Chilly Plant** | Argene | Farm | 800 G | 1,300 G | 1,625 G | 7 days | 8 days | 1.625 | +500 G | +2,000 G | +6.26% |
| **Grouply Grape** | Lethe | Farm | 2,000 G | 85 G | 105 G | 6 days/repeat | — | Tree | — | Multi-Season | Tree |
| **Princess Chestnut**| Lethe | Farm | 2,200 G | 60 G | 75 G | 7 days/repeat | — | Tree | — | Multi-Season | Tree |
| **SnowCap Mikan** | Lethe | Farm | 2,300 G | 65 G | 80 G | 7 days/repeat | — | Tree | — | Multi-Season | Tree |
| **Islet Watermelon**| Shatolla | Waterside | 2,500 G | 4,600 G | 5,800 G | 12 days/repeat | 13 days | 1.840 | +2,100 G | +6,700 G | +4.44% |
| **Lococonut** | Shatolla | Waterside | 3,200 G | 35 G | 45 G | 7 days/repeat | — | Tree | — | Multi-Season | Tree |
| **Lantern Pumpkin** | Lethe | Farm | 3,750 G | 3,750 G | — | 11 days | 12 days | 1.000 | 0 G | 0 G | 0.0% |
| **Wisty Peach** | Nemea | Farm | 4,200 G | 115 G | 230 G | 10 days/repeat | — | Tree | — | Multi-Season | Tree |

---

## 4. Land & Biome Distribution Matrix

| Biome Land Type | Associated Crops | Unlocking Requirement / Conditions |
| :--- | :--- | :--- |
| **Standard Farm** | Wheat, Lettuce, Carrop, Morrocorn, Unionion, Radish, Cucumble, Tomato, Strawbuddy, Garlic, Cabbage, Chilly Plant, Trees | Default field surrounding Bird's Eye Brae |
| **Waterside Biome** | Nectarcane, Honey Flower, Islet Watermelon, Lococonut | Water Faerie orders / Chapter progression |
| **Cave Biome** | Sudor Pepper, Revol Pepper | Fire/Earth Faerie biome unlocks |

---

## 5. Summary Insights for Fast Recall in New Chats

1. **Top Cash Velocity (Days 1–7):** **Dress Lettuce** (Lethe, 55 G, $M=1.545$, 2d) and **Unionion** (Nemea, 105 G, $M=1.857$, 3d).
2. **Top High-Density Scaler (Day 8+):** **Morrocorn** (Shatolla/Lethe, 200 G, $M=2.000$, 4d, 50 G/day net profit).
3. **Repeat Crop Staples:** **Cucumble** (Lethe, 370 G, Farm) and **Nectarcane** (Shatolla/Nemea, 370 G, Waterside) planted on Days 1–5.
4. **Single-Day Plot Utility:** **Carrop** (Nemea, 95 G, 1d) for gap-filling, daily plot syncing, and Day 29 pre-Quietus cashouts.
