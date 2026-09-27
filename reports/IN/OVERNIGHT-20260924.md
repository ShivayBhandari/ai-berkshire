# Overnight run — 24 Sep 2026

1. **What ran tonight:** a screen of 17 companies that make money from people investing (exchanges, fund houses, fund record-keepers, a rating firm, brokers), full studies of the three it picked (CRISIL, CAMS, IEX), and a full study of UltraTech so it finally has written sell rules.
2. **What came out:** 10 companies came through the screen and were added to Notion as candidates. **CAMS: worth buying below ₹805** (₹723.90 today), and it just beats a Nifty 50 index fund. **CRISIL: only below ₹4,730** (₹4,605.80 today); it beats the index fund by a hair. **UltraTech: only below about ₹3,860** (₹11,155 today); the index fund is better at today's price. **IEX: only below about ₹27.5** (₹113.16 today). The last two changed on 24 Sep under the new buy-below rule (item 6).
3. **Decisions waiting for you: 12.** Two are about whether a company can be trusted, and those come first.

---

## 1. Screen: Capital markets — done

File: `reports/IN/_screens/capital-markets-20260924.md`. Audit passed, 30 of 30. But 12 of those 30 were star scores, counts or read times, so the real check is 18 figures, and only 3 of those had a second source.

- **Screened: all 17** in the theme, all in the Nifty 500. This is the list you chose tonight: CAMSBANKING fixed to CAMS, IIFL Finance out, eight names added.
- **One bug fixed in `local/capmkt-20260924/step1.py`:** CRISIL's balance sheet has an extra Jun 2026 half-year column. That shifted every ROE year by one. CRISIL's ten-year ROE is 30.8%, not 27.3%. No other name was affected. The original script is kept as `step1.orig.py`.
- **Dilution checked in the offer documents:**
  - ABSLAMC: a face-value split, then a 7-for-1 bonus in Apr 2021.
  - ICICIAMC: a split, then a 1.8-for-1 bonus.
  - Anand Rathi: a 1-for-2 bonus in 2021 and a 1-for-1 bonus in 2025.
  - All are bonuses or splits, not new shares. Real dilution is 0.0-0.9%.
- **Step 1:** 12 of 17 pass checks 1-7. UTI AMC fails check 5 (0.65). Angel One, Motilal Oswal, Nuvama and 360 ONE fail checks 2 and 5, and are eliminated as the rules say.
- **New finding, check 8: Anand Rathi Wealth is eliminated.** 13.83% of the promoter holding is pledged (Trendlyne, Jun 2026), up from 0.01% in Dec 2025. The promoters' own filings back it: pledges with Yes Bank "for availing margin limits", May-Jun 2026.
- **Step 2: 10 survive.**
  - 5 of 5: BSE, MCX, IEX, CAMS, CRISIL, HDFC AMC.
  - 4 of 5, kept with a ⚠ flag: CDSL (price 40% over its own median), KFin (ROE 14.3% against 15%), ICICI AMC (price), Nippon AMC (price 39% over its own median).
  - ABSL AMC dropped, 3 of 5: price, and a moat of 2 stars (its share of fund assets fell from 7.7% to 6.02%).
- **Written in the report as assumptions:** your rule from tonight on which figures to use, and the valuation bar (pass at or below its own median PE, or PEG under 1.5). BSE and MCX pass only on PEG, from an options boom SEBI is cooling.
- **Final three:** CRISIL (steady compounder), CAMS (grower), IEX (high risk; the cheapest it has been, because of market coupling). HDFC AMC is the reserve.

## 2. Deep reads of the final three

The three studies started as soon as the final three were fixed, before the screen's audit and Notion step had finished. They used only step 1 and step 2 figures, which did not change afterwards.

### 2a. CRISIL — done

Files: `reports/IN/CRISIL/research-20260924.md` and `reports/IN/CRISIL/thesis.md`. Audit passed: 30 of 197 sampled, 29 pass, 1 warning (Screener rounds the operating margin to 30%; 29.73% is used). The terminal-value audit passed at r = 11%, 12% and 14%.

- **Gates: passed 5 of 6** (4 / 5 / 4 / 4 / 3; gate 6 is yours). No integrity question.
- **Recommendation: Conditional, buy below ₹4,730.** Price ₹4,605.80, 2.6% under that line.
- **Against the index fund:** the base-case ten-year return is **12.32% a year, only just above 12%.** At CRISIL's own ten-year profit growth of 10.4% it is 11.72%, and the index fund wins. Strict model −0.82%.
- **Confidence:** low on beating the index fund. The business itself is high-certainty.
- **Fair value range:** ₹1,450–₹6,285.
- **Dividend settled:** ₹61 for 2025, from the annual report, a 1.32% yield. Screener's 0.54% was wrong.
- **Fit:** it shares Indian mutual fund activity with CAMS. It also owns ₹419.56 cr of CARE Ratings shares.

### 2b. CAMS — done

Files: `reports/IN/CAMS/research-20260924.md` and `reports/IN/CAMS/thesis.md`. Audit passed: 30 of 224 sampled, all within 1% (about a third were tool outputs or dates). The terminal-value audit passed at r = 11%, 12% and 14%.

- **Gates: passed 5 of 6** (4 / 5 / 4 / 4 / 3; gate 6 is yours). No integrity question.
- **Recommendation: Pass, narrowly. Buy below ₹805.** Price ₹723.90.
- **Against the index fund:** the base-case ten-year return is **13.38% a year, above 12%.** Strict model +0.88%.
- **Confidence:** medium. At 10% growth the return is 11.38%, below the bar. At an exit PE of 30x it is 11.28%.
- **Fair value range:** ₹260–₹950.
- **The screen's open questions, answered:**
  - Share count: 24,79,84,498 (annual report). stockanalysis uses a stale count, which explains all of its 2.5% gap.
  - Split: 1 share of ₹10 became 5 of ₹2 on 5 Dec 2025.
  - No promoter: Warburg Pincus sold its last 19.87% to institutions on 4 Dec 2023. It was a private-equity exit, not a pledge.
  - Flat FY2026 profit: a price cut agreed with a client, slow asset growth in Q4, and 27% higher depreciation. Q1 FY27 profit was up 17.3%.
- **Not found:** today's revenue by client (the last figure is from the 2020 prospectus: the top five gave 67.4%), and what SEBI's expense-ratio cut does to CAMS's own fees.

### 2c. IEX — stopped at gate 4 for you

Files: `reports/IN/IEX/research-20260924.md` and `reports/IN/IEX/thesis.md`. Audit passed: 28 of 182 sampled (about half were tool outputs, dates or labels). The terminal-value audit passed at r = 11%, 12% and 14%.

- **Gates: 4 of 6 before the stop** (3 / 5 / 2 / 3 / 3; gate 6 is yours).
- **⚠ Gate 4, an integrity question.** An internal whistle-blower complaint alleged "conflict of interest and potential diversion of business involving certain officials" (annual report FY2026, note 49). The Audit Committee investigated and "appropriate actions" were taken. The findings were not published. Tonight's brief says to stop there, so IEX has no recommendation.
- **The study ran past the stop anyway.** That was my mistake; see "What didn't work". Parts 2-4 are kept in the report, marked "for reference only", and `thesis.md` is marked "not in force".
- **Gate 4 cleared on 24 Sep:** Conditional, buy below about ₹27.5 (buy-below rule of 24 Sep), against ₹113.16 today. The base-case ten-year return is **2.39% a year, far below 12%**, so the index fund is the better bet. Coupling failing gives 13.99%, put at 40%. The weighted return is 5.30%. Fair value ₹61–₹111.
- **Market coupling:** ordered 23 Jul 2025; draft rules 17 Apr 2026, covering day-ahead, real-time "and other market segments"; the Supreme Court declined the challenge on 3 Aug 2026. CERC's list of notified rules shows no final rule as of tonight. IEX still has 99.94% of day-ahead and 99.82% of real-time trading (CERC, Mar 2026).
- **Dividend settled:** ₹3.50 for FY2026, a 3.09% yield. stockanalysis counts one payment twice.

## 3. UltraTech — done

Files: `reports/IN/ULTRACEMCO/research-20260924.md` and `reports/IN/ULTRACEMCO/thesis.md` (new; UltraTech now has sell conditions). Audit passed, 30 of 221 sampled, all within 1% (about half were tool outputs, inputs or star scores). The terminal-value audit passed at r = 11%, 12% and 14%.

- **Gates: passed 3 of 6** (4 / 2 / 4 / 3 / 2; gate 6 is yours). Gate 4 carries a ⚠ integrity question: the cement cartel matters.
- **Recommendation: Conditional, buy below about ₹3,860** (buy-below rule of 24 Sep). Price ₹11,155.
- **Against the index fund:** the base-case ten-year return is **10.7% a year, below 12%**, so at today's price the index fund is the better bet. Strict model −5.0%.
- **Confidence:** medium.
- **Fair value range:** ₹2,900–₹11,600, unchanged from 22 Sep.
- **Your Verdict (Conditional) was already on the row and was not touched.** Status stays Watching.
- **Facts that change the 22 Sep report:**
  - The ₹240 dividend was a special dividend. The regular yield is 0.69%, not 2.15%.
  - Earnings per tonne without other income is ₹1,103, the same as Shree's ₹1,108.
  - The group management fee to Aditya Birla Management Corporation is ₹743.98 cr, up 36%, about 10% of standalone profit. What it buys is not itemised.

---

## Waiting for you

Integrity first.

1. **Answered 24 Sep: it doesn't count.** IEX now recommends Conditional, buy below about ₹27.5 (after item 6); Notion row updated. ~~**IEX, gate 4:** does the whistle-blower complaint (conflict of interest, possible diversion of business; findings not published) count against the company? (a) No, and the reference study stands. (b) Yes: reject. (c) Not until the findings are known.~~
2. **Answered 24 Sep: they don't count.** The study stands; Notion row updated. ~~**UltraTech, gate 4:** do the cement cartel matters count? The 2016 penalty of ₹1,616.83 cr was upheld by the tribunal, and the Supreme Court stayed it in 2018 and has not ruled. A second probe has had no ruling since 2022. (a) No, a contingent item, as with Shree on 23 Sep. (b) Yes, and the study ends at gate 4. (c) Wait for the second ruling.~~
3. **Answered 24 Sep: kept out of gate 4.** ~~**IEX, the SEBI insider-trading order** (interim, 15 Oct 2025, against 8 outsiders; ₹173.14 cr impounded; the leak came from inside CERC; no IEX official is named). Leave it out of gate 4, as the study did? Or make it a second gate 4 question?~~
4. **Answered 24 Sep: a closed slip-up; nothing changes.** ~~**CRISIL, the 2018 Amtek Auto settlement** (about ₹28 lakh, a rating-process lapse, no admission). (a) A closed process lapse, gate 4 stays at 4 stars. (b) Any settled rating-lapse case is an integrity question.~~
5. **Answered 24 Sep: no, keep dropping them.** Written into `CLAUDE.md` and the screen command. ~~**Brokers:** should brokers and wealth firms get their own rule? (a) No, keep eliminating them on checks 2 and 5. (b) Judge them the way lenders are judged. (c) A broker rule of its own. Only you can decide this.~~ Here is how the four would score if judged like lenders:

   | Company | Lender-style result | Why |
   |---|---|---|
   | Angel One | NA | no NBFC loan book. The margin book (₹5,128 cr, Mar 2026) sits in the broker. Net worth ₹6,149 cr against SEBI's ₹3 cr floor; debt 1.3 times net worth against a 5 times cap |
   | Motilal Oswal | step 1 passes, step 2 NA, leaning fail | capital adequacy 26.1% (NBFC) and 37.8% (home loans), both above 15%. Gross NPA 0.06% and 1.1%. The home-loan arm's provision cover is not published; a rough figure from its gross and net NPA is about 45%, below the 60% bar |
   | Nuvama | fails anyway, on the pledge | NBFC capital adequacy 17.77% (down from 20.87%), no bad loans. But **62.80% of the promoter's holding is pledged**, backing a US$450 m loan. That is a hard fail under your pledge rule |
   | 360 ONE | step 1 passes, step 2 NA | lending arm's capital adequacy 19.87% (Jun 2026, down from 29.6%), gross NPA nil. Lending yield fell from 6.25% to 5.07%. Promoter pledge 0% now; it was 86.57% in May 2025 |

   The "not rising two years running" tests could not be fully judged: only two points in time were found for each. Sources: `local/capmkt-20260924/brokers.md`.
6. **Answered 24 Sep: the lowest of the PE paid, today's PE and the median.** Written into `CLAUDE.md` and the research command. CRISIL, CAMS and HAL keep their prices; UltraTech is about ₹3,860, IEX about ₹27.5, IRCTC about ₹226. ~~**The buy-below method** (UltraTech, CRISIL, CAMS, IEX): keep the year-10 PE fixed at today's PE? That is what all four studies did. Or reset it to the PE at the buy price, capped at the ten-year median? That gives a higher buy-below for CRISIL (about ₹5,500) and CAMS, and a much lower one for UltraTech (about ₹3,900) and IEX (₹26-₹28).~~
7. **Answered 27 Sep, by Claude under the new method rule: one drop, then growth again** (10.08%, still below 12%; the call does not change). ~~**IEX, the base case for a one-time rule change:** keep −0.7% a year for all ten years, as the rule reads (2.39%)? Or a one-time drop and then regrowth (10.08%, still below 12%)?~~
8. **Answered 27 Sep, by Claude: made a rule** in `CLAUDE.md` § Method rules Claude set. ~~**Screen, which figures to use:** consolidated when it has 10 years, otherwise standalone when standalone has 10 years and at least 85% of consolidated sales. Make it a decided rule in `CLAUDE.md`, or keep it as a per-screen assumption?~~
9. **Answered 27 Sep, by Claude: the bar stays, and growth above 25% a year counts as 25%.** BSE and MCX now fail the price check and stay as 4-of-5 ⚠ names. ~~**Screen, the valuation bar:** pass at or below its own median PE, or PEG under 1.5 (three-year growth when the five-year start year fell more than 10%). Keep it? And should a PEG built on a boom the regulator is cooling (BSE, MCX) still count as "high grower"?~~
10. **Verdict for CRISIL.** Status is Researched; the field is empty for you.
11. **Verdict for CAMS.** Status is Researched; the field is empty for you.
12. **Verdict for IEX**, after question 1.

**New Candidates in Companies, waiting for a deep read:** BSE, MCX, CDSL, KFINTECH, HDFCAMC, ICICIAMC, NAM-INDIA. HDFC AMC is the screen's reserve pick.

---

## What didn't work

- **IEX ran past the stop.** Your brief said: where a gate asks you, stop that name. The command file says: mark ⚠ and carry on. I briefed the IEX study from the command file, so it carried on. I found this when it finished. I applied the stop afterwards: the report's first lines, the Notion row and `thesis.md` now say "stopped at gate 4", and the full study is kept only for reference. The original report is saved as `local/iex-20260924/research-20260924.before-stop.md`.
- **UltraTech also carried on past a gate 4 ⚠.** I left it, because step 3 asked for the full research so that it gets sell conditions. If you read the brief's stop rule as covering step 3 too, question 2 (b) undoes it.
- **One edit after the screen's audit:** a section heading said 12 names survived step 1. It is 11 (12 pass checks 1-7, then Anand Rathi fails check 8). No figure changed.
- **The audit samples are weaker than "30 of 30" sounds.** In every report tonight, a third to a half of the sampled items were tool outputs, star scores, labels or dates. Those only prove the report agrees with itself.
- **Not found tonight:**
  - whether CERC's final market-coupling rule was notified;
  - CRISIL's share of the rating market;
  - ICICI AMC's dividend yield (0.86% against 1.57%) and its own PE range (listed only 9 months ago);
  - why KFin's promoter figure (22.82%) does not match the 21.89% reported before the August sale;
  - whether Nippon AMC's promoter fall is only staff-option dilution;
  - why ABSL AMC's promoter holding fell (not checked, because it left at step 2).
- **Secondhand sources:**
  - Anand Rathi's pledge comes from Trendlyne plus news reports of the promoters' filings, not the filings themselves.
  - Several market shares and the coupling timeline come from news summaries of company decks and court hearings.
  - IEX's base case (70% share, 3.5 paise) is a broker's estimate as reported in the news.
- **Guesses, labelled as such in the reports:** IEX's scenario odds (40% / 45% / 15%). CAMS's 12% base growth. CRISIL's domestic ratings revenue (about ₹697 cr).
- **A stale note in my briefs:** I told the studies that `terminal_value.py` takes risk labels only in Chinese. It has taken English labels since commit c66d606. No harm done.
- **One file outside a scratch folder:** the IEX study saved its annual report to `local/cache/ar/`, where the HAL and IRCTC reports keep theirs. It is gitignored.
- **Notion shows `Report file` as a link.** Notion turns the file name into a link (`[research-….md](http://research-….md)`). The same happened on 22-23 Sep. The text written is the plain path.

Nothing was committed, pushed or staged. `CLAUDE.md`, `PLAYBOOK.md` and `.claude/commands/` were not touched. `git diff --stat` on those files is the same as at the start of the run.

---

## Notion

Only the Companies table was written. No Verdict was set. No Status was set to Watching, Held, Exited or Rejected.

| Row | What was written | Receipt |
|---|---|---|
| BSE, MCX, IEX, CDSL, CAMS, KFINTECH, CRISIL, HDFCAMC, ICICIAMC, NAM-INDIA | 10 new rows: Name, Symbol, Sector `Capital markets`, Info grade, Status `Candidate`, Report file. None had a row before | Written to Notion ✔ 2026-09-24 00:59 IST |
| ULTRACEMCO | research block. Status left at Watching; your Verdict (Conditional) left as it was; Notes added to, the old text kept | Written to Notion ✔ 2026-09-24 00:50 IST |
| CRISIL | research block; Status Candidate → Researched | Written to Notion ✔ 2026-09-24 01:05 IST |
| CAMS | research block; Status Candidate → Researched | Written to Notion ✔ 2026-09-24 01:05 IST |
| IEX | the stopped-at-gate-4 block: Checklist Grey, no fair value or thesis lines, the integrity question as the red line; Status Candidate → Researched | Written to Notion ✔ 2026-09-24 01:12 IST |

Read back after writing: the whole UltraTech row, and Status, Checklist, Info grade, fair values, price and Verdict for every Capital markets row. One row per symbol; no Verdict set by this run.
