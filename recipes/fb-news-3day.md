# Recipe — FB Personal News (9-card × 3-day drip)

Personal Facebook news commentary. 9-card mix per drip cycle.

Reference: `fb-personal-news-template-style` (memory).

## The 9-card mix

| # | Type | Posting time |
|---|---|---|
| 1-4 | Info / news commentary (real news ≤ 48h) | 11:00 / 16:00 / 21:00 |
| 5-6 | Motivational (story + lesson) | 11:00 / 16:00 |
| 7-8 | Soft sell (project tease, no hard pitch) | 21:00 / 11:00 |
| 9 | Locked closer ("what I build") | 21:00 (Day 3) |

3-day drip @ 3 posts/day = 9 total.

## Inputs

- 4 news anchors (verify ≤ 48h fresh)
- 2 motivational topics
- 2 soft-sell topics
- 1 closer ("here's what I'm building")

## Steps

### 1. Verify news (5 min)
Each news anchor must be from last 48h. Fetch source URL.

### 2. Pick avatars
```bash
python scripts/pick_avatar.py --count 9 --dest outputs/fb-news-<date>/_avatars/
```

### 3. Fork template
`templates/fb-news-9card/index.html`.

### 4. Write captions
Personal voice. Conversational. One question per post. Apply `references/brand-split.md` (personal side).

### 5. Render PNGs

### 6. Build GHL CSV
```bash
python scripts/build_ghl_csv.py \
  --input posts.json \
  --output csv/ghl-facebook.csv \
  --account "Facebook - Waseem" \
  --start <date> \
  --time 11:00 \
  --cadence daily
```
Manually adjust 3 rows per day to 11:00 / 16:00 / 21:00.

### 7. Mark photos used (post-ship).
