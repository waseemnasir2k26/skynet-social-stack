# FB Personal News — 9-Card Template

Editorial overlay 9-card pack for personal Facebook drips. Built to the
`fb-personal-news-template-style` spec from the brain memory.

## Locked 9-card mix (do not reorder)

| # | Type   | Slot   | Day | Notes                                |
|---|--------|--------|-----|--------------------------------------|
| 1 | info   | 11:00  | 1   | News anchor (≤48h, source URL)       |
| 2 | motiv  | 16:00  | 1   | Motivation, no sell                  |
| 3 | sell   | 21:00  | 1   | Soft offer / keyword reply           |
| 4 | info   | 11:00  | 2   | News anchor (≤48h, source URL)       |
| 5 | info   | 16:00  | 2   | News anchor (≤48h, source URL)       |
| 6 | motiv  | 21:00  | 2   | Motivation, no sell                  |
| 7 | info   | 11:00  | 3   | News anchor (≤48h, source URL)       |
| 8 | sell   | 16:00  | 3   | Soft offer / keyword reply           |
| 9 | closer | 21:00  | 3   | LOCKED — never edit ("What I build") |

Rule: 4 info + 2 motiv + 2 sell + 1 locked closer. Card 9 carries the
`"locked": true` flag and the UI blocks edit.

## News-verification checklist (info cards only)

- [ ] News item published within last 48 hours
- [ ] `source_url` field present and resolves (200 OK)
- [ ] Headline does not exaggerate the source
- [ ] No invented metrics, no fake quotes
- [ ] Source is a primary domain (vendor blog, gov, paper) where possible

The UI flags any info card with a missing or empty `source_url`.

## Aesthetic

- 1080×1350 PNG export (FB feed crop)
- Full-bleed photo background, dark gradient overlay bottom-half
- Gold accent `#D4AF37`, white body
- Fraunces serif headline 72px, Inter body 28px, date stamp 18px
- Top-right `DAY N / 0X` badge in gold

## Responsive contract

1. Viewport meta with `width=device-width, initial-scale=1`
2. Page preview wraps export node at scaled `max-width: 540px;
   aspect-ratio: 1080/1350`
3. Page chrome typography uses `clamp()` so it scales 360 → 1440
4. Export node renders at fixed 1080×1350 in an offscreen sibling so
   html2canvas always exports the correct pixel dimensions
5. Tested at 360 / 480 / 768 / 1024 / 1440
6. All buttons ≥ 44px touch targets
7. Visual cards expose `role="img"` + descriptive `aria-label`

## Files

- `index.html` — preview grid, day tabs, per-card download, download-all zip
- `data.json` — 9-card array (edit copy here, card 9 is locked)
- `_avatars/` — drop photos here, reference path in `data.json`

## Drip schedule

3 days × 3 posts. Slots: 11:00, 16:00, 21:00 local time.
Cadence proven by FB-news-v3 batches in the brain.

## Quality gates (no exceptions)

- No em-dashes anywhere in copy
- No fake claims or invented metrics — humanizer rule
- Card 9 stays locked across drips; rotate weekly photos only
- Photos picked via `python _pick-next.py` from PROFESSIONAL/ — log entry required

## Usage

1. Drop avatar photos into `_avatars/`
2. Edit copy in `data.json` (cards 1-8 only)
3. Open `index.html` in a browser
4. Switch tabs Day 1 / Day 2 / Day 3 to preview each batch
5. Click `Download` on each card or `Download all 9` for the zip
6. Build GHL CSV from the rendered files using the social-stack skill
