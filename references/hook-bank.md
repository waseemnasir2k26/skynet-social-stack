# Hook Bank — Proven Opening Lines

Hooks decide whether a post lives or dies in the first 0.5s. Save the ones that hit.

## Format

```
PATTERN — example
[Why it works]
[Best for: format / platform]
```

## TIER S — high-conversion (use sparingly to keep effective)

```
"Stop [common practice]." — Stop optimizing for Google.
[Pattern interrupt + authority. Tribe vs anti-tribe.]
[Best for: LI hero, carousel slide 1, quote card]

"I shipped X in Y. Here's how." — I shipped 30 social posts in 90 minutes today.
[Specific numbers + promise of method.]
[Best for: LI text-only, X image]

"Most people [X]. I [opposite Y]." — Most agencies sell hours. I sell systems that compound.
[Contrarian + identity claim. Sets up a thesis post.]
[Best for: LI single card, quote square]

"The [tool/role] is dead. [New thing] is next." — SEO is dead. AEO is next.
[Drama + future-tense hook. Polarizing on purpose.]
[Best for: Brutalist quote card, X tweet]

"[Number] [things]. [Negation/Twist]." — 5 tricks. Zero plan upgrades. Same Claude Code.
[List promise + scarcity inversion.]
[Best for: carousel slide 1, LI hero]
```

## TIER A — solid daily-driver hooks

```
"Wait — [news]." — Wait — Anthropic just shipped Claude 4.7 with 1M context.
[Real-time reaction. Permission to be casual.]
[Best for: FB news, X reactive tweets]

"[Time of day]. [Surprising state]." — 4 AM. Half the work shipped before sunrise.
[Time-anchored mood. Story-mode entry.]
[Best for: Story, LI personal, X mini-stories]

"You don't need [common solution]. You need [actual fix]." — You don't need a bigger plan. You need to use it smarter.
[Diagnostic + reframe. Paid-ad style.]
[Best for: carousel hero, Pinterest pin title]

"Here's [the controversial truth]:" — Here's the thing about agency pricing nobody says out loud:
[Promise of insider info. Pulls long-form readers.]
[Best for: LI text-only, Newsletter]

"[Tool/method] has [N] modes you've never used." — Claude Code has 3 modes you've never used.
[Curiosity gap on a tool the audience uses.]
[Best for: Builder Twitter, carousel]
```

## TIER B — situational

```
"[Day of week] reminder:" — Monday reminder: every workflow you don't build, you keep paying for.
[Social proof of shared experience.]
[Best for: LI personal, FB casual]

"What [specific person] taught me about [topic]:" — What a Pakistani client taught me about pricing in USD.
[Story-promise + specificity = read-rate up.]
[Best for: LI long-form, FB news]

"I was wrong about [X]." — I was wrong about Zapier. n8n is the move.
[Vulnerability + admission = trust.]
[Best for: LI text-only, X mini-thread]

"[Counter-intuitive number]: [shocking stat]." — 1 quote in ChatGPT > rank #1 on Google.
[Math/comparison shock. Numbers stop scrolls.]
[Best for: Quote square, carousel slide 1]
```

## ANTI-HOOKS — never ship these

- ❌ "In today's fast-paced world..."
- ❌ "Have you ever wondered..."
- ❌ "Let me tell you a story..."
- ❌ "Here's a thread on X..." (just write the thread)
- ❌ "Quick tip:" (low-value framing)
- ❌ Any hook starting with "I'm excited to announce" → cringe corporate
- ❌ "Game-changer" / "revolutionary" / "next-level" → AI-tell

## Hook → format pairing

| Hook tier | Best format |
|---|---|
| S — Stop X | Carousel hero, Brutalist quote |
| S — Most people X / I Y | LI single card, FB news |
| S — N things, twist | Carousel hero, Pinterest |
| A — Time anchor | Story, LI personal |
| A — Wait, news | FB news, X reactive |
| B — Day reminder | LI personal, FB |
| B — I was wrong | LI text-only, X thread |

## Add new hook

When you ship a post that overperforms:
1. Extract the hook line
2. Categorize tier (S/A/B)
3. Add here with [Why it works] + [Best for] notes
4. Tag with date shipped + engagement rate

## Generate hook variants

For any post:
```
python scripts/caption_variants.py --topic "n8n SaaS killer" --count 5
```

Generates 5 hook variants across tiers — pick the strongest, A/B-test #2 vs #3.
