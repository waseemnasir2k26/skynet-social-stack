"""
Build a GHL-canonical 6-col CSV from a list of posts.

Canonical headers (locked, see references/ghl-csv-format.md):
    postAtSpecificTime (YYYY-MM-DD HH:mm:ss),content,link (OGmetaUrl),imageUrls,gifUrl,videoUrls

NOTE: GHL UI picks platforms at import time. One row = one post to all selected channels.
Caption should be the richest version (Instagram-style with hashtags) — all channels share it.

Usage:
    python build_ghl_csv.py --input posts.json --output ghl-linkedin.csv \
        --start 2026-05-05 --time 11:00 --cadence weekday

posts.json format:
[
  {
    "content": "Caption with hashtags...",
    "link": "https://skynetjoe.com/?utm_source=...",
    "imageUrls": "https://raw.githubusercontent.com/.../card01.png",
    "gifUrl": "",
    "videoUrls": ""
  },
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

CANONICAL_HEADERS = [
    "postAtSpecificTime (YYYY-MM-DD HH:mm:ss)",
    "content",
    "link (OGmetaUrl)",
    "imageUrls",
    "gifUrl",
    "videoUrls",
]


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


def validate_post(post, idx):
    if not isinstance(post, dict):
        sys.exit(f"ERROR: posts[{idx}] is not an object")
    if not post.get("content"):
        sys.exit(f"ERROR: posts[{idx}] missing 'content'")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--start", required=True, help="YYYY-MM-DD")
    p.add_argument("--time", default="11:00", help="HH:MM 24h")
    p.add_argument("--cadence", default="weekday", choices=["daily", "weekday", "mwf", "tt"])
    args = p.parse_args()

    try:
        hour, minute = args.time.split(":")
        time_str = f"{int(hour):02d}:{int(minute):02d}:00"
    except (ValueError, AttributeError):
        sys.exit(f"ERROR: --time must be HH:MM, got '{args.time}'")

    with open(args.input, encoding="utf-8") as f:
        posts = json.load(f)

    if not posts:
        sys.exit("ERROR: input has zero posts")

    rows = []
    d = first_date(args.start, args.cadence)
    for idx, post in enumerate(posts):
        validate_post(post, idx)
        rows.append({
            "postAtSpecificTime (YYYY-MM-DD HH:mm:ss)": f"{d.strftime('%Y-%m-%d')} {time_str}",
            "content": post["content"],
            "link (OGmetaUrl)": post.get("link", ""),
            "imageUrls": post.get("imageUrls", ""),
            "gifUrl": post.get("gifUrl", ""),
            "videoUrls": post.get("videoUrls", ""),
        })
        d = next_date(d, args.cadence)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CANONICAL_HEADERS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    print(f"OK {len(rows)} rows -> {args.output}")
    print(f"  First: {rows[0]['postAtSpecificTime (YYYY-MM-DD HH:mm:ss)']}")
    print(f"  Last:  {rows[-1]['postAtSpecificTime (YYYY-MM-DD HH:mm:ss)']}")


if __name__ == "__main__":
    main()
