# skynet-social-stack

> Build a complete cross-platform social-media post pack — HTML preview, PNG export, GHL CSV drip, ManyChat keyword funnel — in 90 minutes.

A Claude Code skill (and standalone toolkit) distilled from 30+ shipped social-media batches across LinkedIn, Instagram, Facebook, X, and Pinterest.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-c4502e)](https://docs.claude.com/en/docs/claude-code/skills)
[![Status](https://img.shields.io/badge/status-v1.0.0-green)](./CHANGELOG.md)

---

## Why this exists

Posting consistently on 4 platforms is a full-time job. Most "social-media tools" are SaaS subscriptions that don't actually generate the content.

This skill goes the other way:
- **Generate** the visuals (HTML → PNG, browser-rendered, no Photoshop)
- **Author** platform-tuned captions (humanizer-passed, no AI tells)
- **Schedule** via GoHighLevel CSV import (canonical 6-col format)
- **Close the loop** with ManyChat keyword funnels

All by talking to Claude Code.

---

## Post types covered

| Type | Template | Default volume | Ratio |
|---|---|---|---|
| Carousel (multi-slide tip pack) | `carousel-cream-rust` | 5–6 slides × N | 1080×1350 |
| LinkedIn single card | `li-card-editorial-dark` | 15–30 | 1080×1350 |
| Facebook news (personal) | `fb-news-9card` | 9 × 3 days | 1080×1350 |
| X / Twitter pack | `x-pack` | 12–20 | 1200×675 |
| Pinterest batch | `pin-card` | 30 | 1000×1500 |
| Video drip | (no template) | varies | varies |

---

## Quick start

### As a Claude Code skill

1. Copy this repo into your skills folder:
   ```bash
   git clone https://github.com/waseemnasir2k26/skynet-social-stack.git \
     ~/.claude/skills/social-stack
   ```
2. Restart Claude Code.
3. Ask: *"build me a carousel pack on [topic], schedule from [date]"*.

### As a standalone toolkit

```bash
git clone https://github.com/waseemnasir2k26/skynet-social-stack.git
cd skynet-social-stack

# fork a template
cp -r templates/carousel-cream-rust outputs/my-pack

# edit the data array in index.html
# open in browser → click "Download All PNGs"
start outputs/my-pack/index.html

# build CSV
python scripts/build_ghl_csv.py \
  --input posts.json \
  --output csv/ghl-linkedin.csv \
  --account "LinkedIn - YourBrand" \
  --start 2026-05-05 \
  --time 11:00 \
  --cadence weekday
```

---

## The 6 hard rules

This is not a content-spam farm. The rules:

1. **No fake claims.** Real builds only. Real metrics or no metrics. → [`references/no-fake-claims.md`](./references/no-fake-claims.md)
2. **Image rotation.** Photos rotated via log, not by eye. → [`references/image-rotation-rule.md`](./references/image-rotation-rule.md)
3. **Humanize.** Strip em-dashes, "delve", "moreover", AI tells. → [`references/humanizer-checklist.md`](./references/humanizer-checklist.md)
4. **Brand split.** Personal voice ≠ agency voice. → [`references/brand-split.md`](./references/brand-split.md)
5. **GHL = 6-col canonical.** No invented headers. → [`references/ghl-csv-format.md`](./references/ghl-csv-format.md)
6. **24–72h Meta soak** for any DM-keyword WA template. → [`references/manychat-keyword-flow.md`](./references/manychat-keyword-flow.md)

---

## Recipes (full playbooks)

- [`recipes/carousel-launch.md`](./recipes/carousel-launch.md) — 5×6 cross-platform carousel drop
- [`recipes/li-card-batch.md`](./recipes/li-card-batch.md) — 15–30 LinkedIn editorial cards
- [`recipes/fb-news-3day.md`](./recipes/fb-news-3day.md) — 9-card × 3-day FB drip
- [`recipes/x-pack-mwf-drip.md`](./recipes/x-pack-mwf-drip.md) — 12 tweets, MWF
- [`recipes/pin-batch.md`](./recipes/pin-batch.md) — 30 pins, +14d shift
- [`recipes/cross-platform-pack.md`](./recipes/cross-platform-pack.md) — one topic × 4 CSVs

---

## Scripts

- [`scripts/build_ghl_csv.py`](./scripts/build_ghl_csv.py) — generic 6-col CSV builder w/ cadence (daily / weekday / mwf / tt)
- [`scripts/shift_dates.py`](./scripts/shift_dates.py) — date-shift CSV by N days OR re-anchor to new start
- [`scripts/pick_avatar.py`](./scripts/pick_avatar.py) — batch-pick photos from a rotation-tracked folder + auto-mark used

All stdlib Python. No deps.

---

## Example

[`examples/carousel-claude-pack-2026-04-30/`](./examples/carousel-claude-pack-2026-04-30/) — a real shipped pack. 5 carousels × 6 slides = 30 cards, cream+rust circuit style, dropped 2026-04-30.

Open `index.html`, tab through the 5 carousels, click any `↓ PNG` button.

---

## Stack

- **HTML rendering:** vanilla HTML + CSS, [html2canvas](https://html2canvas.hertzen.com/) for PNG export
- **Fonts:** Google Fonts (Archivo Black, Fraunces, JetBrains Mono, Inter)
- **CSV:** Python stdlib (`csv`, `argparse`, `datetime`)
- **Distribution:** [GoHighLevel](https://www.gohighlevel.com/) social planner CSV import
- **Funnel:** [ManyChat](https://manychat.com/) keyword triggers (IG / FB / WA)

No SaaS dependency for content generation. Everything runs locally.

---

## Roadmap

- [ ] Add `templates/li-card-editorial-dark/` (Fraunces dark+gold)
- [ ] Add `templates/fb-news-9card/`
- [ ] Add `templates/x-pack/`
- [ ] Add `templates/pin-card/`
- [ ] `scripts/render_pngs.js` — Playwright batch headless render (no manual download click)
- [ ] CSV → GHL API direct push (skip manual upload)
- [ ] Engagement-tracker recipe (Plausible UTM analysis)
- [ ] Meta WA template generator

PRs welcome — see [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## Author

**Waseem Nasir** — Founder, [SkynetLabs](https://www.skynetjoe.com).

Building agency tooling in public. Distilled from 30+ shipped client + personal social packs.

- [skynetjoe.com](https://www.skynetjoe.com) (agency)
- [waseemnasir.com](https://www.waseemnasir.com) (personal)
- [LinkedIn](https://www.linkedin.com/in/waseemnasir2k26)
- [@waseemnasir2k26](https://twitter.com/waseemnasir2k26)

---

## License

MIT — [LICENSE](./LICENSE)

If you ship something with this, tag me. Always curious to see what gets built.
