# Recipe — Cross-Platform Pack (one topic × 4 platforms)

One topic, four CSVs. Same media, platform-tuned captions, staggered times.

Reference: `linkedin-viral-30-batch` precedent (4-platform 30-card drop).

## Inputs

- One topic
- N posts (15 / 30 / 50)
- Drip start
- DM keyword (optional, scrubbed from FB/IG/Pin if NDA)

## Steps

### 1. Build N media assets once
Use any template (LI editorial, carousel hero slides, single-card). Render N PNGs.

### 2. Re-crop for each platform if needed
- LI / IG carousel: 1080×1350 (same)
- IG single: 1080×1080 (square crop)
- FB: 1080×1350 OK
- Pinterest: 1000×1500 (re-render or vertical crop)

### 3. Write 4 caption variants per post
| Platform | Style |
|---|---|
| LinkedIn | Long-form, 5-7 paragraphs, professional |
| Facebook | Conversational, 1 question, casual |
| Instagram | Hook + CTA, heavy line breaks |
| Pinterest | Title-led, keyword-rich, benefit |

### 4. NDA scrub
Strip client names from FB / IG / Pin if not approved for public mention.
LinkedIn = signal but check.

### 5. Build 4 CSVs
```bash
python scripts/build_ghl_csv.py --input posts-li.json --output csv/ghl-linkedin.csv \
  --account "LinkedIn - Waseem" --start <date> --time 11:00 --cadence weekday

python scripts/build_ghl_csv.py --input posts-fb.json --output csv/ghl-facebook.csv \
  --account "Facebook - Waseem" --start <date> --time 13:00 --cadence weekday

python scripts/build_ghl_csv.py --input posts-ig.json --output csv/ghl-instagram.csv \
  --account "Instagram - waseemnasir2k26" --start <date> --time 19:00 --cadence weekday

python scripts/build_ghl_csv.py --input posts-pin.json --output csv/ghl-pinterest.csv \
  --account "Pinterest - SkynetLabs" --start <date> --time 20:00 --cadence daily
```

### 6. Stagger checklist
- LI 11:00 EST
- FB 13:00 EST
- IG 19:00 EST
- Pin 20:00 EST

Same calendar day for each post. 4 channels reinforce.

### 7. Upload + ship + mark.
