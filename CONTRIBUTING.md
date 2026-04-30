# Contributing to skynet-social-stack

Adding a new template / recipe / improvement? Welcome.

## Add a new template

1. Drop `templates/<your-template-name>/index.html`
2. Self-contained HTML — embedded CSS, html2canvas via CDN, PNG download per card
3. Document inputs at top of file (data structure for parameterizing)
4. Update `references/post-type-decision-tree.md` with new row
5. PR with screenshot of rendered card

## Add a new recipe

1. Drop `recipes/<recipe-name>.md`
2. Use existing recipes as shape: Inputs → Steps → Pre-flight → Failure modes
3. Reference templates + scripts you use
4. PR

## Improve a script

1. Keep CLI consistent (argparse, descriptive flags)
2. No external deps unless justified — stdlib first
3. Add usage example in docstring
4. PR

## Improve references

References = rules. Keep tight. New rule needs evidence (a real shipped failure or repeated pattern).

## Style

- Markdown: GitHub-flavored
- Python: PEP-8, no Black needed (keep diffs small)
- HTML/CSS: vanilla, no framework

## Issue templates

- 🐛 Bug — template renders wrong, CSV reject, etc.
- 💡 Pattern — share a shipped pattern that should become a recipe
- 📦 Template — propose a new format

## License

By contributing, you agree your contributions land under the MIT license.
