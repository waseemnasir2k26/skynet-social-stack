"""
Generate hook + caption variants for A/B testing a single post.

Usage:
    python caption_variants.py --topic "n8n saas killer" --count 3

Outputs N variants pulling from hook-bank tiers. You pick strongest, A/B-test #2 vs #3.

Note: this is a SCAFFOLD — fills templates, doesn't call an LLM. For LLM-generated
variants, pipe topic into Claude/Anthropic API in your wrapper script.
"""
import argparse, json

HOOK_PATTERNS = [
    # Tier S
    {"tier": "S", "pattern": "Stop {common_practice}.", "example": "Stop optimizing for Google."},
    {"tier": "S", "pattern": "I {action} in {time}. Here's how.", "example": "I shipped 30 posts in 90 minutes today."},
    {"tier": "S", "pattern": "Most {group} {common}. I {opposite}.", "example": "Most agencies sell hours. I sell systems."},
    {"tier": "S", "pattern": "{old} is dead. {new} is next.", "example": "SEO is dead. AEO is next."},
    {"tier": "S", "pattern": "{N} {things}. {twist}.", "example": "5 tricks. Zero plan upgrades. Same Claude Code."},
    # Tier A
    {"tier": "A", "pattern": "Wait — {news}.", "example": "Wait — Anthropic just shipped Claude 4.7 with 1M context."},
    {"tier": "A", "pattern": "{time}. {state}.", "example": "4 AM. Half the work shipped before sunrise."},
    {"tier": "A", "pattern": "You don't need {common_solution}. You need {actual_fix}.", "example": "You don't need a bigger plan. You need to use it smarter."},
    {"tier": "A", "pattern": "Here's {controversial_truth}:", "example": "Here's the thing about agency pricing nobody says out loud:"},
    {"tier": "A", "pattern": "{tool} has {N} modes you've never used.", "example": "Claude Code has 3 modes you've never used."},
    # Tier B
    {"tier": "B", "pattern": "{day_of_week} reminder:", "example": "Monday reminder: every workflow you don't build, you keep paying for."},
    {"tier": "B", "pattern": "What {person} taught me about {topic}:", "example": "What a Pakistani client taught me about pricing in USD."},
    {"tier": "B", "pattern": "I was wrong about {X}.", "example": "I was wrong about Zapier. n8n is the move."},
    {"tier": "B", "pattern": "{counter_intuitive_number}: {shocking_stat}.", "example": "1 quote in ChatGPT > rank #1 on Google."},
]


def generate(topic, count):
    print(f"\nHook variants for topic: \"{topic}\"\n")
    print("-" * 70)
    n = min(count, len(HOOK_PATTERNS))
    variants = []
    for i, p in enumerate(HOOK_PATTERNS[:n], 1):
        print(f"\n{i}. [TIER {p['tier']}]")
        print(f"   PATTERN: {p['pattern']}")
        print(f"   EXAMPLE: {p['example']}")
        print(f"   ADAPT FOR \"{topic}\": [fill in the placeholders]")
        variants.append({
            "n": i,
            "tier": p["tier"],
            "pattern": p["pattern"],
            "example": p["example"],
        })

    print("\n" + "-" * 70)
    print(f"\nWorkflow:")
    print(f"  1. Pick variants 1, 2, 3 (one S, one A, one B).")
    print(f"  2. Adapt placeholders to your topic.")
    print(f"  3. Run all 3 through humanizer checklist.")
    print(f"  4. Ship #1 as primary post.")
    print(f"  5. Test #2 vs #3 in next 2 weeks (same content, different hook).")
    print(f"  6. Track engagement — promote winner to hook-bank Tier S.")
    return variants


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--topic", required=True)
    p.add_argument("--count", type=int, default=5)
    p.add_argument("--json", action="store_true", help="Output JSON only")
    args = p.parse_args()
    variants = generate(args.topic, args.count)
    if args.json:
        print("\n" + json.dumps(variants, indent=2))


if __name__ == "__main__":
    main()
