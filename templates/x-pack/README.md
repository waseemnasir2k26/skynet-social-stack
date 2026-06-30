# Template — X Pack (12 image tweets, MWF drip)

Editorial dark+gold image tweet template for X / Twitter.
Renders 12 tweet cards at exactly **1200×675** (X 16:9 image card).

> **No GHL.** X is scheduled via native X Scheduler or Hypefury. See `recipes/x-pack-mwf-drip.md`.

---

## Pack rules

- **Volume:** 12 tweets per pack
- **Cadence:** MWF × 4 weeks (Mon / Wed / Fri = 12 slots = 4 weeks)
- **Mix:**
  - 4 punchy 1-liners (`type: oneliner`)
  - 4 mini-stories (`type: story`)
  - 4 threaded teases (`type: thread`) with `thread_followups[]`
- **Tweet text:** ≤240 chars (leaves room for X link card preview)
- **Structure:** Hook line 1 / punch or specific line 2 / optional CTA line 3
- **No em-dashes, no fake claims** (see `references/no-fake-claims.md`, `references/humanizer-checklist.md`)

---

## Card layout

```
┌──────────────────────────────────────────────┐  1200×675 (16:9)
│ ● @waseembali2k26                  [TYPE]    │
│                                              │
│                                              │
│         The hook headline goes here          │  Fraunces 72px (auto-shrinks 60→54)
│         Italicized accent in gold            │
│                                              │
│   Body sits below in two-line Inter 24px.    │  Inter 24px, dim gold body
│                                              │
│  SkynetLabs · WASEEM NASIR     [photo 96px]  │  Bottom row, gold ring
└──────────────────────────────────────────────┘
```

### Color tokens

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#0a0a0a` | Card background |
| `--paper` | `#F5F1EA` | Primary text |
| `--gold` | `#D4AF37` | Accent / dot / pill / photo ring |
| `--dim` | `#7a7268` | Brand metadata |

### Type

- **Hook** — Fraunces 72px, line-height 1.05, letter-spacing -1.2px
- **Body** — Inter 24px, line-height 1.4
- **Pill / handle / brand** — JetBrains Mono 13–18px

Hook auto-shrinks to **60px** at 32+ chars and **54px** at 50+ chars.

---

## How to use

```bash
# 1. Edit data.json (12 entries)
# 2. Drop avatar photos into _avatars/ (run image rotation pick first)
# 3. Serve locally (file:// blocks fetch)
python -m http.server 8000
# 4. Open http://localhost:8000/templates/x-pack/

# In the page:
# - Tabs filter by type (All / 1-liner / story / thread)
# - Each card has live char counter (red ≥ 240)
# - "Copy tweet text" copies the actual tweet_text (NOT the card hook)
# - "Download PNG" exports exact 1200×675 PNG
# - "Download all 12 PNGs (zip)" bulk-renders the pack
```

---

## `data.json` schema

```jsonc
[
  {
    "id": 1,
    "type": "oneliner | story | thread",
    "tweet_text": "≤240 char body actually posted to X",
    "card_hook": "Visual card hook, 3–7 words",
    "card_body": "1–2 lines for the image card",
    "photo": "_avatars/IMG_XXXX.jpg",
    "thread_followups": ["(2/N) ...", "(3/N) ..."]   // only for type=thread
  }
]
```

---

## Tweet ranking rubric (post-flight)

After the pack drips, rank top tweets to feed back into `references/hook-bank.md`.

**Score = (impressions × 1) + (replies × 5) + (saves/bookmarks × 10) + (reposts × 8)**

| Metric | Weight | Why |
|---|---|---|
| Impressions | 1× | Reach baseline. Cheap signal. |
| Replies | 5× | Conversation depth. X's algo loves it. |
| Saves / bookmarks | 10× | Highest-intent signal — "I'll act on this later" |
| Reposts | 8× | Network amplification |
| Profile clicks | 3× | Funnel-adjacent |

**After every pack:**
1. Pull X native analytics for all 12 tweets.
2. Rank by score above. Top 3 → `references/hook-bank.md` (Tier S/A based on score band).
3. Bottom 3 → `references/anti-patterns.md` (mark the failure mode: weak hook, no specificity, no payoff, etc.).
4. Run full retro per `recipes/post-mortem.md`.

> Cross-link: see `recipes/post-mortem.md` for the full data-pull → patterns → action-items flow.

---

## Hook bank source

All 12 hooks should pull from or feed back into:

- **Source:** `references/hook-bank.md` (Tier S / Tier A patterns)
- **Optional X/Twitter evidence:** reviewed TweetClaw exports or another
  approved source, summarized into `outputs/<batch-slug>/source-notes.md`
- **Anti-patterns to avoid:** `references/anti-patterns.md`
- **Voice:** Real proof only. SkynetLabs receipts, not invented metrics. See `references/no-fake-claims.md`.

After a pack ships, top 3 hooks promote into `hook-bank.md`. Bottom 3 demote/log into `anti-patterns.md`.

---

## RESPONSIVE CONTRACT

This template MUST satisfy all of the following — same contract used across the social-stack templates.

1. **Viewport meta** — `<meta name="viewport" content="width=device-width, initial-scale=1">` is set in `<head>`.
2. **Fixed export node + scaled preview** — the actual `.card` is rendered at exact **1200×675**. The preview frame uses `aspect-ratio: 1200/675; max-width: 100%;` and a JS-driven `transform: scale()` keeps the preview fluid without distorting the export size.
3. **Fluid page chrome** — page padding, headline, and tab sizes all use `clamp()` / vw-aware values so layout breathes from 320 → 1920.
4. **Dedicated 1200×675 export sibling** — html2canvas captures from a freshly-spawned, off-screen `.export-stage` node at exact dims. Preview scale never affects export output.
5. **Tested breakpoints** — `360 / 480 / 768 / 1024 / 1440`. Grid collapses to 1-col below 768. Bulk bar stacks below 480. Tabs shrink below 768.
6. **Touch targets ≥ 44px** — all `.tab`, `.btn`, `.btn-zip`, `.btn-gold` enforce `min-height: 44px` for thumb tap on mobile.
7. **Accessibility** — preview wrapper has `role="img"` + `aria-label` describing the card content. Tabs use `role="tab"`. Native button semantics retained.

---

## Quality gates

Before shipping a pack, verify:

- [ ] 12 entries, type-mix is 4/4/4
- [ ] All `tweet_text` ≤ 240 chars (counter green or neutral, never red)
- [ ] Each `thread` entry has 3–4 `thread_followups`
- [ ] No em-dashes anywhere (find/replace before commit)
- [ ] No invented metrics — every claim traceable to a real client/repo
- [ ] All photos picked via `python _pick-next.py` (rotation log, no repeats)
- [ ] One PNG renders cleanly at 1200×675 before bulk-zipping
- [ ] Tested at 360/768/1440 widths

---

## Related

- **Recipe:** `recipes/x-pack-mwf-drip.md` (full drip flow, image-tweet variant note)
- **Post-mortem:** `recipes/post-mortem.md` (engagement retro after every pack)
- **Hook bank:** `references/hook-bank.md`
- **Image rotation:** `references/image-rotation-rule.md`
- **Anti-patterns:** `references/anti-patterns.md`
- **No-fake-claims:** `references/no-fake-claims.md`
