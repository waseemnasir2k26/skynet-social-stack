# Social Stack — Master Social-Media Post Engine

> Build, render, and schedule social-media post packs end-to-end.
> One topic → cross-platform drop → GHL CSV → live drip in ~90 minutes.

## What it does

- Picks the right template per post type (carousel, LI card, FB news, X pack, Pin, video drip)
- Generates 1080×1350 (or platform-correct) HTML with `html2canvas` PNG download
- Builds canonical 6-col GHL CSV per platform (LI / FB / IG / Pin)
- Stages cross-platform drip with staggered times (LI 11:00 / FB 13:00 / IG 19:00 / Pin 20:00)
- Wires ManyChat keyword funnels (IG / FB / WA)
- Enforces image rotation, no-fake-claims, humanizer pass

## Triggers

User says any of:
- "build a carousel"
- "social pack"
- "LI cards batch"
- "FB news drip"
- "X pack"
- "Pinterest batch"
- "GHL CSV"
- "schedule drip"
- "post pack for [topic]"
- `/social-stack`
- Pastes a topic + asks for cross-platform content

## Layout

```
social-stack/
├── SKILL.md                 # main entry, decision logic, flow
├── README.md                # this file
├── templates/
│   ├── carousel-cream-rust/    # tenfoldmarc-style 1080×1350 carousels
│   ├── li-card-editorial-dark/ # Fraunces dark+gold LI single cards
│   ├── fb-news-9card/          # FB personal-news 9-card mix
│   ├── x-pack/                 # 1200×675 image tweets
│   └── pin-card/               # 1000×1500 vertical pins
├── recipes/
│   ├── carousel-launch.md          # 5×6 cross-platform drop
│   ├── li-card-batch.md            # 15-30 LI editorial cards
│   ├── fb-news-3day.md             # 9-card × 3-day drip
│   ├── x-pack-mwf-drip.md          # 12 tweets MWF
│   ├── pin-batch.md                # 30 pins +14d
│   └── cross-platform-pack.md      # one topic × 4 CSVs
├── references/
│   ├── post-type-decision-tree.md
│   ├── ghl-csv-format.md
│   ├── image-rotation-rule.md
│   ├── no-fake-claims.md
│   ├── humanizer-checklist.md
│   ├── brand-split.md
│   └── manychat-keyword-flow.md
├── scripts/
│   ├── build_ghl_csv.py     # generic 6-col CSV builder
│   ├── shift_dates.py       # date-shift CSV by N days OR re-anchor
│   └── pick_avatar.py       # batch picker + copy + auto-mark
└── examples/
    └── carousel-claude-pack-2026-04-30/   # shipped reference
```

## The 6 hard rules

1. **No fake claims.** Real builds only. `references/no-fake-claims.md`.
2. **Image rotation.** Always `_pick-next.py`. Never by eye. Mark used after.
3. **Humanize.** Strip em-dashes, "delve", AI-tells. Run `/humanizer`.
4. **Brand split.** Personal voice ≠ SkynetLabs voice. Don't paste-blanket.
5. **GHL = 6-col canonical.** Don't invent headers.
6. **24-72h Meta soak** for any DM-keyword WA template before Day 1.

## Quick start

```
You: "build me a 5-carousel pack on Claude Code, n8n, AEO. Schedule from May 5, weekday cadence, DM keyword JARVIS"

Claude (loads skill):
  → reads SKILL.md
  → confirms inputs (volume, brand)
  → forks templates/carousel-cream-rust/
  → calls scripts/pick_avatar.py for 5 portraits
  → renders HTML → opens browser
  → writes 4 caption variants
  → builds 4 GHL CSVs
  → flags ManyChat WA template submit deadline
```

## Improving the skill

Each shipped pack is a new data point. After every drop:
- Note what worked (engagement, DM conversion)
- Note what broke (rendering, CSV reject, dead funnel)
- Update the relevant recipe or reference
- Bump version in SKILL.md

## License

MIT. See `LICENSE`.

## Author

[Waseem Nasir](https://www.skynetjoe.com) — Founder, SkynetLabs.
[GitHub](https://github.com/waseemnasir2k26) · [LinkedIn](https://linkedin.com/in/waseemnasir2k26)

Distilled from 30+ shipped social packs across LinkedIn, IG, FB, X, Pinterest.
