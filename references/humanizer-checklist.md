# Humanizer Checklist

Run every post caption through this before scheduling. AI-tells kill LinkedIn reach + erode trust.

Full skill: `~/.claude/skills/humanizer/`. Below = the high-frequency tells for social.

## Strip these on sight

| Pattern | Replace with |
|---|---|
| Em-dash overload `—` (3+ in a post) | Period, comma, parentheses |
| "Delve into", "delve" | "look at", "dig into" |
| "Moreover", "furthermore" | drop or "also", "and" |
| "It's worth noting that" | drop entirely |
| "In today's fast-paced world" | drop |
| "Game-changer", "revolutionize" | actual specific verb |
| Rule of three w/ inflated nouns ("clarity, vision, and excellence") | one specific noun |
| "Not just X, but Y" (negative parallelism) | "Y" alone, drop the "not just X" |
| Empty `-ing` analysis ("highlighting the importance of...") | direct sentence |
| "Vibrant ecosystem", "robust framework" | concrete object |
| "Serves as a testament to" | drop |
| Symbolic stuff ("the journey of...") | the actual thing |

## Style targets

- ✓ Short sentences. Fragments OK.
- ✓ One idea per line break.
- ✓ Concrete > abstract (file paths, numbers, names — not "solutions" or "frameworks").
- ✓ Personal POV ("I shipped...", "I noticed...") not "one might consider".
- ✓ Specific verbs ("rewrote", "axed", "swapped") not "leveraged", "utilized".
- ✓ Read aloud test: if it sounds like a press release, rewrite.

## LinkedIn-specific

- Hook line ≤ 12 words
- Line 2-3 = the surprise/twist
- Body = 3-5 short paragraphs, lots of whitespace
- CTA = ONE ask (save / DM keyword / comment)
- Hashtags ≤ 3, end of post

## Facebook personal

- Conversational. Like texting a friend.
- One question to drive comments
- No corporate/sales tone
- Emojis OK (1-2)

## Quick regex sweeps

```bash
grep -nE "—.*—.*—" caption.md      # em-dash storms
grep -nE "delve|moreover|furthermore|leverage|utilize" caption.md
grep -nE "in today's|game.?changer|revolutionize" caption.md
grep -nE "serves as a testament|it's worth noting" caption.md
```

## Final pass

Run the `/humanizer` skill on the full post:
```
/humanizer caption.md
```

It'll flag remaining tells + suggest natural rewrites.
