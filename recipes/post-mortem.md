# Recipe — Post-Mortem (Engagement Retro)

After every batch / drip cycle. 30 min review. Learning loop.

Without this, you ship the same anti-patterns forever.

## When to run

- After every 5+ post drip ends
- Weekly Monday review of last 7 days
- Before starting next major batch (use last batch's lessons)

## Inputs

- Last drip's GHL CSV (sent posts)
- LI / IG / FB / X / Pin native analytics
- Plausible / GA dashboard for landing page traffic
- ManyChat conversion stats per keyword

## Steps

### 1. Pull data (10 min)

For each platform:

| Metric | Source |
|---|---|
| Impressions | Native analytics |
| Engagement rate | Native analytics |
| Saves | LI/IG (key signal for LinkedIn algo) |
| Shares/reposts | Native |
| Comments | Native |
| Click-through | Plausible (UTM-tagged URLs) |
| DM keyword hits | ManyChat |
| Email captures | ManyChat → GHL |
| Booked calls | Calendly / GHL |

### 2. Rank top + bottom (5 min)

```
TOP 5 (by save-rate × reach):
1. {post} — {hook}
2. ...

BOTTOM 5 (lowest engagement):
1. {post} — {hook}
2. ...
```

### 3. Identify patterns (10 min)

For top 5: what do they have in common?
- Hook tier?
- Aesthetic?
- Time of day?
- Format type?
- Topic theme?
- Length?

For bottom 5: what's the shared anti-pattern?
- Same template repeated?
- Hook starts with "I'm excited"?
- Photo blurry / low contrast?
- No CTA?

### 4. Update artifacts (5 min)

- **`references/hook-bank.md`** → promote top hook to Tier S
- **`references/anti-patterns.md`** → add bottom-pattern as new entry
- **`references/aesthetic-rotation.md`** → adjust rotation if one aesthetic dominated

### 5. Action items for next batch

```
NEXT BATCH:
- [ ] Use hook pattern from top performer #1
- [ ] Avoid template reused in bottom 3 (rotate aesthetic)
- [ ] Add UTM if missing (lost attribution this time)
- [ ] Schedule for {best-performing time}
```

## Output template

Save to `outputs/<batch-slug>/post-mortem.md`:

```markdown
# Post-Mortem — {batch slug}
Period: {start date} → {end date}
Posts shipped: {N}

## Top 5
1. {post-id} — {hook line}
   - Reach: {N}, Saves: {N}, Comments: {N}
   - Why it worked: {hypothesis}

## Bottom 5
1. {post-id} — {hook line}
   - Reach: {N}
   - Why it failed: {root cause}

## Patterns identified
- Top 5 share: {pattern}
- Bottom 5 share: {anti-pattern}

## Rules to apply next batch
- Promote: {pattern}
- Kill: {anti-pattern}

## Action items
- [ ] Update hook-bank.md
- [ ] Update anti-patterns.md
- [ ] Adjust aesthetic-rotation if needed
- [ ] Re-test {variant}
```

## Compounding effect

After 5 post-mortems:
- 5 new Tier-S hooks identified
- 5 anti-patterns in the avoid-list
- Template usage data → kill underperformers, double down on winners

After 20 post-mortems = a tight, evidence-based content system. Most agencies skip this and stay generic forever.
