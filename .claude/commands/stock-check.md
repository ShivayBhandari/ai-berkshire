# Weekly portfolio check

Run the weekly check. With no argument, take the holdings from Notion. With symbols —
`/stock-check TITAN,RVNL` — check only those.

Report goes to `reports/IN/_checks/<YYYYMMDD>.md`.

---

## Step 1 — what is held

From Notion:
- the Companies database, rows where Status is **Held** — gives the thesis lines, the
  fair value range, and the next check date
- the Transactions and Financial Profile pages — gives quantity, buy price, and
  uncommitted capital

If Notion cannot be reached, say so and ask for the symbols. **Do not keep a second copy
of the holdings in this repo.** Notion is the only place that knows what is owned.

## Step 2 — prices, from the official file

```bash
python3 tools/india_data.py bhavcopy
```

One download covers every holding. Take the close, the volume and the delivery
percentage from it. Do not fetch prices one stock at a time.

For anything that moved more than 5% in the week, also:

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
```

## Step 3 — the table

| Holding | Qty | Buy price | Close | Gain | Fair value range | Where the price sits | Thesis |
|---|---|---|---|---|---|---|---|

"Where the price sits" is one of: **below the range**, **inside the range**, **above the
range**. That is arithmetic against the range from the last research report, not a view.

## Step 4 — thesis lines, quickly

For each holding, read the thesis lines from its Notion row and say whether anything in
the last week speaks against them. This is the light version. Anything that looks
damaged gets flagged for a full `/stock-thesis <SYMBOL>` run, which is where the real
check happens.

Only follow up where there is a reason: a result published, a large price move, a filing,
a sector-wide event.

## Step 5 — what is due

- Results dates falling in the next two weeks
- Any Companies row whose Next check date has passed
- Any candidate still sitting at Queued with no research done

## Step 6 — capital

From Financial Profile: what is uncommitted.

Then, for each company whose Status is **Researched** and whose Verdict is **Pass**:

| Company | Fair value range | Close | Position vs range | Thesis health | Last researched |
|---|---|---|---|---|---|

Order them by how far below the range the price sits. That ordering is arithmetic.

Say plainly which one is furthest below its range and why the gap exists if the reason
is known — a result, a sector move, an index exclusion. Then stop.

**No buy instruction.** The report gives the prices, the ranges, the gaps and the free
capital. The buy, the amount and the timing are Shivay's.

## Step 7 — the report

```
# Portfolio check — <DD Mon YYYY>
Prices: NSE bhavcopy <date>

## Holdings
<the table from step 3>

## Needs attention
Anything flagged, one line each, with the reason and the command to run.

## Due in the next two weeks
Results, checks past due, candidates stuck at Queued.

## Capital and the Pass list
Uncommitted: ₹<amount>
<the table from step 6>

## Nothing-happened note
If nothing moved and nothing is due, say that in one line and end the report.
```

A week where nothing needs doing is the normal case. Say so in one line rather than
filling the page.

## The Notion block

```
NOTION
Check date:        <date>
Holdings checked:  <n>
Flagged:           <symbols, or none>
Checks now due:    <symbols, or none>
Check file:        reports/IN/_checks/<YYYYMMDD>.md
```
