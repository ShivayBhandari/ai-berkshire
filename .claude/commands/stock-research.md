# Deep research: the eight-step read

Research $ARGUMENTS — one NSE symbol. One company per run. Two companies in one run
produces two shallow reports.

Report goes to `reports/IN/<SYMBOL>/research-<YYYYMMDD>.md`.

Four lenses run through every step, and they are meant to disagree:

| Lens | Asks |
|---|---|
| **Business model** | is this a good business at all |
| **Moat and price** | is the advantage real, and is the price right |
| **Inversion** | how does this fail, and why would a smart person not buy it |
| **Long horizon** | will this still matter in ten years |

Do not resolve the disagreement early. A report where all four agree on page one has
skipped the work.

---

## Step 0 — how much can actually be known

Before any analysis, grade the company and write the grade at the top of the report.

| Grade | Looks like | The trap | What to do |
|---|---|---|---|
| **A** | listed for years, many analysts, heavy news coverage | consensus is strong, so the output matches the market price and there is no edge | spend the effort on the inversion: why is a smart person not buying |
| **B** | listed 1-3 years, thin coverage, some figures must be derived | plausible-looking numbers get filled into gaps and the report reads more certain than it is | mark every derived figure with its confidence, and separate "derived from data" from "assumed" |
| **C** | recent listing, ignored, or a small name | too little material reads as "bad business", when it may just be unfollowed | drop the templates, work from first principles |

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

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
python3 tools/india_data.py screener <SYMBOL>
python3 tools/india_data.py bhavcopy --symbol <SYMBOL>
python3 tools/india_data.py screener <SYMBOL> --only documents
```

Collect: revenue split and growth, 10-year margins, free cash flow, cash and debt,
market share against named competitors, the moat evidence, promoter and institutional
holding trend, management record, addressable market, the risk list, current valuation,
and the strongest argument on each side.

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

> **This report does not say buy or sell.** It gives the range, the thesis lines, and
> what would break them. The call is Shivay's.

Then the thesis lines — 2 to 4 statements that must stay true for this to work. Each one
specific enough to be checked against a quarterly result. "Good company" is not a thesis
line. "Operating margin stays above 12%" is.

Then the red lines — anything that, if it happens, means reopening the whole case.

## Output rules

1. Every figure has a source and a date.
2. Key data in tables.
3. Each step ends with its lens question answered.
4. Information grade at the top, with what could not be known.
5. At the end, separate **how confident the analysis is** — a function of how much
   material existed — from **how certain the business is**, which is a function of the
   business. They are not the same, and a C-grade company can be a better business than
   an A-grade one.
6. A C-grade company ends with a list of questions only first-hand work can answer:
   store visits, using the product, talking to a distributor.
7. Valuation is a range, never a point.
8. No recommendation. See step 8.

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

## The Notion block

End the file with exactly this, filled in:

```
NOTION
Symbol:            <SYMBOL>
Name:              <company name>
NSE industry:      <industry>
Info grade:        <A|B|C>
Fair value low:    <number>
Fair value high:   <number>
Price on report:   <close, with date>
Thesis lines:      <2-4 lines, one per row>
Red lines:         <the events that reopen the case>
Report:            reports/IN/<SYMBOL>/research-<YYYYMMDD>.md
Audit:             <pass | draft, audit not run>
Status:            Researched
Verdict:           (Shivay fills this)
```

Nothing else from this report goes into Notion.
