# Capital markets screen — 24 Sep 2026

1. **What was looked at:** 17 Indian companies that make money from people investing — stock and commodity exchanges, the two share depositories, mutual fund houses, the firms that keep mutual fund records, a bond-rating firm, and brokers.
2. **What came out:** ten came through: BSE, MCX, IEX, CDSL, CAMS, KFin, CRISIL, HDFC AMC, ICICI AMC and Nippon AMC. Four brokers failed because the cash they lend to clients leaves the business, one firm because its owners have pawned shares for loans, and two on cash or price. The three picked for a closer study: **CRISIL** (a steady rating and research firm, fairly priced), **CAMS** (keeps the records for two-thirds of India's mutual fund money, near the cheapest it has been), and **IEX** (the power exchange, the cheapest it has ever been, because a new rule may take away its lead).
3. **What Shivay does now:** nothing for the screen itself — the three deep reads ran tonight. The broker question is decided: no rule of their own (24 Sep 2026, `CLAUDE.md`).

**Universe: the 17-name Capital markets theme in `data/themes-in.json`.** All 17 are in the Nifty 500. All 17 were screened.

**Audit: passed.** `report_audit.py` sampled 30 of 221 data points (15%, seed 42) on 2026-09-24 after the last edit; all 30 re-read and matched within 1%. Be clear about what that proves: 12 of the 30 were star scores, check counts or read times, which only confirm the report agrees with itself. The other 18 were re-read from the saved Screener pages; only 3 of those (two PEs and ICICIAMC's share count) also had a second, independent source.

## What was screened

- **Universe:** `india_data.py universe --theme "Capital markets"`, 17 names. There is no NSE industry called Capital markets (all 17 sit under Financial Services), so the theme is the universe.
- **The list changed tonight, and Shivay chose it.** The wrong symbol CAMSBANKING was fixed to CAMS. IIFL Finance was removed, because it is a gold-loan lender, not a capital-markets business. Eight names were added: HDFCAMC, ICICIAMC, NAM-INDIA, UTIAMC, ABSLAMC, ANANDRATHI, CRISIL and IEX.
- **Under 30 names**, so nobody was left out on size. **Nothing outside the Nifty 500**, so the Not screened list is empty.
- **Data:** Screener.in pages, consolidated (`.c`) and standalone (`.s`), read 2026-09-24 00:23-00:24 IST and kept in `local/capmkt-20260924/`. Prices: NSE bhavcopy 23-Sep-2026. Second source for price, market cap, PE and yield: stockanalysis.com via `crosscheck`, read 2026-09-24 00:38 IST.
- **Own PE range:** Screener's price-to-earnings chart, weekly points, up to ten years (from listing for younger companies). Points where Screener did not adjust EPS for a bonus issue were dropped; the names are listed under step 2.
- **ROE bar:** 8% for all 17. None is in the asset-heavy list.

### Which figures were used — an assumption, not a decided rule

Consolidated when it has 10 years. When consolidated has fewer, standalone is used if standalone has 10 years and its sales are at least 85% of consolidated sales. Otherwise consolidated, labelled "short data window".

| Basis | Names | Why |
|---|---|---|
| Consolidated, 10 years | BSE, MCX, CDSL, CRISIL, NAM-INDIA, UTIAMC, ABSLAMC, ANGELONE, MOTILALOFS | the default |
| Standalone, 10 years | IEX (standalone sales 99% of consolidated), CAMS (93%), HDFCAMC (100%), ANANDRATHI (96%) | consolidated has only 4-9 years |
| Consolidated, short data window | KFINTECH (8 years; standalone also has only 9), NUVAMA (7 years; standalone sales are 26% of consolidated), 360ONE (9 years; standalone 17%) | standalone would hide most of the business |
| Standalone only, short data window | ICICIAMC, 6 years (FY2021-FY2026) | Screener's consolidated page has only FY2024-FY2025 |

### How each check was computed

Same method as the 23 Sep Defence screen.

| # | Check | How |
|---|---|---|
| 1 | 10-year average ROE | net profit / average of opening and closing (equity capital + reserves), each year, then averaged |
| 2 | 5-year cumulative FCF | Screener's Free Cash Flow row summed over the last five years |
| 3 | Interest cover | (profit before tax + interest) / interest, last year. "No interest" = no interest cost, a pass |
| 4 | Operating margin | Screener OPM %, ten-year average |
| 5 | OCF / net profit | five-year cash from operations / five-year net profit |
| 6 | Net margin | net profit / sales each year, ten-year average |
| 7 | Dilution | equity capital, last year against five years earlier. Where a bonus or split moved the capital, the share count from net profit / EPS is used instead, and the row says so |
| 8 | Pledge / promoter | pledge from Trendlyne's shareholding page for the names that passed checks 1-7; promoter % Sep 2023 → Jun 2026 from Screener. Names eliminated on checks 1-7 were not searched and stay NA |

CRISIL's financial year ends in December, so its "last year" is Dec 2025.

**One fix to tonight's `step1.py`.** CRISIL's balance sheet carries an extra half-year column (Jun 2026) that its profit and loss table does not. The script matched years by position, so each ROE year used the next year's equity. Fixed by dropping that column. CRISIL's ten-year ROE moves from 27.3% to 30.8%. No other name has the problem, and no other number changed.

### Dilution checked by hand

Screener's EPS is not always adjusted for bonus issues, so three capital jumps were checked in the offer documents.

| Company | Capital move | What it was | Source | Real dilution |
|---|---|---|---|---|
| ABSLAMC | ₹18 cr → ₹144 cr, FY2022 | face value split ₹10 → ₹5 (1.80 cr → 3.60 cr shares), then a **7-for-1 bonus** allotted 9 Apr 2021 (25.20 cr new shares, 28.80 cr in total). The Oct 2021 IPO was all existing shares sold by the promoters | Red herring prospectus, Sep 2021, pages 26, 72 and 84 (BofA copy) | none. 28.80 cr (Apr 2021) → 28.88 cr (FY2026, profit / EPS) = **+0.3%**, ESOPs |
| ICICIAMC | ₹18 cr → ₹49 cr, FY2026 | face value split ₹10 → ₹1 (1.765 cr → 17.65 cr shares), then a **1.8-for-1 bonus** (to 49.43 cr shares). The Dec 2025 IPO was all shares sold by Prudential | DRHP as reported by HDFC Sky (17.65 cr → 49.42 cr shares, 1.8:1); Chittorgarh IPO page (49,42,58,520 shares before and after the IPO, offer for sale only) | none. 1.765 × 10 × 2.8 = 49.42 cr, equal to FY2026 profit / EPS. **0.0%** |
| ANANDRATHI | ₹14 cr → ₹21 cr, FY2022 | **1-for-2 bonus**, 13,872,087 shares allotted 16 Jul 2021. Also two ESOP allotments in Jun 2021 (178,560 and 52,020 shares) | Red herring prospectus, 26 Nov 2021, page 83 (NSE archive) | the ESOPs only |
| ANANDRATHI | ₹21 cr → ₹42 cr, FY2025 | **1-for-1 bonus**, record date 5 Mar 2025. A further 1-for-1 bonus had record date 3 Jun 2026 | Trendlyne bonus history; Business Standard, 5 Mar 2025 | none. Share count on Screener's EPS, adjusted for the 2021 bonus: 16.43 cr → 16.58 cr = **+0.9%** |

## Summary table

All money in ₹ crore. ⚑ = promoter stake fell; see the note under the table (a flag, not a fail).

| Company | Symbol | 1 ROE (10y avg) | 2 FCF (5y) | 3 Interest cover | 4 OPM (10y avg) | 5 OCF/PAT (5y) | 6 Net margin (10y avg) | 7 Dilution (5y) | 8 Pledge / promoter | Result |
|---|---|---|---|---|---|---|---|---|---|---|
| BSE Ltd. | BSE | ✅ 17.4% | ✅ 6,494 | ✅ 98.4x | ✅ 40.8% | ✅ 1.48 | ✅ 41.3% | ✅ +2.4% share count (capital +811% is bonus issues) | ✅ no promoter | Survived |
| Multi Commodity Exchange of India Ltd. | MCX | ✅ 18.0% | ✅ 4,495 | ✅ no interest | ✅ 39.5% | ✅ 2.19 | ✅ 44.4% | ✅ 0.0% | ✅ no promoter | Survived |
| Indian Energy Exchange Ltd. | IEX | ✅ 44.7% | ✅ 1,865 | ✅ 313.5x | ✅ 81.7% | ✅ 1.05 | ✅ 69.2% | ✅ −0.3% share count (capital +196.7% is the FY2022 bonus) | ✅ no promoter | Survived |
| Central Depository Services (India) Ltd. | CDSL | ✅ 23.8% | ✅ 1,349 | ✅ no interest | ✅ 56.3% | ✅ 0.97 | ✅ 52.6% | ✅ −0.5% share count (capital +101% is the FY2025 bonus) | ✅ 0.0% (Jun 2026) / 15.0% → 15.0% | Survived |
| Computer Age Management Services Ltd. | CAMS | ✅ 40.6% | ✅ 1,659 | ✅ 98.3x | ✅ 40.7% | ✅ 1.14 | ✅ 28.3% | ✅ +2.0% | ✅ no promoter now / 19.87% → 0.0% ⚑ | Survived |
| KFin Technologies Ltd. | KFINTECH | ✅ 14.3% (8 years) | ✅ 1,115 | ✅ 94.6x | ✅ 41.6% | ✅ 1.21 | ✅ 16.2% | ✅ +14.6% | ✅ 0.0% (Jun 2026) / 49.12% → 22.82% ⚑ | Survived, short data window |
| CRISIL Ltd. | CRISIL | ✅ 30.8% | ✅ 2,850 | ✅ 48.3x | ✅ 27.4% | ✅ 1.01 | ✅ 19.9% | ✅ 0.0% | ✅ 0.0% (Jun 2026) / 66.66% → 66.64% | Survived |
| HDFC Asset Management Company Ltd. | HDFCAMC | ✅ 32.8% | ✅ 8,521 | ✅ 286.4x | ✅ 73.8% | ✅ 0.86 | ✅ 53.7% | ✅ +0.6% share count (capital +101.9% is the FY2026 bonus) | ✅ 0.0% (Jun 2026) / 52.55% → 52.34% | Survived |
| ICICI Prudential Asset Management Company Ltd. | ICICIAMC | ✅ 77.5% (6 years) | ✅ 9,708 | ✅ 245.8x | ✅ 74.7% | ✅ 0.94 | ✅ 54.5% | ✅ 0.0% (split and bonus, see above) | ✅ 0.0% (Mar 2026) / 87.59% → 87.59% | Survived, short data window |
| Nippon Life India Asset Management Ltd. | NAM-INDIA | ✅ 24.2% | ✅ 3,962 | ✅ 282.7x | ✅ 57.2% | ✅ 0.86 | ✅ 42.1% | ✅ +3.6% | ✅ 0.0% (Jun 2026) / 73.47% → 71.80% ⚑ | Survived |
| Aditya Birla Sun Life AMC Ltd. | ABSLAMC | ✅ 30.8% | ✅ 3,065 | ✅ 254.2x | ✅ 56.3% | ✅ 0.81 | ✅ 39.8% | ✅ +0.3% (split and bonus, see above) | ✅ 0.0% (Jun 2026) / 86.48% → 74.72% ⚑ | Survived step 1, dropped at step 2 |
| Anand Rathi Wealth Ltd. | ANANDRATHI | ✅ 41.4% | ✅ 1,044 | ✅ 33.9x | ✅ 38.6% | ✅ 0.94 | ✅ 24.2% | ✅ +0.9% (bonuses, see above) | ❌ **13.83% of promoter holding pledged** (Jun 2026) / 48.69% → 41.37% | Eliminated (check 8) |
| UTI Asset Management Company Ltd. | UTIAMC | ✅ 15.7% | ✅ 1,740 | ✅ 51.2x | ✅ 50.8% | ❌ 0.65 | ✅ 37.0% | ✅ +1.6% | NA / no promoter | Eliminated |
| Angel One Ltd. | ANGELONE | ✅ 27.8% | ❌ −5,590 | ✅ 3.9x | ✅ 31.6% | ❌ −1.05 | ✅ 18.9% | ✅ +11.0% | NA / 38.26% → 28.59% | Eliminated |
| Motilal Oswal Financial Services Ltd. | MOTILALOFS | ✅ 21.5% | ❌ −7,981 | ✅ 2.9x | ✅ 47.8% | ❌ −0.80 | ✅ 23.5% | ✅ +2.4% share count (capital +300% is the FY2025 bonus) | NA / 69.53% → 67.20% | Eliminated |
| Nuvama Wealth Management Ltd. | NUVAMA | ✅ 19.5% (7 years) | ❌ −8,602 | ✅ 2.4x | ✅ 46.9% | ❌ −2.19 | ✅ 18.6% | ✅ +2.9% | NA / 56.19% → 53.98% | Eliminated, short data window |
| 360 ONE WAM Ltd. | 360ONE | ✅ 17.2% (9 years) | ❌ −6,580 | ✅ 2.4x | ✅ 60.1% | ❌ −1.46 | ✅ 24.9% | ✅ +15.6% share count (capital +127.8% includes a bonus) | NA / 20.84% → 6.20% | Eliminated, short data window |

**Promoter changes (check 8).**
- **CAMS ⚑** — the promoter, Great Terrain (Warburg Pincus), sold its whole 19.87% on 4 Dec 2023 at ₹2,766.47 a share, about ₹2,700 cr. CAMS has had no promoter since. No formal SEBI reclassification was found. The seller gave no reason; a private-equity fund leaving is the plain reading.
- **KFINTECH ⚑** — General Atlantic, still classed as promoter, sold about 5.8% in May 2024, 10% in May 2025 and 8.75% on 20 Aug 2026 at ₹925, taking it to about 13.14%. No reason was stated. Screener's 22.82% for Jun 2026 does not match the 21.89% reported just before the August sale; the gap is not explained.
- **NAM-INDIA ⚑** — 73.47% → 71.80%, a small fall every quarter. Five staff-option allotments are on record in 2026 and no sale by Nippon Life was found. The Sep 2023 share count was not found, so it is not proven that dilution alone explains the fall.
- **ABSLAMC ⚑** — 86.48% → 74.72%. The reason was not checked, because the name left at step 2.
- **ICICIAMC** — unchanged at 87.59% through Jun 2026. After that, Prudential sold 2% in late Aug 2026 at ₹3,065 a share. Stated reason: the minimum public shareholding rule. The promoter group is now about 85.60%.
- **HDFCAMC** — 52.55% → 52.34%, in step with staff-option allotments. No sale by HDFC Bank was found. Not flagged.
- **BSE, MCX, IEX** have no promoter, so there is nothing to pledge. UTI AMC has none either.

## Survived (11 after step 1, 10 after step 2)

Step 1 carried twelve names forward: the twelve that passed checks 1-7. Anand Rathi then fails check 8, leaving eleven for step 2.

### Step 2 — five value checks

Peer median PE, all 17 names: **36.3x**. PE is Screener's (consolidated page, standalone for ICICIAMC), with stockanalysis as the second source; gaps over 1% are under the table.

| Company | 1 Valuation | 2 ROE | 3 Cash flow (OCF/PAT, 5y) | 4 Debt (D/E) | 5 Moat | Passed |
|---|---|---|---|---|---|---|
| BSE | ✅ PE 47.1, own range 5.5-106.2, own median 31.6 — 49% above it; above the peer median; PEG 0.61 on five-year profit growth of 77.3% (high-grower relaxation) | ✅ 17.4%; FY2024-26: 25.7% → 34.2% → 44.8% | ✅ 1.48 | ✅ 0.00 | ✅ 4 | **5 of 5, keep** |
| MCX | ✅ PE 55.8, own range 21.7-255.7, own median 42.8 — 30% above it; PEG 1.31 on five-year profit growth of 42.7% (high-grower relaxation) | ✅ 18.0%; FY2026 56.3% | ✅ 2.19 | ✅ 0.00 | ✅ 4 | **5 of 5, keep** |
| IEX | ✅ PE 19.8, own range 19.9-104.9 (since 2019), own median 38.2 — at the bottom of its own range; below the peer median | ✅ 44.7%; FY2026 39.4% | ✅ 1.05 | ✅ 0.01 | ✅ 3, narrowing | **5 of 5, keep** |
| CDSL | ❌ PE 59.9, own range 16.5-76.2, own median 42.8 — 40% above it; above the peer median; PEG 3.37 on five-year profit growth of 17.8% | ✅ 23.8%; FY2026 24.5% | ✅ 0.97 | ✅ 0.00 | ✅ 4 | **4 of 5, keep ⚠** — price: 40% above its own median |
| CAMS | ✅ PE 36.3, own range 33.7-96.6 (since 2020 listing), own median 42.8 — 15% below it; at the peer median | ✅ 40.6%; FY2026 38.9% | ✅ 1.14 | ✅ 0.04 | ✅ 4 | **5 of 5, keep** |
| KFINTECH | ✅ PE 44.9, own range 27.1-86.6 (since Dec 2022 listing), own median 50.2 — 11% below it | ❌ 14.3% eight-year average, against 15%; FY2024-26: 24.5% → 26.1% → 22.3%, not a rise | ✅ 1.21 | ✅ 0.03 | ✅ 3 | **4 of 5, keep ⚠** — ROE: 14.3% against 15%, a narrow miss that comes from the FY2021 loss year |
| CRISIL | ✅ PE 38.0, own range 23.8-66.7, own median 45.2 — 16% below it; near the peer median | ✅ 30.8%; FY2023-25: 33.1% → 28.8% → 27.4% | ✅ 1.01 | ✅ 0.10 | ✅ 4 | **5 of 5, keep** |
| HDFCAMC | ✅ PE 35.8, own range 25.6-66.8 (since 2018 listing), own median 41.0 — 13% below it; below the peer median | ✅ 32.8%; FY2026 32.9% | ✅ 0.86 | ✅ 0.00 | ✅ 3 | **5 of 5, keep** |
| ICICIAMC | ❌ PE 45.1; own range NA (listed 19 Dec 2025, and Screener's PE series is broken until Jun 2026 by the bonus); above the peer median and above HDFC AMC's 35.8; PEG 2.10 on five-year profit growth of 21.5% | ✅ 77.5% (6 years); FY2026 85.8% | ✅ 0.94 | ✅ 0.00 | ✅ 3 | **4 of 5, keep ⚠** — price: PE 45.1 against a peer median of 36.3 and PEG 2.10 |
| NAM-INDIA | ❌ PE 45.5, own range 18.3-50.8, own median 32.8 — 39% above it; above the peer median; PEG 2.59 on five-year profit growth of 17.6% | ✅ 24.2%; FY2024-26: 29.5% → 31.4% → 34.5% | ✅ 0.86 | ✅ 0.02 | ✅ 3 | **4 of 5, keep ⚠** — price: 39% above its own median |
| ABSLAMC | ❌ PE 29.4, own range 14.5-34.9 (since Apr 2022), own median 21.2 — 39% above it; PEG 2.24 on five-year profit growth of 13.1% | ✅ 30.8%; FY2026 25.1% | ✅ 0.81 | ✅ 0.02 | ❌ 2 — market share falling: 7.7% of mutual fund assets (excluding ETFs) in Q4 FY2023 to 6.02% at 31 Mar 2026 | **3 of 5, dropped** |

**The valuation bar, an assumption and not a decided rule.** The method says "PE reasonable against its own 10-year range and its peers", relaxed for a high grower with PEG below 1.5. This screen used: **pass when the PE is at or below its own median, or when PEG is below 1.5**; fail otherwise. The peer median is shown for context. PEG uses five-year profit growth, or three-year growth when the five-year start is a loss or fell more than 10% on the year before (KFINTECH, FY2021 loss; Anand Rathi, FY2021 fell 38%, though it left at check 8).

**What the valuation bar lets through.** BSE and MCX pass only on PEG. Their five-year profit growth (77% and 43% a year) comes from a boom in options trading that SEBI has been acting to cool. A bar that reads "high grower" off the last five years treats that boom as if it lasts. This is written down so the reading can be changed, not because the screen changed it.

**Own PE ranges repaired.** Screener's PE series used EPS not yet adjusted for a bonus in three cases, which gives impossible PEs of 0.7-5.2x. Dropped: ABSLAMC, 28 points from Oct 2021 to 22 Apr 2022; NAM-INDIA, 37 points from Nov 2017 to Jul 2018; ICICIAMC, 107 points from Dec 2025 to May 2026 — which leaves only four months, so ICICIAMC's own range is NA. HDFC AMC's range uses the standalone series (from its Aug 2018 listing), because the consolidated series starts only in 2023.

**Moat stars** are a judgement from the evidence in each short analysis below. ABSLAMC is the only name marked below 3.

**Keep rule.** 4 of 5 keeps with a ⚠ flag, whether the fifth failed narrowly or clearly (`CLAUDE.md`, decided 23 Sep). Ten survive, under 12, so the moat bar was not raised.

## Eliminated (7)

| Company | Failed check | The number | Why it was dropped |
|---|---|---|---|
| Anand Rathi Wealth | 8 | 13.83% of promoter holding pledged, Jun 2026 (11.42% Mar 2026; 0.01% Dec 2025) | a pledge above zero is a hard fail. Passed checks 1-7 cleanly. The promoters' own filings confirm it: the promoter company Anand Rathi Financial Services had 25.60% of its shares encumbered, pledged with Yes Bank "for availing margin limits" (disclosures of 29 May-10 Jun 2026) |
| Aditya Birla Sun Life AMC | step 2 | PE 29.4 vs own median 21.2; moat 2 stars | 3 of 5 value checks |
| UTI AMC | 5 | OCF / profit 0.65 (standalone 0.69) | profit not fully collected as cash; the 0.7 bar is missed on both bases |
| Angel One | 2, 5 | FCF −₹5,590 cr; OCF / profit −1.05 | cash goes out as margin loans to clients |
| Motilal Oswal | 2, 5 | FCF −₹7,981 cr; OCF / profit −0.80 | cash goes out as margin loans and the lending arm's loans |
| Nuvama | 2, 5 | FCF −₹8,602 cr; OCF / profit −2.19 | cash goes out as client margin and loans |
| 360 ONE | 2, 5 | FCF −₹6,580 cr; OCF / profit −1.46 | cash goes out as loans to clients |

**The four brokers and wealth firms.** Angel One, Motilal Oswal, Nuvama and 360 ONE fail checks 2 and 5 for the same reason a lender does: the money they lend to clients (margin funding, loans against shares) leaves through operating cash flow. The lender rule in `CLAUDE.md` covers banks and NBFCs only. These four are brokers or wealth managers, so the rule was applied as written and they are eliminated. Shivay decided on 24 Sep 2026 that brokers get no rule of their own (`CLAUDE.md`), so the elimination stands. The overnight summary has a table of what each would have scored if judged like a lender.

## Exempted (0)

No exemption applied. None of the eliminated names was a candidate: exemptions A, B and C cover checks 1, 4 and 6, and no name failed those.

## Not screened (0)

All 17 were screened.

## Short analysis — one section per survivor

Money in ₹ crore. Growth is five years, FY2021 to FY2026 (CRISIL: CY2020 to CY2025), on the basis the checks used. "Q1 FY27" is Apr-Jun 2026. Facts not from Screener carry their source in the Sources section.

### BSE

**The business in one line.** A stock exchange. It earns a fee on every trade, most of it now on Sensex options; also listing fees, the StAR mutual fund platform and interest on its cash.

**Financial quality.** Sales ₹630 cr → ₹5,124 cr, 52.1% a year. Profit ₹142 cr → ₹2,487 cr, 77.3% a year. Operating margin 45% → 58% → 68% over FY2024-26. ROE 44.8% in FY2026. The change that matters: equity derivatives were about 68% of Q1 FY27 revenue, and BSE's share of options premium went from about 3% in FY2024 to about 31.5% in Apr-Jun 2026 (worked out from NSE's own prospectus figures).

**Moat.** Licence plus network effect: an exchange licence is scarce, and traders go where the other traders are. Widening fast, because BSE took share from NSE after SEBI allowed one weekly expiry per exchange. 4 stars.

**Top 3 risks.** 1) SEBI acting on options: a higher securities tax from 1 Apr 2026, the closing auction from Aug 2026 (BSE index options turnover fell 26% in August), and a possible end to weekly expiries. 2) Almost all profit now rests on one product. 3) NSE fighting back on share. 4) Other income is only 1% of pre-tax profit, so there is no cushion from interest if trading slows.

**Valuation now.** PE 47.1x (stockanalysis 47.58x, a 1.0% gap), PB 19.9x, dividend yield 0.31%. 49% above its own median of 31.6x, above the peer median. **Expensive** unless the boom lasts.

**Into the final three?** No. It passes on PEG only, and that PEG rests on a boom that the regulator is actively cooling.

### MCX

**The business in one line.** India's commodity futures and options exchange. It earns a fee on each trade, mostly in crude oil, natural gas and gold.

**Financial quality.** Sales ₹391 cr → ₹2,302 cr, 42.6% a year. Profit ₹225 cr → ₹1,332 cr, 42.7% a year. FY2024 was a trough (profit ₹83 cr, operating margin 9%) during the move to a new trading system. Margin 60% in FY2025 and 71% in FY2026. The change that matters: options. Average daily options turnover was ₹4,71,641 cr in FY2026 against ₹1,91,909 cr in FY2025. Quarterly profit went ₹203 cr, ₹197 cr, ₹401 cr, ₹530 cr, then ₹413 cr in Q1 FY27, so the latest quarter fell 22% from the one before. Cash from operations is 2.19 times profit over five years, flattered by margin money that members park at the exchange. No debt. Other income is 8% of pre-tax profit.

**Moat.** Network effect and licence. Over 98% of commodity futures in FY2026. Stable, but NSE got SEBI approval in Feb 2026 for natural gas and crude contracts. 4 stars.

**Top 3 risks.** 1) NSE entering energy, MCX's biggest product (about 70% of options turnover). 2) SEBI or RBI rules that cut options activity; the RBI bank-guarantee rules are now in force. 3) One asset class, energy, carries most of the volume.

**Valuation now.** PE 55.8x (stockanalysis 55.81x), PB 30.1x, dividend yield 0.24%. 30% above its own median of 42.8x. **Expensive.**

**Into the final three?** No. The same options-boom question as BSE, at a higher price, and a new competitor in its core product.

### IEX

**The business in one line.** India's main power exchange. Buyers and sellers of electricity each pay a small fee per unit traded.

**Financial quality.** Sales ₹317 cr → ₹608 cr, 13.9% a year. Profit ₹213 cr → ₹474 cr, 17.3% a year. Operating margin 84-85% for three years. ROE 39.4%. Other income is 22% of pre-tax profit (interest on cash). Q1 FY27 volume 37.5 billion units, up 15.9%. The change that matters: CERC's market coupling. Ordered 23 Jul 2025; sent back by the appeals tribunal in Feb 2026 for proper regulations; draft regulations 20 Apr 2026 with Grid India as the single operator; the Supreme Court refused to stop it on 3 Aug 2026. Whether the final rules were notified by 24 Sep: not found.

**Moat.** Network effect: about 85% of exchange volume and about 99% of day-ahead and real-time trading. Coupling pools all exchanges' bids, which removes exactly that advantage. Narrowing, and the regulator is the one narrowing it. 3 stars.

**Top 3 risks.** 1) Coupling: analysts estimate a 20-40% cut in day-ahead volume. 2) Fee cuts by CERC once the exchanges share one price. 3) Rivals (PXIL, HPX) competing on fees once liquidity no longer decides.

**Valuation now.** PE 19.8x (stockanalysis 19.85x), PB 7.4x, dividend yield 3.09% (₹3.50 for FY2026; stockanalysis's 3.53% uses ₹4.00, which its own dividend list does not add up to). At the bottom of its own range of 19.9-104.9x, median 38.2x, and half the peer median. **Cheap** on history. The price already assumes damage.

**Into the final three?** Yes, as the high-risk, high-payoff name. The question for the deep read is how much coupling takes, not whether the business is good.

### CDSL

**The business in one line.** One of India's two share depositories. It earns yearly fees from listed companies, a fee each time shares leave an account, and IPO and KYC fees.

**Financial quality.** Sales ₹344 cr → ₹1,145 cr, 27.2% a year. Profit ₹201 cr → ₹455 cr, 17.8% a year. FY2026 profit fell 13.5%, from ₹526 cr. Operating margin 60% → 58% → 51% over FY2024-26. The change that matters: the margin falling while accounts kept growing (18.01 cr accounts at 31 Mar 2026, 2.72 cr added in FY2026). Revenue in Q1 FY27 was ₹292.76 cr: yearly fees from listed companies about 44%, transaction fees about 23%, IPO and corporate-action fees ₹27 cr, and the KYC arm CDSL Ventures ₹45 cr. Quarterly profit over the last five quarters: ₹102 cr, ₹140 cr, ₹133 cr, ₹80 cr, ₹118 cr. Other income is 15% of pre-tax profit. No debt. Cash from operations is 0.97 times profit.

**Moat.** Licence and switching cost; a duopoly with NSDL. About 80% of demat accounts, but only about 13% of the value held. Accounts reached 18.59 cr at Jun 2026; most new retail investors open with a CDSL broker. 4 stars.

**Top 3 risks.** 1) KYC fee cuts by the regulator. 2) Transaction fees fall when retail trading slows. 3) Investment income swings with bond prices.

**Valuation now.** PE 59.9x (stockanalysis 59.93x), PB 14.4x, dividend yield 0.94%. 40% above its own median of 42.8x, the highest PE among the survivors. **Expensive.**

**Into the final three?** No. The most expensive name, with profit falling in the last year.

### CAMS

**The business in one line.** The registrar for most of India's mutual funds. Fund houses pay it, mostly as a small share of the assets it services, to keep investor records and process every purchase and redemption.

**Financial quality.** Sales ₹674 cr → ₹1,412 cr, 15.9% a year. Profit ₹219 cr → ₹437 cr, 14.8% a year. Operating margin 45-46% for three years. ROE 38.9% in FY2026. The change that matters: profit was flat in FY2026 (₹441 cr → ₹437 cr), as SEBI's expense-cap cuts from 1 Apr 2026 reached fund houses and the KYC business lost pricing (non-asset revenue −3.5% in Q1 FY27).

**Moat.** Switching cost and scale. 67.2% of mutual fund assets serviced (Q1 FY27), against about 61% in Mar 2015; KFintech has the rest. Changing registrar is a years-long data migration for a fund house. Stable to slightly narrowing in the last year (68% → 67.2%). 4 stars.

**Top 3 risks.** 1) Fund houses pass their own fee cuts on to CAMS. 2) Revenue moves with market levels. 3) ₹290 cr of spending on rebuilding its systems, a delivery risk.

**Valuation now.** PE 36.3x (stockanalysis 35.39x, a 2.5% gap; market caps differ by the same 2.5%, so the share count differs), PB 13.6x, dividend yield 1.77% (₹12.8 over twelve months). 15% below its own median of 42.8x, near the bottom of its 33.7-96.6x range, at the peer median. **Fair.**

**Into the final three?** Yes, as the moderate-certainty grower. A toll on the whole mutual fund industry, at the low end of its own price history. Note it shares the fee-cut risk with every fund house in this screen.

### KFINTECH

**The business in one line.** The second mutual fund registrar, and the largest registrar for listed companies' shareholders. Paid per asset serviced or per account, plus overseas fund administration.

**Financial quality.** Sales ₹481 cr → ₹1,301 cr, 22.0% a year. Profit went from a ₹65 cr loss in FY2021 to ₹344 cr; three-year growth 20.6% a year. Operating margin 41-44%. The change that matters: going overseas; it bought 51% of Ascent Fund Services (Singapore) for US$34.68 m in Oct 2025, and international was 20.5% of Q1 FY27 revenue. Q1 FY27 revenue was ₹356.5 cr, up 30%: domestic mutual funds 60.4%, international 20.5%, company registry 9.0%. But profit did not follow: the last five quarters were ₹77 cr, ₹93 cr, ₹92 cr, ₹81 cr and ₹75 cr. The quarter carried a ₹9.16 cr provision for share transfers a depository participant made without authority. Cash from operations is 1.21 times profit. Debt is ₹55 cr against ₹1,674 cr of equity.

**Moat.** Switching cost, as for CAMS. 32.8% of mutual fund assets serviced (Q1 FY27), steady; 38.3% of main-board IPOs by count in FY2026. 3 stars.

**Top 3 risks.** 1) Fee pressure from fund houses. 2) Overseas deals it has not run before. 3) Supply of shares: General Atlantic keeps selling.

**Valuation now.** PE 44.9x (stockanalysis 46.29x, a 3.1% gap), PB 9.4x, dividend yield 1.32%. 11% below its own median of 50.2x, but that median covers only its high-priced years since the Dec 2022 listing. **Fair to expensive.**

**Into the final three?** No. CAMS is the stronger of the two registrars at a lower PE.

### CRISIL

**The business in one line.** India's best-known credit rating agency, plus a larger research and analytics business that sells to banks and funds worldwide. S&P Global owns 66.64%.

**Financial quality.** Sales ₹1,982 cr → ₹3,649 cr, 13.0% a year. Profit ₹355 cr → ₹766 cr, 16.6% a year. Operating margin 28% → 28% → 30% over CY2023-25. ROE 27.4% in CY2025. Profit has risen every year since CY2020. The change that matters: ratings are now only about 28% of revenue (Q2 CY26: ₹305.1 cr of ₹1,075.4 cr); the rest is research and analytics, which it keeps adding to (McKinsey PriceMetrix bought for US$38 m, announced Sep 2025).

**Moat.** Licence and brand. A rating licence from SEBI, and a name that bond buyers expect to see. Research is a switching-cost business with global banks. Market share against ICRA, CARE and India Ratings: NA, no figure found. 4 stars.

**Top 3 risks.** 1) Research revenue depends on global banks' budgets, and on work for the S&P group. 2) A rating failure would damage the brand (IL&FS-type events). 3) Slower bond issuance in India.

**Valuation now.** PE 38.0x (stockanalysis 38.09x), PB 10.3x. Dividend yield **1.37%** on ₹63 over twelve months (CY2025 total ₹61 confirmed by CRISIL; one ₹9 payment only on stockanalysis). Screener's 0.54% looks stale. 16% below its own median of 45.2x, inside a 23.8-66.7x range. **Fair.**

**Into the final three?** Yes, as the high-certainty compounder. The steadiest profit record in the screen, and its main risk is not the Indian trading boom that drives most of the others.

### HDFCAMC

**The business in one line.** The second-largest mutual fund house by active assets. It earns a yearly fee as a share of the money it manages.

**Financial quality.** Sales ₹2,194 cr → ₹4,611 cr, 16.0% a year. Profit ₹1,326 cr → ₹2,859 cr, 16.6% a year; three-year growth 26.2% a year. Operating margin 80-83%. ROE 32.9%. No debt. The change that matters: SEBI's new expense caps from 1 Apr 2026, cut by up to 0.15 percentage points on most slabs. The same rules cut the brokerage a fund may pay from 0.12% to 0.05% on cash trades. Quarterly profit over the last five quarters: ₹748 cr, ₹718 cr, ₹770 cr, ₹623 cr, ₹838 cr, so the new caps have not yet shown as a fall. A 1-for-1 bonus had record date 26 Nov 2025. HDFC Bank's stake slips a little each quarter as staff options are issued; no sale by the bank was found.

**Moat.** Brand and distribution through HDFC Bank. Share of assets 11.5% (Jun 2025) → 11.2% (Jun 2026); 65.7% of its assets are in equity, against 56.6% for the industry, which earns more per rupee. Flat to slightly narrowing. 3 stars.

**Top 3 risks.** 1) Fee caps cut again. 2) Market falls cut assets and fees together. 3) Losing share to Nippon, SBI and ICICI.

**Valuation now.** PE 35.8x (stockanalysis 35.71x), PB 11.4x, dividend yield 2.21%. 13% below its own median of 41.0x, below the peer median. **Fair.**

**Into the final three?** No, narrowly. It is the nearest miss. It rides the same mutual fund flows as CAMS, and a CAMS pick already covers that, with no fund-performance risk.

### ICICIAMC

**The business in one line.** The largest mutual fund house by active assets, owned by ICICI Bank and Prudential. It earns fees as a share of assets.

**Financial quality.** Six years only. Sales ₹2,230 cr → ₹5,999 cr, 21.9% a year. Profit ₹1,245 cr → ₹3,298 cr, 21.5% a year. Operating margin 73-75%. ROE 85.8% in FY2026, because it pays out almost everything. The change that matters: the Dec 2025 listing, all shares sold by Prudential. Q1 FY27 revenue was ₹1,564 cr: mutual funds about ₹1,300 cr, alternative funds ₹120 cr, advisory ₹20 cr, at a fee of 0.52% of assets. Quarterly profit over the last five quarters: ₹784 cr, ₹835 cr, ₹917 cr, ₹769 cr, ₹965 cr. No debt. Cash from operations is 0.94 times profit over six years.

**Moat.** Scale and bank distribution. 13.4% of assets in Jun 2026 (13.3% in Dec 2025), 14.0% of equity funds and 26.6% of equity-hybrid funds. 3 stars.

**Top 3 risks.** 1) Fee caps. 2) Supply: Prudential sold 2% more in late Aug 2026 (stated reason: the minimum public shareholding rule), and more must follow. 3) A short listed history.

**Valuation now.** PE 45.1x (Screener standalone; stockanalysis 45.18x; Screener's consolidated page shows 53.4x on stale figures), PB 37.7x, dividend yield 0.86% on Screener against 1.57% on stockanalysis, not resolved. Own range NA. Above the peer median and above HDFC AMC's 35.8x. **Expensive.**

**Into the final three?** No. The highest price among the fund houses, and a steady stream of promoter shares still to come.

### NAM-INDIA

**The business in one line.** Nippon India Mutual Fund, the largest ETF manager in India. Fees as a share of assets.

**Financial quality.** Sales ₹1,419 cr → ₹2,924 cr, 15.6% a year. Profit ₹680 cr → ₹1,529 cr, 17.6% a year; three-year growth 28.4% a year. Operating margin 68-69%. ROE 29.5% → 31.4% → 34.5%. The change that matters: it is gaining share fastest among the top ten, 8.50% → 9.04% in the year to Jun 2026, the highest since Jun 2019, and 21.35% of ETF assets. Revenue has risen every quarter for five quarters: ₹607 cr, ₹658 cr, ₹705 cr, ₹739 cr, ₹767 cr. Q1 FY27 profit of ₹504 cr included ₹170 cr of other income, mostly gains on its own investments, which will not repeat every quarter. Cash from operations is 0.86 times profit. Nippon Life's stake fell from 73.47% to 71.80% over Sep 2023-Jun 2026. Five staff-option allotments are on record in 2026 and no sale by Nippon Life was found, but the Sep 2023 share count was not found, so dilution alone is not proven.

**Moat.** Scale in ETFs and a wide distributor network. Widening. 3 stars.

**Top 3 risks.** 1) ETFs earn thin fees, so share gains bring less profit. 2) Fee caps. 3) Yield falls about 1-2 basis points a year as assets grow (management's own guide).

**Valuation now.** PE 45.5x (stockanalysis 46.13x, a 1.4% gap), PB 16.0x, dividend yield 1.85%. 39% above its own median of 32.8x. **Expensive.**

**Into the final three?** No. The price already pays for the share gains.

## The final three

| Company | Type | Why it is here | Main risk | What would change my mind |
|---|---|---|---|---|
| CRISIL | high-certainty compounder | profit up every year since CY2020; 5 of 5 value checks; PE 38.0x, 16% below its own median; ratings are only 28% of revenue, so it does not rest on India's trading boom | research revenue depends on global banks' budgets and on work for the S&P group | a fall in research revenue two quarters running, or a large related-party change with S&P |
| CAMS | moderate-certainty grower | 67.2% of mutual fund assets serviced; 5 of 5; PE 36.3x, near the bottom of its own 33.7-96.6x range | fund houses pass SEBI's fee cuts on to it; profit was flat in FY2026 | share of assets serviced falling below 65%, or a second flat year |
| IEX | high-risk, high-payoff | 5 of 5; PE 19.8x, the lowest in its own history and half the peer median; 84% operating margin; 3.09% dividend | market coupling removes the liquidity lead that is its whole moat | the final coupling rules, and how much day-ahead volume leaves in the first two quarters |

**Why these three and not the top three by score.** Seven names passed 5 of 5. BSE and MCX pass valuation only on growth from an options boom the regulator is cooling, so they are the same bet twice. HDFC AMC is the nearest miss: it and CAMS both ride mutual fund flows, and CAMS carries no fund-performance risk. The three picked have different main risks: global research budgets, Indian mutual fund fees, and one power-market rule. **Shared risk to note:** CAMS and all four fund houses in this screen are hit by the same SEBI fee rules.

## Sector verdict

Pass rate 10/17 after step 2, 3 into the final. The businesses are unusually good — margins of 40-85%, no debt, cash that follows profit — but much of the sector is priced for a trading boom to last. Worth more time, mainly where the price is low against its own history: CRISIL, CAMS, IEX, and HDFC AMC as the reserve.

## Information grade

| Area | A/B/C | Note |
|---|---|---|
| Company financials | A | ten years of Screener data for 13 of 17; ICICIAMC 6 years, KFINTECH, NUVAMA and 360ONE 7-9 years |
| Valuation freshness | A | NSE close 23 Sep; Screener and stockanalysis agree within 1% on price for all 17; PE gaps over 1% are written next to each name |
| Competitive picture | B | market shares mostly from company decks and press; BSE's options share worked out from NSE's prospectus; IEX's share has no official CERC figure; CRISIL's rating share NA |
| Management | B | not assessed beyond the checks and the promoter changes |

**Where the sources disagree by more than 1%.** PE: BSE 1.0%, CAMS 2.5%, KFINTECH 3.1%, ANANDRATHI 1.8%, NAM-INDIA 1.4%, UTIAMC 15.9%, ANGELONE 1.8%, MOTILALOFS 1.8%. ICICIAMC: Screener's consolidated page shows PE 53.4x on stale two-year figures; the standalone 45.1x agrees with stockanalysis 45.18x and is used. Dividend yield: CRISIL 0.54% vs 1.32% (dividends add to 1.37%); IEX 3.09% vs 3.53% (dividends add to 3.09%); ICICIAMC 0.86% vs 1.57% (not resolved). Market cap: CAMS 2.5%, 360ONE 3.5%.

**Info grade by survivor (for the Notion rows):** A for BSE, MCX, IEX, CDSL, CAMS, CRISIL, HDFCAMC and NAM-INDIA. B for KFINTECH (listed Dec 2022) and ICICIAMC (listed Dec 2025).

## Sources

- **NSE:** full bhavcopy 23-Sep-2026 (closes); Nifty 500 constituent file; archive copy of Anand Rathi Wealth's red herring prospectus, 26 Nov 2021 (`archives.nseindia.com/content/equities/IPO_RHP_ARWL.pdf`).
- **Screener.in:** consolidated and standalone pages for all 17, read 2026-09-24 00:23-00:24 IST; the price-to-earnings chart API for own ranges, read 2026-09-24.
- **stockanalysis.com:** price, market cap, PE and dividend for all 17 via `crosscheck` (NAM-INDIA as NAM.INDIA), 2026-09-24 00:38 IST; dividend histories for CRISIL, IEX and CAMS.
- **Offer documents:** Aditya Birla Sun Life AMC red herring prospectus, Sep 2021 (BofA copy, pages 26, 72, 84-86); ICICI Prudential AMC DRHP as summarised by HDFC Sky, and the Chittorgarh IPO page (share count 49,42,58,520).
- **Trendlyne shareholding pages:** pledge 0.0% for ABSLAMC, HDFCAMC, NAM-INDIA, CRISIL, KFINTECH, ICICIAMC (Mar 2026) and CDSL, Jun 2026; Anand Rathi Wealth 13.83% (Jun 2026), 11.42% (Mar 2026). Trendlyne bonus history for Anand Rathi Wealth.
- **Anand Rathi pledge filings:** promoter disclosures of 15 May, 2 Jun and 10 Jun 2026 as reported by InvestyWise and ScanX (pledges with Yes Bank for margin limits; 25.60% of Anand Rathi Financial Services' holding encumbered).
- **Company decks and results:** BSE, MCX, IEX, CDSL, CAMS, KFintech, HDFC AMC, ICICI Pru AMC, Nippon AMC Q1 FY27 presentations and results (Jul-Aug 2026), CRISIL Q2 CY26 results (22 Jul 2026) and CY2025 results (13 Feb 2026), as summarised by Investing.com, InvestyWise, Business Standard, Multibagg and Sahi; HDFC AMC's own Q1 FY27 shareholder deck; KFintech Q4 FY26 factsheet; CAMS Q4 FY25 press release.
- **Market share and regulation:** NSE prospectus figures on options premium share (via Multibagg, 19 Sep 2026); MCX directors' report FY25; IEX market coupling timeline (IndMoney, Power Peak Digest, Sahi, Jul-Aug 2026); SEBI's 2026 expense-ratio rules (Cafemutual, 17 Feb 2026); SEBI closing auction effect (Business Today, 14 Sep 2026); STT change (IndMoney, Feb 2026); ABSL market share (company QAAUM disclosures, Q4 FY23 and 31 Mar 2026).
- **Promoter sales:** CAMS / Great Terrain (Moneycontrol via TradingView, 4 Dec 2023); KFintech / General Atlantic (Kotak Neo, 20 Aug 2026); ICICI Pru AMC / Prudential (Business Today, 27 Aug 2026; Investing.com, Aug 2026).
- **Brokers, for the summary table:** credit rating reports (CARE, ICRA, India Ratings, CRISIL) and company decks; full list with URLs in `local/capmkt-20260924/brokers.md`.
- Full per-fact URLs for the short analyses are in `local/capmkt-20260924/facts.md`.

## Notion block

Written to Notion ✔ 2026-09-24 00:59 IST

BSE | BSE Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
MCX | Multi Commodity Exchange of India Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
IEX | Indian Energy Exchange Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
CDSL | Central Depository Services (India) Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
CAMS | Computer Age Management Services Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
KFINTECH | KFin Technologies Ltd. | Capital markets | info grade B | status Candidate | reports/IN/_screens/capital-markets-20260924.md
CRISIL | CRISIL Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
HDFCAMC | HDFC Asset Management Company Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
ICICIAMC | ICICI Prudential Asset Management Company Ltd. | Capital markets | info grade B | status Candidate | reports/IN/_screens/capital-markets-20260924.md
NAM-INDIA | Nippon Life India Asset Management Ltd. | Capital markets | info grade A | status Candidate | reports/IN/_screens/capital-markets-20260924.md
