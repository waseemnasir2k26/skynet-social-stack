"""
Generate first-30-min engagement-seed comments per post.

LinkedIn / IG algo: first 30 min decides reach. You post → you self-comment 3-5 seeds
→ replies prime the conversation → algo sees engagement → distributes wider.

Usage:
    python seed_replies.py --post-topic "claude code limits" --count 5

Outputs 5 reply seeds varying in style (question / agreement / counterpoint / story / link).

You post these as your own comments 2-5 minutes after the main post lands.
"""
import argparse, json, sys

# Templates by intent
TEMPLATES = [
    # Question seeds — invite responses
    ("question", "Anyone else hitting this? I had to {pain} last week before I figured it out."),
    ("question", "Curious — which of these is biting you most? {topic} feels especially common."),
    # Story seeds — add a personal anchor
    ("story", "First time this hit me was on a {context}. Cost me {cost}. Now I {fix} reflexively."),
    # Counterpoint seeds — controversy = engagement
    ("counter", "Some will disagree with #2 but the data is wild — {claim}."),
    # Tactical seeds — extra value in comments
    ("tactical", "Bonus: if you {action}, the result compounds. I run this every {cadence}."),
    # Resource seeds — drive to deeper content
    ("resource", "Wrote a longer breakdown on this if useful — DM `{keyword}` for the doc."),
    # Self-tag seeds — mention adjacent peers
    ("tag", "@friend1 @friend2 — this fits the convo we had last week."),
    # Reframe seeds — flip the headline
    ("reframe", "Reading this back, the real lesson is: {meta_lesson}."),
]


def generate(topic, count):
    print(f"Engagement-seed comments for: {topic}\n")
    print(f"Post these as YOUR OWN comments 2-5 min after main post.")
    print(f"Spaced 1-2 min apart. Algo reads as conversation.\n")
    print("-" * 60)

    n = min(count, len(TEMPLATES))
    for i, (intent, tpl) in enumerate(TEMPLATES[:n], 1):
        print(f"\n{i}. [{intent.upper()}]")
        print(f"   {tpl}")
        print(f"   ---")
        print(f"   FILL IN: tweak placeholders for the actual post topic.")

    print("\n" + "-" * 60)
    print(f"\nWorkflow:")
    print(f"  1. Post main content at scheduled time.")
    print(f"  2. Wait 2-3 min.")
    print(f"  3. Drop seed #1 (question or story).")
    print(f"  4. Wait 1-2 min.")
    print(f"  5. Drop seed #2.")
    print(f"  6. Continue every 2 min for first 30 min.")
    print(f"  7. Reply to any incoming comments within 5 min.")
    print(f"\nOutput JSON:")

    output = [
        {"order": i, "intent": intent, "template": tpl}
        for i, (intent, tpl) in enumerate(TEMPLATES[:n], 1)
    ]
    print(json.dumps(output, indent=2))
    return output


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--post-topic", required=True, help="Topic of the main post")
    p.add_argument("--count", type=int, default=5, help="How many seeds (max 8)")
    args = p.parse_args()
    generate(args.post_topic, args.count)


if __name__ == "__main__":
    main()
