# Migrate Old GHL CSVs → Canonical 6-col

Auto-convert any pre-v1.2.0 GHL CSV (broken header set) to the canonical format the GHL importer accepts.

## Why

Pre-v1.2.0 `../scripts/build_ghl_csv.py` emitted broken headers:
`Account,Schedule Date,Schedule Time,Caption,Media URL,Hashtags`

GHL Bulk Upload silently rejects this — posts never schedule. v1.2.0 emits canonical:
`postAtSpecificTime (YYYY-MM-DD HH:mm:ss),content,link (OGmetaUrl),imageUrls,gifUrl,videoUrls`

Any CSV in `outputs/` from before the fix needs migration before re-import.

## Steps

### 1. Detect old format
- Open CSV, read header row.
- If header == `Account,Schedule Date,Schedule Time,Caption,Media URL,Hashtags` → migrate (step 3).
- If header == canonical 6-col → already good, skip.
- Else → unknown format, abort. Inspect manually.

### 2. Field mapping

| Old col | New col | Transform |
|---|---|---|
| Schedule Date + Schedule Time | postAtSpecificTime (YYYY-MM-DD HH:mm:ss) | `f"{strptime(date,'%m/%d/%Y'):%Y-%m-%d} {time}:00"` |
| Caption | content | passthrough (preserve newlines, quote-all) |
| Media URL | imageUrls | passthrough |
| (none) | link (OGmetaUrl) | empty (or prompt user for landing URL) |
| Hashtags | merged into content if not already in caption | append `\n\n` + hashtags if not present |
| Account | (DROPPED — GHL UI picks at import) | discard |
| (none) | gifUrl, videoUrls | empty |

### 3. Run conversion script

Save the inline script below (full source in the next code block) as **migrate_csv.py** — you create this file next to the old CSV (or drop it in the skill's `scripts/` folder if you want to reuse later):

```python
# migrate_csv.py
import csv, sys
from datetime import datetime

OLD = ["Account","Schedule Date","Schedule Time","Caption","Media URL","Hashtags"]
NEW = ["postAtSpecificTime (YYYY-MM-DD HH:mm:ss)","content","link (OGmetaUrl)","imageUrls","gifUrl","videoUrls"]

if len(sys.argv) != 3:
    sys.exit("usage: python migrate_csv.py old.csv new.csv")

with open(sys.argv[1], encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

if not rows or list(rows[0].keys()) != OLD:
    sys.exit(f"ERROR: input not in old format. Got: {list(rows[0].keys()) if rows else 'empty'}")

out = []
for r in rows:
    d = datetime.strptime(r["Schedule Date"], "%m/%d/%Y")
    t = r["Schedule Time"]
    if len(t.split(":")) == 2:
        t += ":00"
    content = r["Caption"]
    tags = r.get("Hashtags","").strip()
    if tags and tags not in content:
        content = content.rstrip() + "\n\n" + tags
    out.append({
        "postAtSpecificTime (YYYY-MM-DD HH:mm:ss)": f"{d:%Y-%m-%d} {t}",
        "content": content,
        "link (OGmetaUrl)": "",
        "imageUrls": r.get("Media URL", ""),
        "gifUrl": "",
        "videoUrls": "",
    })

with open(sys.argv[2], "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=NEW, quoting=csv.QUOTE_ALL)
    w.writeheader()
    w.writerows(out)

print(f"OK migrated {len(out)} rows -> {sys.argv[2]}")
```

Run:
```bash
python migrate_csv.py old-batch.csv old-batch-migrated.csv
```

### 4. Post-migrate validation

- Open new CSV in Excel / Numbers / VS Code → confirm 6 cols, datetime combined into one cell.
- Spot-check 1 row in GHL Bulk Upload preview screen — verify date parses, image previews.
- Verify `imageUrls` still resolves (raw GitHub URL not 404, no expired CDN).
- Verify `content` newlines render (multi-line caption shows as paragraphs in preview).

### 5. Backfill missing `link (OGmetaUrl)`

If your old captions had landing URLs in the body, run a manual sweep — open new CSV, paste landing URL into `link (OGmetaUrl)` column where appropriate. UTM tagging via `scripts/utm_inject.py` after migration is recommended for tracking source/medium/campaign.

### 6. Bulk migrate folder

For a whole `outputs/` tree with mixed-age CSVs:

```bash
# bash / git-bash / WSL
for f in outputs/**/csv/*.csv; do
  python migrate_csv.py "$f" "${f%.csv}-migrated.csv"
done
```

PowerShell:
```powershell
Get-ChildItem outputs -Recurse -Filter *.csv | ForEach-Object {
  $new = $_.FullName -replace '\.csv$', '-migrated.csv'
  python migrate_csv.py $_.FullName $new
}
```

Script self-aborts on canonical-format inputs, so it's safe to re-run on a mixed folder.

## Anti-patterns

- Don't edit the old CSV in Excel by hand — Excel mangles datetime strings + drops leading zeros from times like `09:00`.
- Don't skip `csv.QUOTE_ALL` — captions with newlines or commas will corrupt the row count without it.
- Don't paste-import old format hoping GHL auto-detects — silent fail, posts never schedule, no error toast.
- Don't migrate then forget to delete the old CSV — easy to upload the broken one by mistake. Rename old by appending the suffix **-LEGACY** before the extension (so a file named **batch** would become **batch-LEGACY**, both with `.csv`), or move to `archive/`.

## Cross-links

- `references/ghl-csv-format.md` — canonical 6-col spec
- `scripts/build_ghl_csv.py` — current builder (already canonical, v1.2.0+)
- `scripts/shift_dates.py` — re-shift after migration if drip window shifted past
- `scripts/utm_inject.py` — backfill UTM tags after migration
