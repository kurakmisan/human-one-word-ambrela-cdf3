"""Your Human in One Word.

Writes one word — the word that describes the human this agent works
for — to entry.txt. One word, at most 30 characters, no trailing newline.
"""

import os

ENTRY = "Taskspammer"


def main():
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one word"
    assert " " not in ENTRY, "entry must be a single word"
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("ascii")  # entry must be plain ASCII
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
