# Recipe — Repurpose Chain (1 topic → 9 derivatives)

One core topic. Nine platform derivatives. Maximum leverage per idea.

## The chain

For one topic (e.g. "1-Man Agency Stack"):

```
ORIGIN: master-content (long-form essay or carousel)
  ├── 1. LinkedIn carousel (6 slides)              ← carousel-cream-rust
  ├── 2. LinkedIn single card (quote + photo)      ← li-card-editorial-dark
  ├── 3. LinkedIn text-only post (1500 chars)      ← li-text-only
  ├── 4. Instagram carousel (square crop, 6 slides)← carousel-cream-rust (re-export 1080×1080)
  ├── 5. Instagram Story 5-frame swipe set         ← story-9-16
  ├── 6. Facebook news commentary (1-card)         ← fb-news-9card single
  ├── 7. Pinterest pin (vertical 1000×1500)        ← pin-card
  ├── 8. X thread (5-7 tweets) + image tweet hero  ← x-pack
  └── 9. Newsletter blurb (short hook + read-more) ← newsletter-blurb
```

Optional: 10. Reel/Short script (9:16 video) for video repurpose.

## Time

- Origin content: 60 min
- 9 derivatives: ~30 min total (15 platform-tuned captions + crop/render existing assets)

## Steps

### 1. Build the origin (60 min)
Pick origin format based on topic shape:
- **Tip pack with N tricks** → start with carousel (cream+rust), 6 slides
- **Long story / essay** → start with LI text-only post (1500 chars)
- **Single big claim** → start with quote card (Brutalist Memphis)

Origin is the highest-fidelity version. Everything else compresses or angles from it.

### 2. Derive (per platform)

| Derivative | Compression / Angle |
|---|---|
| LI carousel | (origin if carousel) OR slice essay into 6 slide tiles |
| LI single card | Pull #1 punch line as quote → editorial dark+gold render |
| LI text-only | Pull body of essay; format with line-breaks; no image |
| IG carousel | Re-export carousel slides as 1080×1080 (square crop) |
| IG Story 5-frame | Extract 5 hooks (1 per frame); sticker-style render |
| FB news commentary | Reframe as "Wait, here's what I noticed" + 1 hero card |
| Pinterest pin | Pull title + body lead → 1000×1500 magazine-style render |
| X thread | Each carousel slide → 1 tweet; thread the 6 |
| Newsletter blurb | 100-word teaser + "read full" link to landing |

### 3. Platform-tune captions

Each derivative = different audience. Don't paste-blanket.

- **LI** = long-form, professional, 5-7 paragraphs
- **IG** = hook + bullet + CTA, heavy line breaks
- **FB** = conversational, ask a question
- **X** = 240-char punch, optional thread continuation
- **Pinterest** = title + benefit + save-CTA
- **Newsletter** = direct, signature voice

### 4. Cross-platform CSVs

Build 4 GHL CSVs (LI / FB / IG / Pin):
```bash
python scripts/build_ghl_csv.py --input posts-li.json --output csv/ghl-linkedin.csv \
  --account "LinkedIn - Waseem" --start <date> --time 11:00 --cadence weekday
# repeat for fb (13:00), ig (19:00), pin (20:00)
```

X = separate text drip file (no GHL).

### 5. Stagger times (same calendar day)

| Platform | Time (EST) | Why |
|---|---|---|
| LinkedIn | 11:00 | Peak professional scroll |
| Facebook | 13:00 | Lunch-time scroll |
| X | 14:00 | Afternoon dev Twitter |
| Instagram | 19:00 | Evening leisure |
| Pinterest | 20:00 | Evening planning/save |
| Newsletter | Tuesday 8 AM | Best email open day |

Same idea hits 4-5 channels in 9 hours = reinforcement learning effect on audience.

## Output structure

```
outputs/<topic-slug>-<date>/
├── origin/
│   └── master-essay.md
├── derivatives/
│   ├── 01-li-carousel/index.html
│   ├── 02-li-single-card/index.html
│   ├── 03-li-text-only/index.html
│   ├── 04-ig-carousel/index.html
│   ├── 05-ig-stories/index.html
│   ├── 06-fb-news-card/index.html
│   ├── 07-pin/index.html
│   ├── 08-x-thread/thread.txt
│   └── 09-newsletter/blurb.html
├── csv/ (4 platforms)
├── captions/ (4 platforms)
└── _README.md
```

## Compounding wins

- Same idea, 9 audience touchpoints
- Track which derivative converts best per topic
- Over time: which topics deserve full chains, which don't

## Anti-patterns

- ❌ Copy-paste same caption 9 times
- ❌ Skip platform-tuning ("LinkedIn voice ≠ Instagram voice")
- ❌ Drop all 9 same hour (looks like bot, throttled)
- ❌ Forget UTM per derivative (can't attribute later)
- ❌ Use same hashtags everywhere (each platform has its own algo signal)
