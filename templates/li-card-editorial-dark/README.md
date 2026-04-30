# LI Editorial Dark + Gold | Card Template

Reference template for SkynetLabs LinkedIn image cards. Editorial dark background, gold accent rule, Fraunces serif hook, Inter body, circular avatar with gold ring. Exports at exactly **1080 x 1350 px** PNG via html2canvas, regardless of preview viewport.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Template page. Loads `data.json`, renders 5 responsive previews, ships per-card and bulk PNG export buttons. |
| `data.json` | Array of card objects. Edit this to change copy. |
| `_avatars/` | Drop circular-cropped photos here (square JPGs). Reference per card via `"avatar": "_avatars/IMG_XXXX.jpg"`. |
| `README.md` | This file. |

## Card schema

```json
{
  "slug": "card-01",
  "label": "FIELD NOTES / 01",
  "hook": "Build the demo before the deck.",
  "body": "Pitches die in slide review. Working prototypes get forwarded. Ship the proof first, write the words second.",
  "name": "Waseem Nasir",
  "role": "Founder, SkynetLabs",
  "avatar": "_avatars/IMG_2742.jpg"
}
```

| Field | Constraint |
|-------|------------|
| `slug` | Filename for the exported PNG. Lowercase, kebab-case. |
| `label` | Top-left kicker. Uppercase, 14 px tracked. Keep under 32 chars. |
| `hook` | Big serif statement. 3-7 words ideal. Hard cap ~50 chars or it overflows the 96 px type. |
| `body` | 2-4 lines of supporting copy. 200-280 chars sweet spot. |
| `name` | Bottom-left identity. Fraunces 30 px. |
| `role` | Below name. Inter 16 px tracked. |
| `avatar` | Path relative to `index.html`. 1:1 ratio. Cropped to circle automatically. |

## Workflow

### 1. Fork

Copy the entire `li-card-editorial-dark/` folder to a working directory. Do not edit the template in place.

### 2. Pick photos (rotation-enforced)

```bash
cd "C:/Users/info/OneDrive/Desktop/GITHUB/WASEEM IMAGES/PROFESSIONAL"
python _pick-next.py --count 5
```

Copy each chosen file into `<your-fork>/_avatars/`. Update each card's `avatar` path in `data.json`.

After publishing, mark them used:

```bash
python _pick-next.py --use IMG_2742.JPG li-card-2026-05-XX
```

### 3. Edit copy

Open `data.json`. Each object is one card. Add or remove entries freely. The grid auto-fills.

### 4. Preview

Open `index.html` in a browser. The page scales each card to its container so previews stay readable on phone, tablet, and desktop. The Export node at 1080 x 1350 lives offscreen and is what html2canvas screenshots.

### 5. Export PNGs

- **Per card:** click "Download PNG" under each preview. File saved as `<slug>.png`.
- **Bulk:** click "Export all 5 cards" in the page header. Browser will save one file per card with ~350 ms spacing.

### 6. Headless render (optional, for CI / batches)

If you have Playwright wired:

```python
# render the same HTML headlessly, scroll each .card into view, screenshot at 1080x1350
# see ~/.claude/skills/social-stack/scripts/_render_<batch>.py for canonical pattern
```

## Responsive Contract (every social-stack template inherits)

1. **Viewport meta.** `<meta name="viewport" content="width=device-width, initial-scale=1">` is in the `<head>`.
2. **Scaled preview.** Each card lives inside a `.card-frame` with `width: 100%; aspect-ratio: 1080/1350;`. JavaScript reads the frame width and applies `transform: scale(frameWidth / 1080)` to the inner `.card`. The `.card` itself stays at exact 1080 x 1350 px in the DOM.
3. **Fluid page chrome.** Page header, controls, and gaps use `clamp()` and `vw` units. Card typography is fixed pixel sizes because the card is fixed pixel size.
4. **Dedicated export node.** `<div class="export-stage">` sits offscreen at `left: -10000px`. When you trigger an export, the script clones the chosen card into the export stage, runs html2canvas at the native 1080 x 1350, then clears the stage. The visible scaled preview is never the screenshot source.
5. **Tested viewports.** 360 / 480 / 768 / 1024 / 1440. Cards remain legible at all widths.
6. **Touch targets.** Buttons are >= 44 px tall. On <= 480 px the per-card actions stack vertically and span full width.
7. **Accessibility.** Each card uses `role="img"` + `aria-label` summarising its content. Avatars include `alt`.

## Quality gates

- HTML validates (no broken tags, single H1, semantic landmarks).
- html2canvas renders at exact 1080 x 1350 because the export stage is fixed at that size and `scale: 1` is forced.
- No fake claims in default copy. Real workflow, real positioning, no invented metrics.
- No em-dashes in default copy.
- Fonts (Fraunces, Inter) loaded via Google Fonts; export waits for `document.fonts.ready` before screenshotting.

## Customising the aesthetic

Tokens live at the top of `<style>` in `index.html`:

```css
:root {
  --bg: #0a0a0a;
  --ink: #F5F1EA;
  --gold: #D4AF37;
  --gold-soft: #E8C389;
}
```

Swap `--gold` to retune accent (warmer `#E8C389`, cooler `#C9A227`, deeper `#A8893E`). Keep `--bg` deep black; anything lighter loses the editorial weight.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Avatar shows "WN" initials | Image path wrong or file missing. Check `_avatars/` and the `avatar` field. |
| Hook text overflows | Hook >50 chars. Shorten or split across two cards. |
| Browser blocks bulk download | Some browsers throttle multiple `a.click()` saves. Use per-card download or accept the prompt. |
| Fonts look wrong on first export | Run export once to warm font cache, then re-export. The script awaits `document.fonts.ready` but cold loads can still race. |
| PNG looks blurry | You exported the scaled preview by accident. Confirm script targets `.export-stage > .card`, not the `.card-frame > .card`. |

## Source style spec

Distilled from `~/.claude/projects/C--Users-info/memory/linkedin-card-template-style.md`. Tokens, layout, and export pipeline are 1:1 with shipped batches (viral 30, May 15, etc.) minus the photo background. This template is the typographic / portrait variant of the same aesthetic.
