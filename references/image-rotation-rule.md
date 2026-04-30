# Image Rotation Rule (Waseem Photos)

**Hard rule. No exceptions.**

Always pick photos via the rotation script. Never by eye. Mark used after every post.

## Folder

`C:\Users\info\OneDrive\Desktop\GITHUB\WASEEM IMAGES\PROFESSIONAL\`

## Pick

```bash
cd "C:/Users/info/OneDrive/Desktop/GITHUB/WASEEM IMAGES/PROFESSIONAL"
python _pick-next.py                 # 1 photo, lowest used_count
python _pick-next.py --count 5       # batch 5
python _pick-next.py --stats         # usage report
```

Logic: lowest `used_count` first; tie-break by oldest `last_used`.

## Mark used (REQUIRED — do not skip)

```bash
python _pick-next.py --use IMG_2742.JPG.jpeg "carousel-claude-code-2026-04-30"
```

`<post-tag>` should include format + topic + date so future stats are scannable.

## Why this matters

- Without rotation: same 5 "good" photos appear in every post, looks spammy.
- 170+ photos available — use the long tail.
- Log = single source of truth, survives across sessions.

## Same-origin trick for html2canvas

When rendering HTML carousels with `html2canvas`, embed photos as **same-origin file paths** (copy into `outputs/<slug>/_avatars/`) — file:// URLs to a different folder will CORS-taint the canvas.

```bash
mkdir -p outputs/<slug>/_avatars
for f in $(python _pick-next.py --count N); do
  cp "$SRC/$f" "outputs/<slug>/_avatars/"
done
```

Reference relatively in HTML: `<img src="_avatars/IMG_2742.jpg">`.

## After ship

For each photo used in a shipped post:
```bash
python _pick-next.py --use <FILE> "<format>-<topic>-<date>"
```

Batch helper at `scripts/pick_avatar.py` does pick + copy + auto-mark in one call.
