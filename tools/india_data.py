#!/usr/bin/env python3
"""India market data for the value-research workflow.

Every number printed here carries the source it came from, so a report can cite it.
Nothing is estimated: a field that could not be read prints "NA".
"""

import argparse
import csv
import io
import json
import os
import re
import sys
import time
import zipfile
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation

import requests
from bs4 import BeautifulSoup

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(REPO_ROOT, "local", "cache")
THEMES_FILE = os.path.join(REPO_ROOT, "data", "themes-in.json")

BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

NIFTY_500_URL = "https://nsearchives.nseindia.com/content/indices/ind_nifty500list.csv"
BHAVCOPY_URL = "https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_{ddmmyyyy}.csv"
SCREENER_URL = "https://www.screener.in/company/{symbol}/"
SCREENER_CONSOLIDATED_URL = "https://www.screener.in/company/{symbol}/consolidated/"
STOCKANALYSIS_URL = "https://stockanalysis.com/quote/nse/{symbol}/"
BSE_QUOTE_URL = (
    "https://api.bseindia.com/BseIndiaAPI/api/StockReachGraph/w"
    "?scripcode={scripcode}&flag=0&fromdate=&todate=&seriesid="
)

# BE is trade-for-trade: NSE moves a share there while it is under surveillance. It is
# still a mainboard share a long-term buyer can hold, so it is kept and marked rather than
# silently dropped. BZ (listing-rule breach) and the SME series SM/ST stay out.
MAINBOARD_SERIES = ("EQ", "BE")
WATCH_NOTE = "BE series: under exchange watch (trade-for-trade)"


def fetch(url, cache_hours=6, referer=None):
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_name = re.sub(r"[^A-Za-z0-9._-]", "_", url)[-180:]
    cache_path = os.path.join(CACHE_DIR, cache_name)

    if cache_hours and os.path.exists(cache_path):
        age_hours = (time.time() - os.path.getmtime(cache_path)) / 3600
        if age_hours < cache_hours:
            with open(cache_path, "rb") as cached:
                return cached.read()

    headers = dict(BROWSER_HEADERS)
    if referer:
        headers["Referer"] = referer

    response = requests.get(url, headers=headers, timeout=40)
    response.raise_for_status()
    with open(cache_path, "wb") as cached:
        cached.write(response.content)
    return response.content


def to_decimal(text):
    if text is None:
        return None
    cleaned = re.sub(r"[^0-9.\-]", "", str(text).replace(",", ""))
    if cleaned in ("", "-", ".", "-."):
        return None
    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return None


def last_trading_day(offset_days=0):
    day = date.today() - timedelta(days=offset_days)
    while day.weekday() >= 5:
        day -= timedelta(days=1)
    return day


# ---------------------------------------------------------------- universe


def load_universe():
    raw = fetch(NIFTY_500_URL, cache_hours=24 * 7, referer="https://www.nseindia.com/")
    rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
    return [
        {
            "symbol": row["Symbol"].strip(),
            "name": row["Company Name"].strip(),
            "industry": row["Industry"].strip(),
            "isin": row["ISIN Code"].strip(),
        }
        for row in rows
    ]


def load_themes():
    if not os.path.exists(THEMES_FILE):
        return {}
    with open(THEMES_FILE, encoding="utf-8") as handle:
        return json.load(handle)


def command_universe(args):
    universe = load_universe()
    themes = load_themes()

    if args.list_sectors:
        counts = {}
        for row in universe:
            counts[row["industry"]] = counts.get(row["industry"], 0) + 1
        print("NSE industries in Nifty 500 (source: NSE index constituent file)\n")
        for industry, count in sorted(counts.items(), key=lambda pair: -pair[1]):
            print(f"{count:4d}  {industry}")
        print("\nCustom themes (data/themes-in.json)\n")
        for theme, symbols in themes.items():
            print(f"{len(symbols):4d}  {theme}")
        return

    traded_on, bhav_rows = load_bhavcopy()
    series_by_symbol = {row["SYMBOL"]: row["SERIES"] for row in bhav_rows}

    selected = universe
    label = "Nifty 500"
    source_note = "NSE index constituent file"

    if args.sector:
        wanted = args.sector.lower()
        selected = [row for row in universe if wanted in row["industry"].lower()]
        label = f"industry ~ {args.sector}"

        # An NSE industry tag and a theme can carry the same name. The theme is usually
        # the wider universe, because most of a sector often sits below the Nifty 500.
        # Say so loudly rather than let a screen run on a fifth of the sector.
        twin = next((key for key in themes if key.lower() == wanted), None)
        if twin and len(themes[twin]) > len(selected):
            print(f"# WARNING: a theme named '{twin}' holds {len(themes[twin])} names, "
                  f"against {len(selected)} tagged '{args.sector}' in the Nifty 500.")
            print(f"# The theme is almost certainly what you want: "
                  f"--theme \"{twin}\"")
    elif args.theme:
        theme_key = next(
            (key for key in themes if key.lower() == args.theme.lower()), None
        )
        if theme_key is None:
            sys.exit(f"Unknown theme '{args.theme}'. Known: {', '.join(themes) or 'none'}")
        symbols = set(themes[theme_key])
        selected = [row for row in universe if row["symbol"] in symbols]
        label = f"theme {theme_key}"

        # A theme is often built around companies too small for the Nifty 500 — textiles
        # and defence especially. Resolve those against the bhavcopy instead of dropping
        # them. The bhavcopy holds only the mainboard series, so the SME board stays out,
        # which the house rules ban anyway.
        missing = symbols - {row["symbol"] for row in selected}
        if missing:
            mainboard = set(series_by_symbol)
            for symbol in sorted(missing & mainboard):
                selected.append({
                    "symbol": symbol,
                    "name": "",
                    "industry": "outside Nifty 500",
                    "isin": "",
                })
            unlisted = sorted(missing - mainboard)
            if unlisted:
                print(f"# not on the NSE mainboard, skipped: {', '.join(unlisted)}")
            source_note = (f"NSE index constituent file, plus the "
                           f"{traded_on:%d-%b-%Y} bhavcopy for names outside it")

    watched = sorted(row["symbol"] for row in selected
                     if series_by_symbol.get(row["symbol"]) == "BE")
    print(f"# {label} — {len(selected)} companies — source: {source_note}")
    if watched:
        print(f"# ⚠ {WATCH_NOTE}: {', '.join(watched)}")
    print("symbol,name,industry,isin,watch")
    for row in sorted(selected, key=lambda item: item["symbol"]):
        watch = WATCH_NOTE if row["symbol"] in watched else ""
        print(f"{row['symbol']},\"{row['name']}\",{row['industry']},{row['isin']},{watch}")


# ---------------------------------------------------------------- prices


def load_bhavcopy(day=None):
    day = day or last_trading_day()
    for attempt in range(5):
        candidate = day - timedelta(days=attempt)
        if candidate.weekday() >= 5:
            continue
        url = BHAVCOPY_URL.format(ddmmyyyy=candidate.strftime("%d%m%Y"))
        try:
            raw = fetch(url, cache_hours=12, referer="https://www.nseindia.com/")
        except requests.HTTPError:
            continue
        rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))
        cleaned = [
            {key.strip(): (value or "").strip() for key, value in row.items() if key}
            for row in rows
        ]
        return candidate, [row for row in cleaned if row.get("SERIES") in MAINBOARD_SERIES]
    raise SystemExit("No NSE bhavcopy found in the last 5 days")


def command_bhavcopy(args):
    day = datetime.strptime(args.date, "%d%m%Y").date() if args.date else None
    traded_on, rows = load_bhavcopy(day)
    print(f"# NSE full bhavcopy {traded_on:%d-%b-%Y} — {len(rows)} EQ and BE series rows")
    if args.symbol:
        wanted = args.symbol.upper()
        match = next((row for row in rows if row["SYMBOL"] == wanted), None)
        if match is None:
            sys.exit(f"{wanted} not in the {traded_on:%d-%b-%Y} bhavcopy")
        if match["SERIES"] == "BE":
            print(f"# ⚠ {WATCH_NOTE}")
        for key, value in match.items():
            print(f"{key:16s} {value}")
        return
    print("symbol,series,prev_close,open,high,low,close,volume,delivery_pct")
    for row in rows:
        print(
            f"{row['SYMBOL']},{row['SERIES']},{row['PREV_CLOSE']},{row['OPEN_PRICE']},"
            f"{row['HIGH_PRICE']},{row['LOW_PRICE']},{row['CLOSE_PRICE']},"
            f"{row['TTL_TRD_QNTY']},{row['DELIV_PER']}"
        )


# ---------------------------------------------------------------- screener


def screener_soup(symbol, consolidated=True):
    url = (SCREENER_CONSOLIDATED_URL if consolidated else SCREENER_URL).format(
        symbol=symbol.upper()
    )
    try:
        raw = fetch(url, cache_hours=6, referer="https://www.screener.in/")
    except requests.HTTPError:
        url = SCREENER_URL.format(symbol=symbol.upper())
        raw = fetch(url, cache_hours=6, referer="https://www.screener.in/")
    return BeautifulSoup(raw.decode("utf-8", "ignore"), "lxml"), url


def screener_top_ratios(soup):
    ratios = {}
    for item in soup.select("#top-ratios li"):
        name = item.select_one(".name")
        value = item.select_one(".value")
        if name and value:
            ratios[name.get_text(" ", strip=True)] = re.sub(
                r"\s+", " ", value.get_text(" ", strip=True)
            )
    return ratios


def screener_table(soup, section_id):
    section = soup.select_one(f"section#{section_id}")
    if section is None:
        return [], []
    table = section.select_one("table")
    if table is None:
        return [], []
    header = [cell.get_text(" ", strip=True) for cell in table.select("thead th")]
    rows = []
    for tr in table.select("tbody tr"):
        cells = [cell.get_text(" ", strip=True) for cell in tr.select("td")]
        if cells:
            rows.append(cells)
    return header, rows


def print_table(title, header, rows, limit=None):
    if not rows:
        print(f"\n## {title}: NA")
        return
    print(f"\n## {title}")
    print(" | ".join(header))
    for row in rows[:limit] if limit else rows:
        print(" | ".join(row))


def command_screener(args):
    symbol = args.symbol.upper()
    soup, url = screener_soup(symbol, consolidated=not args.standalone)
    ratios = screener_top_ratios(soup)
    if not ratios:
        sys.exit(f"Screener returned no ratios for {symbol} — check the symbol")

    print(f"# {symbol} — screener.in — {url}")
    print(f"# read at {datetime.now():%Y-%m-%d %H:%M} IST")
    print("\n## Headline ratios")
    for key, value in ratios.items():
        print(f"{key:18s} {value}")

    about = soup.select_one(".company-profile .about p")
    if about:
        print("\n## Business")
        print(re.sub(r"\s+", " ", about.get_text(" ", strip=True))[:800])

    for section_id, title, limit in (
        ("profit-loss", "Profit & loss (yearly)", None),
        ("quarters", "Quarterly results", None),
        ("balance-sheet", "Balance sheet", None),
        ("cash-flow", "Cash flow", None),
        ("ratios", "Ratios", None),
        ("shareholding", "Shareholding", None),
    ):
        if args.only and section_id not in args.only:
            continue
        header, rows = screener_table(soup, section_id)
        print_table(title, header, rows, limit)

    documents = soup.select_one("section#documents")
    if documents and (not args.only or "documents" in args.only):
        print("\n## Filings")
        for link in documents.select("a[href]")[:25]:
            text = re.sub(r"\s+", " ", link.get_text(" ", strip=True))
            href = link["href"]
            if text and href.startswith("http"):
                print(f"- {text} — {href}")


# ---------------------------------------------------------------- cross-check


def stockanalysis_stats(symbol):
    raw = fetch(STOCKANALYSIS_URL.format(symbol=symbol.upper()), cache_hours=6)
    soup = BeautifulSoup(raw.decode("utf-8", "ignore"), "lxml")
    stats = {}
    for table in soup.select("table"):
        for tr in table.select("tr"):
            cells = tr.select("td")
            if len(cells) == 2:
                key = cells[0].get_text(" ", strip=True)
                value = cells[1].get_text(" ", strip=True)
                if key and value and key not in stats:
                    stats[key] = value
    price_node = soup.select_one("div[class*='text-4xl'], .text-4xl")
    if price_node:
        stats["Quoted price"] = price_node.get_text(" ", strip=True)
    return stats


CRORE = Decimal(10) ** 7
MAGNITUDES = {"T": Decimal(10) ** 12, "B": Decimal(10) ** 9, "M": Decimal(10) ** 6}


def to_crore(text):
    """Read a money figure in any of the forms these sources use, return ₹ crore."""
    if not text:
        return None
    cleaned = str(text).replace(",", "").replace("₹", "").strip()

    crore_match = re.search(r"([\d.]+)\s*Cr", cleaned, re.IGNORECASE)
    if crore_match:
        return to_decimal(crore_match.group(1))

    magnitude_match = re.search(r"([\d.]+)\s*([TBM])\b", cleaned)
    if magnitude_match:
        amount = to_decimal(magnitude_match.group(1))
        if amount is None:
            return None
        return amount * MAGNITUDES[magnitude_match.group(2)] / CRORE

    absolute = to_decimal(cleaned)
    return absolute / CRORE if absolute else None


def bracketed_percent(text):
    if not text:
        return None
    match = re.search(r"\(([\d.]+)\s*%\)", str(text))
    return to_decimal(match.group(1)) if match else None


def range_ends(text):
    if not text:
        return None, None
    numbers = re.findall(r"[\d,]+\.?\d*", str(text).replace("₹", ""))
    if len(numbers) < 2:
        return None, None
    values = sorted(value for value in (to_decimal(n) for n in numbers) if value)
    return (values[-1], values[0]) if len(values) >= 2 else (None, None)


def command_crosscheck(args):
    symbol = args.symbol.upper()
    soup, screener_link = screener_soup(symbol)
    screener = screener_top_ratios(soup)
    analysis = stockanalysis_stats(symbol)
    traded_on, bhav_rows = load_bhavcopy()
    bhav = next((row for row in bhav_rows if row["SYMBOL"] == symbol), None)

    screener_high, screener_low = range_ends(screener.get("High / Low"))
    analysis_high, analysis_low = range_ends(analysis.get("52-Week Range"))

    print(f"# {symbol} — two-source cross-check — {datetime.now():%Y-%m-%d %H:%M} IST")
    print(f"# source 1: screener.in  ({screener_link})")
    print(f"# source 2: stockanalysis.com/quote/nse/{symbol}/")
    print(f"# source 3: NSE bhavcopy {traded_on:%d-%b-%Y} (official close)")
    if bhav and bhav["SERIES"] == "BE":
        print(f"# ⚠ {WATCH_NOTE}")

    comparisons = [
        ("Price", to_decimal(screener.get("Current Price")),
         to_decimal(analysis.get("Quoted price")),
         to_decimal(bhav["CLOSE_PRICE"]) if bhav else None, "₹"),
        ("Previous close", None, to_decimal(analysis.get("Previous Close")),
         to_decimal(bhav["PREV_CLOSE"]) if bhav else None, "₹"),
        ("Market cap", to_crore(screener.get("Market Cap")),
         to_crore(analysis.get("Market Cap")), None, "₹ cr"),
        ("PE", to_decimal(screener.get("Stock P/E")),
         to_decimal(analysis.get("PE Ratio")), None, "x"),
        ("Dividend yield", to_decimal(screener.get("Dividend Yield")),
         bracketed_percent(analysis.get("Dividend")), None, "%"),
        ("52-week high", screener_high, analysis_high, None, "₹"),
        ("52-week low", screener_low, analysis_low, None, "₹"),
    ]

    flagged = []
    print(f"\n{'field':16s} {'screener':>14s} {'stockanalysis':>14s} {'NSE':>12s}  {'unit':6s} gap")
    for label, first, second, official, unit in comparisons:
        gap = "—"
        if first is not None and second is not None and first != 0:
            difference = abs(first - second) / first * 100
            gap = f"{difference:.1f}%"
            if difference > 1:
                gap += "  FLAG"
                flagged.append(label)
        elif second is not None and official is not None and second != 0:
            difference = abs(second - official) / second * 100
            gap = f"{difference:.1f}%"
            if difference > 1:
                gap += "  FLAG"
                flagged.append(label)

        def show(value):
            return f"{value:,.2f}" if isinstance(value, Decimal) else "NA"

        print(
            f"{label:16s} {show(first):>14s} {show(second):>14s} "
            f"{show(official):>12s}  {unit:6s} {gap}"
        )

    market_cap = to_crore(screener.get("Market Cap"))
    price = to_decimal(screener.get("Current Price"))
    if market_cap and price:
        implied_shares = market_cap * CRORE / price
        print(f"\nImplied shares outstanding = market cap / price = {implied_shares:,.0f}")
        print("Check that against the annual report's share count before using it.")

    if flagged:
        print(f"\nFLAGGED, gap over 1%: {', '.join(flagged)}")
        print("Take the figure from the annual report or the exchange filing, and write")
        print("in the report which source you used and why. Do not average the two.")
    else:
        print("\nBoth sources agree within 1% on every field above.")


# ---------------------------------------------------------------- bse live


def command_bse(args):
    raw = fetch(BSE_QUOTE_URL.format(scripcode=args.scripcode), cache_hours=0,
                referer="https://www.bseindia.com/")
    payload = json.loads(raw.decode("utf-8", "ignore"))
    for key in ("Scripname", "CurrDate", "CurrTime", "CurrVal", "PrevClose",
                "HighVal", "LowVal"):
        print(f"{key:12s} {payload.get(key, 'NA')}")


# ---------------------------------------------------------------- cli


def build_parser():
    parser = argparse.ArgumentParser(
        description="India market data: NSE universe, official closes, Screener "
                    "fundamentals, two-source cross-check."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    universe = subparsers.add_parser("universe", help="Nifty 500 list, by sector or theme")
    universe.add_argument("--sector", help="NSE industry, partial match")
    universe.add_argument("--theme", help="custom theme from data/themes-in.json")
    universe.add_argument("--list-sectors", action="store_true",
                          help="print sectors and themes with counts")
    universe.set_defaults(handler=command_universe)

    bhavcopy = subparsers.add_parser("bhavcopy", help="official NSE daily prices")
    bhavcopy.add_argument("--date", help="DDMMYYYY, default last trading day")
    bhavcopy.add_argument("--symbol", help="print one company's full row")
    bhavcopy.set_defaults(handler=command_bhavcopy)

    screener = subparsers.add_parser("screener", help="fundamentals from screener.in")
    screener.add_argument("symbol")
    screener.add_argument("--standalone", action="store_true",
                          help="standalone numbers instead of consolidated")
    screener.add_argument("--only", nargs="*",
                          help="sections: profit-loss quarters balance-sheet cash-flow "
                               "ratios shareholding documents")
    screener.set_defaults(handler=command_screener)

    crosscheck = subparsers.add_parser("crosscheck", help="two-source check, flags gaps >1%%")
    crosscheck.add_argument("symbol")
    crosscheck.set_defaults(handler=command_crosscheck)

    bse = subparsers.add_parser("bse", help="live BSE quote by scrip code")
    bse.add_argument("scripcode")
    bse.set_defaults(handler=command_bse)

    return parser


if __name__ == "__main__":
    arguments = build_parser().parse_args()
    arguments.handler(arguments)
