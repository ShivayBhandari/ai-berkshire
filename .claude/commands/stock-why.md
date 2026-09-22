# Why did it move?

Explain the price move in $ARGUMENTS. Quick, factual, three minutes.

No file is written unless the reason turns out to touch a thesis line. Then it goes to
`reports/IN/<SYMBOL>/note-<YYYYMMDD>.md`.

---

## Step 1 — size the move

```bash
python3 tools/india_data.py bhavcopy --symbol <SYMBOL>
```

Take the close, the previous close, the day's range, and the delivery percentage.

Delivery percentage matters: a big move on low delivery is traders, a big move on high
delivery is people taking or leaving positions.

## Step 2 — find the cause, in this order

1. A company filing — `python3 tools/india_data.py screener <SYMBOL> --only documents`
2. A result, an order win, a block deal, a rating action
3. Something sector-wide — check two or three peers in the same bhavcopy. If the whole
   sector moved, it is not company news
4. Something index-wide — if the market moved, say so
5. No identifiable cause

Option 5 is a real answer. Say "no cause found in filings or sector moves" rather than
attaching the move to whatever news happened to be nearby.

## Step 3 — the answer, in four lines

- **Move:** ₹<from> to ₹<to>, <n>%, delivery <n>%
- **Cause:** <what, with the source> or <none found>
- **Scope:** this company only / the sector / the market
- **Thesis:** does this touch a thesis line — yes, and which, or no

## Step 4 — only if it touches a thesis

Write the note file and flag the company for a `/stock-thesis` run. Otherwise say so and
stop. Most price moves are not news about the business, and recording them all would
bury the ones that matter.

No action advice. A price move is not a reason to do anything.
