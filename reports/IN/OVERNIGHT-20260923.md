# Overnight run — 23 Sep 2026

Five steps, in order: `/stock-check`, three screens (Defence, Railways, Power), `/stock-research SHREECEM`. Each step's result is added below as it finishes.

## 1. /stock-check — done

File: `reports/IN/_checks/20260923.md`. Prices from the NSE bhavcopy of 22 Sep.

- **Held: 0.** No Companies row is Held, so there was nothing to price against a buy.
- **Watching: 1, UltraTech.** Close ₹11,000, inside its ₹2,900–₹11,600 range, +2.8% on the week. No new result, and no check due (next check 2026-10-26).
- **Flagged:** UltraTech has no `thesis.md`. That means no sell conditions are written. Run `/stock-research ULTRACEMCO` before any buy.
- **Stuck at Queued:** SHREECEM. It is step 5 tonight.
- **Notion:** nothing written. No full check and no results read ran.

## 2. /stock-screen --theme "Defence" — done

File: `reports/IN/_screens/defence-20260923.md`. Audit passed, 20 of 20.

- **Screened: all 12** in the theme (9 in the Nifty 500, 3 below it).
- **Step 1, eight hard checks:** 3 of 12 pass checks 1-7 (HAL, BDL, Solar Industries). Solar then fails check 8: Trendlyne shows **2.27% of the promoter holding pledged** (Jun 2026), up from 1.52% in Dec 2025. That is one source; the company's own FY26 declaration supports a pledge existing but gives no number.
- **Step 2, five value checks:** 1 survives, **HAL**, amber. PE 34.4 is 2.4x its own 10-year median of 14.4, but the lowest of the 12. BDL was dropped: PE 82.2 against an own median of 26.9, and ROE fell to 10.2% in FY26.
- **Cash was the killer.** 8 of the 9 names cut at checks 1-7 failed a cash check. BEL failed only on OCF / profit (0.59).
- **Notion:** HAL added as Candidate ✔.
- **Tool problems found:** `themes-in.json` had Jupiter Wagons as JUPITERWAG; the NSE symbol is **JWL**, now corrected. `universe` drops MTAR because it trades in the BE (surveillance) series, not EQ, so MTAR was screened by hand. `india_data.py --help` crashes on a `%` in a help string (not fixed).

## 3. /stock-screen --theme "Railways" — done

File: `reports/IN/_screens/railways-20260923.md`. Audit passed, 19 of 19.

- **Screened: all 11** (10 in the Nifty 500, Texmaco below it). JWL added after fixing the symbol.
- **Step 1:** 4 of 11 pass all eight checks (IRCTC, RailTel, RITES, CONCOR). All four show 0.0% pledged.
- **Step 2:** 3 survive. **IRCTC** keep: PE 27.2, the bottom of its own range. **RailTel** keep: ROE rising three years running. **RITES** amber: PE is 50% above its own median while profit has fallen three years.
- **CONCOR dropped:** 4 value checks passed and 1 clearly failed (ROE 9.8% against 15%). The keep rule does not cover this case. I read it as a drop, and wrote that down as an assumption.
- **IRFC eliminated on checks 2 and 5**, because a lender's loan growth runs through operating cash flow. The method only exempts lenders from check 3.
- **Notion:** IRCTC, RailTel and RITES added as Candidate ✔.

## 4. /stock-screen --theme "Power" — done, no survivors

File: `reports/IN/_screens/power-20260923.md`. Audit passed, 30 of 30.

- **Screened: all 13** (all in the Nifty 500). ROE bar 10% for power companies (asset-heavy), 8% for the lenders PFC and REC.
- **Step 1:** 6 of 13 pass all eight checks: NTPC, Power Grid, Tata Power, Torrent, CESC, NLC India. All six show 0.0% pledged.
- **Step 2: 0 survive.** Five of the six passed 4 value checks and clearly failed one. NTPC, Power Grid, CESC and NLC failed on debt (D/E 1.30-1.73 against the 1.0 power bar). Torrent failed on price (PE 65% above its own median). Tata Power passed only 3.
- Same reading as CONCOR: 4 pass plus 1 clear fail = drop. **Under the other reading, 5 come back as amber.**
- **PFC and REC** eliminated on checks 2 and 5, the same lender question as IRFC.
- The relaxed step-2 ROE bar for asset-heavy businesses (10-year average above 10%) has now been used twice, for cement and for power. The method says a bar used twice should go into `CLAUDE.md`.
- **Notion:** nothing written, because nothing survived.

## 5. /stock-research SHREECEM — done

Files: `reports/IN/SHREECEM/research-20260923.md` and `reports/IN/SHREECEM/thesis.md`. Audit passed, 30 of 30. The terminal-value audit also passed at r = 11%, 12% and 14%.

- **Gates: passed 3 of 6** (4 / 3 / 3 / 2 / 2, gate 6 yours). Gate 4 dropped from 3 stars on 22 Sep to 2, for three reasons:
  - Executive pay is large: the chairman earns 942 times the median employee, and the three executive directors together about ₹126 cr, about 7% of profit (estimate from the annual report's ratios).
  - A June 2023 tax allegation (about ₹7,000 cr of section 80IA deductions said to rest on fake bills). The High Court quashed the notices as time-barred, not on the merits.
  - Capital returns are weak: ₹4,820 cr of new capital since FY22 added ₹543 cr of EBITDA.
- **Correction to the 22 Sep checklist:** Shree's reported EBITDA includes treasury income. EBITDA per tonne is **₹1,108 without it**, not ₹1,266, so the per-tonne lead over UltraTech (₹1,141) is small or nil.
- **Fair value range: ₹5,600–₹18,800. The price is ₹22,200, above the top.** On EV/EBITDA it is 15.4x against UltraTech's 20.0x, because of ₹8,745 cr of net cash.
- **The five sentences cannot be completed.** Sentence 4 has no discount to name, so the case is not ready.
- Ten-year IRR is negative on every in-band path up to 15% growth.
- **Notion:** SHREECEM row set to Researched, with the full block written ✔. Info grade changed from B to A. Notes were added to, not replaced. Verdict not touched.
- **Tool problem found:** `terminal_value.py` accepts the risk labels only in Chinese. The English labels in the command file are rejected.

---

## Waiting for you

**Decisions**

1. **The 4-of-5 gap in step 2 of the screen.** When 4 value checks pass and 1 clearly fails, I dropped the name. That dropped CONCOR, NTPC, Power Grid, Torrent Power, CESC and NLC India. Read the other way, all six come back as amber, with no rerun needed. Which reading is the rule?
2. **Lenders in the screen.** IRFC, PFC and REC fail checks 2 and 5 by design, because new loans run through operating cash flow. Keep that as the rule, or judge lenders on net interest margin, NPA and capital instead?
3. **The asset-heavy ROE bar in step 2** (10-year average above 10%) has been used twice, for cement and for power. The method says it should now go into `CLAUDE.md`. Your call.
4. **Shree's tax allegation.** I did not treat it as an integrity problem, because nothing is proven and the notices were quashed. If you do, the method says the research stops at the gates.
5. **Verdict for SHREECEM.** Status is Researched; the field is empty for you.

**New Candidates in Companies, waiting for a deep read:** HAL (Defence), IRCTC, RailTel and RITES (Railways). RITES is marked "to watch", not a pick. No deep reads were run, as asked.

**Needs attention**

- UltraTech (Watching) has no `thesis.md`. Its sell conditions were never written.
- Solar Industries: its only fail is a 2.27% promoter pledge, and that comes from one source (Trendlyne).
- Shree's Q2 result is on **23 Oct 2026**. UltraTech's next check is **26 Oct 2026**.

**Changed outside `reports/IN/`:** `data/themes-in.json`, where JUPITERWAG was corrected to JWL. Nothing committed or pushed.
