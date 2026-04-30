"""
Shift Schedule Date column in a GHL CSV by N days OR re-anchor to a new start.

Usage:
    python shift_dates.py --input old.csv --output new.csv --shift 21
    python shift_dates.py --input old.csv --output new.csv --start 2026-05-05 --cadence weekday

When --start is given, the cadence applies (re-spaces dates).
When --shift is given, simple +N days per row preserves cadence.
"""
import argparse, csv, sys
from datetime import datetime, timedelta


def next_date(d, cadence):
    while True:
        d += timedelta(days=1)
        wd = d.weekday()
        if cadence == "daily": return d
        if cadence == "weekday" and wd < 5: return d
        if cadence == "mwf" and wd in (0, 2, 4): return d
        if cadence == "tt" and wd in (1, 3): return d


def first_date(start, cadence):
    d = datetime.strptime(start, "%Y-%m-%d")
    wd = d.weekday()
    if cadence == "daily": return d
    if cadence == "weekday" and wd < 5: return d
    if cadence == "mwf" and wd in (0, 2, 4): return d
    if cadence == "tt" and wd in (1, 3): return d
    return next_date(d - timedelta(days=1), cadence)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--shift", type=int, help="days to add per row")
    g.add_argument("--start", help="YYYY-MM-DD new anchor")
    p.add_argument("--cadence", default="weekday", choices=["daily", "weekday", "mwf", "tt"])
    args = p.parse_args()

    with open(args.input, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if args.shift is not None:
        for r in rows:
            d = datetime.strptime(r["Schedule Date"], "%m/%d/%Y") + timedelta(days=args.shift)
            r["Schedule Date"] = d.strftime("%m/%d/%Y")
    else:
        d = first_date(args.start, args.cadence)
        for r in rows:
            r["Schedule Date"] = d.strftime("%m/%d/%Y")
            d = next_date(d, args.cadence)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    print(f"✓ {len(rows)} rows shifted → {args.output}")
    print(f"  First: {rows[0]['Schedule Date']}")
    print(f"  Last:  {rows[-1]['Schedule Date']}")


if __name__ == "__main__":
    main()
