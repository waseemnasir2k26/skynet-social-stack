# Pinterest Pin-Card Template (1000x1500)

Pinterest-native pin batch builder. 30 pins per batch. Cream / Claret / Dark palettes. Keyword-first titles. Save-bait CTAs. Per-pin and bulk-zip PNG export. UTM auto-injected.

Part of the `social-stack` skill. Trigger: "Pinterest batch", "Pin pack", "/social-stack pinterest".

---

## Files

| File | Purpose |
|---|---|
| `index.html` | 30-pin grid. Filter by palette. Per-pin download. Bulk zip export. html2canvas at exact 1000x1500. |
| `data.json` | 30-pin payload (palette, title, body, CTA, destination_path, photo, batch tag). |
| `_avatars/` | Optional Waseem photos for pins that need a face. Pull via `python _pick-next.py`. |
| `README.md` | This file. |

---

## Pinterest Title Rules (locked)

Pinterest sorts by keyword. Title bar carries 90 percent of the click. Follow these or lose impressions.

1. **Keyword first.** Start with a strong keyword stem — `5 AI Tools`, `How to`, `Best`, `Why`, `Top 10`. Algorithm matches the first 30 chars to search intent.
2. **Benefit-led.** Reader must see the win in 3 seconds. `…That Saved Me 20 hrs/Week`. `…With Zero Ad Spend`.
3. **<= 100 chars.** Pinterest truncates at 100 in feed. Anything longer dies in the fold.
4. **No em-dashes, no fake claims.** Use commas, periods, plus, or `and`. Numbers must be real.
5. **Number + benefit + audience** beats clever copy 9/10 times.
6. **Body 100-200 chars.** Setup the click. Don't oversell. Save bait CTA closes it.
7. **CTA = `Save for later` or `Get the guide`.** Pinterest culture is save-first, click-second. Save bait outperforms hard CTA by 3-5x.

---

## UTM Injection

Every pin URL gets:

```
?utm_source=pinterest&utm_medium=pin&utm_campaign=<batch>&utm_content=pin-NN
```

Example: `https://skynetjoe.com/guides/ai-stack-2026?utm_source=pinterest&utm_medium=pin&utm_campaign=claude-stack-2026-04&utm_content=pin-01`

The `index.html` injects this automatically at render time. The download CSV pulls the same URL.

Batch name lives in `data.json -> batch`. Pin number is zero-padded `pin-01`, `pin-02`, … `pin-30`.

---

## Build Workflow

1. Edit `data.json`. Change `batch` (e.g., `claude-stack-2026-04`), `destination_base`, and the 30-pin array.
2. Drop optional photos in `_avatars/` and reference as `_avatars/IMG_2742.jpg`. Photos go on the top 70 percent overlay.
3. Open `index.html` in Chrome. Filter palette to QA each color. Hit `Download All as ZIP`.
4. Unzip to `Desktop\waseem-pin-batch-<DATE>\`. 30 PNGs at exact 1000x1500.
5. Run `scripts/build_ghl_csv.py` to schedule:

```bash
python scripts/build_ghl_csv.py \
  --input pins.json \
  --output ghl-pinterest.csv \
  --start 2026-05-05 \
  --time 20:00 \
  --cadence daily
```

6. Upload PNGs to GitHub raw / Vercel / Cloudinary. Replace `imageUrls` column with hosted URL.
7. Upload CSV to GHL. Pinterest channel.
8. Mark photos used in `~/.claude/projects/C--Users-info/memory/feedback-image-rotation.md` rotation log.

---

## Date-Shift Trap (CRITICAL)

When **reusing** a batch CSV (e.g., re-uploading because GHL ate the schedule, or running again next month):

**ALWAYS shift dates +14 days minimum** before upload. Pinterest dedupes pins by URL+date. If the same UTM hits the same day twice, half the pins silently drop.

The `index.html` shows a yellow banner reminding you of this before bulk export.

Use `scripts/shift_dates.py`:

```bash
python scripts/shift_dates.py --input ghl-pinterest.csv --output ghl-pinterest-v2.csv --days 14
```

---

## 30-Pin Drip Schedule

Default: **1 pin/day for 30 days.** Pinterest rewards consistency. Posting all 30 at once gets you suppressed.

| Cadence | Use when |
|---|---|
| `daily` (default) | Standard 30-day batch. Burst tolerance up to 3/day. |
| `weekday` | If your niche skews B2B. Skip weekends. |
| `mwf` | Slow drip, 10 weeks runway. Use for evergreen guides. |

Time of day: **20:00 EST** is the Pinterest peak (US dinner-scroll). Override with `--time 20:00`.

---

## Responsive Contract

The export node is fixed 1000x1500 for html2canvas. The preview frame uses `aspect-ratio: 1000/1500; max-width: 400px;` and scales fluidly down to 360px. Test at 360 / 480 / 768 / 1024 / 1440. All controls are >= 44px touch targets.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

The page chrome uses `clamp()` and `vw` units. The card itself is `transform: scale()` to preview but exports unscaled.

ARIA: each pin is `role="img"` with descriptive `aria-label` built from title + palette.

---

## Quality Gates (per batch)

- [ ] All 30 pins render (cream + claret + dark mix)
- [ ] Every title <= 100 chars and starts with keyword
- [ ] Every body 100-200 chars, no em-dashes, no fake metrics
- [ ] UTM auto-injected on every link
- [ ] Bulk zip exports 30 files at exact 1000x1500 px
- [ ] CTA reads `Save for later` or `Get the guide`
- [ ] URL stamp readable on all palettes
- [ ] Date-shift warning visible in UI before bulk export
- [ ] Test on 360 / 768 / 1440 viewports

---

## Reference

- GHL CSV format: `references/ghl-csv-format.md`
- Pinterest batch ops: `recipes/pinterest-batch.md`
- Image rotation rule: `~/.claude/projects/C--Users-info/memory/feedback-image-rotation.md`
- No-fake-claims rule: `~/.claude/projects/C--Users-info/memory/feedback-no-fake-claims.md`
