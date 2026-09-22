# Construction Materials screen — 22 Sep 2026

**Audit: passed.** `report_audit.py` sampled 21 data points (15%, seed 42) on 2026-09-22 after the promoter-pledge update; all 21 re-read from source, 20 exact and one rounding (Shree PE 49x in the final table against 49.4 computed). An earlier pass on the pre-pledge version passed 22 of 22.

## What was screened

- **Universe:** the 11 Nifty 500 companies NSE tags as "Construction Materials", from the official constituent file `ind_nifty500list.csv`. All 11 are cement makers. Under 30 names, so all 11 were screened.
- **Data:** Screener.in consolidated pages read on 2026-09-22 between 00:53 and 01:03 IST (Grasim also standalone, as the holding-company rule requires). Prices from the NSE bhavcopy of 21-Sep-2026. Second source for price, market cap, PE and yield: stockanalysis.com, same night.
- **Cyclical rule applied:** cement is a cyclical, so checks 1, 4 and 6 use ten-year averages (FY2017-FY2026) and checks 2, 3 and 5 use five-year sums (FY2022-FY2026). No single-year figure eliminates anyone.
- **Period quirks handled:** ACC and Ambuja used December year-ends until Dec 2021, then a 15-month period to Mar 2023, then March year-ends. Shree has a 9-month period to Mar 2016. The 15-month period is counted as one period in the five-year sums; that makes ACC and Ambuja's "five years" cover 63 months.
- **Left out:** nothing inside the Nifty 500. Smaller listed cement makers below the Nifty 500 cut were not screened (see "Not screened").
- **Pledge data (check 8):** not readable by script from Screener (login) or BSE (no scriptable page), and the annual reports do not carry the pledge column. It was found later the same night from SEBI takeover-regulation disclosures summarised on the web, for the three names that had passed checks 1-7: UltraTech 0.0% (Jun 2026 quarter, Trendlyne), Shree nil (company declaration under SAST Regulation 31(4), 3 Apr 2026), Ramco 9.46% of equity pledged by the promoter group (24 Jul 2026 disclosure). The eight names eliminated on other checks were not searched and stay NA. Check 8 also records the promoter stake trend over the last 12 quarters (Screener).

### How each check was computed

| # | Check | How |
|---|---|---|
| 1 | 10-year average ROE | net profit / average of opening and closing (equity capital + reserves), each year FY2017-FY2026, then averaged |
| 2 | 5-year cumulative FCF | Screener's Free Cash Flow row summed FY2022-FY2026 |
| 3 | Interest cover | (profit before tax + interest) / interest; latest year, five-year sum-over-sum, and the trough year |
| 4 | Operating margin | Screener OPM %, ten-year average and the worst year |
| 5 | OCF / net profit | five-year cash from operations divided by five-year net profit |
| 6 | Net margin | net profit / sales each year, ten-year average and worst year |
| 7 | Dilution | shares = equity capital / face value; change from the balance sheet five years before the latest one |
| 8 | Pledge / promoter | pledge NA; promoter % from Sep 2023 to Jun 2026 (Screener quarterly shareholding) |

## Summary table

All money in ₹ crore. FCF = five-year sum. Interest cover = latest year unless stated.

| Company | Symbol | 1 ROE (10y avg) | 2 FCF (5y) | 3 Interest cover | 4 OPM (10y avg) | 5 OCF/PAT (5y) | 6 Net margin (10y avg) | 7 Dilution (5y) | 8 Pledge / promoter | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| ACC Ltd. | ACC | ✅ 11.7% | ❌ −2,523 | ✅ 20.3x | ✅ 14.1% | ❌ 0.51 | ✅ 8.9% | ✅ 0.0% | NA / 56.69% → 56.69% | Eliminated |
| Ambuja Cements Ltd. | AMBUJACEM | ✅ 11.8% | ❌ −5,520 | ✅ 15.7x | ✅ 17.0% | ✅ 0.86 | ✅ 11.3% | ❌ +24.4% | NA / 63.19% → 67.33% | Eliminated |
| Dalmia Bharat Ltd. | DALBHARAT | ❌ 4.8% | ❌ −633 | ✅ 4.0x | ✅ 21.3% | ✅ 2.42 | ⚠️ 5.6% | ✅ +2.7% | NA / 55.85% → 55.84% | Eliminated |
| Grasim Industries Ltd. (consolidated) | GRASIM | ✅ 11.1% | ❌ −1,22,937 | ⚠️ 2.0x | ✅ 20.2% | ❌ −1.02 | ✅ 8.1% | ✅ +3.0% | NA / 42.75% → 43.73% | Eliminated |
| Grasim Industries Ltd. (standalone) | GRASIM | ❌ 3.7% | ❌ −8,543 | ❌ 1.5x | ✅ 13.1% | ✅ 1.41 | ✅ 7.2% | same | same | Eliminated |
| India Cements Ltd. | INDIACEM | ❌ 0.2% | ✅ +601 | ❌ 0.3x | ❌ 8.2% | ❌ negative PAT | ❌ 0.1% | ✅ 0.0% | NA / 28.42% → 75.00% (UltraTech took control) | Eliminated |
| J.K. Cement Ltd. | JKCEMENT | ✅ 14.7% | ⚠️ −218 | ✅ 4.4x | ✅ 18.0% | ✅ 2.14 | ✅ 6.8% | ✅ 0.0% | NA / 45.80% → 45.66% | Carried forward, flagged |
| JSW Cement Ltd. | JSWCEMENT | ❌ 2.8% | ❌ −2,418 | ❌ −1.1x | ✅ 16.3% | ❌ negative PAT | ❌ 0.6% | ❌ +36.0% (IPO) | NA / 72.34% → 72.02% | Eliminated, short data window |
| Nuvoco Vistas Corporation Ltd. | NUVOCO | ❌ 1.8% | ✅ +4,837 | ❌ 1.08x (5y) | ✅ 15.3% | ✅ CFO +7,339 (PAT too small for a ratio) | ❌ 1.4% | ✅ +13.3% (IPO) | NA / 71.78% → 72.02% | Eliminated |
| The Ramco Cements Ltd. | RAMCOCEM | ✅ 10.9% | ✅ +630 | ⚠️ 2.82x (5y), 1.7x trough | ✅ 20.9% | ✅ 2.96 | ✅ 9.9% | ✅ 0.0% | ❌ 9.46% of equity pledged (24 Jul 2026) / 42.11% → 42.55% | Eliminated (check 8) |
| Shree Cement Ltd. | SHREECEM | ✅ 12.2% | ✅ +2,743 | ✅ 11.8x | ✅ 24.1% | ✅ 1.95 | ✅ 11.5% | ✅ 0.0% | ✅ nil (declared 3 Apr 2026) / 62.56% → 62.56% | Survived |
| UltraTech Cement Ltd. | ULTRACEMCO | ✅ 11.5% | ✅ +16,181 | ✅ 6.8x | ✅ 20.0% | ✅ 1.64 | ✅ 9.8% | ✅ +2.1% (Kesoram merger) | ✅ 0.0% (Jun 2026) / 59.96% → 59.33% (merger) | Survived |

## Survived (3 after step 1, 2 after step 2)

Step 1 carried three names forward: UltraTech and Shree clean, J.K. Cement flagged. Ramco passed checks 1-7 (check 3 borderline) but fails check 8: its promoter group has 9.46% of the company's equity pledged.

### Step 2 — five value checks

Relaxation used: cement is asset-heavy, so the ROE bar for check 2 was relaxed to "ten-year average above 10%". That relaxed level is my assumption; the method does not fix a number. PE is market cap divided by trailing-twelve-month net profit. "Own range" is the PE at each March year-end FY2017-FY2026, using the official NSE close and that year's profit. Peer median PE is 32.4 across all 11 names.

| Company | 1 Valuation | 2 ROE | 3 Cash flow | 4 Debt (D/E) | 5 Moat | Result |
|---|---|---|---|---|---|---|
| UltraTech | ✅ close — PE 39.4, own range 16.3-56.2, median 40.3; above peer median | ✅ 11.5% (relaxed) | ✅ 1.64 | ✅ 0.31 | ✅ 4 of 5 | **Keep** |
| Shree | ⚠️ PE 49.4, own range 37.0-97.7, median 45.5; far above peers | ✅ 12.2% (relaxed); FY25 5.3%, FY26 7.8% | ✅ 1.95 | ✅ 0.08 | ✅ 3 of 5 | **Keep, amber** |
| J.K. Cement | ❌ PE 41.9, own median 34.9; PB 5.58 is the highest in the sector | ✅ 14.7% | ✅ 2.14 | ❌ 0.88 | ✅ 3 of 5 | **Dropped** (3 of 5) |

Ramco is not in this table because it fails check 8. Two survive, so the moat bar was not raised.

## Eliminated (9)

| Company | Failed check | The number | Why it was dropped |
|---|---|---|---|
| ACC | 2, 5 | FCF FY2022-26 −₹2,523 cr; OCF/PAT 0.51 (CFO ₹4,942 cr vs PAT ₹9,622 cr) | Profit is not turning into cash. FY26 cash from operations was −₹1,364 cr on an operating profit of ₹2,958 cr, and FY26 tax was 1%, so the low PE of 12.3 is not what it looks like. |
| Ambuja Cements | 2, 7 | FCF −₹5,520 cr; shares 198.5 cr (Dec 2020) → 247.0 cr (Mar 2026), +24.4% | Dilution came from the promoter's warrant conversions, cash into the company and not a merger, so the rule as written fails it. FCF negative in three of the last five periods on acquisition-scale capex. Other income of ₹2,646 cr in FY25 and a −71% tax rate in FY26 flatter the net margin. |
| Dalmia Bharat | 1, 2 | ROE ten-year average 4.8%; FCF −₹633 cr | The 2019 restructuring lifted reserves from ₹3,681 cr to ₹10,600 cr, so book ROE has never reached 8%. FCF negative in three of the last four years. |
| Grasim | consolidated 2, 5; standalone 1, 2, 3 | consolidated FCF −₹1,22,937 cr, OCF/PAT −1.02; standalone ROE 3.7%, FCF −₹8,543 cr, FY26 interest cover 1.5x | Consolidated numbers carry Aditya Birla Capital's lending book, so they cannot be read as a cement business. Standalone shows the paints launch: OPM 3.7% (FY25) and 4.3% (FY26); FCF −₹9,273 cr over FY23-FY25, back to +₹605 cr in FY26. The cement exposure is UltraTech, which is screened on its own. |
| India Cements | 1, 3, 4, 5, 6 | ROE 0.2%; interest cover 0.3x; OPM 8.2%; net margin 0.1%; losses in FY23-FY26 | Loss-making for four years. UltraTech took control in Dec 2024 (promoter 28.42% → 75.00%), so it is now an UltraTech turnaround, not a stand-alone business. |
| The Ramco Cements | 8 (and 3 borderline) | Promoter group pledge 2,23,44,489 shares = 9.46% of equity on 24 Jul 2026; Rajapalayam Mills alone 1,91,53,625 shares = 8.11% (8.04% on 25 Mar 2026); group pledge moved 9.09% → 9.39% → 9.19% → 9.46% between 22 and 24 Jul 2026 as pledges were released to Barclays and re-created with Tata Capital | The pledge secures a promoter textile company's borrowing, not Ramco's. Rule 8 fails anything above zero, and it is not falling. Interest cover also troughed at 1.7x in FY25. Re-enters only if the pledge goes to zero. |
| J.K. Cement | step 2: 1, 4 (step 1 flag on 2) | PE 41.9 vs own median 34.9; PB 5.58; D/E 0.88; FCF −₹218 cr | Best ROE (14.7%) and best profit growth (21.4% a year, FY17-FY26) in the sector, but the most expensive on book and the most levered of the four finalists. Re-screen if PE falls toward 30. |
| JSW Cement | 1, 2, 3, 5, 6, 7 | ROE 2.8%; FCF −₹2,418 cr; FY26 loss ₹799 cr; shares +36% at the Aug 2025 IPO | Listed 13 months, seven years of data: short data window. FY26 carried a −₹1,323 cr other-income hit. Too new and too weak to read yet. |
| Nuvoco Vistas | 1, 3, 6 | ROE 1.8%; interest cover 1.08x (5-year); net margin 1.4% | Listed Aug 2021. Loss or near-zero profit in five of the last eight years. Cash flow is real (FCF +₹4,837 cr) but goes to servicing debt. |

## Exempted (0)

No exemption was granted. Considered: JSW Cement and Nuvoco under A (building phase) — both fail the 30% OPM condition (16.3%, 15.3%). Nobody has OPM above 30% (B) or ROE above 20% (C).

## Not screened

| Company | Why |
|---|---|
| Birla Corporation, Star Cement, Heidelberg Cement India, Sagar Cements, Orient Cement, and other listed cement makers | Below the Nifty 500 cut; not in the NSE constituent file this screen uses. The tool printed no "outside Nifty 500" names because the input was the sector tag, not a symbol list. |

## Short analysis — one section per survivor

### UltraTech Cement (ULTRACEMCO)

**The business in one line.** India's largest cement maker by capacity, selling grey cement, white cement (Birla White), ready-mix concrete and building products to dealers, builders and infrastructure contractors, paid at dispatch or on short trade credit (debtor days 25).

**Financial quality.** Sales grew from ₹25,375 cr (FY17) to ₹88,512 cr (FY26), 14.9% a year. Net profit grew from ₹2,714 cr to ₹8,188 cr, 13.1% a year. OPM averaged 20.0% over ten years, between 17% and 26%; FY26 was 19%. ROE averaged 11.5%; FY26 11.1%. Five-year cash from operations was ₹55,239 cr against net profit of ₹33,639 cr (1.64x). FCF was positive in every one of the last five years, ₹16,181 cr in total. The most important change of the last two years: growth switched from building to buying. Borrowings jumped from ₹11,403 cr (Mar 2024) to ₹24,102 cr (Mar 2025) for Kesoram's cement business and India Cements. Interest cost nearly doubled, ₹968 cr to ₹1,872 cr. Fixed assets rose from ₹62,878 cr to ₹98,794 cr. FCF thinned to ₹1,723 cr in FY25 and recovered to ₹5,805 cr in FY26.

**Moat.** Scale and cost advantage, plus limestone leases as a resource barrier. Evidence: the highest OPM floor among the large names (17% in its worst year, when Ramco fell to 14% and ACC to 9%), and its profit compounded at 13.1% a year while Shree's and Ramco's stood still. Widening: it is the consolidator. The flip side is that India Cements is loss-making (OPM −8% in FY25) and has to be fixed.

**Top 3 risks.** (1) Acquisitions bought near the top of the cycle: returns on Kesoram and India Cements are unproven and India Cements still loses money. (2) A price war with Adani's Ambuja-ACC. Sector margins are near a ten-year low and UltraTech cannot set prices alone. (3) Leverage and dilution creep: D/E 0.31 is fine, but borrowings doubled in a year and shares rose 2.1% for the Kesoram merger.

**Valuation now.** PE 39.4 on TTM profit (own ten-year year-end range 16.3-56.2, median 40.3; peer median 32.4). PB 4.27 (own range 2.40-4.80, median 4.13). Dividend yield 2.16%: UltraTech paid ₹240 per share for FY26 (ex-date 30 Jul 2026, stockanalysis dividend history; Screener payout 87%), against ₹77.50 for FY25. Stockanalysis's headline yield of 0.70% is stale and was rejected. Whether ₹240 repeats is a question for the deep read. Market cap: Screener ₹3,37,639 cr, stockanalysis ₹3,24,000 cr, price × balance-sheet shares (₹11,100 × 29.5 cr) ₹3,27,450 cr; the last one is used. One word: **fair** against its own history; among peers only Shree and J.K. Cement trade higher.

**Into the final three?** Yes. The only company of eleven that passed all seven computable checks without a flag while compounding profit at 13.1% a year.

### Shree Cement (SHREECEM)

**The business in one line.** North and East India's low-cost cement maker (Bangur, Rockstrong, Roofon brands), selling grey cement through dealers, paid on dispatch; it also sells surplus power from captive plants.

**Financial quality.** Sales grew from ₹8,594 cr (FY17) to ₹20,943 cr (FY26), 10.4% a year. Net profit grew from ₹1,339 cr to ₹1,749 cr, 3.0% a year: nine years of volume growth produced almost no profit growth. OPM was 29-30% in FY17, FY20 and FY21 and has been 17-22% since FY23; the ten-year average of 24.1% is still the highest in the set. ROE averaged 12.2% but was 5.3% in FY25 and 7.8% in FY26. Cash is strong: five-year CFO ₹17,298 cr against PAT ₹8,875 cr (1.95x); FCF positive in four of five years, ₹2,743 cr in total. Borrowings ₹1,868 cr against equity ₹23,267 cr, D/E 0.08; net debt to EBITDA −1.5x (stockanalysis), so it is net cash. The most important change of the last two years: the cost edge over UltraTech has closed. Shree's OPM (20-22%) now sits 1-3 points above UltraTech's (17-19%), against an 8-point gap in FY20-21. Depreciation jumped to ₹3,007 cr in FY25 from ₹1,897 cr and halved FY25 EPS. The stock fell from ₹30,503 (28 Mar 2025 close) to ₹22,550.

**Moat.** Cost advantage from energy-efficient plants, split grinding units and captive power, plus limestone reserves. Evidence: highest ten-year OPM in the sector. Narrowing: the margin gap to the leader has shrunk, and ROIC fell to 4.8% in FY25 (stockanalysis) before recovering to 8.8% in FY26.

**Top 3 risks.** (1) Profit has not grown in nine years; 49x earnings pays for a margin recovery that may not come. (2) Capital allocation: about ₹3,700 cr a year of investing outflow in FY25 and FY26 at falling returns; the balance sheet is safe but the money is not compounding. (3) Regional: North India pricing has been the sector's weak spot, and new Adani and UltraTech capacity lands in its markets.

**Valuation now.** PE 49.4 (own ten-year year-end range 37.0-97.7, median 45.5; peer median 32.4). PB 3.50 (own range 3.56-7.77, median 5.08): the bottom of its own ten-year PB range. Dividend yield 0.67%. One word: **expensive** on earnings; on book value it is the cheapest it has been in ten years.

**Into the final three?** Yes, as the moderate-certainty name. The balance sheet is certain; the margin recovery is not. Amber because of valuation.

### The Ramco Cements (RAMCOCEM)

*Eliminated on check 8 after the pledge data arrived. The analysis below was written before that and its numbers stand.*

**The business in one line.** South India's regional cement maker (Tamil Nadu, Andhra Pradesh, Karnataka, Kerala, Odisha), selling grey cement and dry-mix products through dealers, paid on dispatch.

**Financial quality.** Sales grew from ₹3,967 cr (FY17) to ₹9,029 cr (FY26), 9.6% a year. Net profit went from ₹664 cr to ₹699 cr, 0.6% a year, essentially zero. OPM was 30% in FY17 and 29% in FY21; it has been 14-17% since FY23; the ten-year average is 20.9%. ROE averaged 10.9%; FY23-FY25 were 4.7%, 5.1% and 3.7%; FY26 9.0%, but FY26 other income was ₹595 cr against a normal ₹25-40 cr, so most of the FY26 profit did not come from cement. Interest cover: 1.7x in FY25, 2.82x over five years, 3.1x in FY26. Cash: five-year CFO ₹7,455 cr against PAT ₹2,522 cr (2.96x). FCF was negative in FY22-FY24 during the expansion (−₹1,044 cr over the three years) and turned positive: ₹458 cr in FY25 and ₹1,216 cr in FY26. Borrowings peaked at ₹4,936 cr (Mar 2024) and are ₹3,871 cr (Mar 2026); D/E 0.48. The most important change: the capex cycle ended and debt started falling, helped by asset sales that show up as other income.

**Moat.** Regional scale and limestone reserves in the South, brand strength in Tamil Nadu and Kerala. Evidence: OPM held at 14% in its worst year and it never made a loss in ten years. Narrowing: the South is India's most oversupplied region, and Ramco's OPM fell more from peak to trough than UltraTech's or Shree's.

**Top 3 risks.** (1) Earnings quality: TTM other income is ₹608 cr of ₹797 cr profit before tax. (2) The interest cover trough of 1.7x in FY25: one more bad pricing year in the South and check 3 fails outright. (3) Leverage: net debt to EBITDA 2.6x (stockanalysis), the highest of the three survivors.

**Valuation now.** PE 32.4 on reported TTM profit (own ten-year year-end range 20.3-79.7, median 31.1; peer median 32.4). Screener shows 110; it strips out the one-off income, and that is the truer number for the cement business. PB 2.58 (own range 2.46-4.25, median 2.84). Dividend yield 0.28%. One word: **expensive** on core earnings.

**Into the final three?** No. It fails check 8: promoter group pledge of 9.46% of equity (24 Jul 2026), rotating between lenders. It would re-enter only if the pledge goes to zero, and then only with two quarters of OPM above 18%, other income back at ₹30-40 cr, and borrowings under ₹3,500 cr.

## The final three

Two names earned a deep read. The sector cannot fill three honestly: the third candidate, Ramco, failed check 8 on promoter pledge once the pledge data arrived, and J.K. Cement fell on price and debt.

| Company | Type | Why it is here | Main risk | What would change my mind |
|---|---|---|---|---|
| UltraTech Cement | high-certainty compounder | Only clean pass of 11; profit compounded 13.1% a year for nine years; the sector's consolidator; FCF positive every year | Acquisitions bought near the cycle top, India Cements still loss-making, borrowings doubled in FY25 | Two years of ROCE below 10% after the acquisitions, or FCF negative two years running |
| Shree Cement | moderate-certainty recovery | Highest long-run OPM (24.1%), net cash, PB at the bottom of its own ten-year range | Paying 49x for a business whose profit has not grown in nine years | OPM back above 25% for a full year lifts it; a third year below 20% drops it |
| (no third name) | — | Ramco removed: promoter group pledge 9.46% of equity (Jul 2026) | — | Ramco re-enters only at zero pledge |

## Sector verdict

Pass rate 2/11 after both steps (3/11 after the eight hard checks). Indian cement is consolidating into UltraTech, Adani's Ambuja-ACC and the regionals while margins sit near a ten-year low: two of the three names that passed the hard checks grew profit slower than sales over nine years, and only UltraTech did so while passing every check. Worth more time only for a margin-recovery thesis on UltraTech and Shree; everything else here is a bet on regional pricing.

## Information grade

| Area | Grade | Note |
|---|---|---|
| Company financials | A | Ten to twelve years from Screener for every name; five-year ratios cross-checked against stockanalysis and they agree. The ACC and Ambuja 15-month periods are handled, not smoothed. |
| Valuation freshness | A | Official NSE close of 21-Sep-2026; Screener and stockanalysis read the same night; the ten-year PE range is built from official NSE year-end closes. UltraTech's market cap and dividend yield disagreed across sources; both are resolved in the text, not averaged. On first pass I used the wrong yield (0.70%); the ₹240 FY26 dividend in stockanalysis's own history table settles it at 2.16%. |
| Competitive picture | B | Moat ratings are judgment backed by margin data only. No capacity or market-share figures are used, because none was taken from a primary source. |
| Management | B | Promoter pledge is known for the three names that passed checks 1-7 (web summaries of SEBI disclosures, not the filings themselves) and NA for the eight eliminated on other checks. No annual report was opened for the screen; the checklist of the same date reads the FY2026 reports. |

## Sources

**NSE**
- Nifty 500 constituent file: https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv (sector universe and industry tags)
- Daily bhavcopy, 21-Sep-2026 (closes, volume, delivery %): https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_21092026.csv
- Year-end closes for the ten-year PE range: sec_bhavdata_full for 31-Mar-2020, 31-Mar-2021, 31-Mar-2022, 31-Mar-2023, 29-Mar-2024, 28-Mar-2025, 31-Mar-2026; and the older archive https://nsearchives.nseindia.com/content/historical/EQUITIES/{YYYY}/MAR/cm{DD}MAR{YYYY}bhav.csv.zip for 31-Mar-2017, 28-Mar-2018, 29-Mar-2019

**Screener.in** (consolidated pages, read 2026-09-22 00:53-01:03 IST): P&L, balance sheet, cash flow, ratios, shareholding for all 11 — https://www.screener.in/company/{SYMBOL}/consolidated/ ; plus https://www.screener.in/company/GRASIM/ (standalone). Every check-1 to check-8 figure comes from these pages.

**stockanalysis.com** (read 2026-09-22): quote pages https://stockanalysis.com/quote/nse/{SYMBOL}/ for the two-source price, market cap, PE and yield check on all 11; ratio pages https://stockanalysis.com/quote/nse/{SYMBOL}/financials/ratios/ for UltraTech, Shree, Ramco and J.K. Cement (five-year PE, PB, ROE, ROIC, net debt to EBITDA, payout).

**Annual reports:** none opened for this screen. **News:** none used.

**Promoter pledge (web summaries of SEBI SAST disclosures, read 2026-09-22):** UltraTech 0.0% pledged, Jun 2026 quarter — https://trendlyne.com/equity/share-holding/1443/ULTRACEMCO/latest/ultratech-cement-ltd/ ; Shree nil encumbrance in FY2025-26, Regulation 31(4) declaration of 3 Apr 2026 — https://scanx.trade/stock-market-news/companies/shree-cement-promoters-report-no-share-encumbrance-in-fy26/42269325 ; Ramco: Rajapalayam Mills pledge of 6,32,000 shares to Tata Capital, 24 Jul 2026, group encumbrance 2,23,44,489 shares = 9.46% — https://scanx.trade/stock-market-news/companies/rajapalayam-mills-pledges-6-32-lakh-ramco-cements-shares-to-tata-capital/46503184 ; release of 4,70,000 shares to Barclays the same day — https://scanx.trade/stock-market-news/companies/rajapalayam-mills-releases-pledge-on-4-7-lakh-ramco-cements-shares/46501280 ; event list — https://scanx.trade/stock-news/ramco-cements-ltd

Two-source gaps over 1% found by `india_data.py crosscheck` and how they were resolved: UltraTech market cap 4.0% (used price × balance-sheet shares), UltraTech dividend yield 67.6% (used Screener 2.16%; stockanalysis's dividend history shows the ₹240 FY26 payout that its headline yield misses), Ramco PE 71% (both figures reported, reason explained), Ambuja market cap 1.6% and PE 7.8%, Dalmia PE 17.6%, India Cements PE 45.6%, J.K. Cement PE 2.7%, JSW Cement market cap 1.6%, Nuvoco PE 7.6% — all on eliminated names except J.K. Cement, where the computed 41.9 is used.

## Notion block

```
ULTRACEMCO | UltraTech Cement Ltd. | Construction Materials | B | Candidate | reports/IN/_screens/construction-materials-20260922.md
SHREECEM | Shree Cement Ltd. | Construction Materials | B | Candidate | reports/IN/_screens/construction-materials-20260922.md
```
