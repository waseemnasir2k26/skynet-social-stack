# Recipe — Weekly Competitor Sweep

15 min, every Sunday. Watch 10-15 peers, score their best 3 posts, **promote signal into the system**: hook-bank, aesthetic-rotation, anti-patterns. Observation that doesn't move artifacts is wasted observation.

## Why

If the sweep ends in a screenshot folder, you ship in a vacuum. This recipe closes the loop — every Sunday's findings feed Monday's batch via `recipes/li-card-batch.md` and `recipes/x-pack-mwf-drip.md`.

## Inputs

- 10-15 peer accounts (curated list below — refresh quarterly)
- Public engagement on each peer's top posts (LI / X / IG native UI)
- 15 minutes, scheduled recurring Sunday slot

## Workflow (15 min)

### 1. Identify peers (one-time, refresh quarterly)

Curate **10-15** accounts split:
- 5 same-niche operators
- 5 adjacent-niche (lateral inspiration)
- 3-5 aspiration-tier (1-2 levels ahead)

Cite aesthetics seen in `references/aesthetic-rotation.md` — log peer next to the aesthetic they own (e.g. `@tenfoldmarc → cream+rust`).

If peer hasn't shipped in 30 days → drop, replace with active operator.

### 2. Snapshot top 3 posts per peer (8 min)

For each peer, open profile → identify the **3 posts with highest visible engagement this week**. For each post record:
- Hook line (first 1-2 lines)
- Format (carousel / single / video / text / news / quote)
- Aesthetic tag (palette + layout, not pixels)
- Engagement (likes + comments + reposts)
- URL (for source attribution)

### 3. Score each post (4 min)

Use the rubric from `recipes/post-mortem.md` (steps 2-3). Rate 1-5 on:
- **Hook strength** — pattern interrupt, specificity, tension
- **Aesthetic novelty** — does it stand out in the feed
- **Engagement** — normalize against peer's baseline (a 2K-like post on a 50K-follower account ≠ on a 5K account)

Total /15. Keep posts scoring **≥10** for promotion. Drop the rest.

### 4. Promote signal into artifacts (3 min)

Four parallel actions — every sweep MUST update at least three of these files:

**Action 1 — Top 3 hooks → `references/hook-bank.md`**
Append to the appropriate tier (S/A/B). Format:
```
"<pattern>" — <example, paraphrased not copied>
[Why it works]
[Best for: format / platform]
[Source: @peerhandle, observed YYYY-WW]
```
Source attribution + week tag is mandatory — lets you trace stale entries 6 months later.

**Action 2 — Top 3 aesthetics → `references/aesthetic-rotation.md`**
Note PALETTE + LAYOUT patterns only (e.g. "cream + rust + circuit motif, single-template across all 6 slides"). NEVER pixel-copy — see Action 5.

**Action 3 — Anti-patterns spotted → `references/anti-patterns.md`**
If a peer's top post failed despite high reach (low save rate, ratio'd comments, generic hook) → log as anti-pattern with "why it failed" hypothesis.

**Action 4 — Feed next batch**
Hook-bank deltas from Action 1 are now seed input for the next:
- `recipes/li-card-batch.md` (15-30 LI cards)
- `recipes/x-pack-mwf-drip.md` (12 tweets MWF)
- `recipes/carousel-launch.md` (5 carousels)

Mark hook-bank entries with `WEEK-TAG` so next batch can filter "promote anything from last 2 weeks".

**Action 5 — Humanizer pass on absorbed hooks**
Before any borrowed hook ships, run through `references/humanizer-checklist.md`. AI-tell phrases ("In today's fast-paced world", em-dash overuse, rule-of-three padding) get stripped. Voice must match Waseem/SkynetLabs, not the source peer.

### 5. Save sweep output

Write to: `outputs/competitor-sweep-<YYYY-MM-DD>.md`

```markdown
# Competitor Sweep — <YYYY-MM-DD> (Week W of YYYY)

## Peers scanned
@peer1, @peer2, ... (12 total)

## Top 3 hooks promoted → hook-bank
1. "<pattern>" — Tier <S/A/B> — source @peer — score 13/15
2. ...
3. ...

## Top 3 aesthetics logged → aesthetic-rotation
1. <palette + layout note> — source @peer
2. ...
3. ...

## Top 3 anti-patterns logged → anti-patterns
1. <pattern> — why it failed
2. ...
3. ...

## Feed-forward
- Next LI batch (`li-card-batch.md`): use hook #1 + #3
- Next X pack (`x-pack-mwf-drip.md`): use hook #2 as 1-liner template
- Next carousel: try aesthetic #2 in slide-1 hero

## Skipped
- @peer-X (no posts this week)
- @peer-Y (dropped — 35-day silence)
```

## Active peer list (curate)

**Builder LinkedIn / X (5):**
- @tenfoldmarc — design + builder content (cream+rust template ref)
- @yashprakash13 — solo founder
- @swyx — AI dev tools
- @mattshumer_ — AI shipping
- @raulonastool — automation systems

**Agency / Freelance (5):**
- @AINewsByJoseph — news + commentary
- @dvassallo — solo consultant
- (3 slots open — fill from your niche)

**Aspiration tier (3-5):**
- @nikitabier — growth/product
- @paulg — long-form essays
- (1-2 slots open)

Refresh quarterly. Drop dead accounts, add new operators.

## No-fake-claims rule (HARD)

Per `references/no-fake-claims.md`:
- **NEVER copy a competitor's exact hook, caption, or claim.** Algo flags duplicates. Audience notices.
- Learn the **pattern** (hook structure, palette family, post format), then rebuild with your own real proof.
- Every promoted hook gets a Waseem/SkynetLabs proof anchor before shipping. No invented metrics.

## Anti-patterns of the sweep itself

- Sweep daily — too noisy, weekly is plenty.
- Sweep 30 peers — too many = no insight. 10-15 max.
- Skip recording — without notes, you forget the angle by Monday.
- Sweep but never feed artifacts — observation without promotion = wasted hour.
- Pixel-copy aesthetics — track palette/layout patterns, not exact templates.

## Compounding effect

12 weeks × 3 hooks promoted = 36 evidence-backed hooks added to hook-bank per quarter. After 6 months you have 70+ peer-validated openers feeding every batch.

## Cross-links

- `recipes/post-mortem.md` — scoring rubric source (1-5 hook/aesthetic/engagement)
- `recipes/li-card-batch.md` — consumes promoted hooks
- `recipes/x-pack-mwf-drip.md` — consumes promoted hooks
- `recipes/carousel-launch.md` — consumes promoted aesthetics
- `references/hook-bank.md` — Action 1 destination
- `references/aesthetic-rotation.md` — Action 2 destination + peer aesthetic map
- `references/anti-patterns.md` — Action 3 destination
- `references/humanizer-checklist.md` — Action 5 strip pass
- `references/no-fake-claims.md` — copy-vs-learn boundary
