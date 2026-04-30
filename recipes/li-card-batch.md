# Recipe — LinkedIn Card Batch (15-30 editorial cards)

Single-post LinkedIn image cards, dark + gold editorial style. Fraunces serif. 1080×1350.

Reference: `linkedin-card-template-style` (memory) + 30-batch precedent.

## Inputs

- Topic theme (e.g. "AI stack value", "viral career advice", "n8n flows")
- Volume (15 / 30 default)
- Drip window
- Photo per card (rotate)

## Steps

### 1. Pick template
`templates/li-card-editorial-dark/index.html`.

### 2. Pick avatars (1 photo per card)
```bash
python scripts/pick_avatar.py --count 30 --dest outputs/li-batch-<date>/_avatars/
```

### 3. Draft 30 hooks
Format: `<HOOK> · <BODY> · <CTA>`
- Hook ≤ 12 words
- Body 30-50 words
- CTA = save / DM / comment

Apply no-fake-claims + humanizer.

### 4. Render HTML
Edit `cards` array in template. Open + click "Download All".

### 5. Build GHL CSV
```bash
python scripts/build_ghl_csv.py \
  --input posts-li.json \
  --output csv/ghl-linkedin.csv \
  --account "LinkedIn - Waseem" \
  --start 2026-05-05 \
  --time 11:00 \
  --cadence weekday
```

### 6. Upload + ship + mark photos used.

## Cross-platform fork

Same 30 cards → re-export square crop (1080×1080) for IG → 4-platform CSV pack (LI/FB/IG/Pin) per `linkedin-viral-30-batch` precedent.

NDA scrub: strip client names from FB/IG/Pin captions.

## Cadence default

- LinkedIn: weekday 11:00
- Facebook: 13:00
- Instagram: 19:00
- Pinterest: 20:00

40-day drip @ 30 posts × 4 platforms.
