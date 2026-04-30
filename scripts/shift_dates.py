"""
Shift postAtSpecificTime column in a GHL canonical CSV by N days OR re-anchor to a new start.

Canonical column: 'postAtSpecificTime (YYYY-MM-DD HH:mm:ss)'

Usage:
    python shift_dates.py --input old.csv --output new.csv --shift 21
    python shift_dates.py --input old.csv --output new.csv --start 2026-05-05 --cadence weekday
"""
import argparse, csv, sys
from datetime import datetime, timedelta

DATE_COL = "postAtSpecificTime (YYYY-MM-DD HH:mm:ss)"
DATE_FMT = "%Y-%m-%d %H:%M:%S"


def next_date(d, cadence):
    while True:
        d += timedelta(days=1)
        wd = d.weekday()
        if cadence == "daily": return d
        if cadence == "weekday" and wd < 5: return d
        if cadence == "mwf" and wd in (0, 2, 4): return d
        if cadence == "tt" and wd in (1, 3): return d


def first_date(start, cadence):
    try:
        d = datetime.strptime(start, "%Y-%m-%d")
    except ValueError:
        sys.exit(f"ERROR: --start must be YYYY-MM-DD, got '{start}'")
    wd = d.weekday()
    if cadence == "daily": return d
    if cadence == "weekday" and wd < 5: return d
    if cadence == "mwf" and wd in (0, 2, 4): return d
    if cadence == "tt" and wd in (1, 3): return d
    return next_date(d - timedelta(days=1), cadence)


def parse_row_dt(value, row_idx):
    try:
        return datetime.strptime(value, DATE_FMT)
    except ValueError:
        sys.exit(f"ERROR: row {row_idx} has malformed date '{value}'. Expected '{DATE_FMT}' (e.g. '2026-05-05 11:00:00')")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--shift", type=int, help="days to add per row")
    g.add_argument("--start", help="YYYY-MM-DD new anchor")
    p.add_argument("--cadence", default="weekday", choices=["daily", "weekday", "mwf", "tt"])
    p.add_argument("--time", default="11:00", help="HH:MM 24h, used with --start")
    args = p.parse_args()

    with open(args.input, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        sys.exit("ERROR: input has zero rows")
    if DATE_COL not in rows[0]:
        sys.exit(f"ERROR: input missing column '{DATE_COL}'. Found: {list(rows[0].keys())}")

    if args.shift is not None:
        for i, r in enumerate(rows):
            d = parse_row_dt(r[DATE_COL], i) + timedelta(days=args.shift)
            r[DATE_COL] = d.strftime(DATE_FMT)
    else:
        try:
            hour, minute = args.time.split(":")
            time_str = f"{int(hour):02d}:{int(minute):02d}:00"
        except (ValueError, AttributeError):
            sys.exit(f"ERROR: --time must be HH:MM, got '{args.time}'")
        d = first_date(args.start, args.cadence)
        for r in rows:
            r[DATE_COL] = f"{d.strftime('%Y-%m-%d')} {time_str}"
            d = next_date(d, args.cadence)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys(), quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    print(f"OK {len(rows)} rows shifted -> {args.output}")
    print(f"  First: {rows[0][DATE_COL]}")
    print(f"  Last:  {rows[-1][DATE_COL]}")


if __name__ == "__main__":
    main()
