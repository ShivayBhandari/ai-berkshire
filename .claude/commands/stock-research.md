# Research: gates, deep read, sell conditions

Research $ARGUMENTS — one NSE symbol. One company per run. Two companies in one run
produces two shallow reports.

Three parts, in order, in one run:

1. **The gates** — rule out a bad decision fast. A company that fails here does not need
   a valuation, and the run stops.
2. **The deep read** — the eight steps, ending in a fair value range.
3. **The sell conditions** — written now, while calm and before any buy.

Reports go to `reports/IN/<SYMBOL>/research-<YYYYMMDD>.md` and
`reports/IN/<SYMBOL>/thesis.md`.

Four lenses run through the deep read, and they are meant to disagree:

| Lens | Asks |
|---|---|
| **Business model** | is this a good business at all |
| **Moat and price** | is the advantage real, and is the price right |
| **Inversion** | how does this fail, and why would a smart person not buy it |
| **Long horizon** | will this still matter in ten years |

Do not resolve the disagreement early. A report where all four agree on page one has
skipped the work.

---

## Step 0 — identify, and how much can actually be known

Full company name, NSE symbol, BSE code, industry. Not listed, or SME board? Stop and
write "not investable under house rules".

Then grade the company and write the grade at the top of the report.

| Grade | Looks like | The trap | What to do |
|---|---|---|---|
| **A** | listed for years, many analysts, heavy news coverage | consensus is strong, so the output matches the market price and there is no edge | spend the effort on the inversion: why is a smart person not buying |
| **B** | listed 1-3 years, thin coverage, some figures must be derived | plausible-looking numbers get filled into gaps and the report reads more certain than it is | mark every derived figure with its confidence, and separate "derived from data" from "assumed" |
| **C** | recent listing, ignored, or a small name | too little material reads as "bad business", when it may just be unfollowed | drop the templates, work from first principles |

For a C-grade company, "not enough data" in a gate is neither a pass nor a fail. It is
grey, and the report says what would resolve it.

**First principles, for a C:**
1. Who is the customer, and why do they pay?
2. What brings them back — habit, lock-in, or new value each time?
3. Could a competitor with ₹1,000 crore copy this?
4. What has management actually decided, and what do those decisions reveal?

**Bias check, to re-read at the end:**
- Is my sense of certainty coming from the business, or from the amount of material?
- If half the material vanished, would the conclusion change?
- Does this read like the consensus? If yes, where is the edge?
- Could a business this good be this quiet?

## Step 1 — collect and verify the data

Collect once. The gates and the deep read both work from this.

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py screener <SYMBOL>
python3 tools/india_data.py bhavcopy --symbol <SYMBOL>
python3 tools/india_data.py screener <SYMBOL> --only documents
```

Collect: revenue split and growth, 3-year growth, 10-year ROE and margins, free cash flow, cash and
debt, market share against named competitors and its direction, the moat evidence,
promoter holding and pledge, institutional holding trend, management record, addressable
market, the risk list, current valuation, anything significant in the last 6 months, and
the strongest argument on each side.

### Verification that is not optional

Every one of these runs as a command. None is done in the head.

**Market cap identity:**
```bash
python3 tools/financial_rigor.py verify-market-cap \
  --price <price> --shares <share count> --reported <reported mcap> --currency INR
```

**Each key figure, across two sources:**
```bash
python3 tools/financial_rigor.py cross-validate \
  --field revenue --values '{"screener": 20412, "annual report": 20412}' --unit crore
```
Run it for revenue, net profit, and cash and debt separately.

**Valuation ratios:**
```bash
python3 tools/financial_rigor.py verify-valuation \
  --price <price> --eps <eps> --bvps <book value per share> \
  --fcf-per-share <fcf per share> --dividend <dividend per share>
```

Rules:
1. Two independent sources per key figure.
2. When they disagree, the annual report or the exchange filing wins, and the report
   says which was used and why. Never average them.
3. A tool that reports a large deviation stops the analysis until the cause is found.
4. The tool output goes into an appendix called **Data verification record**.

Indian traps worth naming: consolidated against standalone; ₹ crore against ₹ lakh;
promoter holding against promoter pledge; whether "debt" includes lease liabilities;
face value changes and bonus issues breaking a per-share series.

---

# Part 1 — the gates

Their purpose is to **rule out a bad decision**, not to find the best idea.

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
and stop the run here.

## Gate 2 — is it a good business?

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

**Hard stop:** a real integrity problem is a 1 star and ends the run.

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

## The quick reject list

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

## The gate result

| Result | What happens next |
|---|---|
| ✅ Passed, N of 6 | go on to Part 2 |
| ❌ Failed | name the red line that triggered. Write the report with Part 1 only and stop |
| ❓ Grey | name the one unresolved question and what would settle it. Write the report with Part 1 only and stop |

Stars are whole stars, 1 to 5, no halves.

---

# Part 2 — the deep read

## Step 2 — the business

- One sentence: what is this business
- Revenue split, and how it has moved
- Ten-year margin and return trend, as a table
- One-time sale or repeat revenue? product, service, or platform?
- How locked in is the customer
- Margin against named peers, and the reason for the difference
- Operating leverage: what happens to profit when revenue moves 10%

**Ask:** what is good about this business, in one sentence?

## Step 3 — the moat

| Type | The test |
|---|---|
| Brand and pricing power | can it raise price without losing volume? find the instance |
| Switching cost | what does it cost a customer to leave |
| Network effect | does each new user make it better for the others |
| Scale and cost | how much cheaper is it per unit than the number two |
| Licence, patent, resource | how many years of lead, and can it be bought |

Score each 1-5 with evidence. Then: was it wider or narrower five years ago, and which
way is it heading.

**Ask:** will this moat still be here in ten years, and what would destroy it?

## Step 4 — how it fails

- A table of failure paths: path, rough likelihood, damage
- A historical parallel — a company that stood here before, and what happened to it
- The short case, written as well as its best holder would write it
- My own biases on this name: am I anchored on a price, or on a story
- India-specific: related-party transactions, auditor changes or qualifications, promoter
  pledge, regulated tariffs, a single government customer, land and approval risk

**Ask:** where am I most likely to be wrong, and why would a smart person be short?

## Step 5 — management

- The key decisions of the last five years: date, decision, outcome, a grade
- Capital allocation: return on what was reinvested, acquisitions, buybacks, dividend
- Are they aligned: holding, pledge, pay, and any selling
- Governance: related-party dealings, auditor history, board independence
- For a PSU: who really decides, and what happens when policy changes
- Does it keep working if the CEO leaves

**Ask:** if this CEO retired tomorrow, would the business still be this good?

## Step 6 — the long horizon

- Is this industry going through a real, permanent shift, or a cycle
- The closest historical parallel
- Addressable market, the growth curve, and the ceiling
- Where it sits in its value chain, and who holds the pricing power there
- Customer and supplier concentration
- For India specifically: is the growth coming from the country's own build-out, or from
  one government order book

**Ask:** looking back from twenty years out, is this a lasting business or a moment?

## Step 7 — value and margin of safety

Every number here comes from a tool.

**Where the market is now:** market cap, PE, PB, dividend yield, EV/EBITDA, each against
its own 10-year range and against peers.

**Reverse DCF:** what growth does today's price already assume?

**Three scenarios:**
```bash
python3 tools/financial_rigor.py three-scenario \
  --price <price> --eps <eps> --shares <shares in crore> \
  --growth <good> <base> <bad> --pe <good PE> <base PE> <bad PE> \
  --years 3 --currency INR
```

**Ten-year view — only if the report quotes a 10-year return.**

The exit multiple has one legal source, the perpetual growth model. Never a peer
comparison, because that just carries today's price into the future.

Before any number is published:
```bash
python3 tools/terminal_value.py audit \
  --currency INR --r 0.12 --roic <steady state ROIC> \
  --g 0.03,0.04,0.05 --rf 0.0705 --beta 1.0 \
  --discrete-risks "<risk>:<scenario|tail|probability|unmodelled>,..."
```

Read `CLAUDE.md` for the rupee bands: r 11-14% (use 12%), g at most 5%, rf 7.05%. The three constraints, and what fails them:

| # | Constraint | Fails when |
|---|---|---|
| 1 | r and g in the same currency | r from one currency's band and g from another's |
| 2 | r − g at least 5 percentage points | any case narrower. A thin denominator means g is driving the answer |
| 3 | A discrete risk never goes into r or beta | a licence loss, a tariff reset, a policy change put into the discount rate |

Constraint 3 matters because raising r punishes year 10 far more than year 1, while a
policy risk is roughly flat across the years. Putting it in r gets the timing of the risk
backwards. Give it its own scenario and a probability.

Then:
```bash
python3 tools/terminal_value.py pe --roic <roic> --g <g> --r 0.12
python3 tools/terminal_value.py irr --profit <terminal year profit> \
  --mcap <market cap today> --pe <exit PE> --years 10 --payout <yield minus dilution>
```

The report must state: the r used and the g ceiling it pairs with, at least two values of
r and whether the ranking holds at both, the r − g width in each case, and every discrete
risk left unmodelled.

**Ask:** if r is wrong by 2 percentage points, does the conclusion flip? If it does, the
conclusion is about the discount rate, not the company.

**Ask:** if the market shut for five years, would this price still be acceptable?

## Step 8 — the memo

| Area | Finding | Confidence |
|---|---|---|
| Business quality | | |
| Moat | | |
| Management | | |
| Biggest risk | | |
| Ten-year position | | |
| Value | | |

Then a **fair value range** — a low and a high in rupees, with the assumption behind
each end.

Then, and this is the boundary:

> **This report does not say buy or sell.** It gives the range, the sell conditions, and
> what would break them. The call is Shivay's.

---

# Part 3 — the sell conditions, before any buy

> Most people do research, buy, and then hope. What is missing is the checking.
> The fix is to write the sell conditions down while calm.

They are written here, at the end of the research, so they exist before any money moves.
There is nothing to run after a buy. The weekly `/stock-check` checks them from then on.

## Step 9 — the reason, in five sentences

> I would buy **<name>** at about **₹<price>** because:
> 1. The business is **<what it does>**, and I understand how it earns.
> 2. Its moat is **<which one>**, and it is **widening / stable / narrowing**.
> 3. Management is **<judgement>**, because **<evidence>**.
> 4. The price is about **<fraction>** of estimated value, and the margin of safety
>    comes from **<what>**.
> 5. If I am wrong, the downside is limited because **<reason>**.

Under 200 words. **Five sentences that cannot be completed means the case is not ready.**
Say so at the top of the report.

## Step 10 — the assumptions, made checkable

| # | Assumption | How it is checked | How often | Status |
|---|---|---|---|---|
| 1 | e.g. revenue growth stays above 15% | quarterly revenue | quarterly | 🟢 holds |
| 2 | e.g. operating margin stays above 20% | quarterly margin | quarterly | 🟢 holds |
| 3 | e.g. promoter pledge stays at zero | shareholding filing | quarterly | 🟢 holds |
| 4 | e.g. the number two does not close the gap | peer results | half-yearly | 🟢 holds |

Three to seven assumptions. Fewer means the thinking is thin; more means it is not
focused. Each one must be answerable from a filing, not from an opinion. "Good company"
is not an assumption. "Operating margin stays above 12%" is.

## Step 11 — the red lines

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

## Step 12 — the valuation anchors

| Measure | On the report date | Good case | Base case | Bad case |
|---|---|---|---|---|
| Price | | | | |
| PE | | | | |
| Market cap (₹ cr) | | | | |
| Estimated value | | | | |
| Margin of safety | | | | |

## Step 13 — save the thesis file

Write `reports/IN/<SYMBOL>/thesis.md` with: the date written, the price on the report
date, the five sentences, the assumptions table, the red lines, the anchors, and an empty
check log:

| Date | Health | What changed | Thesis state |
|---|---|---|---|

The buy price and quantity are not written here. They live in Notion, and the weekly
check reads them from there.

If `thesis.md` already exists, keep its check log, replace everything above it, and say
in the research report what changed from the old version.

---

## Output rules

1. Every figure has a source and a date. An estimate is labelled "estimate".
2. Key data in tables.
3. Each deep-read step ends with its lens question answered.
4. Information grade at the top, with what could not be known.
5. At the end, separate **how confident the analysis is** — a function of how much
   material existed — from **how certain the business is**, which is a function of the
   business. They are not the same, and a C-grade company can be a better business than
   an A-grade one.
6. A C-grade company ends with a list of questions only first-hand work can answer:
   store visits, using the product, talking to a distributor.
7. Valuation is a range, never a point.
8. No buy or sell instruction anywhere. The gates say whether they were passed; the buy
   is Shivay's.

## The audit gate

```bash
python3 tools/report_audit.py extract --report reports/IN/<SYMBOL>/research-<date>.md
```

Re-read each sampled figure from its source. Fill `fetched_value`, `fetched_source`,
`fetched_value2`, `fetched_source2`. Then:

```bash
python3 tools/report_audit.py verdict --results '<filled JSON>' --report <file>
```

Pass means every sampled figure is within 1%. A fail means fix that figure and sample
again.

If the report quotes a 10-year IRR, run the `terminal_value.py audit` once more with the
parameters that actually ended up in the report. The step 7 audit ran before the writing,
and r and g often move during it. The last audit is the one that counts.

A run that stopped at the gates skips the audit gate, and says so in the Notion block.

## The Notion block

End the file with exactly this, filled in. Each line is one column of the Companies
row, by its exact name. Then write it to that row, following `CLAUDE.md` § Notion is
the other half, and put the receipt line directly above the block.

```
NOTION
Name:              <company name>
Symbol:            <SYMBOL>
Sector:            <one of the Sector options>
Status:            Researched, or unchanged if the row was already past Queued
Info grade:        <A | B | C>
Checklist:         <Passed | Failed | Grey>
Fair value low:    <number, or blank if stopped at the gates>
Fair value high:   <number, or blank if stopped at the gates>
Price on report:   <close on the report date>
Thesis lines:      <the assumptions, one per line, or blank if stopped at the gates>
Red lines:         <the red lines, or the one that triggered at the gates>
Last researched:   <YYYY-MM-DD>
Report file:       reports/IN/<SYMBOL>/research-<YYYYMMDD>.md
Notes (added):     <YYYY-MM-DD> research — gates <N>/6 · audit <pass | not run | skipped, stopped at the gates>
Verdict:           (Shivay fills this)
```

Nothing else from this report goes into Notion.
