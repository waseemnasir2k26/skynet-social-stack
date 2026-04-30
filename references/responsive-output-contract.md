---
name: responsive-output-contract
description: Master cross-format responsiveness rule every social-stack template + recipe must follow. Covers HTML cards, PNG exports, PDF carousels, MP4 video drips, and QA gates before GHL upload.
type: reference
---

# Responsive Output Contract

Single source of truth for every visual social-stack ships. HTML renders into PNG, PDF, and MP4 — those land on phones, tablets, desktops, GHL UI, native FB / IG / X / LI feeds. One contract, no exceptions.

If a template or recipe ships visuals, it MUST conform. If it does not, treat as broken.

---

## 1. HTML Templates (cards, carousels, pins, x-pack)

All preview HTML — single cards, carousel decks, X-pack stacks, Pin sheets — uses the **two-node pattern**.

### 1.1 Required document head

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>...</title>
</head>
```

`viewport-fit=cover` matters on iOS notch — preview pages get opened on phones during review.

### 1.2 Two-node pattern (NON-NEGOTIABLE)

Every visual is rendered by **two stacked DOM nodes**:

| Node | Purpose | Sizing |
|---|---|---|
| `.card-export` | Frozen pixel target html2canvas screenshots | Fixed `width` + `height` in `px` (1080×1350 / 1200×675 / 1000×1500 / etc) |
| `.card-frame` | On-page preview, scales to viewport | `aspect-ratio` + `max-width: 100%` — never fixed px |

```html
<div class="card-frame">
  <div class="card-export" id="card-01">
    <!-- all content lives here -->
  </div>
</div>
```

```css
.card-frame {
  width: 100%;
  max-width: 540px;          /* phone-friendly preview width */
  aspect-ratio: 1080 / 1350; /* match export ratio */
  margin: 0 auto 24px;
}
.card-export {
  width: 1080px;
  height: 1350px;
  /* fixed pixel layout inside */
}
/* visually scale export node into the frame */
.card-frame {
  display: grid;
  place-items: center;
  overflow: hidden;
}
.card-export {
  transform: scale(var(--preview-scale, 0.5));
  transform-origin: center;
}
```

JS sets `--preview-scale` based on `card-frame` width / 1080 on resize. Or use CSS `container queries` if all browsers in scope support them.

### 1.3 Typography rules

- **Inside `.card-export`** — fixed `px` for everything. No `vw`, `clamp()`, `em`, `rem` cascading from page root. The export must look identical at any viewport.
- **Outside `.card-export`** (page chrome, download buttons, headings) — `clamp()` / `vw` allowed. This is the live page UI.

```css
/* page chrome — fluid */
h1.page-title { font-size: clamp(1.5rem, 4vw, 2.5rem); }

/* card content — frozen */
.card-export .headline { font-size: 64px; line-height: 1.1; }
```

### 1.4 Touch + accessibility

- Every clickable / tappable element ≥ **44×44 px** (WCAG 2.5.5 / Apple HIG).
- Visual blocks that read as a single image carry `role="img"` + `aria-label="..."`.
- Download buttons stack vertically on `max-width: 480px` viewport. No horizontal scroll on mobile.

```css
@media (max-width: 480px) {
  .download-row { flex-direction: column; gap: 12px; }
  .download-btn { width: 100%; min-height: 48px; }
}
```

### 1.5 Required viewport tests

Before declaring a template done, render the preview HTML at each width and confirm the card-frame is legible AND export buttons are reachable:

| Width | Device class | Must verify |
|---|---|---|
| 360 px | Old Android (Pixel 5 = 393, A-series = 360) | No horizontal scroll |
| 480 px | iPhone SE / small Android | Buttons stacked |
| 768 px | iPad portrait | Frame uses available width gracefully |
| 1024 px | iPad landscape / small laptop | Two-up cards if grid template |
| 1440 px | Desktop / QA monitor | No giant whitespace, max-widths capped |

Use Chrome DevTools device toolbar OR `/browse` skill to take 5 screenshots.

---

## 2. PNG Exports (html2canvas)

The PNG is the artifact GHL / Buffer / Meta accept. The preview is throwaway — the PNG is the product.

### 2.1 Capture config

```js
import html2canvas from 'html2canvas';

async function exportCard(node, filename) {
  // IMPORTANT: temporarily un-scale the export node so it captures at native px
  node.style.transform = 'none';
  const canvas = await html2canvas(node, {
    width: node.offsetWidth,           // 1080 / 1200 / etc
    height: node.offsetHeight,         // 1350 / 675 / etc
    scale: window.devicePixelRatio,    // retina sharpness
    useCORS: true,                     // external images (Unsplash, Vercel CDN)
    backgroundColor: null,             // transparent — OR explicit hex like '#0B0B0F'
    logging: false,
    imageTimeout: 15000,
  });
  // restore preview transform
  node.style.transform = '';

  const blob = await new Promise(r => canvas.toBlob(r, 'image/png', 1.0));
  const url = URL.createObjectURL(blob);
  const a = Object.assign(document.createElement('a'), { href: url, download: filename });
  a.click();
  URL.revokeObjectURL(url);
}
```

### 2.2 Filename pattern

`<format>-<batch>-<NN>.png` — lowercase, kebab-case, two-digit index.

| Format slug | Use for |
|---|---|
| `li` | LinkedIn 1080×1350 / 1080×1080 |
| `fb` | Facebook 1080×1350 / 1200×630 |
| `ig` | Instagram 1080×1350 / 1080×1080 / 1080×1920 |
| `x` | Twitter / X 1200×675 |
| `pin` | Pinterest 1000×1500 |
| `car` | Carousel slide (1080×1350) |

Examples: `li-claude-pack-01.png`, `car-aeo-pivot-03.png`, `pin-batch5-12.png`.

### 2.3 Sanity checks before download

- `card-export` `offsetWidth` matches the platform spec (log it before capture).
- Web fonts loaded — call `document.fonts.ready` before `html2canvas()`.
- External images loaded — wait for all `<img>` `complete === true`.

```js
await document.fonts.ready;
await Promise.all([...node.querySelectorAll('img')].map(img =>
  img.complete ? null : new Promise(r => { img.onload = img.onerror = r; })
));
```

---

## 3. PDF Carousels (slide bundles)

When a recipe ships a carousel as a single PDF (LI document post, Pinterest idea pin alternative, lead-magnet bundle):

### 3.1 Print CSS

```css
@media print {
  @page { size: 1080px 1350px; margin: 0; }
  body { margin: 0; }
  .slide {
    width: 1080px;
    height: 1350px;
    page-break-inside: avoid;
    break-inside: avoid;
    page-break-after: always;
    break-after: page;
  }
  .slide:last-child { page-break-after: auto; break-after: auto; }
  .preview-only { display: none !important; } /* download buttons, page chrome */
}
```

`@page` sizing in `mm`: 1080px ≈ 285.75mm at 96dpi, 1350px ≈ 357.19mm. Use whichever unit your generator respects (`px` works in Chrome, `mm` is the spec-safe choice).

### 3.2 Generation

Preferred — Playwright headless:

```js
await page.pdf({
  path: 'carousel-claude-pack.pdf',
  printBackground: true,
  preferCSSPageSize: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});
```

Fallback — manual Chrome → File → Print → Save as PDF, "More settings" → Background graphics ON, "Paper size" → Custom matching `@page`.

### 3.3 Font embedding

Use `@font-face` with locally bundled `.woff2` OR Google Fonts `display=block`. Never `display=swap` for PDF — FOUT bakes the fallback into the export.

```css
@font-face {
  font-family: 'Fraunces';
  src: url('./fonts/Fraunces.woff2') format('woff2');
  font-display: block;
  font-weight: 100 900;
}
```

---

## 4. Video Drip (MP4 outputs from CapCut / FFmpeg pipeline)

Any recipe that produces video — Reels, YT Shorts, X cards, LI native video, FB native — follows these.

### 4.1 Aspect ratio wrappers (preview HTML)

```css
.v-wrap { width: 100%; max-width: 540px; margin: 0 auto; }
.v-wrap[data-ratio="9:16"]  { aspect-ratio: 9 / 16; }
.v-wrap[data-ratio="1:1"]   { aspect-ratio: 1 / 1; }
.v-wrap[data-ratio="16:9"]  { aspect-ratio: 16 / 9; }
.v-wrap video { width: 100%; height: 100%; object-fit: cover; }
```

### 4.2 Export specs per platform

| Platform | Resolution | Aspect | Max length | Codec | Bitrate |
|---|---|---|---|---|---|
| IG Reel | 1080×1920 | 9:16 | 90 s | H.264 | 8–12 Mbps |
| IG Feed | 1080×1080 | 1:1 | 60 s | H.264 | 5–8 Mbps |
| LI native | 1080×1080 OR 1080×1350 | 1:1 / 4:5 | 10 min | H.264 | 5–10 Mbps |
| X video card | 1280×720 | 16:9 | 2:20 | H.264 | 6–8 Mbps |
| YT Shorts | 1080×1920 | 9:16 | 60 s | H.264 | 8–12 Mbps |
| FB feed | 1080×1080 OR 1080×1350 | 1:1 / 4:5 | 240 min | H.264 | 5–8 Mbps |

### 4.3 FFmpeg recipe (reference)

```bash
ffmpeg -i master.mov \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" \
  -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart \
  ig-reel-aeo-pivot.mp4
```

`-movflags +faststart` is mandatory — moves moov atom to front so platform players start without buffering.

### 4.4 Subtitles (NON-NEGOTIABLE for any drip)

Mobile feeds default to sound-off. Every video ships with **burned-in subtitles** (open captions), not just `.srt` sidecar.

- Generate `.srt` via Whisper or CapCut auto-caption.
- **Hand-correct** every brand name + technical term (Claude, n8n, AEO, citelift, GHL — Whisper mangles these).
- Burn in via FFmpeg `subtitles=captions.srt:force_style='FontName=Inter,FontSize=24,...'` OR CapCut export.
- Position 70% from top on 9:16 (avoid IG/TikTok UI overlay at bottom).

---

## 5. Cross-Platform Layout Poll (MUST do before ship)

Before any PNG / PDF / MP4 leaves the build folder for GHL or a client folder, run the poll:

| Device | Width | Test |
|---|---|---|
| iPhone 12 / 13 / 14 | 390 px | Open PNG in Photos, scroll feed thumbnail |
| iPad portrait | 768 px | PDF carousel swipe-through |
| Pixel 5 / Android | 393 px | Video plays inline (data saver mode) |

### 5.1 Pass criteria

- **Hook visible above the fold on mobile.** If the headline is in the bottom half of a 4:5 card, the LI feed crops it. Move it up.
- **Text legible at 50% scale.** Open the PNG, zoom out to 50% in Windows Photos / Preview app — body text must still read. If it doesn't, font size too small.
- **Color contrast holds.** WCAG AA (4.5:1 for body, 3:1 for large) checked at thumbnail size — gold-on-cream collapses to mud at 200 px wide.
- **No CTA cropped.** Platforms apply safe-area cropping; keep CTA inside the central 80% of the canvas.

### 5.2 Tools

- `/browse` skill — open URL on simulated devices, take screenshots.
- Chrome DevTools Device Mode + DPR slider.
- Real phone — last resort, but the only way to catch font rendering bugs (Inter on iOS Safari renders ~3% wider than Chrome desktop).

---

## 6. QA Gates (before GHL upload)

Hard gates. If any fails, do NOT upload.

### 6.1 PNG gate

- [ ] Filename matches `<format>-<batch>-<NN>.png` pattern.
- [ ] Open in Windows Photos — no banding, no missing fonts (fallback serif = fail).
- [ ] Open on phone (DM yourself, AirDrop, or scp) — looks identical.
- [ ] File size ≤ 2 MB. If >2 MB, run through `pngquant --quality=80-95` or convert to JPG q90.
- [ ] Dimensions match platform spec exactly — verify via `Get-ItemProperty <file>` or `identify <file>` (ImageMagick).

### 6.2 Video gate

- [ ] Plays inline in FB feed (test post to private group / draft).
- [ ] Plays inline in IG feed (test reel to close-friends or private account).
- [ ] Plays in X timeline (draft tweet preview).
- [ ] Plays in LI native player (LI accepts MP4 up to 5 GB, but rejects oddball codecs — H.264 + AAC only).
- [ ] First frame is the hook (not a black/loading frame). Set explicit `-vf "tpad=start_mode=clone:start_duration=0"` if needed.
- [ ] Subtitles burned in, readable, no typos.
- [ ] File size ≤ 512 MB (FB cap). Most drips ship at 30–80 MB.

### 6.3 PDF gate

- [ ] Open in Chrome — pages flip cleanly, no missing chars (□ box = font not embedded, fail).
- [ ] Open in Adobe Acrobat — same render. If different, font embedding failed.
- [ ] File size ≤ 8 MB. Compress images via `gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook` if needed.
- [ ] Page count = slide count. No accidental blank trailing page.

### 6.4 GHL upload gate

- [ ] CSV columns match canonical 6-col format (see `ghl-csv-format.md`).
- [ ] Image URL or local path resolvable from GHL.
- [ ] Caption length within platform limit (LI 3000 / FB 63206 / IG 2200 / X 280 / Pin 500).
- [ ] First emoji or hook within first 125 chars (mobile feed truncation point on FB / LI).

---

## 7. Cross-links

Every template README must include this line:

```md
**Responsive contract:** see [`references/responsive-output-contract.md`](../references/responsive-output-contract.md). Two-node pattern + viewport tests + QA gates are non-negotiable.
```

Every recipe that ships visuals must include this line in its QA section:

```md
**Before GHL upload:** run all gates in [`references/responsive-output-contract.md`](../references/responsive-output-contract.md) §6.
```

Files that MUST link back:
- `templates/li-card/README.md`
- `templates/carousel/README.md`
- `templates/fb-news/README.md`
- `templates/x-pack/README.md`
- `templates/pinterest/README.md`
- `templates/video-drip/README.md`
- `recipes/*.md` — any recipe producing visuals
- Top-level `SKILL.md` — link in the "Quality" section

---

## 8. Diff with anti-patterns

This contract overrides any older guidance. If an existing template contradicts it, the template is wrong, not the contract. Common violations to grep for and fix:

- `.card { width: 100vw; }` — viewport-relative export → blurry PNG. Fix: two-node pattern.
- `font-size: 1.5rem` inside `.card-export` — root font scaling leaks in. Fix: fixed px.
- `html2canvas(node)` with no `scale` — half-resolution PNG on retina. Fix: `scale: window.devicePixelRatio`.
- No `useCORS: true` — Unsplash images render as black rectangles. Fix: add it.
- Subtitle `.srt` shipped without burn-in — 80% of feed views silent. Fix: burn in.
- Single download button row that overflows on mobile. Fix: stack at `max-width: 480px`.

---

**Last updated:** 2026-04-30
**Owners:** social-stack skill maintainers
**Change rule:** any change here ripples to every template + recipe — bump skill MINOR version and note in CHANGELOG.
