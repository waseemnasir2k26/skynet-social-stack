# Recipe — Pinterest Batch (30 pins, +14d shift)

Pinterest pack: 30 vertical 1000×1500 pins.

Reference: `pinterest-batch5-csv` (memory).

## Inputs

- Topic theme
- 30 hooks (one per pin)
- Drip window (14-21 day shift typical)
- Up to 8 commercial pins (Fiverr/Etsy deep links)

## Steps

### 1. Draft 30 pin titles
- Pinterest searches like Google: keyword-rich, benefit-led
- Hook ≤ 60 chars
- Body 100-200 chars

### 2. Pick avatars (or use product imagery)
For personal-brand pins:
```bash
python scripts/pick_avatar.py --count 30 --dest outputs/pin-batch-<date>/_avatars/
```

### 3. Fork template
`templates/pin-card/index.html`. 1000×1500.

### 4. Render 30 PNGs

### 5. Build GHL CSV
```bash
python scripts/build_ghl_csv.py \
  --input posts.json \
  --output csv/ghl-pinterest.csv \
  --account "Pinterest - SkynetLabs" \
  --start <date+14> \
  --time 20:00 \
  --cadence daily
```

### 6. CRITICAL: date-shift if pack ages
If you delay upload more than start date, run:
```bash
python scripts/shift_dates.py --input csv/ghl-pinterest.csv --output csv/ghl-pinterest-shifted.csv --shift 21
```
**Skipping this loses every past-dated row silently.** Pinterest precedent: 9/30 pins lost in batch5 audit.

### 7. Funnel gaps to watch
- Pixel installed (pin → site tracking)
- Beehiiv signup destination
- Fiverr deep links (UTM tagged)
- CTA hooks consistent across pin titles

### 8. Mark photos used.
