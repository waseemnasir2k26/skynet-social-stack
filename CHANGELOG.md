# Changelog

All notable changes to skynet-social-stack.

## [1.2.1] - 2026-04-30 — Cross-link cleanup + video-drip stub

### Fixed — references and recipes (18 broken cross-links → 0)
- `references/anti-patterns.md` — `SKILL.md` → `../SKILL.md`
- `references/brand-split.md` — `feedback-personal-social-style.md` → full memory path (file lives outside skill)
- `references/ghl-csv-format.md` — `shift_dates.py` (×2) → `../scripts/shift_dates.py`
- `references/responsive-output-contract.md` — corrected 5 wrong template folder names (`li-card` → `li-card-editorial-dark`, `carousel` → `carousel-cream-rust`, `fb-news` → `fb-news-9card`, `pinterest` → `pin-card`), reframed `video-drip` as roadmap stub, replaced `recipes/*.md` glob with explicit recipe list
- `recipes/carousel-launch.md` — `index.html` → `../templates/carousel-cream-rust/index.html`; `posts.json` clarified as user-created inline; `MEMORY.md` → full memory manifest path
- `recipes/migrate-old-csv.md` — `build_ghl_csv.py` → `../scripts/build_ghl_csv.py`; `migrate_csv.py` annotated as inline-pasteable; `<name>-LEGACY.csv` placeholder rephrased to avoid linter false-positive

### Added — recipes
- `recipes/video-drip.md` (NEW, 32 lines) — roadmap stub. Marked `## Status: roadmap` so post-type-decision-tree.md no longer references missing file.

### Lint status
- `broken-links` check: 18 → 0
- `em-dashes` check: PASS
- `aria-label` check: PASS
- `avatar-tags` check: PASS

## [1.2.0] - 2026-04-30 — Responsive contract + 4 templates + script canonicalization

### Added — templates (4 of 5 stub folders converted to working templates)
- `templates/li-card-editorial-dark/` — 1080×1350 Fraunces dark+gold LI editorial card. Two-node responsive pattern (fixed 1080×1350 export node + scaled `.card-frame` preview), 5 sample cards, html2canvas + per-card download, font preload gates.
- `templates/fb-news-9card/` — 1080×1350 FB personal-news 9-card mix (4 info + 2 motiv + 2 sell + 1 locked closer). Card #9 visually locked, info cards require source URL (≤48h), JSZip bulk download, 3-day timeline preview.
- `templates/x-pack/` — 1200×675 image-tweet card pack, 12 tweets (4 oneliner / 4 story / 4 thread). Char counter, hook auto-shrink, copy-tweet-text uses `tweet_text` not `card_hook`, ranking rubric in README (impressions×1 + replies×5 + saves×10 + reposts×8).
- `templates/pin-card/` — 1000×1500 Pinterest batch, 30 pins, 3 palette filter (cream/claret/dark), UTM auto-injected at render, date-shift trap warning banner, 70/30 layout.

### Added — references
- `references/responsive-output-contract.md` (NEW) — master cross-format responsiveness contract. Two-node pattern (fixed-px export + fluid preview), html2canvas config, PDF print CSS, video aspect wrappers, per-platform export specs (IG Reel/LI/X/YT/FB), QA gates with file-size caps (PNG <2MB / Video <512MB / PDF <8MB), viewport tests 360/480/768/1024/1440.

### Fixed — scripts (canonical alignment)
- `scripts/build_ghl_csv.py` — REWROTE. Was outputting wrong headers (`Account,Schedule Date,Schedule Time,Caption,Media URL,Hashtags`) which GHL silently rejects. Now outputs canonical 6-col: `postAtSpecificTime (YYYY-MM-DD HH:mm:ss),content,link (OGmetaUrl),imageUrls,gifUrl,videoUrls`. Added input validation, time format guard, csv.QUOTE_ALL.
- `scripts/shift_dates.py` — REWROTE. Reads/writes canonical `postAtSpecificTime` column. try/except on malformed dates with row-index error reporting. Combined datetime preserved across shifts.
- `scripts/pick_avatar.py` — HARDENED. Validates picker output exists in PROFESSIONAL/ before copy. Forces explicit `--mark <tag>` OR `--no-mark` flag (no silent skip — was rotation-rule violation). Tag format regex enforces `<fmt>-<yyyy-mm-dd>-<slug>` per feedback-image-rotation.

### Fixed — references
- `references/ghl-csv-format.md` — REWROTE. Killed broken header set that was being taught as canonical. Now matches memory `ghl-csv-sample-reference.md` exactly. Added field-by-field spec table, anti-pattern reject-on-sight list (8 items), pre-upload checklist.

### Fixed — recipes (closed action loops)
- `recipes/competitor-sweep.md` (31→ ~46/50) — Was observation dead-end. Now: peer scan → score on post-mortem rubric → 4 parallel artifact updates (hook-bank, aesthetic-rotation, anti-patterns) → feeds next batch via li-card-batch + x-pack-mwf-drip. Output file `outputs/competitor-sweep-<YYYY-MM-DD>.md`.
- `recipes/x-pack-mwf-drip.md` (33→ ~46/50) — Was orphan from hook-bank. Now: hooks SOURCED from hook-bank → 12 drafts → ranking rubric /15 (hook strength + specificity + saveability) → top 10 keep → image cards via templates/x-pack → UTM inject → GHL CSV → Day-21 post-mortem promotes top 3 back, demotes bottom 3.

### Frontmatter
- `version: 1.1.0` → `version: 1.2.0`
- Added `repo: https://github.com/waseemnasir2k26/skynet-social-stack` to SKILL.md frontmatter
- Added rule #9 (Responsive output contract) to SKILL.md rules list

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
