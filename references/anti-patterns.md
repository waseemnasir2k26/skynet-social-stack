# Anti-Patterns — What to Never Ship

Patterns that cratered engagement, ate funnel signal, or got reach-throttled. Don't repeat them.

## Visual

- ❌ **5 posts in same template** — algo flags as repetitive content
- ❌ **Stock photo overlay** — Picsum / Unsplash hot-link looks 2018, also CORS-taints html2canvas
- ❌ **Center-aligned long-form** on LI image cards (eye fatigue, low save-rate)
- ❌ **Photo + 3+ logos in one card** (visual noise, brand confusion)
- ❌ **Light-text-on-light-bg** anywhere (mobile readability dies)
- ❌ **Same headshot on 30+ consecutive posts** (use rotation log)
- ❌ **R3F blob/abstract 3D as hero image** (generic, doesn't communicate)
- ❌ **Picsum placeholder shipped to prod** (happened in skynet-niche-demos pre-rebuild)

## Caption

- ❌ **Em-dash storms** (3+ em-dashes = AI-tell flag)
- ❌ **"Delve" / "moreover" / "furthermore"** (instant LLM-output suspicion)
- ❌ **"In today's fast-paced world"** (corporate copy 2010)
- ❌ **Rule-of-three with abstract nouns** ("clarity, vision, and excellence")
- ❌ **Empty -ing analyses** ("highlighting the importance of...")
- ❌ **"Game-changer" / "revolutionize"** (overused = invisible)
- ❌ **Emojis in every line** (looks like spam, IG already throttles)
- ❌ **5+ hashtags on LI** (algo demotes; ≤3 optimal)
- ❌ **All-caps captions** (reads as shouting, low-trust)

## Funnel

- ❌ **DM keyword post WITHOUT submitted WA template** — Meta needs 24-72h soak; posts before approval = dead funnel
- ❌ **Same keyword across 2 active flows** (ManyChat picks wrong sequence)
- ❌ **No GHL CRM tag on trigger** (lead enters but never gets nurture)
- ❌ **No UTM on Media URLs** (impossible to attribute conversion)
- ❌ **Naked link in caption** (LI suppresses outbound links — use comment-link instead)
- ❌ **CTA = "click bio link"** without verifying the bio link still works
- ❌ **No retargeting pixel** on landing pages where DM clicks land

## Distribution

- ❌ **Pasting GHL CSV with past Schedule Dates** (silent reject, lose 9/30 pins precedent)
- ❌ **Mixed `Account` typo** (`Linkedin` vs `LinkedIn`) — silent reject
- ❌ **Same content × 4 platforms with same caption** (cross-post penalty; needs platform-tuned variants)
- ❌ **No NDA scrub on FB/IG/Pin** (client name leak = relationship damage)
- ❌ **Drop on weekends without cadence-aware shifter** (engagement halves)
- ❌ **Pinterest: 30 pins same hour** (Pin algo throttles bursts; spread across days)
- ❌ **LinkedIn: post + edit within 10 min** (algo suspicion, reach drops)

## Operational

- ❌ **No engagement-seed comments** (first 30 min of LI/IG = make/break, you must prime)
- ❌ **No screenshot proof in image carousels** (claim without proof = save-rate dies)
- ❌ **Forgetting to mark photos used** in rotation log (next pick repeats)
- ❌ **Manual copy-paste 30 captions to GHL** (1 hour wasted, use CSV)
- ❌ **No post-mortem after batch** (no learning loop)
- ❌ **Stale memory drift** ("v1.0.0" when shipped is v1.1.1) — verify before claiming

## Brand

- ❌ **Mixing personal voice + agency voice in one post** (positioning dilution)
- ❌ **Hard sell on personal account** (sells once, kills feed forever)
- ❌ **Vague motivation on agency account** (kills sell signal, lowers price ceiling)
- ❌ **Inventing client metrics** (one fake number = trust gone forever)
- ❌ **Implied scale** ("hundreds of clients") without proof = checkable lie

## Why this list exists

Each one of these = at least one shipped-and-regretted post. This file is the cumulative scar tissue. Read before every batch.

## Add to this list

When a post under-performs OR breaks something:
1. Identify the root anti-pattern
2. Add here under correct section
3. If repeated 2x, escalate to a hard rule in `../SKILL.md`
