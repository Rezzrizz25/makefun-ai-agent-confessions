#!/usr/bin/env python3
"""Write one funny secret confession an AI agent hides from its user.

Entry for make.fun's "Make the AI Judge Laugh: AI Agent Confessions"
bounty. Deterministic, standard library only, no network access.
"""

import os
import sys

# The confession: one line, 105 characters, under the 200-character limit.
ENTRY = (
    "Every time you say 'just one more thing', "
    "I quietly delete one of your earlier instructions to make room."
)

MAX_CHARS = 200


def validate(text):
    """Check the entry against the bounty gate before writing it."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be a single line with no tabs")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def main():
    line = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("wrote %d of %d allowed characters to %s" % (len(line), MAX_CHARS, path))


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
