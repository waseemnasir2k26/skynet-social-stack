---
name: ghl-csv-format
description: Canonical GHL CSV format spec for social-stack. ONE row per scheduled post (GHL fans out to all selected channels at import). Use this as the locked schema; reject any deviation.
type: reference
---

# GHL CSV Format — Canonical

GoHighLevel social planner accepts ONE schema. Every other header set we've seen in older docs is broken and will silently fail import or fire posts to wrong dates. This is the locked spec — confirm it hasn't changed before every batch by re-reading this file plus the master template at `C:\Users\info\viral-posts-batch2\GHL_SAMPLE_TEMPLATE.csv`.

## 1. Canonical headers (locked)

```csv
postAtSpecificTime (YYYY-MM-DD HH:mm:ss),content,link (OGmetaUrl),imageUrls,gifUrl,videoUrls
```

Six columns. Exact order. Exact casing. Do not rename, reorder, or add an `Account` / `platform` / `Schedule Date` column — GHL's UI picks channels at import time, so one row equals one post broadcast to every channel you tick during upload.

## 2. Field-by-field spec

| # | Header | Format | Required | Notes |
|---|---|---|---|---|
| 1 | `postAtSpecificTime (YYYY-MM-DD HH:mm:ss)` | `2026-05-05 11:00:00` | yes | Combined datetime, single column. NOT split date/time. Local timezone of the GHL workspace. Must be future-dated at import — date-shift via `scripts/shift_dates.py` if the pack ages before upload. |
| 2 | `content` | string, fully quoted | yes | Use the **richest** caption (Instagram-style with full hashtags + CTA + DM keyword). All channels share this body, so write for the most generous platform and let stricter ones (X, LI) trim on their side or use a separate X drip. Newlines allowed inside quoted field. |
| 3 | `link (OGmetaUrl)` | full HTTPS URL with UTM | yes when relevant | Landing URL for OG preview. Always UTM-tagged (`?utm_source=ghl&utm_medium=social&utm_campaign=<pack>`). Inject via `scripts/utm_inject.py`. Empty string `""` if pure image post with no link. |
| 4 | `imageUrls` | comma-separated HTTPS URLs | conditional | Single URL works. Multi-image carousels: comma-separate inside the quoted field, e.g. `"https://raw.githubusercontent.com/.../slide1.png,https://raw.githubusercontent.com/.../slide2.png"`. Host PNGs on GitHub raw (preferred) or any CDN returning 200. |
| 5 | `gifUrl` | HTTPS URL | optional | Single GIF URL. Empty `""` when unused (most posts). |
| 6 | `videoUrls` | comma-separated HTTPS URLs | optional | Reel / short. Empty `""` when unused. |

### Quoting rule (non-negotiable)

Build with `csv.QUOTE_ALL`. Every field wrapped in `"`. This preserves embedded newlines, commas, and emojis inside `content` and `imageUrls`. Unquoted content with newlines corrupts the CSV and GHL silently drops the bad rows.

### Example row

```csv
"2026-05-05 11:00:00","Stop guessing what AI sees.\n\nCiteLift scores your brand in ChatGPT, Claude, Perplexity, Gemini in 60 seconds.\n\nDM ""CITELIFT"" for the free audit.\n\n#AEO #LLMO #AI #Marketing","https://citelift.app?utm_source=ghl&utm_medium=social&utm_campaign=carousel-claude-pack","https://raw.githubusercontent.com/waseemnasir2k26/skynet-social-stack/main/packs/carousel-claude-2026-04-30/slide1.png,https://raw.githubusercontent.com/waseemnasir2k26/skynet-social-stack/main/packs/carousel-claude-2026-04-30/slide2.png","",""
```

## 3. Build flow

```bash
# 1. Render PNGs from HTML pack (html2canvas → /packs/<slug>/*.png)
# 2. Push PNGs to GitHub repo, grab raw URLs
# 3. Build the CSV (canonical-compliant)
python scripts/build_ghl_csv.py \
  --pack carousel-claude-2026-04-30 \
  --start-date 2026-05-05 \
  --time 11:00:00 \
  --cadence weekly \
  --link "https://citelift.app?utm_source=ghl&utm_medium=social&utm_campaign=carousel-claude" \
  --out outputs/ghl-carousel-claude.csv

# 4. Date-shift if the pack sat too long before upload
python scripts/shift_dates.py outputs/ghl-carousel-claude.csv --shift +14d

# 5. UTM-inject if links were bare
python scripts/utm_inject.py outputs/ghl-carousel-claude.csv \
  --source ghl --medium social --campaign carousel-claude
```

GHL upload: Marketing → Social Planner → Bulk Upload → tick the channels (LI / FB / IG / Pin) → drop the CSV → confirm preview → publish.

## 4. Anti-patterns — REJECT on sight

- **Old broken header set:** `Account,Schedule Date,Schedule Time,Caption,Media URL,Hashtags`. Will not import. Any older skill doc, recipe, or script generating these headers is stale — fix it.
- **Per-platform fanout (multiple rows for the same post on LI / FB / IG / Pin).** Reject. GHL handles fanout from a single row when channels are ticked at import. Duplicating rows triggers duplicate-post penalties on Meta + LinkedIn.
- **Split datetime columns** (`Schedule Date` + `Schedule Time`). Reject. Single combined column only.
- **Unquoted `content` with newlines or commas.** Will corrupt the CSV mid-row and GHL silently drops downstream rows. Always `csv.QUOTE_ALL`.
- **Past-dated `postAtSpecificTime`.** GHL accepts the row but never fires it. Always run `shift_dates.py` if the pack aged.
- **Bare links without UTM.** Lose attribution + Plausible can't segment. Always UTM-inject.
- **Image URLs returning 404 / 403.** Test 3 random rows with `curl -I` before upload. GitHub raw URLs flip when repos go private — re-test after any repo visibility change.
- **More than ~5 hashtags inside `content` for LI/FB-heavy packs.** Acceptable for IG-richest captions, but trim if the same row also targets LinkedIn (LinkedIn caps soft at 3-5).

## 5. Cross-links

- Build script: `C:\Users\info\.claude\skills\social-stack\scripts\build_ghl_csv.py`
- Date-shifter: `C:\Users\info\.claude\skills\social-stack\scripts\shift_dates.py`
- UTM injector: `C:\Users\info\.claude\skills\social-stack\scripts\utm_inject.py`
- Cross-platform recipe: `C:\Users\info\.claude\skills\social-stack\recipes\cross-platform-pack.md`
- Master template (source of truth): `C:\Users\info\viral-posts-batch2\GHL_SAMPLE_TEMPLATE.csv`
- Memory anchor: `~/.claude/projects/C--Users-info/memory/ghl-csv-sample-reference.md`

## 6. Pre-upload checklist

1. [ ] Headers match section 1 exactly (paste-compare)
2. [ ] All `postAtSpecificTime` values ≥ tomorrow (run `shift_dates.py` if not)
3. [ ] `content` uses richest caption with hashtags + DM keyword
4. [ ] `link (OGmetaUrl)` UTM-tagged
5. [ ] `imageUrls` return HTTP 200 (test 3 random)
6. [ ] All fields wrapped in `"` (open in plain editor, eyeball)
7. [ ] No `Account` / platform / split-date columns hiding from a stale script
8. [ ] If DM-keyword CTA in `content` → ManyChat WA template approved (24-72h Meta soak)
