# Sector screen: whole sector down to 3 names

Screen $ARGUMENTS — an NSE industry, a theme from `data/themes-in.json`, or a list of
symbols. The job is to **eliminate**, not to pick. A name that survives is not good yet;
it has only earned a deep read.

Report goes to `reports/IN/_screens/<sector>-<YYYYMMDD>.md`.

---

## Step 0 — build the universe

```bash
python3 tools/india_data.py universe --list-sectors
python3 tools/india_data.py universe --sector "<NSE industry>"
python3 tools/india_data.py universe --theme "<theme>"
```

The Nifty 500 file is the universe. It is official NSE data with official industry tags.

**A name marked ⚠ "BE series: under exchange watch" is screened like any other.** NSE has
put it under surveillance, usually after unusual price or trading activity. That is a
caution, not a fault. Carry the ⚠ mark next to its name in every table of the report.

**A theme always wins over an NSE industry of the same name.** Several sector names exist
as both — Textiles, Power, Capital markets. The theme is the wider universe, because most
of a sector often sits below the Nifty 500 cut. Run `universe --list-sectors` first, and if
a theme of that name exists, use `--theme`.

**The report's first line must state which universe was used and how many names were in
it.** A screen that ran on a fifth of a sector and does not say so is worse than no screen.

Anything the tool prints as "outside Nifty 500" is a smaller company — list it in the
report under **Not screened** with its name, and say why (below the Nifty 500 cut).
Never silently drop it.

If the universe is over 30 names, screen the largest 30 by market cap first and say in
the report how many were left out and at what market cap the line fell.

## Step 1 — hard elimination, 8 checks

For each company:

```bash
python3 tools/india_data.py screener <SYMBOL> --only profit-loss ratios shareholding cash-flow
```

| # | Check | Eliminate when | What it measures |
|---|---|---|---|
| 1 | 10-year average ROE | below 8%, or below 10% for an asset-heavy business — textiles, cement, metals, power, paper, sugar (decided, see `CLAUDE.md`) | can it beat the cost of capital at all |
| 2 | 5-year cumulative free cash flow | negative | is the profit real cash |
| 3 | Interest cover (EBIT / interest) | below 2x | can it service its debt |
| 4 | Operating margin, long-run | below 10% | does it have any pricing power |
| 5 | Operating cash flow / net profit, 5-year average | below 0.7 | does the profit get collected |
| 6 | Net margin, long-run | below 5% | does profit survive a bad year |
| 7 | 5-year equity dilution, non-merger | above 20% | is management diluting me |
| 8 | Promoter pledge | above zero — **hard fail**. A promoter stake falling with no stated reason is a **flag**, not a fail (decided, see `CLAUDE.md`) | the Indian red flag the other seven miss |

Checks 1-7 are upstream's. Check 8 is an India addition: a pledged promoter stake is
how Indian mid-caps fail, and it does not show up in any margin. A pledge and a stake
sale are not the same thing — `CLAUDE.md` says which one eliminates and which one only
flags, and that is not a judgement call to make again per screen.

Mark each ✅ pass, ❌ fail, ⚠️ borderline with the number.

### Three exemptions

An exemption is only granted when **every** condition under it holds. Write the
exemption and its evidence into the report.

**A. Building phase** — exempts check 1.
1. Listed under 10 years
2. Operating margin above 30%
3. Operating cash flow positive in each of the last 2 years

**B. Margin by choice** — exempts check 6.
1. Operating margin above 30%
2. Net margin already back above 5%, or clearly rising

**C. Thin margin, high turnover** — exempts checks 4 and 6.
1. ROE above 20%
2. Operating cash flow / net profit above 1.0
3. The business earns from turnover, fees or subscription rather than markup

### Sectors where a check does not apply

| Sector | Skip | Use instead |
|---|---|---|
| Banks, NBFCs, insurers | check 3 | net interest margin, gross NPA trend, capital adequacy, provision cover |
| REITs and InvITs | check 1 | ROE on core operating profit, distribution yield and cover |
| Cyclicals — metals, cement, sugar, chemicals | single-year figures | full-cycle averages covering one peak and one trough |
| Listed under 5 years | nothing | use all available years and label it "short data window" |

**Missing data is not a pass and not a fail.** Mark it "NA — data not available" and
carry the company forward flagged.

## Step 2 — five value checks, down to 10 or fewer

| # | Check | Pass | Relax when |
|---|---|---|---|
| 1 | Valuation | PE reasonable against its own 10-year range and its peers | high grower, PEG below 1.5 |
| 2 | ROE | above 15%, or a clear 3-year improvement | asset-heavy business |
| 3 | Cash flow | operating cash flow positive and above 70% of net profit | — |
| 4 | Debt | debt to equity below 0.6 | utilities, power and infra up to 1.0 |
| 5 | Moat | 3 stars or better out of 5 | — |

Moat types: brand and pricing power, switching cost, network effect, scale and cost
advantage, licence or regulatory or resource barrier.

**Where this table says "relax" without a number, pick one, and put it in the report as
its own line: the number used, and that it is an assumption rather than a decided rule.**
Two screens cannot be compared if each quietly chose a different bar. If the same relaxed
bar gets used twice, it should stop being an assumption and go into `CLAUDE.md`.

Keep rule: 5 of 5 pass, keep. 4 pass and 1 close, keep and mark amber. Under 4, drop
with the reason written down. If more than 12 survive, raise the moat bar to 4 stars and
run it again.

## Step 3 — short analysis on each survivor

250-400 words each:

- **The business in one line** — what it sells, to whom, how it gets paid
- **Financial quality** — revenue and profit growth, margin, ROE, cash flow, and the one
  most important change of the last two years
- **Moat** — which type, the evidence, and whether it is widening or narrowing
- **Top 3 risks**
- **Valuation now** — PE, PB, dividend yield, where each sits in its own 10-year range,
  against peers. One word: expensive, fair, or cheap
- **Into the final three?** yes or no, with the reason

## Step 4 — the final three

Not the top three by score. Three that complement each other:

- at least one high-certainty, low-excitement compounder
- at least one moderate-certainty grower
- optionally one high-risk, high-payoff name

If a sector cannot fill three honestly, write "two picks and one to watch". Never pad
the list.

## Step 5 — the report

```
# <Sector> screen — <DD Mon YYYY>

## What was screened
Universe size, source, and what was left out and why.

## Summary table
| Company | Symbol | 1 ROE | 2 FCF | 3 Interest | 4 OPM | 5 OCF/PAT | 6 Net margin | 7 Dilution | 8 Pledge | Result |

## Survived (N)
## Eliminated (N)
| Company | Failed check | The number | Why it was dropped |
## Exempted (N)
| Company | Exemption | The numbers | Why it was granted |
## Not screened
| Company | Why |

## Short analysis — one section per survivor

## The final three
| Company | Type | Why it is here | Main risk | What would change my mind |

## Sector verdict
Pass rate N/M. Is this sector worth more of my time, in two lines.

## Information grade
| Area | A/B/C | Note |
Company financials / valuation freshness / competitive picture / management

A = enough to trust. B = gaps that do not change the conclusion. C = large gaps,
conclusions are provisional.

## Sources
Every figure's source, grouped: NSE, Screener, stockanalysis, annual reports, news.

## Notion block
<Written to Notion ✔ <YYYY-MM-DD HH:MM IST> | Notion write failed: <the error> — paste these lines by hand>
For each survivor, one line — skipped ones marked "already in Companies, skipped":
SYMBOL | Name | Sector | info grade | status Candidate | screen file path
```

## Step 6 — audit before it counts

```bash
python3 tools/report_audit.py extract --report reports/IN/_screens/<file>.md
```

Re-read each sampled figure from its source, fill the JSON, then:

```bash
python3 tools/report_audit.py verdict --results '<filled JSON>' --report <file>.md
```

A fail means fix the number and sample again. A screen that has not passed the audit is
a draft, and the report must say so at the top.

## Step 7 — write the survivors to Notion

One new Companies row per survivor, following `CLAUDE.md` § Notion is the other half:
Name, Symbol, Sector, Info grade, Status `Candidate`, Report file. A company that already
has a row is skipped and left exactly as it is. Then put the receipt line above the
Notion block.

## Biases to fight, out loud

| Bias | How it shows up | What to do |
|---|---|---|
| Large-cap pull | big companies have more coverage so they read better | rank on the checks, never on how much was written |
| Story pull | a stock that has run hard looks like a good business | separate real revenue from the narrative; check the numbers before the news |
| Recency | this year's good numbers hide a weak decade | checks 1, 5 and 6 are all long-run on purpose |
| Filling gaps | writing a plausible number where data is missing | "NA — data not available", every time |

## Last rule

Every eliminated company keeps its name and its reason in the report. A screen you
cannot re-read in six months and check is not a screen.
