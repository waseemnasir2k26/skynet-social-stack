"""
Build a GHL-canonical 6-col CSV from a list of posts.

Usage:
    python build_ghl_csv.py --input posts.json --output ghl-linkedin.csv \
        --account "LinkedIn - Waseem" --start 2026-05-05 --time 11:00 \
        --cadence weekday

posts.json format:
[
  {"caption": "...", "media_url": "https://...", "hashtags": "#AI #n8n"},
  ...
]

Cadence:
  daily    → every day
  weekday  → Mon-Fri only
  mwf      → Mon/Wed/Fri only
  tt       → Tue/Thu only
"""
import argparse, csv, json, sys
from datetime import datetime, timedelta


def next_date(d, cadence):
    while True:
        d += timedelta(days=1)
        wd = d.weekday()  # 0=Mon
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
    p.add_argument("--account", required=True)
    p.add_argument("--start", required=True, help="YYYY-MM-DD")
    p.add_argument("--time", default="11:00", help="HH:MM 24h")
    p.add_argument("--cadence", default="weekday", choices=["daily", "weekday", "mwf", "tt"])
    args = p.parse_args()

    with open(args.input) as f:
        posts = json.load(f)

    rows = []
    d = first_date(args.start, args.cadence)
    for post in posts:
        rows.append({
            "Account": args.account,
            "Schedule Date": d.strftime("%m/%d/%Y"),
            "Schedule Time": args.time,
            "Caption": post["caption"],
            "Media URL": post.get("media_url", ""),
            "Hashtags": post.get("hashtags", ""),
        })
        d = next_date(d, args.cadence)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Account", "Schedule Date", "Schedule Time", "Caption", "Media URL", "Hashtags"])
        w.writeheader()
        w.writerows(rows)

    print(f"✓ {len(rows)} rows → {args.output}")
    print(f"  First: {rows[0]['Schedule Date']} {rows[0]['Schedule Time']}")
    print(f"  Last:  {rows[-1]['Schedule Date']} {rows[-1]['Schedule Time']}")


if __name__ == "__main__":
    main()
