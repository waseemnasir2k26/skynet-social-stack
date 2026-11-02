# skynet-social-stack

A Claude Code skill and template set for building a full social post pack from one topic: HTML templates that export to PNG, caption variants for each platform, and a six-column GoHighLevel scheduling CSV.

- **Templates** in `templates/`: cream-and-rust carousel (1080x1350), editorial dark LinkedIn card, Facebook 9-card news mix, X image pack (1200x675), Pinterest pin (1000x1500). Each has an `index.html` and a `data.json` you edit.
- **Recipes** in `recipes/`: carousel launch, LinkedIn card batch, 3-day Facebook drip, X pack, Pin batch, cross-platform pack, video drip, repurpose chain, migrating an old CSV.
- **References** in `references/`: post-type decision tree, GHL CSV format, image rotation rule, no-fake-claims checklist, humanizer checklist, brand split, ManyChat keyword flow, hook bank.
- **Scripts** in `scripts/`: `build_ghl_csv.py`, `shift_dates.py`, `caption_variants.py`, `utm_inject.py`, `seed_replies.py`, `pick_avatar.py`, `lint_skill.py`.
- **Examples**: a 10-format showcase, a carousel pack and a shipped launch pack (`packs/fable51-launch-2026-09-02/`).

## Quickstart

```bash
git clone https://github.com/waseemnasir2k26/skynet-social-stack.git ~/.claude/skills/social-stack
```

In Claude Code, ask for a pack, for example:

```
/social-stack build a 5-carousel pack on Claude Code, n8n and AEO, weekday cadence
```

The skill reads `SKILL.md`, forks the matching template, renders the HTML for PNG export and builds the CSVs with `scripts/build_ghl_csv.py`. You can also use the templates alone: open a template's `index.html`, edit `data.json`, and use the in-page PNG download.

## The rules it enforces

1. No fake claims: only real builds and results (`references/no-fake-claims.md`).
2. Rotate images with the picker script, not by eye.
3. Strip AI tells and em-dashes before anything ships.
4. Keep personal voice and company voice separate.
5. Use the canonical six-column GHL CSV, no invented headers.

## For you if

You make carousels and platform cards on a schedule, use GoHighLevel for scheduling, and want the layout, copy checks and CSV handled the same way every time.

## Status and limits

- Written for Claude Code. The scripts run on their own, but the flow in `SKILL.md` assumes Claude drives it.
- The CSV format targets GoHighLevel's bulk scheduler. For other schedulers you would adapt `build_ghl_csv.py`.
- `pick_avatar.py` expects a local folder of portrait images you supply.
- Templates carry the SkynetLabs look. Change fonts, colours and handles in `data.json` and the template CSS.

## License

MIT, see [LICENSE](LICENSE).

---

Built by SkynetLabs. Contact: waseem@skynetjoe.com

Need this wired into your business? SkynetLabs builds voice agents, n8n back offices and sites that convert → https://skynetjoe.com
