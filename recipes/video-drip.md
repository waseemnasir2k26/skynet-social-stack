# Video Drip — roadmap stub

## Status: roadmap

This recipe is **not yet built**. It's a placeholder so cross-references in `../references/post-type-decision-tree.md` and `../references/responsive-output-contract.md` resolve.

## Scope (planned)

Drip a batch of existing MP4 files (e.g. CapCut renders, screen-recordings, AI-generated VEO3 clips) across LI / FB / IG Reels / X / YouTube Shorts via GHL Bulk Upload — same canonical 6-col CSV format as image packs, but `videoUrls` populated instead of `imageUrls`.

## Inputs (planned)

- Folder of MP4s (already cut, captioned, aspect-ratio-correct per platform)
- Per-clip caption JSON (hook + body + CTA + hashtags + DM keyword)
- Drip schedule (start date, cadence, time slots)

## Outputs (planned)

- 1× GHL CSV per platform (LI / FB / IG / X / YT)
- Captions humanizer-passed
- ManyChat keyword wiring (if DM-CTA)

## Cross-links

- `../references/ghl-csv-format.md` — canonical 6-col spec (already supports `videoUrls`)
- `../references/post-type-decision-tree.md` — picks this recipe for "video drip" intent
- Existing memory: `~/.claude/projects/C--Users-info/memory/video-pending.md` (16 ship / 54 fix / 32 kill triage from 2026-04-27)

## Build trigger

Promote from stub → real recipe when the next video batch (working-laptop-timelapse, opus-4-7-video, keep-climbing-reel-v2) hits the GHL upload step.
