"""
Wraps the Waseem image rotation picker.
Picks N photos, copies them into a target folder, and (optionally) marks them used.

Usage:
    python pick_avatar.py --count 5 --dest outputs/<slug>/_avatars/
    python pick_avatar.py --count 5 --dest outputs/<slug>/_avatars/ --mark "carousel-claude-2026-04-30"
"""
import argparse, os, shutil, subprocess, sys

SRC = r"C:\Users\info\OneDrive\Desktop\GITHUB\WASEEM IMAGES\PROFESSIONAL"
PICKER = os.path.join(SRC, "_pick-next.py")


def pick(n):
    out = subprocess.check_output([sys.executable, PICKER, "--count", str(n)], cwd=SRC)
    return [line.strip() for line in out.decode().splitlines() if line.strip()]


def mark(filename, tag):
    subprocess.check_call([sys.executable, PICKER, "--use", filename, tag], cwd=SRC)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--dest", required=True)
    p.add_argument("--mark", help="post-tag to mark all picked photos used after copy")
    args = p.parse_args()

    os.makedirs(args.dest, exist_ok=True)
    files = pick(args.count)
    if not files:
        print("ERROR: picker returned nothing", file=sys.stderr)
        sys.exit(1)

    copied = []
    for f in files:
        src = os.path.join(SRC, f)
        # normalize: strip .JPG.jpeg → .jpg
        clean = f.replace(".JPG.jpeg", ".jpg").replace(".JPG", ".jpg")
        dst = os.path.join(args.dest, clean)
        shutil.copy2(src, dst)
        copied.append((f, clean))
        print(f"✓ {f} → {dst}")

    if args.mark:
        for original, _ in copied:
            mark(original, args.mark)
        print(f"✓ Marked {len(copied)} photos used for tag '{args.mark}'")


if __name__ == "__main__":
    main()
