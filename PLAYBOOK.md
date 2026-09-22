# The investing workflow

Three parts. Each has one job.

| Part | Job | Never does |
|---|---|---|
| **This repo** | the method, the tools, every research file | hold what I own or what I decided |
| **Notion** | sectors, companies, verdicts, holdings, and the reminders | hold the long report |
| **Claude Code, on this laptop** | does one job when I type one command | run on its own |

Nothing is automatic. Notion reminds me, I run a command, Claude does that job and stops.

It runs locally because the NSE and BSE data sources only answer an Indian IP. A cloud
routine gets 403 and a timeout; this laptop gets the official files.

---

## The three commands

Run them from this folder, `~/Personal/ai-berkshire`.

| Command | Does | Takes | Writes |
|---|---|---|---|
| `/stock-screen <sector>` | whole sector down to 3 names, 8 elimination checks then 5 value checks | 10-15 min | `reports/IN/_screens/` |
| `/stock-research <SYMBOL>` | the six gates first (stops if they fail), then the eight-step read and a fair value range, then the sell conditions | 30-45 min | `reports/IN/<SYM>/research-*.md`, `reports/IN/<SYM>/thesis.md` |
| `/stock-check` | every holding: price against range, why anything moved over 5%, a results read for any new result, the sell-conditions check where one is due, and the buy list | 10 min, more in a results week | `reports/IN/_checks/`, `reports/IN/<SYM>/earnings-*.md` |

`/stock-screen` and `/stock-research` are the expensive ones. One deep read per sitting.

---

## The cycle

**1. Pick a sector.** Monthly reminder. `/stock-screen "Capital Goods"` or a theme from
`data/themes-in.json` — Defence, Railways, Power, Capital markets.

Survivors go into Notion as **Candidate**.

**2. I choose.** Move two or three to **Queued**. This gate is mine and it is the money
gate: a deep read is the costly job, so it only runs on names I picked.

**3. Research.** `/stock-research <SYMBOL>`, one company per sitting. The six gates run
first and stop a bad name before any valuation work. If they pass, the deep read gives
the fair value range, and the run ends by writing the sell conditions — the things that
must stay true and the events that mean reopening the case. They are written now, while
calm and before any money moves. Status becomes **Researched**.

**4. I write the verdict.** Pass, Conditional, Grey, or Reject. Claude never fills this.

**5. Wait for price.** Sunday reminder, `/stock-check`. It tells me which Pass and
Conditional names sit below their range, and it reads any
new result from a Watching name. It does not tell me to buy.

**6. I buy.** Then one line to Notion AI: `Bought 10 RVNL at 350 on Groww today`. It
writes the Transactions row, the Holdings Snapshot row, and sets the Companies row to
**Held** with the next check date — the day after the next quarterly result, or 90 days
out if that is not known. Nothing to run on the laptop — the sell conditions already
exist.

**7. Track.** The same Sunday `/stock-check`. It explains big moves, reads any new
result, and checks the sell conditions when one is due. Exit when a thesis line breaks,
not when the price falls.

---

## Cadence

| When | Reminder in Notion | Command |
|---|---|---|
| 1st of the month | Screen 3 sectors | `/stock-screen <sector>` × 3 |
| Every Sunday | Portfolio check | `/stock-check` |

That is all. Results, price moves and thesis checks are part of the Sunday check.

---

## Where each fact lives

| Fact | One home |
|---|---|
| The method, the filters, the thresholds | this repo, `.claude/commands/` |
| The long report | this repo, `reports/IN/` |
| Fair value range, thesis lines, verdict, status | Notion, Companies row |
| What I own and at what price | Notion, Holdings Snapshot. The rupees that paid for it are in Transactions |
| When the next check is due | the reminder on the Notion row |
| Prices and ratios | nowhere — fetched fresh each run |

Nothing appears twice. Each command writes its own fields into the Companies row, and
the report ends with that same block as a receipt: `Written to Notion ✔`, or the error
and the block to paste by hand. The rules for what a command may write are in
`CLAUDE.md` § Notion is the other half.

---

## What Claude may and may not write

| Claude writes | Shivay writes |
|---|---|
| the fair value range, computed by the tools | the verdict |
| the thesis lines, drafted | the approval of those lines |
| thesis health out of 10 | buy, add, hold, sell |
| "this line has broken", with the evidence | the amount and the timing |
| how far below its range a price sits | which candidate gets a deep read |

A report that ends in "buy this" is broken and gets rewritten.

---

## Token cost

Local runs come out of my own session limits.

| Command | Rough input | Sensible ceiling |
|---|---|---|
| `/stock-research` | 3-6M, less when it stops at the gates | one per sitting |
| `/stock-screen` | 1-2M | three sectors a month |
| `/stock-check` | 0.5M, plus 0.2-0.8M per holding with a new result (estimate) | weekly |

A normal month is three screens, four deep reads and four weekly checks. The deep reads
are most of it.

---

## Rules that do not bend

- Two independent sources for every number. A gap over 1% is written down, not smoothed.
- Never invent a figure. "NA — data not available", and say what would answer it.
- A report is not finished until `report_audit.py` passes.
- Never F&O, never intraday, never SME board.
- My employer's shares stay out of new buying.
- No standing cap on how much goes into stocks. I decide the amount at each buy.
- English everywhere.
