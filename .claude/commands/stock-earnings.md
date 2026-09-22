# Results read

Read the results for $ARGUMENTS — a symbol and a quarter, for example `TITAN Q2FY27`.

The point is not to summarise the result. It is to answer one question: **do the thesis
lines still hold?**

Report goes to `reports/IN/<SYMBOL>/earnings-<quarter>.md`.

---

## Step 1 — the filing itself, not the coverage

```bash
python3 tools/india_data.py screener <SYMBOL> --only quarters documents
```

The documents section gives the exchange filing and the concall transcript. Read the
filing. Media coverage is for the reaction, not for the numbers.

## Step 2 — the numbers, against the quarter a year ago

Compare against the same quarter last year, not the previous quarter, unless the
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

Verify at least revenue and net profit against a second source:

```bash
python3 tools/india_data.py crosscheck <SYMBOL>
```

## Step 3 — the thesis lines

Read `reports/IN/<SYMBOL>/thesis.md`. For each line:

| # | Thesis line | What this quarter says | Holds? |
|---|---|---|---|

This is the whole purpose of the exercise. A results read that does not touch the thesis
lines has not been done.

## Step 4 — the red lines

Check each red line from `thesis.md` against this filing, especially the two that fire in
practice: promoter pledge, and any change in the auditor's position.

## Step 5 — what was said, against what was done

- What did management promise on the last call, and did it happen?
- What are they promising now?
- Which questions on the concall did they not answer?

The unanswered question is usually the most useful part of a transcript.

## Step 6 — the report

1. The numbers table
2. Thesis lines, checked
3. Red lines, checked
4. What actually changed, under 300 words
5. What to watch next quarter

No recommendation. If the thesis is damaged, say which line and by how much, then run
`/stock-thesis <SYMBOL> quarter` to update the health score.

## The Notion block

```
NOTION
Symbol:            <SYMBOL>
Quarter:           <quarter>
Revenue growth:    <n>% year on year
Margin:            <n>%, was <n>%
Thesis lines:      <n> of <n> hold
Red lines fired:   <none, or which>
Earnings file:     reports/IN/<SYMBOL>/earnings-<quarter>.md
Next check:        <date>
```
