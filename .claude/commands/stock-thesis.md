# Thesis: write the sell conditions before buying

Run on $ARGUMENTS. Two modes, chosen automatically:

- `reports/IN/<SYMBOL>/thesis.md` does not exist → **write the thesis**
- it exists → **check the thesis**

Add `new` to force a rewrite, or `quarter` to check against the latest result.

> Most people do research, buy, and then hope. What is missing is the checking.
> The fix is to write the sell conditions down while calm.

---

# Mode A — write the thesis

## A1 — gather

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py screener <SYMBOL> --only profit-loss quarters ratios
```

If a `/stock-research` report exists for this company, take the fair value range and
thesis lines from it rather than deriving them again.

## A2 — the thesis in under 200 words

> I bought **<name>** at **₹<price>** on **<date>** because:
> 1. The business is **<what>**, and I understand how it earns.
> 2. Its moat is **<which>**, and it is widening or stable.
> 3. Management is **<judgement>**, because **<evidence>**.
> 4. The price was about **<fraction>** of value, and the safety came from **<what>**.
> 5. If I am wrong, the downside is limited because **<reason>**.

If those five cannot be completed, the thesis is not ready and neither is the position.

## A3 — the assumptions, made checkable

| # | Assumption | How it is checked | How often | Status |
|---|---|---|---|---|
| 1 | e.g. revenue growth stays above 15% | quarterly revenue | quarterly | 🟢 holds |
| 2 | e.g. operating margin stays above 20% | quarterly margin | quarterly | 🟢 holds |
| 3 | e.g. promoter pledge stays at zero | shareholding filing | quarterly | 🟢 holds |
| 4 | e.g. the number two does not close the gap | peer results | half-yearly | 🟢 holds |

Three to seven assumptions. Fewer means the thinking is thin; more means it is not
focused. Each one must be answerable from a filing, not from an opinion.

## A4 — the red lines

| # | Red line | Severity | What happens if it triggers |
|---|---|---|---|
| 1 | fraud, or accounts that cannot be trusted | fatal | exit fully |
| 2 | revenue falling two quarters running in the core business | serious | cut by half, reopen the case |
| 3 | the moat clearly matched by a competitor | serious | full re-research |
| 4 | regulation changes the business model | serious | revalue from scratch |
| 5 | promoter pledge appears, or a large unexplained sale | warning | investigate before anything else |
| 6 | auditor resigns or qualifies the accounts | serious | exit unless it is explained |

Red lines 5 and 6 are India-specific and they are the ones that actually fire.

> Selling has three reasons: the buy was a mistake, the business changed, or something
> better turned up. A falling price is not one of them.

## A5 — the valuation anchors

| Measure | At purchase | Good case | Base case | Bad case |
|---|---|---|---|---|
| Price | | | | |
| PE | | | | |
| Market cap (₹ cr) | | | | |
| Estimated value | | | | |
| Margin of safety | | | | |

## A6 — save it

Write `reports/IN/<SYMBOL>/thesis.md` with: date written, buy price and quantity, the
five sentences, the assumptions table, the red lines, the anchors, and an empty check log.

---

# Mode B — check the thesis

## B1 — load

Read the existing `thesis.md`: the five sentences, the assumptions, the red lines, and
the last check.

## B2 — gather what is new

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py screener <SYMBOL> --only quarters shareholding documents
```

Plus: the latest results, anything significant since the last check, the current price
and valuation, and any change in promoter or institutional holding.

## B3 — check each assumption

| # | Assumption | Was | Latest evidence | Now | Moved |
|---|---|---|---|---|---|

| Status | Meaning |
|---|---|
| 🟢 holds | the data supports it |
| 🟡 weakening | still acceptable, but the trend is against it |
| 🔴 damaged | the data does not support it |
| ⚫ broken | it has been disproved |

## B4 — check each red line

| # | Red line | Triggered | Evidence |
|---|---|---|---|

Any trigger goes at the top of the report in bold, not buried in a table.

## B5 — update the anchors

| Measure | At purchase | Last check | Now | Moved |
|---|---|---|---|---|

## B6 — the report

1. Thesis health, out of 10
2. Assumptions table
3. Red lines table
4. What changed this period, under 400 words
5. Valuation now
6. Where the thesis stands
7. What to watch before the next check

**Health = 10 − (3 × broken) − (2 × damaged) − (1 × weakening) − (5 × red lines
triggered)**, floored at 1.

| Health | Meaning |
|---|---|
| 9-10 | stronger than at purchase |
| 7-8 | intact, something weakening at the edge |
| 5-6 | one or two assumptions damaged, core still standing |
| 3-4 | several damaged, the base is shaking |
| 1-2 | a red line fired, or the core assumption is broken |

The report answers two questions and stops:

1. **Is the thesis intact?** intact / weakening / damaged / broken
2. **What is the next check date?** after the next result, or after a named event

It does not say add, hold, or sell. The health score and the broken lines are the
finding; the action is Shivay's.

> A 30% fall is not a reason to sell. A broken thesis is.

## B7 — append to the log

Add a row to the check log in `thesis.md`:

| Date | Health | What changed | Thesis state |
|---|---|---|---|

## The Notion block

```
NOTION
Symbol:            <SYMBOL>
Thesis health:     <n>/10
Thesis state:      <intact | weakening | damaged | broken>
Red lines fired:   <none, or which>
Next check:        <date, or the event>
Thesis file:       reports/IN/<SYMBOL>/thesis.md
```
