# Weekly portfolio check

Run the weekly check. With no argument, take the holdings from Notion. With symbols —
`/stock-check TITAN,RVNL` — check only those.

One run covers everything that happens after a buy:

- prices against the fair value range
- why anything moved more than 5% this week
- a results read for any holding or Watching company that published results since the
  last check
- a full sell-conditions check where one is due, or where a move or a result touched one

Reports go to `reports/IN/_checks/<YYYYMMDD>.md`, plus
`reports/IN/<SYMBOL>/earnings-<quarter>.md` for each results read and an updated check
log in `reports/IN/<SYMBOL>/thesis.md`.

---

## Step 1 — what is held, and what is watched

From Notion:
- the Companies database, rows where Status is **Held** — gives the thesis lines, the
  fair value range, and the next check date
- the Companies database, rows where Status is **Watching** — companies researched and
  waiting for a price. They get the results read in step 5 and nothing else before it
- Holdings Snapshot, under Financial Profile — gives quantity (`Quantity/Units`) and
  buy price (`Avg Cost`) for each Held company

If Notion cannot be reached, say so and ask for the symbols. **Do not keep a second copy
of the holdings in this repo.** Notion is the only place that knows what is owned.

For each holding, check that `reports/IN/<SYMBOL>/thesis.md` exists. If it does not,
flag it under Needs attention: "no sell conditions written — run `/stock-research
<SYMBOL>`".

## Step 2 — prices, from the official file

```bash
python3 tools/india_data.py bhavcopy
```

One download covers every holding. Take the close, the volume and the delivery
percentage from it. Do not fetch prices one stock at a time.

If a Held or Watching company shows `BE` in the series column, NSE has put it under
surveillance. Say so under Needs attention, with the date it was first seen in BE if an
earlier check file shows it in EQ.

## Step 3 — the table

| Holding | Qty | Buy price | Close | Gain | Fair value range | Where the price sits | Thesis |
|---|---|---|---|---|---|---|---|

"Where the price sits" is one of: **below the range**, **inside the range**, **above the
range**. That is arithmetic against the range from the last research report, not a view.

## Step 4 — why it moved, for anything over 5% this week

For each holding that moved more than 5% in the week:

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py bhavcopy --symbol <SYMBOL>
```

Size the move: the close, the previous week's close, the range, and the delivery
percentage. A big move on low delivery is traders; a big move on high delivery is
people taking or leaving positions.

Then find the cause, in this order:

1. A company filing — `python3 tools/india_data.py screener <SYMBOL> --only documents`
2. A result, an order win, a block deal, a rating action
3. Something sector-wide — check two or three peers in the same bhavcopy. If the whole
   sector moved, it is not company news
4. Something index-wide — if the market moved, say so
5. No identifiable cause

Option 5 is a real answer. Say "no cause found in filings or sector moves" rather than
attaching the move to whatever news happened to be nearby.

Write it in four lines:

- **Move:** ₹<from> to ₹<to>, <n>%, delivery <n>%
- **Cause:** <what, with the source> or <none found>
- **Scope:** this company only / the sector / the market
- **Thesis:** does this touch a thesis line — yes, and which, or no

A move that touches a thesis line sends that holding to step 6. Most price moves are not
news about the business, and nothing more is written for them. No action advice: a price
move is not a reason to do anything.

## Step 5 — results read, for any holding or Watching company with new results

For each Held or Watching company that published a quarterly result since the last
check. This replaces any separate results-season routine: a result that lands in a week
is read that week.

**5a. The filing itself, not the coverage.**

```bash
python3 tools/india_data.py screener <SYMBOL> --only quarters documents
```

The documents section gives the exchange filing and the concall transcript. Read the
filing. Media coverage is for the reaction, not for the numbers.

**5b. The numbers, against the quarter a year ago.** Not the previous quarter, unless the
business is genuinely not seasonal.

| Line | This quarter | Year ago | Change | Previous quarter |
|---|---|---|---|---|
| Revenue | | | | |
| Operating profit | | | | |
| Operating margin | | | | |
| Other income | | | | |
| Interest | | | | |
| Net profit | | | | |
| EPS | | | | |

Verify at least revenue and net profit against a second source with `crosscheck`.

**5c. What was said, against what was done.**

- What did management promise on the last call, and did it happen?
- What are they promising now?
- Which questions on the concall did they not answer?

The unanswered question is usually the most useful part of a transcript.

**5d. Save it** to `reports/IN/<SYMBOL>/earnings-<quarter>.md`: the numbers table, what
actually changed in under 300 words, and what to watch next quarter.

Every company with a new result goes to step 6. A results read that does not touch the
thesis lines has not been done.

## Step 6 — the sell conditions

**The full check** runs for a Held or Watching company that has a `thesis.md`, when any
of these is true:

- its Next check date in Notion has passed
- step 5 read a new result for it
- step 4 found a move that touches a thesis line

**6a. Load** `thesis.md`: the five sentences, the assumptions, the red lines, the anchors,
and the last check.

**6b. Gather what is new.**

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py screener <SYMBOL> --only quarters shareholding documents
```

Plus anything significant since the last check, the current price and valuation, and any
change in promoter or institutional holding.

**6c. Each assumption.**

| # | Assumption | Was | Latest evidence | Now | Moved |
|---|---|---|---|---|---|

| Status | Meaning |
|---|---|
| 🟢 holds | the data supports it |
| 🟡 weakening | still acceptable, but the trend is against it |
| 🔴 damaged | the data does not support it |
| ⚫ broken | it has been disproved |

**6d. Each red line**, especially the two that fire in practice: promoter pledge, and any
change in the auditor's position.

| # | Red line | Triggered | Evidence |
|---|---|---|---|

Any trigger goes at the top of the whole weekly report in bold, not buried in a table.

**6e. The anchors.**

| Measure | On the thesis date | Last check | Now | Moved |
|---|---|---|---|---|

**6f. Health, out of 10.**

**Health = 10 − (3 × broken) − (2 × damaged) − (1 × weakening) − (5 × red lines
triggered)**, floored at 1.

| Health | Meaning |
|---|---|
| 9-10 | stronger than when written |
| 7-8 | intact, something weakening at the edge |
| 5-6 | one or two assumptions damaged, core still standing |
| 3-4 | several damaged, the base is shaking |
| 1-2 | a red line fired, or the core assumption is broken |

It answers two questions and stops:

1. **Is the thesis intact?** intact / weakening / damaged / broken
2. **What is the next check date?** after the next result, or after a named event

Then what changed since the last check, in under 400 words, and what to watch before the
next one.

**6g. Append a row** to the check log in `thesis.md`:

| Date | Health | What changed | Thesis state |
|---|---|---|---|

**A Watching company with no `thesis.md`** — researched before the sell conditions were
part of research — gets its new result checked against the Thesis lines and Red lines on
its Notion row instead: one line per thesis line, holds or not. Then flag it under Needs
attention: "no sell conditions written — run `/stock-research <SYMBOL>` before any buy".

**The light read** runs for every other holding: read the thesis lines from its Notion
row and say in one line whether anything in the last week speaks against them. Nothing
is written to `thesis.md` for a light read. Watching companies with no new result and no
check due get no light read; they appear only in the buy list in step 8.

> A 30% fall is not a reason to sell. A broken thesis is.

## Step 7 — what is due

- Results dates falling in the next two weeks, for Held and Watching companies, so the
  next checks know to expect them
- Any Companies row whose Next check date is within the next week
- Any candidate still sitting at Queued with no research done

## Step 8 — the buy list

For each company whose Status is **Researched** or **Watching** and whose Verdict
is **Pass** or **Conditional** — the same rows as the "Watching for price" view in
Notion:

| Company | Verdict | Fair value range | Close | Position vs range | Thesis health | Last researched |
|---|---|---|---|---|---|---|

Order them by how far below the range the price sits. That ordering is arithmetic.

Say plainly which one is furthest below its range and why the gap exists if the reason
is known — a result, a sector move, an index exclusion. Then stop.

**A recommendation, never an amount.** For each holding, and for each name on the buy
list, give a one-line recommendation — hold, review, or sell because a thesis line broke;
buy below a price, or wait — each with its comparison against a Nifty 50 index fund and
its confidence, as `CLAUDE.md` principle 2 sets out. How much money is free is decided by
Shivay on the day, so the check never reads, prints or suggests an amount. The action,
the amount and the timing are Shivay's.

## Step 9 — the report

```
# Portfolio check — <DD Mon YYYY>
Prices: NSE bhavcopy <date>

<any red line that fired, in bold, first>

## Holdings
<the table from step 3>

## Moves over 5%
<the four lines from step 4, per holding, or "none">

## Results read this week
<one line per Held or Watching company, with the earnings file, or "none">

## Sell conditions
<per company: health, state, what changed, next check — full checks first, then the
Watching companies checked against their Notion row, then the light reads, one line
each>

## Needs attention
Anything flagged, one line each, with the reason.

## Due soon
Results in the next two weeks, checks due next week, candidates stuck at Queued.

## Buy list
<the table from step 8>
```

A week where nothing moved, nothing reported and nothing is due is the normal case. Say
so in one line and end the report rather than filling the page.

## The Notion block

Write each company block to its Companies row, following `CLAUDE.md` § Notion is the
other half, and put the receipt line directly above the first block. The check block
itself is not written anywhere; it is only the summary.

One block for the check, then one per company that had a full check or a results read
in step 6.

```
NOTION
Check date:        <date>
Holdings checked:  <n>
Flagged:           <symbols, or none>
Checks now due:    <symbols, or none>
Check file:        reports/IN/_checks/<YYYYMMDD>.md
```

Each line is one column of the Companies row, by its exact name.

```
NOTION
Symbol:            <SYMBOL>
Thesis health:     <n, or blank for a Watching company with no thesis.md>
Next check:        <YYYY-MM-DD>
Notes (added):     <YYYY-MM-DD> check — thesis <intact | weakening | damaged | broken> · red lines fired <none, or which> · results <quarter, or none>
```
