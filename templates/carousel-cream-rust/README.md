# Template — Carousel Cream + Rust (5 carousels x 6 slides)

Tenfoldmarc-style editorial carousel pack for LinkedIn + Instagram.
Renders 5 carousels x 6 slides = **30 cards** at exactly **1080x1350** (IG/LI 4:5).

> Scheduled via GHL or LinkedIn native scheduler. See `recipes/carousel-li-ig-drip.md`.

---

## Pack rules

- **Volume:** 5 carousels x 6 slides = 30 cards per pack
- **Cadence:** 1 carousel / week x 5 weeks (Mon 11:00 EST default slot)
- **Slide structure (per carousel):**
  - Slide 1: `kind: hero` — bold hook + intro terminal
  - Slides 2-5: `kind: trick` — numbered tip with terminal proof
  - Slide 6: `kind: cta` — close + 3 CTA pills (last pill highlighted)
- **No em-dashes, no fake claims** (see `references/no-fake-claims.md`, `references/humanizer-checklist.md`)

---

## Card layout (1080x1350)

```
+---------------------------------------+ 1080x1350 (4:5)
| @handle                       01 / 06 |  tag-row 18px JetBrains Mono
|                                       |
| SECTION TAG (rust accent)             |
|                                       |
| HEADLINE LINE 1                       |  Archivo Black 104px (88 sm / 72 xs)
| HEADLINE LINE 2                       |  .accent -> rust
| HEADLINE LINE 3                       |
|                                       |
| SUBHEAD UPPERCASE INTER 22PX          |
|                                       |
|   [terminal label * Run this:]        |
|   .-----------------------------.     |  terminal block (dark, rounded)
|   | o o o                       |     |
|   | $ command                   |     |  $ prompt = rust
|   | -> arrow line               |     |  -> arrow = grey
|   | [OK] success                |     |  [OK] = green
|   | [X] failure                 |     |  [X] = red
|   '-----------------------------'     |
|                              [ROBOT]  |  mascot SVG bottom-right
|                                       |
|   . . . . . .                         |  dot indicator (current = rust)
|                                       |
| [avatar] handle [v]   SWIPE -->       |
+---------------------------------------+
```

### Color tokens

| Token | Hex | Use |
|---|---|---|
| `--cream` | `#F2EBE0` | Card background |
| `--rust` | `#C4502E` | Accent / arrow / dot active |
| `--rust-dark` | `#A23A1F` | Hover / mascot gradient |
| `--ink` | `#1F1B17` | Primary headline text |
| `--ink-soft` | `#3A332C` | Subhead body |
| `--term-bg` | `#1A1614` | Terminal block bg |
| `--term-fg` | `#E8DFCF` | Terminal text |

### Type

- **Headline** — Archivo Black 104px (sm 88px / xs 72px), letter-spacing -2.5px, line-height 0.92
- **Subhead** — Inter 22px / 700 / uppercase, line-height 1.45
- **Section tag** — JetBrains Mono 18px / 700, rust, tracking 3px
- **Terminal** — JetBrains Mono 22px, line-height 1.65
- **Tag row + handle** — JetBrains Mono 18-20px / 700

---

## How to use

```bash
# 1. Edit data.json (5 carousels x 6 slides)
# 2. Drop avatar photos into _avatars/ (run image rotation pick first)
# 3. Serve locally (file:// blocks fetch)
python -m http.server 8000
# 4. Open http://localhost:8000/templates/carousel-cream-rust/

# In the page:
# - Tabs filter by carousel (5 tabs, 1 = active)
# - Each card frame previews at responsive width
# - "Download PNG" exports exact 1080x1350 PNG
# - "Download all 6 (zip)" bulk-renders one carousel
# - "Download all 30 (zip)" bulk-renders the entire pack into folders by carousel id
# - "Reload data.json" re-fetches without page refresh
```

---

## `data.json` schema

```jsonc
{
  "handle": "@waseemnasir2k26",
  "carousels": [
    {
      "id": "c1",
      "tab": "Tab Label",
      "title": "FULL HEADER TITLE",
      "meta": "6 slides · LinkedIn + IG · keyword XYZ",
      "avatar": "_avatars/IMG_XXXX.jpg",
      "slides": [
        {
          "kind": "hero | trick | cta",
          "n": "01",                       // trick only — slide number
          "tag": "SECTION TAG",            // hero / cta only
          "headline": [
            "PLAIN LINE",
            "<accent>RUST LINE</accent>",  // <accent>...</accent> -> rust accent span
            "ANOTHER LINE"
          ],
          "sub": "Subhead body uppercase",
          "label": "Run this command:",    // hero / trick — terminal label
          "term": [                        // hero / trick — terminal lines
            { "k": "prompt", "v": "claude --check" },
            { "k": "arrow",  "v": "running..." },
            { "k": "ok",     "v": "ready" },
            { "k": "bad",    "v": "broken" },
            { "k": "dim",    "v": "(side note)" }
          ],
          "ctas": [                        // cta only — pill stack
            { "k": "01.", "v": "Save this." },
            { "k": "02.", "v": "DM <kw>KEYWORD</kw> to chat." }
          ],
          "bot": "bot-point | bot-laptop | bot-cross"
        }
      ]
    }
  ]
}
```

### Token rules (safe interpolation)

- `<accent>...</accent>` inside `headline` lines -> wraps in `<span class="accent">`
- `<kw>...</kw>` inside CTA `v` -> wraps in keyword highlight
- All other text is HTML-escaped via `escapeHtml` before interpolation
- No raw HTML accepted — tokens are the only allowed markup

---

## RESPONSIVE CONTRACT (v1.2.0)

This template MUST satisfy all of the following — same contract used across the social-stack templates.

1. **Viewport meta** — `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">` is set in `<head>`.
2. **Two-node pattern** —
   - `.card-content` is the **fixed 1080x1350 px** node. It exists in two places:
     - **Inside `.card-frame > .card-scale`** as the on-page preview, transform-scaled by JS.
     - **Inside `#export-host` (offscreen)** as a freshly-built sibling, rendered at exact 1080x1350 for html2canvas capture.
   - `.card-frame` uses `aspect-ratio: 1080/1350; max-width: 100%;` so the preview fills its grid column without distortion.
   - JS computes `transform: scale(frameWidth / 1080)` per resize and per tab switch, applied to `.card-scale`.
3. **Fluid page chrome** — body padding, headline, tab sizes use `clamp()` so layout breathes from 320 -> 1920. Pixel-perfect text *inside* `.card-content` stays at fixed px (104 / 88 / 22 / 18) so html2canvas exports the exact pixel grid every time.
4. **Dedicated 1080x1350 export sibling** — html2canvas captures from a freshly-spawned, off-screen `.card-export > .card-content` node at exact dims with `width: 1080, height: 1350, scale: 1, useCORS: true, backgroundColor: '#F2EBE0'`. Preview scale never affects export output.
5. **Tested breakpoints** — `360 / 480 / 768 / 1024 / 1440`. Grid collapses to 1-col below 768. Bulk bar stacks below 480. Tabs shrink at 768 and 360.
6. **Touch targets >= 44px** — every `.tab`, `.btn`, `.btn-dl` enforces `min-height: 44px` for thumb tap on mobile.
7. **Accessibility** — preview `.card-frame` and `.card-content` both expose `role="img"` + descriptive `aria-label`. Tabs use `role="tab"` + `aria-selected`. Decorative SVG defs and mascots are `aria-hidden="true"`. Native button semantics retained throughout.
8. **Font + image gates** — `await document.fonts.ready` AND avatar `load`/`error`/2.5s timeout BEFORE html2canvas snapshot.
9. **Safe interpolation** — every dynamic string passes `escapeHtml`. Allowed tokens (`<accent>`, `<kw>`) are parsed by the renderer, never injected raw.
10. **JSZip bulk download** — per-carousel `Download all 6` and pack-level `Download all 30` both build a zip via JSZip CDN with a per-card render loop. Files namespaced under `<carousel-id>/` folders in the pack zip.

---

## Quality gates

Before shipping a pack, verify:

- [ ] 5 carousels x 6 slides = 30 cards present in `data.json`
- [ ] Slide 1 of each = `hero`, slides 2-5 = `trick`, slide 6 = `cta`
- [ ] No em-dashes anywhere (find/replace before commit)
- [ ] No invented metrics — every claim traceable to a real client/repo
- [ ] All photos picked via `python _pick-next.py` (rotation log, no repeats)
- [ ] One PNG renders cleanly at 1080x1350 before bulk-zipping
- [ ] Tested at 360 / 480 / 768 / 1024 / 1440 widths
- [ ] Bulk zip downloads all 30 cards namespaced by carousel id

---

## Files

- `index.html` — preview grid, tabs, per-card download, per-carousel zip, full-pack zip
- `data.json` — 5 carousels x 6 slides (edit copy here)
- `_avatars/` — drop photos here, reference path in `data.json`

## Drip schedule

5 carousels x 1 week each. Mon 11:00 EST primary slot, Wed 13:00 secondary repost.
Default keyword routing: `CLAUDE` (c1) / `CITELIFT` (c2) / `N8N` (c3) / `GITHUB` (c4) / Save-only (c5).

## Quality gates (cross-template, no exceptions)

- No em-dashes anywhere in copy
- No fake claims or invented metrics — humanizer rule
- Photos picked via `python _pick-next.py` from PROFESSIONAL/ — log entry required after the pack ships

## Version

- v1.2.0 (refactor) — two-node pattern, JSZip bulk, escapeHtml everywhere, data.json split, viewport contract, a11y labels, font/image gates
- v1.0 (original) — single-file, hardcoded data, scaled-in-place export
