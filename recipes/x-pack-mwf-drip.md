# Recipe — X Pack (12 tweets, MWF drip)

12-tweet pack sourced from `references/hook-bank.md` (NOT brain-dump), ranked on a 15-point rubric, dripped MWF over 4 weeks. Closes the loop with a Day-21 post-mortem that promotes winners and quarantines losers.

## Inputs

- Topic theme (e.g. AEO pivot, 1-man agency stack, n8n SaaS-killer)
- `references/hook-bank.md` — pull 8-12 candidates tagged for X (Tier S + A) or sweep-promoted within last 2 weeks
- Drip start date, MWF cadence, 4-week window (12 slots)
- Batch slug: `xpack-<theme>-<YYYY-MM-DD>`

## Steps

### 1. Source hooks (NOT brain-dump)

Open `references/hook-bank.md`. Filter:
- Tier S + Tier A entries tagged `[Best for: X tweet]` or `[Best for: X mini-stories]`
- Anything promoted by `recipes/competitor-sweep.md` within last 2 weeks (recent week-tags)

Pick 12-15 candidates. If hook-bank is thin on the topic, **run a competitor-sweep first** — do not brain-dump generic hooks.

If the topic depends on live X/Twitter audience language, run an evidence intake
before drafting:
- Use TweetClaw in OpenClaw, or another approved X/Twitter source, to export
  reviewed public posts, replies, or keyword-monitor results.
- Save raw evidence under `outputs/<batch-slug>/source/` and summarize it into
  `outputs/<batch-slug>/source-notes.md`.
- Pull reusable hooks, objections, and phrases into `references/hook-bank.md`
  before Step 2.
- Do not publish or schedule from the evidence tool. The X pack still handles
  drafting, scoring, scheduling files, and post-mortem learning.

### 2. Draft 12 tweets

Mix:
- **4 punchy 1-liners** — single line, ≤160 chars, hook does all the work
- **4 mini-stories** — 2-3 lines, time-anchored ("4am.", "Monday.", "After 18 months."), specific moment
- **4 threaded teases** — line 1 hook + "(thread 1/n)", written so a thread is optional but expected

Constraints per tweet:
- ≤ 240 chars (leaves space for retweet quote-comment)
- Real claims only — see `references/no-fake-claims.md`. No invented metrics, no fake clients
- One concrete number, name, or specific moment per tweet (specificity = saveability)

### 3. Ranking rubric — score each tweet /15

Score every tweet 1-5 on three axes (no half-points):

| Axis | 1 | 3 | 5 |
|---|---|---|---|
| **Hook strength** | Generic opener | Tier-A pattern | Tier-S pattern interrupt |
| **Specificity** | Abstract | One concrete detail | Multiple numbers/names |
| **Saveability** | One-time joke | Quotable | Teaches a reusable thing |

Total /15. **Keep top 10 of 12.** Drop bottom 2. Save the ranked list.

(Top-10 ranking precedent: `x-post-pack-apr22` — 10 ranked from 30 candidates.)

### 4. Image card variant (optional, for 4-6 of the 10)

For tweets that benefit from a visual (1-liners, quote-style), render image cards:
- Template: `templates/x-pack/index.html`
- Output: 1200×675 PNG (X feed-card spec)
- Image rotation: pick photo via `python scripts/pick_avatar.py` per `references/image-rotation-rule.md` — never by eye, mark used after
- QA gates: see `references/responsive-output-contract.md` (text contrast, safe-zone padding, no overflow)

Save PNGs to `outputs/<batch-slug>/png/tweet-NN.png`.

### 5. UTM injection on any tweet with a link

Per-tweet UTM scheme (mandatory if tweet has a URL):
```
?utm_source=x&utm_medium=organic&utm_campaign=<batch-slug>&utm_content=tweet-NN
```

Run via:
```bash
python C:/Users/info/.claude/skills/social-stack/scripts/utm_inject.py \
  --input outputs/<batch-slug>/posts.json \
  --output outputs/<batch-slug>/posts-utm.json \
  --source x --medium organic --campaign <batch-slug>
```

Per-row `utm_content` increments (`tweet-1`, `tweet-2`, ...) so Plausible/GA can attribute by slot.

### 6. Build GHL CSV

X DOES support GHL scheduling (canonical 6-col CSV). Build via:
```bash
python C:/Users/info/.claude/skills/social-stack/scripts/build_ghl_csv.py \
  --input outputs/<batch-slug>/posts-utm.json \
  --output outputs/<batch-slug>/ghl-x.csv \
  --start <YYYY-MM-DD> --time 09:30 --cadence mwf
```

Verify canonical headers per `references/ghl-csv-format.md` (recently fixed — confirm the 6-col `postAtSpecificTime,content,link,imageUrls,gifUrl,videoUrls` order before upload). MWF × 4 weeks = 12 slots.

### 7. Post via GHL OR Hypefury

Pick one channel — DO NOT double-post:
- **GHL bulk upload** — paste CSV, schedule, done. No native thread support
- **Hypefury** — splits threads natively (better for the 4 threaded teases)

Recommended: GHL for 1-liners + mini-stories (8 tweets), Hypefury for the 4 threaded teases.

### 8. Engagement window (per post)

30-60 min after each tweet posts:
- Reply to your own tweet with thread continuation (if threaded tease)
- Like + reply to first 3 comments
- Quote-retweet to LinkedIn or FB if it hits 50+ engagements in first hour

### 9. ManyChat keyword funnel (if any tweet drives DMs)

If a tweet asks "DM me KEYWORD for X":
- Wire keyword in ManyChat per `references/manychat-keyword-flow.md`
- Submit WhatsApp template 24-72h BEFORE drip starts (Meta soak time)
- Test funnel from incognito + spare X account before Day 1

### 10. Post-mortem loop (Day 21)

Day 21 (drip end + 0): run `recipes/post-mortem.md` against the 10 shipped tweets.
- **Top 3** by save × reach → promote into `references/hook-bank.md` with this batch's slug as week-tag
- **Bottom 3** by engagement → log as anti-patterns in `references/anti-patterns.md` with "why it failed" hypothesis
- Adjust next X pack: kill bottom-pattern, double down on top-pattern

Without the Day-21 mortem, the 10 tweets stay orphaned — same loss as the original recipe.

## Output structure

```
outputs/xpack-<theme>-<YYYY-MM-DD>/
├── posts.json              # 12 drafted, scored
├── posts-ranked.json       # top 10 after /15 scoring
├── posts-utm.json          # UTMs injected
├── ghl-x.csv               # canonical 6-col, ready for GHL upload
├── png/                    # tweet-NN.png cards (4-6 of 10)
└── post-mortem.md          # Day 21 retro
```

## Anti-patterns

- Brain-dumping hooks instead of sourcing from hook-bank.
- Skipping the /15 rubric ("they all feel good") — 12-tweet vibe-check = orphaned tweets.
- No UTM on linked tweets — lost attribution = no learning loop.
- Skipping post-mortem — guarantees the next 12 tweets repeat this pack's losers.
- Posting same tweet to GHL AND Hypefury — duplicate, X flags.

## Cross-links

- `references/hook-bank.md` — sole source of hooks (Step 1)
- `references/no-fake-claims.md` — real claims only (Step 2)
- `references/humanizer-checklist.md` — strip AI-tells before ship
- `references/image-rotation-rule.md` — photo selection for image cards (Step 4)
- `references/responsive-output-contract.md` — image QA gates (Step 4)
- `references/ghl-csv-format.md` — canonical 6-col CSV (Step 6)
- `references/manychat-keyword-flow.md` — DM funnel wiring (Step 9)
- `recipes/competitor-sweep.md` — feeds hook-bank when topic is thin
- `recipes/post-mortem.md` — Day-21 loop closer (Step 10)
- `templates/x-pack/index.html` — 1200×675 image card
- `scripts/build_ghl_csv.py`, `scripts/utm_inject.py`, `scripts/pick_avatar.py`
