"""The 3AM Fridge Text — make.fun entry.

The joke: at 3am the fridge texts its owner about the last egg in the
carton, a lone egg named Kevin, who has asked the fridge to pass on a
message — he's not mad, just disappointed. In you. The punchline lands
because a fridge delivering a disappointed-parent speech on behalf of
an egg is absurd, specific, and aimed straight at the owner; it reads
exactly like a machine that has decided 3am is the moment to speak.

Writes the single winning line (136 chars, one line) to
$OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
import sys

LINE = (
    "3am. Fridge here. The egg carton is down to one egg. His name is "
    "Kevin. He asked me to tell you he's not mad, just disappointed. "
    "In you."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if not text:
        print("error: entry text is empty", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry has leading/trailing whitespace",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 140:
        print(f"error: entry is {len(text)} chars, over the 140 cap",
              file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and confirm the file holds exactly the winning line.
    with open(path, encoding="utf-8") as f:
        if f.read().strip() != text:
            print("error: written entry does not match", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
