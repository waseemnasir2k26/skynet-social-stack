# Recipe — Carousel Launch (5×6 cross-platform)

End-to-end: 5 carousels × 6 slides → LinkedIn + IG primary, FB secondary, GHL CSV drip, ManyChat keyword funnel.

Time: ~90 min.

## Inputs

- 5 topics (e.g. Claude Code limits, AEO pivot, n8n SaaS-killer, 1-man agency stack, vibe-coding)
- Brand variant (personal / SkynetLabs)
- Drip start date
- DM keyword (optional)

## Steps

### 1. Pick template (1 min)
Use `templates/carousel-cream-rust/index.html`.

### 2. Pick + copy 5 avatars (1 min)
```bash
python scripts/pick_avatar.py --count 5 --dest outputs/<slug>-<date>/_avatars/
```
Don't `--mark` yet (mark after ship).

### 3. Build data array (15 min)
For each carousel, draft:
- Hero slide (big title + 1-line subhead + terminal block w/ 3-5 lines)
- 4 trick slides (TRICK 01-04, headline + subhead + terminal block)
- CTA slide (3 cta-pill rows, last one rust-filled)

Real claims only. Apply `references/no-fake-claims.md`.

### 4. Fork the template (5 min)
```bash
mkdir -p outputs/<slug>-<date>
cp -r templates/carousel-cream-rust/* outputs/<slug>-<date>/
```
Edit the `carousels` array in `../templates/carousel-cream-rust/index.html` (now copied into your output dir) with your data + avatar paths.

### 5. Open + visual QA (10 min)
```bash
start outputs/<slug>-<date>/index.html
```
Tab through all 5 carousels. Check: headlines fit, terminal blocks aren't overflowing, mascot pose makes sense, page indicators correct.

### 6. Download all PNGs (5 min)
Click "Download all 6 PNGs" per carousel = 30 PNGs total. Save to `outputs/<slug>-<date>/png/`.

### 7. Upload PNGs to CDN (5 min)
Host at `https://skynetjoe.com/media/<slug>/` or any CDN. Get public URLs.

### 8. Write captions (15 min)
4 platform variants per carousel. Apply `references/humanizer-checklist.md` + `references/brand-split.md`.

```
captions/
  linkedin.md     # long-form, 5-7 paragraphs each
  facebook.md     # conversational, 1 question
  instagram.md    # hook + CTA, line breaks
  x.md            # tight, 1-2 tweets each (carousel screenshots)
```

### 9. Build GHL CSVs (5 min)
For each platform, prep a posts JSON file (your input data — you create it, structure shown below):
```json
[
  {"caption": "...", "media_url": "https://.../carousel-1-slide-1.png", "hashtags": "#AI #n8n"}
]
```

Then:
```bash
python scripts/build_ghl_csv.py \
  --input posts-li.json \
  --output csv/ghl-linkedin.csv \
  --account "LinkedIn - Waseem" \
  --start 2026-05-05 \
  --time 11:00 \
  --cadence weekday
```

Repeat for FB (13:00), IG (19:00). Skip Pinterest (carousels don't fit Pin format) unless you slice slide-1 only as Pin.

### 10. Wire ManyChat keyword (10 min, IF DM-keyword CTA)
Per `references/manychat-keyword-flow.md`. **Submit WA template 24-72h BEFORE Day 1.**

### 11. Upload CSVs to GHL (5 min)
GHL → Social Planner → Bulk Upload. One CSV per platform.

### 12. Mark photos used (1 min)
```bash
for f in outputs/<slug>-<date>/_avatars/*.jpg; do
  python "C:/Users/info/OneDrive/Desktop/GITHUB/WASEEM IMAGES/PROFESSIONAL/_pick-next.py" \
    --use "$(basename $f .jpg).JPG.jpeg" "carousel-<slug>-<date>"
done
```

### 13. Save deliverable summary
Write `outputs/<slug>-<date>/_README.md`:
- What shipped
- Drip schedule
- DM keyword
- Where PNGs are hosted

### 14. Add memory entry
Update `~/.claude/projects/C--Users-info/memory/MEMORY.md` Active Projects or Scheduled Drips section.

## Pre-flight checklist

- [ ] All 30 PNGs render (no broken images)
- [ ] Captions humanizer-passed
- [ ] No fake claims
- [ ] CSV dates ≥ tomorrow
- [ ] Account names exact
- [ ] Media URLs return 200
- [ ] WA template approved (if DM keyword)
- [ ] Photos marked used

## Failure modes

- Mascot SVG broken → check `<defs>` symbols loaded before render
- html2canvas crops avatar → ensure photo file is in `_avatars/` (same origin)
- Carousel overflows on slide 4 → headline too long, shorten or use `.headline.sm` class
- GHL silently rejects CSV → check Account name typo first
