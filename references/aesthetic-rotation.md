# Aesthetic Rotation — Variety Mandate

**Don't ship 5 carousels in the same template. Algorithm penalizes pattern.**

Same look = scroll-past. Variety = stop-scroll.

## The 3-aesthetic rotation (default)

| Week | Aesthetic | When | Mood |
|---|---|---|---|
| 1 | **Cream + Rust Circuit** (carousel-cream-rust) | Tactical / builder content | Editorial, warm, retro-tech |
| 2 | **Dark + Gold Editorial** (li-card-editorial-dark) | Founder / luxury / quote posts | Legacy, premium, serious |
| 3 | **Brutalist Memphis** (quote-card-square) | Hot-take / contrarian / shock | Bold, geometric, scroll-stopping |

Repeat 1→2→3 every 3 weeks. Each post type rotates aesthetic.

## Extended rotation (10-format pack)

For full 10-format coverage, every aesthetic gets a slot:

| Format | Aesthetic | Audience |
|---|---|---|
| Carousel | Cream + Rust Circuit | Builders, tactical |
| LI single | Dark + Gold Editorial | Founders, premium clients |
| FB news | Tabloid / Breaking-News | Friends, news watchers |
| X image | Terminal / Hacker | Dev Twitter |
| Pinterest | Magazine / Editorial | Lifestyle, search-led |
| Quote square | Brutalist / Memphis | IG feed, save-bait |
| Reel script | Cinematic Storyboard | Internal / creator brief |
| Story | Sunset Gradient Gen-Z | Casual, ephemeral |
| LI text-only | Native LinkedIn (no img) | Long-form storytelling |
| Newsletter | Swiss Minimal | Email, brand cover |

## Rules

1. **Never ship 2 carousels back-to-back in same aesthetic.** Min 1-aesthetic gap.
2. **Match aesthetic to message.** Hot-take → Brutalist. Founder essay → Dark+Gold. Tactical → Cream+Rust.
3. **Don't mix aesthetics in one carousel.** All slides same template. Variety happens between posts, not within.
4. **Track which aesthetic converts.** Add to post-mortem: did dark+gold get more saves than cream+rust this month?

## Why this matters

- IG feed grid: 3 same-look posts in a row = profile looks templated → unfollow risk
- LI feed: same image style = "ad blindness" → impressions drop
- Pinterest: same look across pins = boards look like spam
- Audience expects variety = trust your own creative range

## Extending the rotation

When adding a new aesthetic:
1. Build template (working HTML in `templates/<name>/`)
2. Add to this rotation table
3. Test on 5 posts before adopting
4. If save-rate ≥ baseline → keep. If lower → kill.

Past graveyard:
- All-emoji posts (algo penalty 2024)
- Stock-image-overlay (looks like 2018)
- Single-color flat (no contrast)
