# Textiles screen (full theme, 26 names) — 22 Sep 2026

**26 names screened.** This run covers the whole "Textiles" theme in `data/themes-in.json`: the 5 names NSE tags as Textiles inside the Nifty 500, plus 21 listed textile and apparel companies outside the Nifty 500. It replaces nothing: the earlier 5-name screen of the same date (`textiles-20260922.md`) stands, and its audited figures for Page, KPR Mill, Trident, Vardhman and Welspun are carried forward here unchanged.

**Audit: passed.** `report_audit.py` sampled 30 of 344 data points (15%, seed 42) on 2026-09-22; all 30 re-read from source and matched.

## What was screened

- **Universe:** 26 companies. Source for the 5 Nifty 500 names: the NSE constituent file. Source for the other 21: the Textiles theme list, checked against the 21-Sep-2026 NSE bhavcopy for a live EQ-series quote. Every one of the 26 trades on the main board; none is on the SME board. Market caps run from ₹40,657 crore (Page Industries) to ₹223 crore (Shiva Texyarn), all Screener, 2026-09-22.
- **Symbol correction:** the instruction said AMBICO; the NSE symbol for Ambika Cotton Mills is AMBIKCO, and that is what was screened.
- **Thresholds, from `CLAUDE.md` (22 Sep 2026):** ten-year ROE bar 10% for asset-heavy names, and textiles is asset-heavy, so 10% applies to all 26; promoter pledge above zero is a hard fail; a promoter stake falling with no stated reason is a flag, and the name survives.
- **Stated assumptions where the method gives no number:** (1) a figure within 10% of its threshold is marked ⚠️ borderline and carried forward flagged, and step 2 decides; (2) in step 2 the ROE bar for asset-heavy names is relaxed to a ten-year average above 10%; (3) "peers" in step 2 means the 12 names that passed step 1, whose median PE is 17.5.
- **Full-cycle averages:** ten years (FY2017-FY2026) for checks 1, 4 and 6, five-year sums (FY2022-FY2026) for checks 2, 3 and 5. Where fewer years exist the report says so: Raymond Lifestyle 3 years, Sanathan 5, Dollar 9, Lux 9 (consolidated), Siyaram 10 (Screener's page has no FY2017 column).
- **Data collection:** four subagents pulled the Screener pages, cross-checks, year-end closes, pledge and stake data in parallel. Every judgement below was made in one place, by one standard, from their raw figures.
- **Standalone pages used** where Screener's consolidated page was empty or short: Page Industries (no subsidiaries), Ambika Cotton, Nahar Spinning, Nitin Spinners (blank consolidated headline), and Filatex, Shiva Texyarn and Monte Carlo (consolidated pages missing five or more years; standalone has all twelve). Lux is kept consolidated at nine years because its FY2021 merger of group companies makes standalone misleading.
- **Splits and bonuses corrected** before any PE range was written: KPR Mill 5-for-1 (ex 24 Sep 2021), Trident 10-for-1 (ex 13 Dec 2019), Vardhman 5-for-1 (ex 24 Mar 2022), Siyaram ₹10 to ₹2 (ex 25 Oct 2017), Filatex 5-for-1 (ex 27 Jun 2018) and 2-for-1 (ex 27 Dec 2022), Garware 4-for-1 bonus (record 3 Jan 2025, shares 1.99 → 9.93 crore), Kitex 2-for-1 bonus (record 17 Jan 2025, shares 6.65 → 19.95 crore). The two bonuses are not dilution and check 7 is bonus-adjusted for them. Garware's FY2017 and FY2018 closes are read under its old symbol GARWALLROP.
- **The sector event of FY26:** the United States put a 50% tariff on Indian textiles in two steps (7 Aug and 27 Aug 2025). Welspun's Dec 2025 quarter profit was ₹3 crore; Trident's OPM fell to 9%; Kitex's FY26 EPS fell to ₹0.30. Exporters recovered in the Jun 2026 quarter; the reason was not checked here.
- **Left out:** nothing. All 26 names in the theme were screened.

### How each check was computed

As in the Construction Materials screen of the same date: ROE is net profit over average equity each year; FCF is Screener's Free Cash Flow row summed over five years; interest cover is (profit before tax + interest) / interest, shown for FY26, as a five-year sum-over-sum and at the trough year; OCF/PAT is five-year cash from operations over five-year net profit; net margin is net profit over sales averaged; dilution is the change in shares from Mar 2021 to Mar 2026 with bonuses removed; check 8 is pledge (Trendlyne latest quarter, or a SEBI Regulation 31(4) declaration) plus the promoter stake from Sep 2023 to Jun 2026 on Screener.

## Summary table

All money in ₹ crore.

| Company | Symbol | Years of data | 1 ROE (10y avg) | 2 FCF (5y, ₹ cr) | 3 Interest cover | 4 OPM (10y avg) | 5 OCF/PAT (5y) | 6 Net margin (10y avg) | 7 Dilution (5y) | 8 Pledge / promoter | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Page Industries Ltd. | PAGEIND | 12 | ✅ 46.2% | ✅ +2,862 | ✅ 21.5x FY26, 20.6x 5y, 17.8x trough | ✅ 20.0% (worst 18%) | ✅ 1.07 | ✅ 13.1% (worst 11.6%) | ✅ +0.0% | ⚠️ pledge 0.0%; promoter 45.11% → 42.89%, sales Jun-Dec 2024, no reason stated (flag) | Carried forward, flag on 8 |
| K.P.R. Mill Ltd. | KPRMILL | 12 | ✅ 21.7% | ✅ +2,015 | ✅ 22.8x FY26, 20.7x 5y, 14.7x trough | ✅ 20.5% (worst 18%) | ✅ 0.96 | ✅ 12.5% (worst 9.6%) | ✅ +0.0% | ⚠️ pledge 0.0%; promoter 73.75% → 67.52%, block sales Sep 2024 and May 2025, no reason stated (flag) | Carried forward, flag on 8 |
| Garware Technical Fibres Ltd. | GARFIBRES | 12 | ✅ 19.3% | ✅ +646 | ✅ 20.2x FY26, 18.4x 5y, 16.4x trough | ✅ 18.7% (worst 16%) | ✅ 0.85 | ✅ 13.5% (worst 9.9%) | ✅ +0.0% (bonus-adjusted; raw +371.4%) | ✅ pledge 0%; promoter 52.70% → 54.25% | Survived |
| Siyaram Silk Mills Ltd. | SIYSIL | 10 | ✅ 15.8% | ✅ +403 | ✅ 9.9x FY26, 13.4x 5y, 9.9x trough | ✅ 12.6% (worst 5%) | ✅ 0.70 | ✅ 7.1% (worst 0.4%) | ✅ +0.0% | ✅ pledge 0%; promoter 67.18% → 67.45% | Survived (5 at the bar) |
| Ambika Cotton Mills Ltd. | AMBIKCO | 12 | ✅ 13.3% | ✅ +287 | ✅ 7.9x FY26, 12.0x 5y, 5.2x trough | ✅ 18.8% (worst 13%) | ✅ 0.89 | ✅ 10.9% (worst 7.7%) | ✅ +0.0% | ✅ pledge 0%; promoter 50.17% → 50.35% | Survived |
| Dollar Industries Ltd. | DOLLAR | 9 | ✅ 15.0% | ✅ +30 | ✅ 6.7x FY26, 7.6x 5y, 5.3x trough | ✅ 11.7% (worst 7%) | ⚠️ 0.66 | ✅ 6.6% (worst 3.7%) | ✅ +0.0% | ⚠️ pledge 0.0% (Trendlyne); SAST filing says no new encumbrance beyond those previously disclosed; promoter 73.09% → 72.58%, fall Mar 2024, no reason (flag) | Carried forward, flags on 5 and 8 |
| Rupa & Company Ltd. | RUPA | 12 | ✅ 14.1% | ✅ +239 | ✅ 5.9x FY26, 7.0x 5y, 4.0x trough | ✅ 12.8% (worst 8%) | ⚠️ 0.70 | ✅ 7.6% (worst 4.7%) | ✅ +0.0% | ✅ pledge 0%; promoter 73.28% → 73.28% | Carried forward, flag on 5 |
| Monte Carlo Fashions Ltd. | MONTECARLO | 12 | ✅ 12.5% | ✅ +145 | ✅ 3.8x FY26, 4.6x 5y, 3.0x trough | ✅ 17.3% (worst 13%) | ⚠️ 0.64 | ✅ 9.4% (worst 5.7%) | ✅ +0.0% | ✅ pledge 0%; promoter 73.17% → 73.17% | Carried forward, flag on 5 |
| Trident Ltd. | TRIDENT | 12 | ✅ 11.5% | ✅ +2,030 | ✅ 5.6x FY26, 6.6x 5y, 4.1x trough | ✅ 17.0% (worst 13%) | ✅ 1.82 | ✅ 6.9% (worst 5.1%) | ✅ +0.0% | ✅ pledge 0%; promoter 73.19% → 73.68% | Survived |
| Vardhman Textiles Ltd. | VTL | 12 | ✅ 12.4% | ✅ +941 | ✅ 11.4x FY26, 13.9x 5y, 9.2x trough | ✅ 15.1% (worst 10%) | ✅ 1.08 | ✅ 10.0% (worst 6.7%) | ✅ +0.0% | ✅ pledge 0%; promoter 64.11% → 65.08% | Survived |
| Nitin Spinners Ltd. | NITINSPIN | 12 | ✅ 17.4% | ✅ +248 | ✅ 4.4x FY26, 5.0x 5y, 3.1x trough | ✅ 14.7% (worst 12%) | ✅ 1.54 | ✅ 5.6% (worst 1.7%) | ✅ +0.0% | ✅ pledge 0%; promoter 56.41% → 56.71% | Survived |
| Welspun Living Ltd. | WELSPUNLIV | 12 | ✅ 13.1% | ✅ +1,585 | ⚠️ 2.8x FY26, 5.2x 5y, 2.8x trough | ✅ 15.3% (worst 8%) | ✅ 1.60 | ⚠️ 5.5% (worst 2.3%) | ✅ -4.0% | ⚠️ pledge 0.00%; promoter 70.50% → 66.36%, trust sold 3.92% Sep 2024, no reason stated (flag) | Carried forward, flags on 3, 6 and 8 |
| Arvind Ltd. | ARVIND | 12 | ❌ 8.1% | ✅ +2,048 | ✅ 3.7x FY26, 3.4x 5y, 3.0x trough | ✅ 10.2% (worst 9%) | ✅ 1.99 | ❌ 3.4% (worst -0.5%) | ✅ +1.2% | ❌ pledge 7.24% of promoter holding (Aug 2026); promoter 41.14% → 38.09% | Eliminated (1, 6, 8) |
| Raymond Ltd. | RAYMOND | 12 | ✅ 43.8% | ✅ +1,705 | ✅ 62.9x FY26, 25.2x 5y, 2.1x trough | ❌ 7.3% (worst -2%) | ❌ 0.15 | ✅ 81.4% (worst -8.8%) | ✅ +0.0% | ✅ pledge 0.0% Jun 2026 (1.69% released May 2026); promoter 49.11% → 48.87% | Eliminated (4, 5) |
| Raymond Lifestyle Ltd. | RAYMONDLSL | 3 | ❌ 9.4% | ✅ +2,713 | ❌ 1.3x FY26, 5.4x 5y, 1.3x trough | ✅ 10.7% (worst 8%) | ❌ 0.36 | ✅ 13.9% (worst 0.6%) | ❌ +500.0% | ❌ pledge 23.74% of promoter holding (Jun 2026); promoter 54.67% → 59.61% | Eliminated (1, 3, 5, 8); short data window |
| Gokaldas Exports Ltd. | GOKEX | 12 | ❌ 6.3% | ❌ -885 | ✅ 2.8x FY26, 4.2x 5y, 2.8x trough | ❌ 6.6% (worst -3%) | ❌ 0.61 | ❌ 2.5% (worst -5.1%) | ❌ +76.2% | ❌ pledge 96.28% of promoter holding (Jun 2026); promoter 11.05% → 9.15% | Eliminated (1, 2, 4, 5, 6, 7, 8) |
| Himatsingka Seide Ltd. | HIMATSEIDE | 12 | ❌ 6.9% | ✅ +927 | ❌ 1.4x FY26, 1.3x 5y, 0.7x trough | ✅ 17.1% (worst 10%) | ✅ 3.61 | ❌ 3.4% (worst -2.4%) | ❌ +28.6% | ⚠️ pledge 0.0%; promoter 47.57% → 37.48% in Dec 2024 quarter, sale not found, no reason (flag) | Eliminated (1, 3, 6, 7) |
| Lux Industries Ltd. | LUXIND | 9 | ✅ 19.6% | ❌ -296 | ✅ 4.6x FY26, 10.9x 5y, 4.6x trough | ✅ 13.1% (worst 6%) | ❌ -0.04 | ✅ 8.4% (worst 3.6%) | ✅ +0.0% | ✅ pledge 0%; promoter 74.19% → 74.19% | Eliminated (2, 5) |
| Alok Industries Ltd. | ALOKINDS | 12 | ✅ 18.2% | ✅ +192 | ❌ -0.2x FY26, -0.2x 5y, -0.8x trough | ❌ -25.7% (worst -245%) | ⚠️ -0.12 | ❌ -49.1% (worst -337.0%) | ✅ +0.0% | ✅ pledge 0%; promoter 75.00% → 75.00% | Eliminated (3, 4, 6) |
| Filatex India Ltd. | FILATEX | 12 | ✅ 17.3% | ✅ +912 | ✅ 5.7x FY26, 6.8x 5y, 3.1x trough | ❌ 8.8% (worst 5%) | ✅ 1.64 | ❌ 4.1% (worst 2.1%) | ✅ +0.0% | ✅ pledge 0%; promoter 64.76% → 65.47% | Eliminated (4, 6) |
| Sanathan Textiles Ltd. | SANATHAN | 5 | ✅ 15.2% | ❌ -1,026 | ⚠️ 2.1x FY26, 6.2x 5y, 2.1x trough | ✅ 10.0% (worst 8%) | ✅ 1.77 | ✅ 5.5% (worst 2.0%) | ✅ +16.7% | ✅ pledge 0%; promoter 78.58% → 78.58% | Eliminated (2); short data window |
| Shiva Texyarn Ltd. | SHIVATEX | 12 | ❌ 5.5% | ✅ +123 | ❌ 2.1x FY26, 1.5x 5y, -0.3x trough | ❌ 9.7% (worst 2%) | ✅ 6.33 | ❌ 1.8% (worst -3.3%) | ✅ +0.0% | ✅ pledge 0%; promoter 74.04% → 74.04% | Eliminated (1, 3, 4, 6) |
| Nahar Spinning Mills Ltd. | NAHARSPING | 12 | ❌ 5.4% | ✅ +235 | ❌ 1.4x FY26, 3.6x 5y, 0.1x trough | ❌ 8.0% (worst 3%) | ✅ 1.27 | ❌ 2.0% (worst -2.5%) | ✅ +0.0% | ✅ pledge 0%; promoter 66.61% → 68.02% | Eliminated (1, 3, 4, 6) |
| Nahar Industrial Enterprises Ltd. | NAHARINDUS | 12 | ❌ 4.1% | ✅ +171 | ⚠️ 2.6x FY26, 3.0x 5y, 1.4x trough | ❌ 7.6% (worst 4%) | ✅ 2.09 | ❌ 1.9% (worst -1.6%) | ✅ +7.5% | ✅ pledge 0%; promoter 71.25% → 71.25% | Eliminated (1, 4, 6) |
| Kitex Garments Ltd. | KITEX | 12 | ✅ 11.5% | ❌ -1,246 | ❌ 1.2x FY26, 8.3x 5y, 1.2x trough | ✅ 19.1% (worst 4%) | ✅ 1.79 | ✅ 11.1% (worst -1.9%) | ✅ +0.0% (bonus-adjusted; raw +185.7%) | ✅ pledge 0%; promoter 56.66% → 56.66% | Eliminated (2, 3) |
| Banswara Syntex Ltd. | BANSWRAS | 12 | ❌ 9.3% | ❌ -66 | ❌ 2.0x FY26, 3.0x 5y, 1.8x trough | ❌ 9.8% (worst 8%) | ✅ 1.66 | ❌ 2.8% (worst 0.6%) | ✅ +0.0% | ⚠️ pledge 0.0%; promoter 56.11% → 54.19%, promoter sold 6 lakh shares Dec 2023, no reason (flag) | Eliminated (1, 2, 3, 4, 6) |

## Survived (12 after step 1, 4 after step 2)

Step 1 carried twelve names forward. Six clean: Garware, Siyaram, Ambika, Trident, Vardhman, Nitin Spinners. Six flagged: Page and KPR Mill on promoter sales, Welspun on interest cover, net margin and a promoter sale, Dollar on cash conversion and a promoter sale, Rupa and Monte Carlo on cash conversion.

### Step 2 — five value checks

PE is market cap over trailing-twelve-month net profit (Screener, to Jun 2026). "Own range" is the split-corrected year-end PE, FY2017-FY2026. Peer median PE of the twelve is 17.5. Moat is my score out of 5 on the evidence named.

| Company | 1 Valuation | 2 ROE | 3 Cash flow (OCF/PAT, 5y) | 4 Debt (D/E) | 5 Moat | Result |
|---|---|---|---|---|---|---|
| Page Industries | ✅ PE 53.8; own range 46.4x-99.3x, median 69.1x: near its ten-year low. Peers are not comparable | ✅ 52.5% | ✅ 1.07 | ✅ 0.18 | ✅ 4 of 5: the Jockey brand under an exclusive licence to 2040; 38-54% ROE for ten years | **Keep** |
| Siyaram Silk Mills | ✅ PE 10.1; own range 7.8x-25.5x excluding the FY21 outlier (245x on EPS ₹0.76), median 10.8x | ✅ 16.8% FY26; 16.3%, 16.3%, 16.8% last three years | ⚠️ 0.70, exactly at the line; yearly 0.21 to 1.29 | ✅ 0.24 | ✅ 3 of 5: branded men's fabrics and readymades; OPM held 12-16% in every normal year | **Keep, amber** |
| Ambika Cotton Mills | ✅ PE 11.4; own range 5.8x-13.4x, median 9.6x; PB 0.97, at book | ✅ 13.3% ten-year (relaxed bar); but 7.5%, 7.5%, 7.7% in FY24-FY26 | ✅ 0.89 | ✅ 0.00, debt-free | ✅ 3 of 5: speciality compact yarn; ten-year OPM 18.8% against 8-15% for other spinners here | **Keep, amber** (ROE trend) |
| Dollar Industries | ✅ PE 13.9; own range 10.8x-37.6x, median 22.1x: low end | ✅ 15.0% nine-year (relaxed bar); FY26 11.9% | ⚠️ 0.66, close | ✅ 0.31 | ✅ 3 of 5: brands plus distribution; sales doubled in eight years while Rupa's and Lux's stood still | **Keep, amber** |
| K.P.R. Mill | ❌ PE 42.0 against an own range of 6.2x-38.0x (median 20.6x): above its ten-year high while profit has been ₹805-866 crore for five years | ✅ 16.2% FY26; 21.7% ten-year | ✅ 0.96 | ✅ 0.10 | ✅ 3 of 5 | **Dropped** (4 pass; valuation fails outright) |
| Garware Technical Fibres | ❌ PE 37.2 against an own range of 16.7x-37.1x (median 31.3x): at its ten-year high while FY26 profit fell 14% (₹232 → ₹199 crore) | ✅ 15.3% FY26; 19.3% ten-year | ✅ 0.85 | ✅ 0.03 | ✅ 4 of 5: engineered technical textiles, exports, OPM 16-21% for ten years | **Dropped** (4 pass; valuation fails outright) |
| Rupa & Company | ✅ PE 14.5; own range 12.1x-36.8x, median 22.7x | ✅ 14.1% ten-year (relaxed); 6.0-8.4% in each of the last four years | ⚠️ 0.70, at the line | ✅ 0.24 | ❌ 2 of 5: sales ₹1,093 crore in FY17 and ₹1,259 crore in FY26, OPM 20% (FY21) to 9% (FY26); the brands protect nothing | **Dropped** (3 pass, 1 close) |
| Monte Carlo Fashions | ✅ PE 10.6; own median 11.5x | ✅ 12.5% ten-year (relaxed); FY26 12.9% | ⚠️ 0.64, close | ❌ 0.65, close to 0.6 | ✅ 3 of 5: winter-wear brand | **Dropped** (3 pass, 2 close) |
| Trident | ⚠️ PE 29.7; own median 23.4x | ✅ 11.5% ten-year (relaxed); 8.2%, 8.3%, 8.0% flat | ✅ 1.82 | ✅ 0.38 | ❌ 2 of 5: towels, sheets and yarn are commodities | **Dropped** (3 pass, 1 close) |
| Vardhman Textiles | ❌ PE 18.7 at the top of 6.2x-20.3x (median 11.4x) | ✅ 12.4% ten-year (relaxed); FY26 7.4% | ✅ 1.08 | ✅ 0.18 | ❌ 2 of 5 | **Dropped** (3 pass) |
| Nitin Spinners | ❌ PE 16.2 against an own range of 6.6x-13.9x (median 9.6x): above its ten-year high | ✅ 17.4% ten-year (relaxed); FY26 12.8% | ✅ 1.54 | ❌ 0.76 | ❌ 2 of 5: cotton yarn | **Dropped** (2 pass) |
| Welspun Living | ❌ PE 71.3 on trough earnings; own range 4.3x-50.9x | ✅ 13.1% ten-year (relaxed); FY26 4.4% | ✅ 1.60 | ✅ 0.47 | ❌ 2 of 5 | **Dropped** (3 pass) |

Four survive, so the moat bar was not raised. All four go to the checklist.

## Eliminated (22: 14 at step 1, 8 at step 2)

| Company | Failed check | The number | Why it was dropped |
|---|---|---|---|
| Arvind | 1, 6, 8 | ROE 8.1% ten-year; net margin 3.4%; **7.24% of the promoter holding pledged** (Trendlyne, Aug 2026); promoter 41.14% → 38.09% | A pledge is a hard fail on its own. The returns fail too: a denim and fabric maker with a 3.4% net margin over ten years. |
| Raymond | 4, 5 | OPM 7.3% ten-year (−2% worst year); OCF/PAT 0.15 | After demerging Raymond Lifestyle (Sep 2024) and its realty arm, this is a real-estate and engineering company; the 43.8% ROE and 81% net margin in the table are demerger gains, not operations. Pledge was 1.69% until J.K. Investors released it on 20 May 2026; 0% at Jun 2026. Not a textile business now. |
| Raymond Lifestyle | 1, 3, 5, 8 | ROE 9.4% on three years; interest cover 1.3x; OCF/PAT 0.36; **23.74% of the promoter holding pledged** (Trendlyne, Jun 2026; scanx shows 8.35% of capital after a May 2026 release) | Listed Sep 2024 by demerger: short data window, and a pledge. The +500% "dilution" is the demerger listing itself, not a sale. |
| Gokaldas Exports | 1, 2, 4, 5, 6, 7, 8 | ROE 6.3%; FCF −₹885 crore; OPM 6.6%; OCF/PAT 0.61; net margin 2.5%; shares +76% (QIP Apr 2024); **96.28% of the promoter holding pledged**, promoter at 9.15% | A garment exporter that fails seven of eight checks; the promoter owns 9% and has pledged almost all of it. |
| Himatsingka Seide | 1, 3, 6, 7 | ROE 6.9%; interest cover 1.4x (0.7x trough); net margin 3.4%; shares +28.6% | Home-textile exporter with debt to equity 1.23. Promoter stake fell 47.57% → 37.48% in the Dec 2024 quarter with no sale disclosure found; flagged, but the numbers eliminate it first. |
| Lux Industries | 2, 5 | FCF −₹296 crore over five years; OCF/PAT −0.04 (CFO −₹37 crore against PAT ₹872 crore) | A 19.6% ROE that never turned into cash: five years of profit absorbed by inventory and receivables. |
| Alok Industries | 3, 4, 6 | Interest cover −0.2x; OPM −25.7% ten-year; net margin −49.1%; equity −₹21,527 crore | Negative net worth under its new owner; the 18.2% "ROE" is a loss over negative equity. Borrowings ₹26,106 crore. |
| Filatex India | 4, 6 | OPM 8.8%; net margin 4.1% (standalone, 12 years) | Polyester yarn is a commodity spread; the margin has never reached 10% on average. |
| Sanathan Textiles | 2 | FCF −₹1,026 crore over five years | Listed Dec 2024; five years of data. Capacity build-out ahead of the IPO consumed all cash. Exemption A considered and refused: OPM 10.0%, not 30%. |
| Shiva Texyarn | 1, 3, 4, 6 | ROE 5.5%; interest cover 1.5x five-year; OPM 9.7%; net margin 1.8% | Small spinner (₹223 crore market cap) with returns below the cost of capital. |
| Nahar Spinning Mills | 1, 3, 4, 6 | ROE 5.4%; interest cover 1.4x (0.1x trough); OPM 8.0%; net margin 2.0% | Yarn spinner trading at 0.67x book because the book earns 5%. |
| Nahar Industrial Enterprises | 1, 4, 6 | ROE 4.1%; OPM 7.6%; net margin 1.9% | Same group, same economics. |
| Kitex Garments | 2, 3 | FCF −₹1,246 crore over five years; interest cover 1.2x; FY26 EPS ₹0.30 | Infant-wear exporter mid-way through a large Telangana capex; the US tariff took FY26 profit to near zero. Dilution of +186% is the Jan 2025 bonus, not a sale. |
| Banswara Syntex | 1, 2, 3, 4, 6 | ROE 9.3%; FCF −₹66 crore; interest cover 1.8x trough; OPM 9.8%; net margin 2.8% | Fails five checks. Promoter sold 6 lakh shares in Dec 2023 with no stated reason; flagged, but the numbers decide. |
| K.P.R. Mill | step 2: valuation | PE 42.0 against an own ten-year range of 6.2x-38.0x; PB 6.70 against 1.23-6.64 | The best manufacturer in the set (21.7% ten-year ROE, 22.8x interest cover, near-zero debt) at a price above its own ten-year high while profit has been flat since FY22. Promoters sold 6.2 points of stake in two block deals with no stated reason. To watch. |
| Garware Technical Fibres | step 2: valuation | PE 37.2 against an own range of 16.7x-37.1x; PB 5.88 against 2.88-6.90 | Ten years of 16-21% OPM and 15-21% ROE, no debt, a 4-star moat in technical textiles, priced at its ten-year high in a year when profit fell 14%. To watch. |
| Rupa & Company | step 2: moat | Sales ₹1,093 crore (FY17) → ₹1,259 crore (FY26); OPM 20% (FY21) → 9% (FY26); ROE 6-8% for four years | The brands are well known and have protected neither volume nor price for a decade. |
| Monte Carlo Fashions | step 2: debt and cash flow both close | D/E 0.65; OCF/PAT 0.64 | Two near-misses is one too many under the keep rule. Cheap (PE 10.6, dividend yield 3.7%) but working-capital heavy and seasonal. |
| Trident | step 2: moat | ROE 8.0-8.3% for three years; OPM 13% in FY25-FY26 against 19% in FY17-FY19; Dec 2025 quarter OPM 9% | Commodity exporter with no margin floor. |
| Vardhman Textiles | step 2: valuation and moat | PE 18.7 at the top of 6.2x-20.3x; ROE 7.4% FY26 | Well-run spinner whose profit swings with cotton; the market is paying its highest multiple in ten years for a 7% ROE year. |
| Nitin Spinners | step 2: valuation, debt, moat | PE 16.2 against an own range of 6.6x-13.9x; D/E 0.76 | A 17% ten-year ROE spinner, but leveraged and priced above its own ten-year high. |
| Welspun Living | step 2: valuation and moat | PE 71.3; FY26 profit ₹213 crore against ₹644 crore; OPM 8% | The tariff casualty. Promoter trust sold 3.92% in Sep 2024 with no stated reason. |

## Exempted (0)

None granted. Considered: Sanathan under A (listed under 10 years) — fails the 30% OPM condition (10.0%). No name has OPM above 30% (B). Under C, Page has ROE above 20% and OCF/PAT above 1.0 but earns from markup, and needed no exemption.

## Not screened

None. All 26 names in the theme were screened. Data gaps inside the screen: year-end closes missing for Trident (Mar 2022), Nitin Spinners (Mar 2022), Dollar (Mar 2017, before its NSE listing), Lux (Mar 2017), Himatsingka (Mar 2021, Mar 2023), Nahar Spinning (four years) and Alok (most years, and its EPS is negative); those years are left out of the own-range figures. Kitex's FY26 PE (474x on EPS ₹0.30) is treated as not meaningful.

## Short analysis — one section per survivor

### Page Industries (PAGEIND)

**The business in one line.** Page holds the exclusive licence to make and sell Jockey innerwear, loungewear and athleisure in India, Sri Lanka, Bangladesh, Nepal and the UAE, and Speedo swimwear in India, sells through distributors, multi-brand retailers, 1,579 exclusive brand stores run by franchisees and online, and is paid on sale or short trade credit.

**Financial quality.** Sales grew from ₹2,129 crore (FY17) to ₹5,247 crore (FY26), 10.5% a year; net profit from ₹266 crore to ₹764 crore, 12.4% a year. OPM has stayed between 18% and 22% for ten years; FY26 was 22%. ROE averaged 46.2% over ten years and was 52.5% in FY26. Five-year cash from operations ₹3,403 crore against net profit ₹3,170 crore (1.07). Net cash of ₹255 crore at 31 Mar 2026 (annual report). FY26 dividends totalled ₹550 per share in four interims (₹150, ₹125, ₹125, ₹150; annual report), a 1.53% yield. The most important change of the last two years: growth came back after the FY24 dip (sales −3%, profit flat); FY25-FY26 added ₹678 crore of sales and ₹195 crore of profit with OPM back at 22-23%. The Jun 2026 quarter was ₹1,420 crore of sales (+8% year on year) and ₹193 crore of profit (−4%), OPM 20%.

**Moat.** Brand and pricing power, resting on a licence. The licence began in 1994 and was extended in June 2018 to 31 December 2040; Saudi Arabia, Bahrain and Kuwait were added in FY25 (BusinessToday, Business Standard, June 2018; annual report). Evidence: 38-54% ROE every year for a decade with no debt, which no unbranded textile maker in India approaches. Jockey International named Page "Licensee of the Decade" for the second time in 2026 (annual report). Stable: athleisure and online-first brands took share at the edges after FY22, but the FY25-FY26 recovery says the brand was not displaced.

**Top 3 risks.** (1) The brand belongs to Jockey International; the licence runs 14 more years and its royalty and renewal terms outrank every margin in this report. (2) Growth of 10.5% a year over ten years at 54x earnings; the FY24 decline showed the brand is not immune to a slow consumer. (3) Promoters sold 2.2 points of stake in 2024 with no stated reason, on top of periodic sales since 2014.

**Valuation now.** PE 53.8 (own range 46.4x-99.3x, median 69.1x; peers 17.5x but not comparable). PB 26.7 (own range 22.8-43.7, median 29.9). Dividend yield 1.53%. One word: **fair** against its own history.

**Into the final three?** Yes. The only name of 26 to pass every check by a wide margin except price, and the only one with a durable brand.

### Siyaram Silk Mills (SIYSIL)

**The business in one line.** Siyaram makes and sells branded fabrics and readymade garments for men's wear through wholesalers, dealers and its own stores across India, and exports a little to the Gulf and Asia; it is paid on trade credit that runs long in the fabric wholesale channel.

**Financial quality.** Sales grew from ₹1,605 crore (FY16) to ₹2,572 crore (FY26), 4.8% a year over ten years; net profit from ₹85 crore to ₹231 crore, 10.5% a year, with a near-zero FY21 (₹4 crore) in COVID. OPM averaged 12.6% and was 13% in FY26; every normal year sits between 12% and 17%. ROE was 16.8% in FY26 and 16.3% in each of the two years before. Debt to equity 0.24. Five-year FCF +₹403 crore. Cash conversion is the weak point: five-year OCF/PAT 0.70 exactly, with yearly figures from 0.21 to 1.29, because working capital swings with the fabric trade. The most important change of the last two years: FY26 sales +16% (₹2,222 → ₹2,572 crore) and profit +17%, yet the share fell 38% from its 52-week high of ₹850 to ₹530; why was not checked. The business is seasonal: the Jun 2026 quarter had ₹446 crore of sales and ₹11 crore of profit at 4% OPM, against ₹853 crore and ₹98 crore in the Mar 2026 quarter.

**Moat.** Brand, in mid-market men's fabric and readymades, with a deep dealer network. Evidence: OPM held above 12% in every non-COVID year while spinners and exporters swung to single digits, and ROE of 16-17% for three years without leverage. Stable: fabric is losing share to readymades nationally, and Siyaram's own readymade lines are where the growth is.

**Top 3 risks.** (1) Working capital: cash conversion of 0.70 over five years, with two years below 0.5; a bad season shows up as debt, not as a loss. (2) Seasonality and demand: two of four quarters carry the year; a weak festive season is a weak year. (3) Family-run governance and a small free float; promoters hold 67.45% and have made a nil-encumbrance declaration for FY26.

**Valuation now.** PE 10.1 (own range 7.8x-25.5x excluding FY21, median 10.8x; peers 17.5x). PB 1.65 (own range 0.87-4.0, median 1.74). Dividend yield 2.26% on Screener against 3.02% on stockanalysis, a gap over 1% left unresolved; the annual report settles it in the checklist. One word: **fair**.

**Into the final three?** Yes, as the moderate-certainty name: 16-17% ROE for three years at ten times earnings, with cash conversion the thing to prove.

### Ambika Cotton Mills (AMBIKCO)

**The business in one line.** Ambika spins speciality compact cotton yarn in Coimbatore from imported and domestic long-staple cotton and sells it to premium shirting and knitting mills in India and abroad, paid on short trade credit.

**Financial quality.** Sales grew from ₹528 crore (FY17) to ₹781 crore (FY26), 4.4% a year; net profit from ₹56 crore to ₹72 crore, 2.8% a year, with a cotton-price windfall of ₹180 crore in FY22. Ten-year OPM 18.8%, against 8-15% for every other spinner in this screen; FY26 15%. ROE averaged 13.3% over ten years but was 7.5%, 7.5% and 7.7% in FY24-FY26. Debt-free: borrowings nil at Mar 2026 against equity ₹955 crore. Five-year FCF +₹287 crore; OCF/PAT 0.89. The most important change of the last two years: sales fell 15% in FY25 (₹823 → ₹702 crore) as yarn demand weakened, then recovered in FY26 (₹781 crore) and in the Jun 2026 quarter (₹258 crore, +34% year on year; profit ₹26 crore, +63%).

**Moat.** Scale and cost in a niche: a premium yarn with a margin premium of five to ten points over other spinners sustained for ten years is evidence of pricing power in its segment. Narrowing at the moment: the margin premium shrank in FY24-FY26 (OPM 13-15%) and ROE with it.

**Top 3 risks.** (1) Cotton: input price and yarn demand set the year; FY22's ₹180 crore and FY24's ₹63 crore are the same company. (2) Idle capital: PB 0.97 with no debt means the book earns only 7.7%; the cash is not compounding. (3) Size and liquidity: ₹927 crore market cap, 57 lakh shares, promoter 50.35%.

**Valuation now.** PE 11.4 (own range 5.8x-13.4x, median 9.6x; peers 17.5x). PB 0.97 (own range 0.63-2.09, median 1.0): trading at book. Dividend yield 2.28%. One word: **fair** against its own history, cheap against peers.

**Into the final three?** Yes, as the high-risk, high-payoff name: a debt-free niche spinner at book value in a yarn trough. The payoff is OPM back at 19%; the risk is that 7.5% ROE is the new normal.

### Dollar Industries (DOLLAR)

**The business in one line.** Dollar makes and sells economy and mid-market innerwear, thermals and casual wear under its own brands through distributors and retailers across India, and is paid on trade credit.

**Financial quality.** Sales grew from ₹926 crore (FY18) to ₹1,881 crore (FY26), 9.3% a year; net profit from ₹64 crore to ₹107 crore, 6.6% a year. OPM averaged 11.7% over nine years and was 11% in FY26 (16% in FY22, 7% in FY23). ROE averaged 15.0% but was 12.2%, 11.2% and 11.9% in FY24-FY26. Debt to equity 0.31. Cash is the weak point: five-year FCF only +₹30 crore (−59, +81, −107, +19, +96) and OCF/PAT 0.66, because inventory and receivables grow with sales. The most important change of the last two years: sales +10% and profit +16% in FY26, and the Jun 2026 quarter profit ₹26 crore (+18%); and a group restructuring — a demerger of Dindayal Texpro and the merger of eight promoter-group companies into Dollar (board 26 Sep 2025, NCLT order 11 May 2026, meetings July 2026), with a plan to move 51% of the promoter holding into a trust (web summaries; the scheme document was not read).

**Moat.** Brand plus distribution, in the economy segment. Evidence: sales doubled in eight years while Rupa's and Lux's, the two direct rivals here, stood still. Stable.

**Top 3 risks.** (1) Working capital: profit that does not turn into cash for two years in five. (2) The promoter-group merger: eight related companies folded into the listed one at valuations set by the promoter; the terms outrank the margins until read. (3) Pledge wording: Trendlyne shows 0.0% pledged; the FY26 Regulation 31(4) filing says "no new encumbrance beyond those previously disclosed", which must be read as either nil or a carried-over pledge before any money moves.

**Valuation now.** PE 13.9 (own range 10.8x-37.6x, median 22.1x; peers 17.5x). PB 1.65 (own range 1.3-6.08, median 2.71). Dividend yield 1.09%. One word: **cheap** against its own history.

**Into the final three?** No, as the fourth survivor: it goes to the checklist with the other three, but Siyaram earns more on capital at a lower price and Ambika has the cleaner balance sheet.

## The final three

| Company | Type | Why it is here | Main risk | What would change my mind |
|---|---|---|---|---|
| Page Industries | high-certainty, low-excitement compounder | 46% ten-year ROE, net cash, OPM 18-22% through every cotton cycle, PE near its own ten-year low, licence to 2040 | The brand is licensed, not owned; promoters selling without a stated reason | Licence terms read and benign, a stated reason for the sales, and sales growth back above 8% keep it; a third year of promoter selling drops it |
| Siyaram Silk Mills | moderate-certainty grower | ROE 16-17% for three years at ten times earnings, no meaningful debt, brands in a growing readymade segment | Cash conversion of 0.70 over five years; seasonal earnings | Two years of OCF/PAT above 0.9 lifts it; a working-capital-driven debt rise drops it |
| Ambika Cotton Mills | high-risk, high-payoff | Debt-free niche spinner at book value with a ten-year margin premium over its peers, in a yarn trough | ROE stuck at 7.5% for three years; cotton cycle; small and illiquid | OPM back above 18% for a full year lifts it; a fourth year at 7-8% ROE says the premium is gone |

Dollar Industries survives step 2 and goes to the checklist, but is not in the three: its cash conversion and the promoter-group merger are open questions that a screen cannot settle.

## Sector verdict

Pass rate 4/26 after both steps (12/26 after the eight hard checks). Indian listed textiles is mostly spinners and exporters whose returns swing with cotton and US demand and whose margins the 50% US tariff of Aug 2025 showed to have no floor; three of the fourteen step-1 eliminations were on promoter pledge alone. What survives is domestic and branded (Page, Siyaram, Dollar) or a debt-free niche (Ambika). Worth more time on those four, and on KPR Mill and Garware at lower prices.

## Information grade

| Area | Grade | Note |
|---|---|---|
| Company financials | A | Twelve years from Screener for 22 of 26 names; short windows stated for the other four. Seven standalone substitutions and eight split or bonus corrections are listed above. |
| Valuation freshness | A | NSE closes of 21-Sep-2026; two sources agree within 1% on price for all 26. Market cap or PE gaps over 1% on 14 names are recorded in the batch files; the Screener figure is used throughout and the gap is noted where it matters (Raymond and Raymond Lifestyle PE, where demerger accounting makes the two sources disagree by more than 200%). |
| Competitive picture | B | Moat scores rest on margin and return data and on business descriptions; no market-share figures from a primary source. |
| Management | B | Pledge is known for all 26 (Trendlyne, SEBI declarations, or both). Reasons for the promoter-stake falls at KPR Mill, Page, Welspun, Dollar, Himatsingka and Banswara were not found. No annual report was opened for the screen; the checklist reads the survivors'. |

## Sources

**NSE**
- Nifty 500 constituent file: https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv ; theme list: `data/themes-in.json` (Textiles, 26 symbols).
- Daily bhavcopy, 21-Sep-2026: https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_21092026.csv
- Year-end closes FY2017-FY2026: the same series for 2020-2026 and https://nsearchives.nseindia.com/content/historical/EQUITIES/{YYYY}/MAR/cm{DD}MAR{YYYY}bhav.csv.zip for 2017-2019 (GARWALLROP for Garware, WELSPUNIND for Welspun).

**Screener.in** (read 2026-09-22, 02:21-03:10 IST): https://www.screener.in/company/{SYMBOL}/consolidated/ for all 26; standalone pages for PAGEIND, AMBIKCO, NAHARSPING, NITINSPIN, FILATEX, SHIVATEX, MONTECARLO. Every check figure, quarterly result to Jun 2026 and quarterly promoter holding is from these pages.

**stockanalysis.com** (read 2026-09-22): quote pages for the two-source check on all 26; ratio pages for the twelve step-1 survivors.

**Promoter pledge and stake** (read 2026-09-22): Trendlyne latest-shareholding pages for KPR Mill, Page, Arvind, Raymond, Raymond Lifestyle, Gokaldas, Garware, Nitin Spinners, Ambika, Himatsingka, Rupa, Dollar, Lux, Alok, Filatex, Shiva Texyarn, Nahar Spinning, Nahar Industrial, Monte Carlo, Kitex, Banswara; SEBI Regulation 31(4) FY26 declarations via scanx for Siyaram, Rupa, Dollar, Garware, Nitin Spinners, Himatsingka; web summaries for Trident, Vardhman, Welspun, Sanathan. Block deals: Business Standard 25 Sep 2024 and Bajaj Broking May 2025 (KPR Mill); IIFL (Welspun trust sale); Trendlyne bulk-block page (Banswara).

**Splits and bonuses:** Business Standard 27 Sep 2021 (KPR Mill); EquityBulls (Trident, Dec 2019); ICICI Direct (Vardhman, Mar 2022); Trendlyne corporate actions (Siyaram ex 25 Oct 2017; Filatex Jun 2018 and Dec 2022); Business Standard 6 Jan 2025 (Garware bonus allotment); Business Standard 20 Jan 2025 (Kitex bonus allotment).

**Licence:** BusinessToday and Business Standard, June 2018 (Jockey licence extended to 31 Dec 2040); Page Industries Annual Report 2025-26 (territories, 1,579 exclusive brand stores, dividends, net cash, "Licensee of the Decade").

**US tariff:** Business Standard 12 Feb 2026 (Welspun Q3 FY26); INDmoney (tariff dates).

**Blocked or unverified:** the Gokaldas QIP article (HTTP 403); Trendlyne returned 429 on first attempts for three names and succeeded on retry; the reasons for six promoter-stake falls were not found.

**Annual reports:** Page Industries 2025-26 only, for the licence and dividend facts above. The checklist of the same date reads the other survivors'.

## Notion block

```
PAGEIND | Page Industries Ltd. | Textiles | B | Candidate | reports/IN/_screens/textiles-full-20260922.md
SIYSIL | Siyaram Silk Mills Ltd. | Textiles (outside Nifty 500) | B | Candidate | reports/IN/_screens/textiles-full-20260922.md
AMBIKCO | Ambika Cotton Mills Ltd. | Textiles (outside Nifty 500) | B | Candidate | reports/IN/_screens/textiles-full-20260922.md
DOLLAR | Dollar Industries Ltd. | Textiles (outside Nifty 500) | B | Candidate | reports/IN/_screens/textiles-full-20260922.md
```
