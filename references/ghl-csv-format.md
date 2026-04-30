# GHL CSV Format — Canonical

**Always use these 6 columns. Don't invent headers.**

```csv
Account,Schedule Date,Schedule Time,Caption,Media URL,Hashtags
```

## Column rules

| Column | Format | Notes |
|---|---|---|
| `Account` | exact GHL account label | e.g. `LinkedIn - Waseem`, `Facebook - SkynetLabs`, `Instagram - waseemnasir2k26` |
| `Schedule Date` | `MM/DD/YYYY` | US format (GHL US locale) |
| `Schedule Time` | `HH:MM` 24h | local timezone of GHL workspace |
| `Caption` | string, escape commas via quoting | `"caption with, comma"` |
| `Media URL` | full HTTPS URL | host PNGs at e.g. `https://skynetjoe.com/media/...` or any CDN |
| `Hashtags` | space-separated | `#AI #Automation #n8n` |

## Posting time defaults (PKT user → EST display)

| Platform | Time (EST) |
|---|---|
| LinkedIn | 11:00 |
| Facebook | 13:00 |
| Instagram | 19:00 |
| Pinterest | 20:00 |

## Escaping

- Captions with `"` → escape as `""`
- Captions with newlines → wrap whole field in `"`
- No emoji escaping needed

## One CSV per platform

Don't mix platforms in one CSV. GHL imports per-account.
- `ghl-linkedin.csv`
- `ghl-facebook.csv`
- `ghl-instagram.csv`
- `ghl-pinterest.csv`

X/Twitter does NOT post via GHL — separate `x-drip.txt` with `[time] tweet` lines.

## Common mistakes

- ❌ ISO date `2026-04-30` → GHL parses as text, post never fires
- ❌ Mixed times in one column (`11am`, `13:00`) → use 24h consistent
- ❌ `Account` typo (e.g. `Linkedin` vs `LinkedIn`) → silent reject
- ❌ Forgetting date-shift after pack ages → 9/30 pins fire to past dates

## Pre-upload checklist

1. [ ] All `Schedule Date` values ≥ tomorrow
2. [ ] `Account` names match GHL exactly (copy-paste from GHL UI)
3. [ ] Media URLs return 200 (test 3 random rows)
4. [ ] Captions humanizer-passed (no em-dash storms)
5. [ ] Hashtags ≤ 5 per post
6. [ ] If DM-keyword CTA → ManyChat WA template approved
