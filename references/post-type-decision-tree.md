# Post-Type Decision Tree

Pick the template based on user signal + content shape.

## By user signal

| User says... | Template | Default volume | Ratio |
|---|---|---|---|
| "carousel", "swipe", "tip pack", "5 tricks", multi-slide | `carousel-cream-rust` | 5–6 slides × N | 1080×1350 |
| "LI image card", "value post", "quote post", "dark editorial" | `li-card-editorial-dark` | 15–30 | 1080×1350 |
| "FB news", "personal FB", news commentary | `fb-news-9card` | 9 × 3 days | 1080×1350 |
| "X pack", "tweet drip", "Twitter thread" | `x-pack` | 12–20 | 1200×675 (only for image tweets) |
| "Pinterest", "Pin", vertical | `pin-card` | 30 | 1000×1500 |
| "Story", "reel cover", 9:16 | `ig-story` | 5–10 | 1080×1920 |
| "video drip", existing MP4s | (no HTML) — `recipes/video-drip.md` | varies | varies |

## By content shape

- **Single hook + body + CTA** → LI single card (editorial dark)
- **Hook → 3-5 tricks → CTA** → carousel (cream+rust)
- **News commentary** (something happened, here's my take) → FB news 9-card
- **Quote / aphorism / cringe-philosopher** → square IG card OR LI single
- **Mixed daily drip** (motivational + tactical + sell) → FB news 9-card or LI batch
- **Visual-led / SEO** (saved-for-later content) → Pinterest

## By platform priority

- **LinkedIn primary** → carousel OR LI card batch
- **IG primary** → carousel (square crop) OR Story
- **FB primary** → FB news 9-card
- **Pinterest primary** → Pin batch
- **X primary** → X pack (text-only OR text-card)

## Cross-platform pack default

For one content topic shipped everywhere:
1. Build carousel (cream+rust) once
2. Re-export square crop for IG carousel
3. Write platform-tuned captions (long LI / hook+CTA IG / conversational FB / tight X)
4. 4 GHL CSVs (LI / FB / IG / Pin) + 1 X txt file
5. Stagger times: LI 11:00 / FB 13:00 / IG 19:00 / Pin 20:00 / X 09:30 EST
