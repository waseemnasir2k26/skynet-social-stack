# Changelog

All notable changes to skynet-social-stack.

## [1.1.0] - 2026-04-30 — Senior-SMM upgrade

### Added — content strategy
- `references/aesthetic-rotation.md` — 3-aesthetic mandate (cream+rust → dark+gold → brutalist memphis), kills algo-penalty pattern repetition.
- `references/hook-bank.md` — Tier S/A/B proven openers, 14 patterns + anti-hooks list.
- `references/anti-patterns.md` — visual / caption / funnel / distribution / operational / brand failure modes (scar tissue from shipped batches).
- `references/lead-magnet-bank.md` — keyword → magnet mapping, A/B variant strategy, format ROI ranking, conversion-tracking template.

### Added — scripts
- `scripts/utm_inject.py` — adds utm_source/medium/campaign/content per row to GHL CSV Media URLs.
- `scripts/seed_replies.py` — first-30-min engagement seed comments (8 intent templates: question / story / counter / tactical / resource / tag / reframe).
- `scripts/caption_variants.py` — A/B hook variant generator pulling from hook-bank tiers.

### Added — recipes
- `recipes/post-mortem.md` — engagement retro (top 5 / bottom 5 / pattern extraction / hook-bank update / next-batch action items).
- `recipes/repurpose-chain.md` — 1 topic → 9 derivatives across LI/IG/FB/X/Pin/Newsletter, platform-tuned captions, staggered times.
- `recipes/competitor-sweep.md` — 15-min Sunday sweep of 5-10 peers, pattern-match weekly, ship missing angles within 2 weeks.

### Added — examples
- `examples/10-format-showcase-2026-04-30/` — single-page reference of all 10 post types in 10 distinct aesthetics. Per-format PNG download, full caption + style notes per format.

### Senior-SMM diagnoses fixed
- **Brand-aesthetic lock** → 3-aesthetic rotation enforced.
- **Missing UTM tracking** → utm_inject.py.
- **Algorithm dead first 30 min** → seed_replies.py.
- **No A/B hook testing** → caption_variants.py + hook-bank.
- **No learning loop** → post-mortem recipe.
- **Vacuum-shipping** → competitor-sweep recipe.
- **1 topic = 1 platform waste** → repurpose-chain recipe.
- **No DM-magnet variant testing** → lead-magnet-bank.md.

## [1.0.0] - 2026-04-30

### Added
- Initial release.
- `SKILL.md` master decision logic.
- 5 post-type templates: carousel-cream-rust, li-card-editorial-dark, fb-news-9card, x-pack, pin-card.
- 6 recipes: carousel-launch, li-card-batch, fb-news-3day, x-pack-mwf-drip, pin-batch, cross-platform-pack.
- 7 references: post-type-decision-tree, ghl-csv-format, image-rotation, no-fake-claims, humanizer-checklist, brand-split, manychat-keyword-flow.
- 3 scripts: build_ghl_csv.py, shift_dates.py, pick_avatar.py.
- 1 example: carousel-claude-pack-2026-04-30 (5×6 cards, cream+rust style).

### Source patterns
- LinkedIn editorial dark+gold cards (30+ shipped batches).
- Tenfoldmarc-style cream+rust carousels.
- FB personal-news 9-card mix.
- X 12-pack MWF drip.
- Pinterest 30-pin batch.
- GHL CSV canonical 6-col.
- ManyChat keyword + WA template funnel.
