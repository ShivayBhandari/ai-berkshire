# Pre-buy checklist: six gates

Run the checklist on $ARGUMENTS — one or more NSE symbols, comma separated.

This is the gate before money moves. Its purpose is to **rule out a bad decision**, not
to find the best idea. It is faster than `/stock-research` and it is the minimum before
a buy. If both are being run, run the checklist first: a company that fails gate 1 does
not need a valuation.

Report goes to `reports/IN/<SYMBOL>/checklist-<YYYYMMDD>.md`, or
`reports/IN/_screens/checklist-<YYYYMMDD>.md` when comparing several.

---

## Step 0 — identify and grade

For each name: full company name, NSE symbol, BSE code, industry. Not listed, or SME
board? Stop and write "not investable under house rules".

Then the information grade:

| Grade | Effect on the checklist |
|---|---|
| A | run it normally, but watch the consensus trap — clear numbers are not the same as a certain business |
| B | mark the confidence on every derived figure |
| C | do not force the six tables full. "Not enough data to judge" is an honest answer |

For a C-grade company, "not enough data" is neither a pass nor a fail. It is a grey
verdict, and the report says what would resolve it. Do not confuse "little material"
with "bad business".

## Step 1 — collect

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py screener <SYMBOL>
```

Pull: 10-year ROE, margins, free cash flow, the valuation set, 3-year growth, debt and
cash, market share and its direction, moat evidence, management record, promoter and
pledge, and anything significant in the last 6 months.

---

## Gate 1 — can I understand this business?

- Can I say in one sentence how it makes money?
- What will it be selling in ten years?
- Which two or three variables decide whether it wins?
- Is what I know from real reading, or from someone's tip?

| Stars | Meaning |
|---|---|
| 5 | very simple, very durable |
| 4 | clear but needs some domain knowledge |
| 3 | understandable, but ten years out is genuinely unclear |
| 2 | too many business lines, or an industry mid-upheaval |
| 1 | outside what I know |

**Hard stop:** if the money-making cannot be stated plainly, mark "outside my circle"
and stop the checklist here.

## Gate 2 — is it a good business?

```bash
python3 tools/financial_rigor.py verify-valuation \
  --price <price> --eps <eps> --bvps <bvps> --fcf-per-share <fcf ps> --dividend <dps>
```

| Measure | This company | Reference |
|---|---|---|
| ROE, 5-year average | | above 15% good, above 20% excellent |
| Operating margin | | above 20% suggests pricing power |
| Free cash flow | | positive every year, and close to net profit |
| Capital intensity | | asset-light beats asset-heavy |
| Debt | | interest-bearing debt under 3 years of profit |
| Promoter pledge | | zero. Anything above zero is a finding, not a footnote |

5 stars = all six good. Subtract a star per miss. Free cash flow negative for three
straight years is a 1.

## Gate 3 — is the moat deep enough?

| Type | Present | Evidence | Widening or narrowing |
|---|---|---|---|
| Brand and pricing power | | | |
| Switching cost | | | |
| Network effect | | | |
| Scale and cost | | | |
| Licence, patent, resource | | | |

Then: could a competitor with ₹1,000 crore copy this in three years?

5 stars = several moats, widening. 1 star = none visible.

## Gate 4 — can management be trusted?

| Item | Reading |
|---|---|
| Do they deliver what they promised | |
| Capital allocation record — buybacks, dividends, acquisitions | |
| Are they aligned — holding, pledge, pay, selling | |
| Owner or caretaker | |
| Governance — related-party deals, auditor changes, board | |
| Does it run without the CEO | |

**Hard stop:** a real integrity problem is a 1 star and ends the checklist.

For a PSU, add: who sets the price, and what a policy change does to the earnings.

## Gate 5 — is the price low enough?

| Measure | Now | Where in its own 10-year range |
|---|---|---|
| PE | | |
| Forward PE | | |
| PB | | |
| Dividend yield | | |
| Free cash flow yield | | |

```bash
python3 tools/financial_rigor.py three-scenario \
  --price <price> --eps <eps> --shares <shares in crore> \
  --growth <good> <base> <bad> --pe <good PE> <base PE> <bad PE> --currency INR
```

Then two questions:
- If the thesis is wrong, how much is lost at this price?
- If it halves, would I add? If not, the position is too big or the thesis is too thin.

5 stars = half of estimated value or less. 1 star = clearly expensive.

## Gate 6 — am I deciding, or reacting?

- Am I buying because it has already gone up?
- Am I buying because someone recommended it?
- If it stopped trading for five years, would that be acceptable?
- Can I write the reason for buying in under 200 words?

## Step 2 — the mirror test

Write it out, filled in:

> I am buying **<name>** at **₹<price>** because:
> 1. The business is **<what it does>**, and I understand how it earns.
> 2. Its moat is **<which one>**, and it is **widening / stable / narrowing**.
> 3. Management is **<judgement>**, because **<evidence>**.
> 4. The price is about **<fraction>** of estimated value, and the margin of safety
>    comes from **<what>**.
> 5. If I am wrong, the downside is limited because **<reason>**.

**Five sentences that cannot be completed means no buy.** Mark it pass or fail.

## Step 3 — quick reject list

Any one of these triggering is a reject, whatever the stars said:

- Cannot say how it makes money
- Free cash flow negative three years running with no visible turn
- An integrity or governance problem
- The advantage is being eroded and the erosion looks permanent
- It only works if someone later pays more
- Any promoter pledge above zero (a promoter stake sale with no stated reason is a flag, not a reject — see `CLAUDE.md`)
- Losing the whole amount would actually hurt
- The reason for buying is mostly that others are buying, or that it has run up
- The reason cannot be written in 200 words

## Step 4 — the verdict

| Verdict | Meaning |
|---|---|
| ✅ Passed, N of 6 | clear to go into deep research, or to buy if research already exists |
| ❌ Failed | name the red line that triggered |
| ❓ Grey | name the one unresolved question and what would settle it |

For several companies, finish with:

| Company | Passed? | Circle | Business | Moat | Management | Price | One line |
|---|---|---|---|---|---|---|---|

## Output rules

1. Stars are whole stars, 1 to 5, no halves.
2. Every figure carries its source and date. An estimate is labelled "estimate".
3. Each company gets its own section: six gates, key figures, top risks, mirror test,
   verdict.
4. No buy or sell instruction. The verdict says whether the gates were passed; the buy
   is Shivay's.

## The Notion block

```
NOTION
Symbol:            <SYMBOL>
Checklist:         <passed N/6 | failed | grey>
Gate scores:       circle <n> / business <n> / moat <n> / management <n> / price <n>
Red line hit:      <none, or which>
Mirror test:       <pass | fail>
Checklist file:    reports/IN/<SYMBOL>/checklist-<YYYYMMDD>.md
```
