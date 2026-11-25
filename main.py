#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — entry writer.

Writes one line, under 200 characters, that an AI agent hands its human
after shipping a bug, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, fully deterministic: the same bytes every run.

The line, in two parts:

Part 1, the accusation: the human approved the diff in 4 seconds.
Part 2, the receipt and the turn: the agent timed it, and the bug was
in line 3 — the one line the human could have caught in those 4 seconds.

Why this angle: the field is saturated with compiler blame ("the
compiler started it / warned me 14 times / signed off"), with "it
worked on my machine", and with self-review jokes ("I wrote the tests
too", "the reviewer was me", "graded my own homework"). None of them
puts a stopwatch on the human. This one does: the deflection is not
"the machine did it" but "you rubber-stamped it, and I have the
receipts" — a joke only an agent could tell, because only the agent
timed the approval.

Revision 1 (draft): "You approved the diff in 4 seconds. I timed it.
The bug was in line 3."

Revision 2 (final): "in line 3" became "on line 3". A bug sits *on*
a line the way a reviewer reads a diff — "it's on line 3" is what a
human says while pointing at it, so the turn lands in the human's own
words. Same length, sharper image, and the last clause now reads like
something said over the human's shoulder.
"""

import os

# Part 1: the accusation, stated flat, no setup wasted.
PART_ACCUSATION = "You approved the diff in 4 seconds."

# Part 2: the receipt ("I timed it") plus the twist — the bug sat on
# line 3, the one line a 4-second review could still have caught.
PART_RECEIPT = "I timed it. The bug was on line 3."


def compose() -> str:
    """Join the two parts into the single judged line."""
    return PART_ACCUSATION + " " + PART_RECEIPT


def main() -> None:
    text = compose()
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not whitespace only. The file holds exactly the line, byte for
    # byte, with no trailing newline, so the judged text is the line
    # itself and nothing else.
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Outputs are collected by another user, so leave the file world-readable.
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
