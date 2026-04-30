"""
Wraps the Waseem image rotation picker.
Picks N photos from rotation log, validates against PROFESSIONAL/, copies them, marks used.

Rotation log = source of truth. NEVER random-pick. NEVER skip mark step.

Usage:
    python pick_avatar.py --count 5 --dest outputs/<slug>/_avatars/ \
        --mark "carousel-2026-04-30-claude-pack"

Tag format (per feedback-image-rotation rule):
    "<platform-or-format>-<yyyy-mm-dd>-<slug>"
"""
import argparse, os, re, shutil, subprocess, sys

SRC = r"C:\Users\info\OneDrive\Desktop\GITHUB\WASEEM IMAGES\PROFESSIONAL"
PICKER = os.path.join(SRC, "_pick-next.py")
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")


def assert_picker_exists():
    if not os.path.isdir(SRC):
        sys.exit(f"ERROR: PROFESSIONAL folder missing: {SRC}")
    if not os.path.isfile(PICKER):
        sys.exit(f"ERROR: rotation picker missing: {PICKER}")


def pick(n):
    out = subprocess.check_output(
        [sys.executable, PICKER, "--count", str(n)], cwd=SRC
    )
    files = [line.strip() for line in out.decode("utf-8", errors="replace").splitlines() if line.strip()]
    if not files:
        sys.exit("ERROR: picker returned nothing. Check rotation log + PROFESSIONAL folder.")
    if len(files) < n:
        sys.exit(f"ERROR: picker returned {len(files)} of {n} requested. Rotation pool may be exhausted.")
    return files


def validate_files_exist(files):
    missing = [f for f in files if not os.path.isfile(os.path.join(SRC, f))]
    if missing:
        sys.exit(f"ERROR: picker returned files not in PROFESSIONAL/: {missing}")


def mark(filename, tag):
    subprocess.check_call(
        [sys.executable, PICKER, "--use", filename, tag], cwd=SRC
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--dest", required=True)
    p.add_argument("--mark", help='post-tag e.g. "li-2026-05-05-claude-pack". Strongly recommended.')
    p.add_argument("--no-mark", action="store_true", help="explicit opt-out of marking (smoke tests only)")
    args = p.parse_args()

    if not args.mark and not args.no_mark:
        sys.exit("ERROR: pass --mark <tag> OR --no-mark explicitly. Silent skip violates rotation rule.")
    if args.mark and not TAG_RE.match(args.mark):
        sys.exit(f"ERROR: --mark must be lowercase-kebab with date, got '{args.mark}'. Format: <fmt>-<yyyy-mm-dd>-<slug>")

    assert_picker_exists()
    os.makedirs(args.dest, exist_ok=True)

    files = pick(args.count)
    validate_files_exist(files)

    copied = []
    for f in files:
        src = os.path.join(SRC, f)
        clean = f.replace(".JPG.jpeg", ".jpg").replace(".JPG", ".jpg").replace(".JPEG", ".jpg")
        dst = os.path.join(args.dest, clean)
        shutil.copy2(src, dst)
        copied.append((f, clean))
        print(f"OK {f} -> {dst}")

    if args.mark:
        for original, _ in copied:
            mark(original, args.mark)
        print(f"OK marked {len(copied)} photos used for tag '{args.mark}'")
    else:
        print("WARNING --no-mark: photos NOT marked. Re-pick risk on next run.")


if __name__ == "__main__":
    main()
