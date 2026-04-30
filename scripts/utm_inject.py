"""
Inject UTM parameters into Media URLs in a GHL CSV.

Usage:
    python utm_inject.py --input ghl-linkedin.csv --output ghl-linkedin-utm.csv \
        --source linkedin --medium carousel --campaign claude-code-pack-2026-04-30

Adds:
    ?utm_source=linkedin&utm_medium=carousel&utm_campaign=claude-code-pack-2026-04-30
    &utm_content=row-N

Per-row utm_content increments (row-1, row-2, ...) so you can attribute by post slot.

If URL already has query params, appends with &.
"""
import argparse, csv
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse


def inject(url, source, medium, campaign, content):
    if not url or not url.startswith("http"):
        return url
    parsed = urlparse(url)
    q = dict(parse_qsl(parsed.query))
    q.update({
        "utm_source": source,
        "utm_medium": medium,
        "utm_campaign": campaign,
        "utm_content": content,
    })
    new_query = urlencode(q)
    return urlunparse(parsed._replace(query=new_query))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--source", required=True, help="utm_source — usually platform name")
    p.add_argument("--medium", required=True, help="utm_medium — e.g. carousel, image, story")
    p.add_argument("--campaign", required=True, help="utm_campaign — slug + date")
    p.add_argument("--url-column", default="Media URL")
    args = p.parse_args()

    with open(args.input, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    for i, r in enumerate(rows, 1):
        if args.url_column in r:
            r[args.url_column] = inject(
                r[args.url_column],
                args.source, args.medium, args.campaign,
                f"row-{i}",
            )

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

    print(f"✓ {len(rows)} rows · UTM injected → {args.output}")
    print(f"  source={args.source} · medium={args.medium} · campaign={args.campaign}")


if __name__ == "__main__":
    main()
