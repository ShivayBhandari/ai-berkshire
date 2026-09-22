# Notion AI setup prompt — investing layer

Paste into Notion AI inside the Second Brain page. Run **Part 0 alone first**, read what
it reports back, then run Parts 1 to 6 one at a time.

---

## Rules for you, Notion AI — these apply to every part below

1. **Read before you write.** Part 0 is a reading task. Do not create or edit anything
   until I have seen what you found.
2. **English only.** Every property name, option, row, sentence.
3. **No duplication.** If a fact already lives somewhere in this workspace, link to it
   with a page mention. Never copy it into a second place.
4. **Never replace a whole page.** Only add blocks, or edit the exact text I name.
   Replacing a page that contains a database destroys the database.
5. **Do not edit the 22 existing rows** in the Second Brain rules database, except for
   the one single-line edit named in Part 3.
6. **Do not invent a new reminder system.** This workspace already fires phone
   notifications from a date property with a reminder set on it. Use that same mechanism.
7. **Write the way this workspace writes:** short sentences, plain everyday words,
   tables where things are compared, no padding, no "moreover" or "leverage".
8. If a step cannot be done as written, stop and tell me why. Do not do something
   similar instead.

---

## PART 0 — read and report, change nothing

Read these and report back before touching anything:

1. The **Second Brain rules** database. Report: its exact property names and types, the
   full option list of the `Layer` select, the full option list of `Used by`, and the
   highest `Order` number currently used.
2. Rows in that database numbered 1, 12, 13, 14, 19, 21 and 22. Report the name and the
   `When to read` text of each.
3. The **Second Brain** landing page. Report the exact heading names in order, and the
   exact contents of the table under "Where everything lives".
4. The **Transactions** database and the **Financial Profile** page. Report their
   property names, and say which parent page each one sits under.
5. The **Important Dates** database. Report its properties and how a dated entry is
   normally created.
6. The **Items** database. Report its properties, the `Type` options, the `Status`
   options, and how a repeating task is normally set up.

Then answer one question in your own words: **where should a new database about
individual companies sit, so that it is beside Transactions and Financial Profile rather
than somewhere new?** Name the parent page. Do not create it yet.

---

## PART 1 — create the Companies database

Create a database called **Companies** under the parent page you named in Part 0.

Description, one line: *One row per Indian listed company that has entered the research
funnel. The long research report lives in the ai-berkshire repo on the laptop; this row
holds only the state.*

Properties, exactly these:

| Property | Type | Options / notes |
|---|---|---|
| Name | Title | the company's full name |
| Symbol | Text | NSE symbol, uppercase, e.g. TITAN |
| Sector | Select | see Part 2 for the option list |
| Status | Select | Candidate, Queued, Researched, Watching, Held, Exited, Rejected |
| Info grade | Select | A, B, C |
| Checklist | Select | Not run, Passed, Failed, Grey |
| Verdict | Select | Pass, Conditional, Grey, Reject |
| Fair value low | Number, rupee format | |
| Fair value high | Number, rupee format | |
| Price on report | Number, rupee format | |
| Thesis lines | Text | the 2 to 4 things that must stay true |
| Red lines | Text | the events that mean reopening the case |
| Thesis health | Number | 1 to 10 |
| Last researched | Date | |
| Next check | Date | this is the one that carries the reminder |
| Report file | Text | path inside the repo, e.g. reports/IN/TITAN/research-20260922.md |
| Notes | Text | |

Two property descriptions must be set, because they carry a rule:

- On **Verdict**: `Shivay fills this. No AI writes this field.`
- On **Next check**: `Set a reminder on this date. This is what buzzes the phone.`

Then set up the default view:
- Table view named **All companies**
- Group by `Status`
- Sort by `Symbol` ascending
- Show: Name, Symbol, Sector, Status, Verdict, Fair value low, Fair value high,
  Thesis health, Next check
- Hide the rest
- Turn cell wrapping on

Add one more view, a table named **Watching for price**, filtered to `Status` is
`Researched` and `Verdict` is `Pass`, showing Name, Symbol, Fair value low,
Fair value high, Last researched.

Create no rows. The database starts empty.

---

## PART 2 — the Sector options

Give the `Sector` select these options. The first twenty are the official NSE industry
names from the Nifty 500 list. The last four are themes the NSE does not tag.

Financial Services, Capital Goods, Healthcare, Automobile and Auto Components,
Consumer Services, Fast Moving Consumer Goods, Information Technology, Chemicals,
Metals and Mining, Power, Oil Gas and Consumable Fuels, Consumer Durables, Services,
Construction, Construction Materials, Realty, Telecommunication, Textiles,
Media Entertainment and Publication, Diversified, Defence, Railways,
Capital markets, Other

---

## PART 3 — add the rules

The **Second Brain rules** database is where every rule lives, one rule per row. Add
three new rows. Use the next three `Order` numbers after the current highest one that
you reported in Part 0.

For all three rows: `Used by` = Notion AI chat. Layer = a new select option called
**Investing** — create that option.

### Row A — "Investing — where the stock system lives"

`When to read`: *Any question about shares, a company I own or am researching, a stock
verdict, or a fair value range.*

Body:

> The stock research system has two halves and they never hold the same fact.
>
> | Half | Holds | Where |
> |---|---|---|
> | The repo | the method, the python tools, every research report, every thesis file | `~/Personal/ai-berkshire` on the laptop, a fork of github.com/xbtlin/ai-berkshire |
> | Notion | what I own, what I decided, and when the next check is due | the Companies database, Transactions, Financial Profile |
>
> The long report is never copied into Notion. A Companies row carries only the fields
> in Part 1 above, plus the report's file path.
>
> It runs on the laptop, not in a cloud routine, because the NSE and BSE data sources
> only answer an Indian IP address. A cloud routine gets a 403 or a timeout.
>
> Nothing here runs by itself. A reminder fires, Shivay types one command, it does that
> one job and stops.

Link this row to the rows about Transactions, Financial Profile and Reminders using the
`Read with` relation.

### Row B — "Investing — the cycle and the commands"

`When to read`: *When asked what to do next about stocks, or which step comes after
which.*

Body:

> | Step | Command on the laptop | Notion changes to |
> |---|---|---|
> | 1. Screen a sector | `/stock-screen "<sector>"` | new rows, Status **Candidate** |
> | 2. Shivay picks | — | Status **Queued** |
> | 3. Pre-buy gates | `/stock-checklist <SYMBOL>` | Checklist field filled |
> | 4. Deep read | `/stock-research <SYMBOL>` | Status **Researched**, fair value range, thesis lines |
> | 5. Shivay decides | — | **Verdict** filled |
> | 6. Wait for price | `/stock-check` weekly | nothing, unless something is flagged |
> | 7. Buy | — | a Transactions row, Status **Held**, Next check set |
> | 8. Write the thesis | `/stock-thesis <SYMBOL>` | Thesis lines, Red lines |
> | 9. Track | `/stock-thesis`, `/stock-earnings <SYM> <quarter>` | Thesis health, Next check moved |
>
> Exit happens when a thesis line breaks, not when the price falls.

Link this row to Row A with `Read with`.

### Row C — "Investing — what an AI may and may not write"

`When to read`: *Before writing anything into a Companies row, or answering any question
that ends in should I buy.*

Body:

> | An AI may write | Shivay writes |
> |---|---|
> | the fair value range, when a tool computed it | the Verdict |
> | draft thesis lines and red lines | the approval of those lines |
> | the thesis health score | buy, add, hold, sell |
> | "this thesis line has broken", with the evidence | the amount and the timing |
> | how far below its range a price sits | which candidate gets a deep read |
>
> An AI never answers "should I buy this". It gives the range, the gap and the thesis
> state, and stops.
>
> Never invent a number. Write "NA — data not available" and say what would answer it.
>
> Every figure needs two independent sources. A gap over 1% gets written down, never
> averaged away.
>
> Never F&O, never intraday, never the SME board. My employer's shares stay out of new buying.

Link this row to Row A and Row B with `Read with`.

### The one edit to an existing row

Open the row named **System map and layering** (Order 1). Add one line to its body,
inside the existing list of layers, matching the style of the lines already there:

> Investing — company research state. Rows in Companies. The reports themselves live in
> the ai-berkshire repo on the laptop, not in Notion.

Change nothing else in that row.

---

## PART 4 — update the landing page

On the **Second Brain** landing page, find the table under the heading
**Where everything lives**. Add one row to it, in the same style as the rows already
there, with a real page mention in the first cell:

| Cell | Content |
|---|---|
| First column | a page mention of the new **Companies** database |
| Remaining columns | match what the other rows do — a short line saying: One row per company I research or own. The full report stays in the ai-berkshire repo on the laptop. |

Add nothing else to that page. Do not add a new heading or a new section. Do not touch
the child pages or databases below the table.

---

## PART 5 — the three repeating tasks

Create three rows in the **Items** database, using whatever this workspace's normal
pattern is for a repeating task — you reported that pattern in Part 0. Each one carries a
reminder on its date so the phone buzzes.

| Task name | Repeats | Body |
|---|---|---|
| Screen three sectors | monthly, on the 1st | Run `/stock-screen "<sector>"` three times in the ai-berkshire repo. Survivors become Candidate rows in Companies. |
| Portfolio check | weekly, Sunday | Run `/stock-check` in the ai-berkshire repo. It reads holdings from Notion and prices from the NSE bhavcopy. |
| Results due this week | weekly during results season | Check Important Dates for results dates, then run `/stock-earnings <SYMBOL> <quarter>` for each. |

Set them to the times this workspace normally uses for a morning task. Do not invent a
new notification method — use the same date-with-reminder that every other Item uses.

---

## PART 6 — report back

Tell me, in a short list:

1. Where you put the Companies database, and its URL
2. Every property you created, and any you could not create and why
3. The three new rule rows, their Order numbers, and their URLs
4. The exact line you added to System map and layering
5. The exact row you added to the landing page table
6. The three Items you created and when each fires
7. **Anything you changed that I did not ask for** — say it plainly, even if it seemed
   like an improvement

Then stop. Do not add rows to Companies. Do not write any research.
