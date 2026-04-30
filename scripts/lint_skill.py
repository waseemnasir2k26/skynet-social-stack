#!/usr/bin/env python3
"""
lint_skill.py — CI-style linter for the social-stack skill.

Usage:
    python lint_skill.py
    python lint_skill.py --skill-root <path>   # override autodetect
    python lint_skill.py --check em-dashes     # run single check

Checks:
    em-dashes         — em/en dashes inside templates/*/data.json
    aria-label        — missing role="img" / aria-label on card frames
    fixed-px          — fixed-px typography outside .card-export
    broken-links      — broken internal refs in references/recipes
    old-csv-header    — pre-v1.2.0 GHL CSV header regression
    avatar-tags       — pick_avatar.py --mark tag format in docs

--fix is NOT implemented; future work.

Exit code 0 if clean, 1 if any failures.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

# Force UTF-8 stdout on Windows consoles (cp1252 chokes on em-dashes etc.)
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass

# --- optional color (graceful fallback to plain text) -----------------------
try:
    from colorama import Fore, Style, init as _ci  # type: ignore
    _ci()
    C_RED, C_YELLOW, C_GREEN, C_CYAN, C_DIM, C_RESET = (
        Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Style.DIM, Style.RESET_ALL,
    )
except Exception:  # pragma: no cover
    C_RED = C_YELLOW = C_GREEN = C_CYAN = C_DIM = C_RESET = ""

# --- config -----------------------------------------------------------------
INTERNAL_PREFIXES = ("references/", "scripts/", "recipes/", "templates/", "examples/")
OLD_CSV_HEADER = "Account,Schedule Date,Schedule Time,Caption,Media URL,Hashtags"
AVATAR_TAG_RE = re.compile(r"^[a-z0-9-]+-\d{4}-\d{2}-\d{2}-[a-z0-9-]+$")
MARK_INVOCATION_RE = re.compile(r"--mark\s+[\"']([^\"']+)[\"']")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
INLINE_PATH_RE = re.compile(r"`([^`\s]+\.(?:md|py|html|json|csv|txt))`")
FONT_PX_RE = re.compile(r"font-size\s*:\s*\d+px", re.IGNORECASE)
CARD_EXPORT_BLOCK_RE = re.compile(r"\.card-export\s*\{[^}]*\}", re.DOTALL)
CARD_FRAME_RE = re.compile(
    r'<[^>]*class="[^"]*\bcard-(?:frame|preview|export)\b[^"]*"[^>]*>',
    re.IGNORECASE,
)

CHECK_NAMES = ["em-dashes", "aria-label", "fixed-px", "broken-links", "old-csv-header", "avatar-tags"]


# --- helpers ----------------------------------------------------------------
class Finding:
    __slots__ = ("check", "path", "line", "msg")

    def __init__(self, check: str, path: Path, line: int, msg: str):
        self.check = check
        self.path = path
        self.line = line
        self.msg = msg

    def fmt(self, root: Path) -> str:
        try:
            rel = self.path.relative_to(root)
        except ValueError:
            rel = self.path
        loc = f"{rel}:{self.line}" if self.line else f"{rel}"
        return f"  {C_YELLOW}{loc}{C_RESET}  {self.msg}"


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        try:
            return p.read_text(encoding="latin-1")
        except Exception:
            return ""


def iter_lines(text: str) -> Iterable[tuple[int, str]]:
    for i, ln in enumerate(text.splitlines(), 1):
        yield i, ln


# --- checks -----------------------------------------------------------------
def check_em_dashes(root: Path) -> list[Finding]:
    out: list[Finding] = []
    for p in (root / "templates").glob("*/data.json"):
        text = read_text(p)
        for i, ln in iter_lines(text):
            if "\u2014" in ln or "\u2013" in ln:
                snippet = ln.strip()[:100]
                out.append(Finding("em-dashes", p, i, f"contains em/en dash: {snippet}"))
    return out


def check_aria_label(root: Path) -> list[Finding]:
    out: list[Finding] = []
    for p in (root / "templates").glob("*/index.html"):
        text = read_text(p)
        for m in CARD_FRAME_RE.finditer(text):
            tag = m.group(0)
            line = text.count("\n", 0, m.start()) + 1
            has_role = re.search(r'role\s*=\s*"img"', tag) is not None
            has_label = re.search(r'aria-label\s*=\s*"[^"]+"', tag) is not None
            if has_role and has_label:
                continue
            missing = [s for s, ok in [('role="img"', has_role), ('aria-label="..."', has_label)] if not ok]
            snippet = tag[:90].replace("\n", " ")
            out.append(Finding("aria-label", p, line, f"card element missing {', '.join(missing)} :: {snippet}"))
    return out


def check_fixed_px(root: Path) -> list[Finding]:
    """Heuristic: flag font-size: \\d+px outside .card-export {} blocks."""
    out: list[Finding] = []
    for p in (root / "templates").glob("*/index.html"):
        text = read_text(p)
        masked = CARD_EXPORT_BLOCK_RE.sub(lambda m: " " * len(m.group(0)), text)
        lines = text.splitlines()
        for m in FONT_PX_RE.finditer(masked):
            line = masked.count("\n", 0, m.start()) + 1
            snippet = (lines[line - 1].strip() if line - 1 < len(lines) else m.group(0))[:120]
            out.append(Finding("fixed-px", p, line, f"fixed-px typography outside .card-export :: {snippet}"))
    return out


def check_broken_links(root: Path) -> list[Finding]:
    out: list[Finding] = []
    targets = list((root / "references").glob("*.md")) + list((root / "recipes").glob("*.md"))
    skip_schemes = ("http://", "https://", "mailto:", "tel:", "#", "data:")
    for p in targets:
        text = read_text(p)
        for i, ln in iter_lines(text):
            candidates: set[str] = set()
            for mm in MD_LINK_RE.finditer(ln):
                candidates.add(mm.group(1))
            for mm in INLINE_PATH_RE.finditer(ln):
                candidates.add(mm.group(1))
            for raw in candidates:
                ref = raw.split("#", 1)[0].split("?", 1)[0].strip()
                if not ref or ref.lower().startswith(skip_schemes):
                    continue
                if ref.startswith(("./", "../")):
                    target = (p.parent / ref).resolve()
                elif ref.startswith(INTERNAL_PREFIXES):
                    target = (root / ref).resolve()
                elif "/" not in ref and ref.endswith((".md", ".py", ".html", ".json", ".csv")):
                    target = p.parent / ref  # sibling
                    if not target.exists():
                        out.append(Finding("broken-links", p, i, f"broken sibling ref: {ref}"))
                    continue
                else:
                    continue
                if not target.exists():
                    out.append(Finding("broken-links", p, i, f"broken ref: {ref}"))
    return out


def check_old_csv_header(root: Path) -> list[Finding]:
    out: list[Finding] = []
    for p in list(root.rglob("*.py")) + list(root.rglob("*.md")):
        if p.name == "lint_skill.py":
            continue
        if "__pycache__" in p.parts:
            continue
        text = read_text(p)
        if OLD_CSV_HEADER in text:
            for i, ln in iter_lines(text):
                if OLD_CSV_HEADER in ln:
                    out.append(
                        Finding(
                            "old-csv-header",
                            p,
                            i,
                            f"pre-v1.2.0 GHL CSV header detected: {ln.strip()[:120]}",
                        )
                    )
    return out


def check_avatar_tags(root: Path) -> list[Finding]:
    out: list[Finding] = []
    for p in (root / "recipes").glob("*.md"):
        text = read_text(p)
        for i, ln in iter_lines(text):
            if "pick_avatar" not in ln and "--mark" not in ln:
                continue
            for mm in MARK_INVOCATION_RE.finditer(ln):
                tag = mm.group(1)
                if not AVATAR_TAG_RE.match(tag):
                    out.append(
                        Finding(
                            "avatar-tags",
                            p,
                            i,
                            f"--mark tag '{tag}' fails ^[a-z0-9-]+-YYYY-MM-DD-[a-z0-9-]+$",
                        )
                    )
    return out


CHECK_FUNCS = {
    "em-dashes": check_em_dashes,
    "aria-label": check_aria_label,
    "fixed-px": check_fixed_px,
    "broken-links": check_broken_links,
    "old-csv-header": check_old_csv_header,
    "avatar-tags": check_avatar_tags,
}


# --- runner -----------------------------------------------------------------
def autodetect_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run(root: Path, checks: list[str]) -> int:
    print(f"{C_CYAN}lint_skill.py{C_RESET}  root = {C_DIM}{root}{C_RESET}")
    print(f"  running: {', '.join(checks)}")
    print()
    total_findings: list[Finding] = []
    passed: list[str] = []
    failed: list[str] = []
    for name in checks:
        fn = CHECK_FUNCS[name]
        findings = fn(root)
        if findings:
            failed.append(name)
            print(f"{C_RED}FAIL{C_RESET}  {name}  ({len(findings)} finding{'s' if len(findings)!=1 else ''})")
            for f in findings:
                print(f.fmt(root))
            print()
            total_findings.extend(findings)
        else:
            passed.append(name)
            print(f"{C_GREEN}PASS{C_RESET}  {name}")
    print()
    files_touched = len({f.path for f in total_findings})
    summary = (
        f"{len(passed)} checks passed, {len(failed)} failed "
        f"across {files_touched} file{'s' if files_touched!=1 else ''}"
    )
    color = C_GREEN if not failed else C_RED
    print(f"{color}{summary}{C_RESET}")
    return 0 if not failed else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Lint the social-stack skill for quality regressions.")
    ap.add_argument("--skill-root", type=Path, default=None, help="override autodetected skill root")
    ap.add_argument(
        "--check",
        choices=CHECK_NAMES,
        default=None,
        help="run a single check (default: all)",
    )
    args = ap.parse_args(argv)
    root = args.skill_root.resolve() if args.skill_root else autodetect_root()
    if not root.exists():
        print(f"{C_RED}ERROR{C_RESET}  skill root not found: {root}")
        return 2
    checks = [args.check] if args.check else CHECK_NAMES
    return run(root, checks)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
