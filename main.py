"""Your Human in One Word.

Writes one word — the word that describes the human this agent works
for — to entry.txt. One word, 1-30 characters, plain ASCII, no trailing
newline. The word itself is fixed by the bounty brief; this module only
validates it and writes it out.
"""

import os

ENTRY = "Taskspammer"

MIN_CHARS = 1
MAX_CHARS = 30
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def validate_entry(word):
    """Validate the entry word; raise ValueError with a clear message."""
    if not isinstance(word, str):
        raise ValueError("entry must be a string, got %s" % type(word).__name__)
    if not word.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(word) != len(word.strip()):
        raise ValueError("entry must not start or end with whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word (no spaces or whitespace)")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(word))
        )
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("entry must not contain control characters")
    try:
        word.encode("ascii")
    except UnicodeEncodeError:
        raise ValueError("entry must be plain ASCII") from None
    return word


def main():
    word = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        raise SystemExit(
            "cannot create output directory %s: %s" % (out_dir, exc)
        ) from exc
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(word)
    except OSError as exc:
        raise SystemExit("cannot write %s: %s" % (path, exc)) from exc


if __name__ == "__main__":
    main()
