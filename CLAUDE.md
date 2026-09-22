# ai-berkshire — Shivay's fork, Indian market, English only

A fork of [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire). The upstream
repo researches Chinese, Hong Kong, US and Taiwan companies and writes every report in
Chinese. This fork researches **Indian listed companies and writes in English**.

The method is theirs. The market, the data sources and the language are mine.

---

## The two hard rules

**1. English only.** Every report, table, note and commit message. Upstream's
`skills/*.md` are Chinese reference material, not instructions. The English versions in
`.claude/commands/` are what runs.

**2. Claude computes, Shivay decides.** Claude may compute a fair value range, list the
risks, and say that a thesis line has broken. Claude never writes the buy or sell call
and never fills the Verdict field. A report that ends in "buy this" is wrong.

---

## Where things live

| What | Where |
|---|---|
| The English method | `.claude/commands/*.md` |
| Research reports | `reports/IN/<SYMBOL>/research-<YYYYMMDD>.md` |
| Pre-buy checklists | `reports/IN/<SYMBOL>/checklist-<YYYYMMDD>.md` |
| Thesis, one per holding, updated forever | `reports/IN/<SYMBOL>/thesis.md` |
| Sector screens | `reports/IN/_screens/<sector>-<YYYYMMDD>.md` |
| Weekly portfolio checks | `reports/IN/_checks/<YYYYMMDD>.md` |
| Custom sector themes | `data/themes-in.json` |
| Downloaded pages, caches, tokens | `local/` — gitignored, never committed |
| What I own, what I decided, when the next check is due | **Notion**, not here |

Everything of mine goes under `reports/IN/`, which is registered in
`reports/_index/config.json` under `skip_dirs`. Upstream's `reports/`, its live-record
and screening folders are theirs — never write into them. This is what keeps
`git pull upstream main` clean.

Do not run `tools/reports_index.py`. It indexes upstream's Chinese reports and ignores
mine. It already reports itself as stale on a fresh clone; that is upstream's state, not
a signal about this fork.

---

## Indian data sources

Every number needs **two independent sources**. A gap over 1% goes into the report, not
smoothed over.

| Rank | Source | What it gives | How |
|---|---|---|---|
| 1 | **NSE bhavcopy** | official daily close, volume, delivery % for every stock | `india_data.py bhavcopy` |
| 2 | **Screener.in** | 12 years of P&L, balance sheet, cash flow, ratios, shareholding | `india_data.py screener` |
| 3 | **stockanalysis.com** | second source for price, market cap, PE, dividend | `india_data.py crosscheck` |
| 4 | **BSE filings and annual report PDFs** | the primary document | links from `screener --only documents` |
| 5 | **NSE Nifty 500 constituent file** | the sector universe with official industry tags | `india_data.py universe` |

Rules that came out of testing these, not from guessing:

- `nseindia.com` API endpoints return 403 to scripts, even with cookie priming. Do not
  try. The archive host `nsearchives.nseindia.com` works.
- The NSE and BSE endpoints **only answer an Indian IP**. They work on this laptop and
  fail from a cloud sandbox. That is why this system runs locally.
- Screener's consolidated page is the default. Use `--standalone` for a holding company
  or a bank, where consolidated hides the picture.
- The annual report beats every website. When two sites disagree, open the PDF.

### Units

₹ crore is the working unit for company money. 1 crore = 10,000,000. Sources that print
T/B/M must be converted before comparing — `crosscheck` already does this. No bare
number goes into a report without its unit.

---

## The tools, and where they are not optional

No valuation number enters a report from the model's head.

| Tool | Use it for | Mandatory in |
|---|---|---|
| `tools/india_data.py` | prices, fundamentals, universe, two-source check | every command |
| `tools/financial_rigor.py` | market cap identity, PE/PB/ROE/FCF yield, three-scenario | `/stock-research` |
| `tools/terminal_value.py` | ten-year IRR, terminal PE, the three hard constraints | any report quoting a 10-year return |
| `tools/report_audit.py` | 15% re-sample of the finished report | `/stock-research`, `/stock-screen` |

`financial_rigor.py` and `terminal_value.py` print Chinese labels. Their **numbers** go
into the report; translate the labels.

### Discount rate for Indian companies

`terminal_value.py` in this fork carries an **INR band**, added here because upstream
only had CNY, USD and HKD, and Indian rates fail all three.

| Input | Band | Where it comes from |
|---|---|---|
| **r**, cost of capital | 11%-14%, use **12%** | floor = 10-year G-Sec 7.05% + mature-market premium 4.23%. Ceiling = 7.05% + Damodaran's full India ERP 7.08%, which double-counts country risk on purpose so the ceiling stays conservative |
| **g**, perpetual growth | **at most 5%** | RBI's 4% inflation target plus about 1 point of real growth |
| **r - g** | **at least 5 percentage points** | a narrower denominator makes the answer a function of g, not of the business |
| **rf**, risk-free | **7.05%** | India 10-year G-Sec, 21 Sep 2026 |

Sources: India 10Y G-Sec 7.05% on 2026-09-21; Damodaran country risk premiums,
5 January 2026 vintage — India total ERP 7.08%, country risk premium 2.85%, so the
mature-market premium is 4.23%.

Run the audit with `--currency INR`:

```bash
python3 tools/terminal_value.py audit --currency INR --r 0.12 --roic <roic> \
  --g 0.03,0.04,0.05 --rf 0.0705 --beta 1.0
```

**Re-check the G-Sec yield before any report that quotes a ten-year return.** It moves.
If it has moved more than about half a point from 7.05%, update `RF["INR"]` and the band
in `tools/terminal_value.py`, and say in the report which yield was used.

`g` does not move when `r` moves. `g` is a view on the economy after the terminal year;
`r` is the return being demanded. Sensitivity tests move `r` only.

---

## Thresholds Shivay decided

Everything else in the method came from upstream. These two were open questions the
first two screens hit, and they are settled. A screen must use these numbers, not pick
its own.

### A pledge is not a stake sale

**Decided 22 September 2026.**

| What | Treatment |
|---|---|
| Promoter pledge above zero | **hard fail.** The company is eliminated |
| Promoter stake falling with no stated reason | **a flag.** The name survives, and the deep read has to explain the sale |

The two are different things and the first version of check 8 wrongly treated them
alike. A pledge is a lien — a lender can force a sale nobody at the company controls,
which is what made Ramco Cements a red line on 22 Sep 2026. A stake sold to institutions
with control retained is supply, not a lien. Treating a Page or a KPR Mill block deal the
same as Ramco's pledged 9.46% would eliminate good businesses for the wrong reason.

A flag is not nothing. It stays on the row, and a deep read that cannot explain the sale
must say so.

### The ROE bar is 10% for asset-heavy, 8% for everything else

**Decided 22 September 2026.**

| Kind of business | Ten-year average ROE below this eliminates |
|---|---|
| Asset-heavy — textiles, cement, metals, power, paper, sugar | **10%** |
| Everything else | **8%** |

Upstream's single 8% bar lets an asset-heavy business through on a number that, in a
capital-hungry sector, means it is destroying value. The screen was already relaxing the
bar for these sectors; it was choosing the relaxed number itself each run, which is how
two screens stop being comparable.

---

## House rules that override any analysis

- Never F&O, never intraday, never the SME board.
- My employer's shares stay out of new buying.
- Free data sources only.
- Never invent a number to fill a gap. Write "NA" and list what would answer it.
- A report is not finished until `report_audit.py` returns a pass.
- Credentials never get typed into a report. They live in Notion Documents.

---

## Notion is the other half

This repo holds the research. Notion holds the state — what I own, what I decided, and
when the next check is due. Nothing is written in both places.

The three commands write to Notion themselves, through the Notion tools, and only ever
to one table:

**Companies** — `collection://c44ceb7d-fae7-4ae9-a50f-395b63b62730`

| Command | May write |
|---|---|
| `/stock-screen` | one new row per survivor: Name, Symbol, Sector, Info grade, Status `Candidate`, Report file. A company that already has a row is skipped — never a second row, never an overwrite |
| `/stock-research` | that company's row: every line of the report's Notion block. Status becomes `Researched` only when the row is new, `Candidate` or `Queued`; any other Status is left exactly as it is. Create the row if the company has none |
| `/stock-check` | each checked row: Thesis health, Next check, and a Notes line after a full check |

Never, from any command:

- **Verdict.** Shivay fills it.
- **Status `Watching`, `Held`, `Exited` or `Rejected`.** Those are Shivay's calls.
- **Any other page or table** — not Transactions, not Holdings Snapshot, not Items, not a
  comment.

How to write:

1. **Read the row first.** Find it by `Symbol`. Two rows with the same Symbol is an error
   to report, not a choice to make.
2. **Notes are only ever added to.** Put a new paragraph at the end, starting with the
   date, and keep every word above it. Notes hold long research notes, and any property
   write replaces the whole field. So read the current Notes in `rows` mode first — SQL
   mode can drop formatting and links — then write the old text plus the new paragraph.
3. **Dates** go in as `date:<Column>:start` with a `YYYY-MM-DD` value.
4. **Use the exact option names** for Status, Sector, Info grade and Checklist, as the
   table defines them.

**The receipt.** Every report still ends with its Notion block — exactly the fields
written, and nothing more. Directly above it, one line:

- `Written to Notion ✔ <YYYY-MM-DD HH:MM IST>`, or
- `Notion write failed: <the error> — paste this block by hand`

A failed write never stops the report from being written. The block is what makes the
failure recoverable.

---

## Pulling upstream

```bash
git fetch upstream
git merge upstream/main
```

`CLAUDE.md` is the only file that conflicts by design, because this one replaced theirs
(theirs is kept at `docs/CLAUDE.upstream.zh.md`). Keep mine:

```bash
git checkout --ours CLAUDE.md && git add CLAUDE.md
```

Their `skills/` will change. That is useful — read the diff, and fold anything worth
having into `.claude/commands/` in English.
