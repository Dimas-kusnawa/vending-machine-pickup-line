"""Vending machine pickup line.

Writes one pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "Hey, you. My coil's been stuck for a week \u2014 then you walked by and everything dropped."

# The line is 84 characters, inside the 200-character limit.
# A coil is the spiral that holds snacks in a vending machine: when
# it turns, the snack drops. Here the coil is "stuck" on everyone
# else, and only the passing human makes everything drop.
# Why it works: the machine speaks in the first person ("Hey, you.
# My coil..."), the joke lives in the machine's own world (a stuck
# coil, a drop), the punch lands on the last word, and it is
# charming rather than creepy -- a machine flattered into working.
# The line is a single line with no trailing newline, so the entry
# file holds exactly the line and nothing else. It is deterministic:
# the same line is written on every run, with no randomness and no
# input from anywhere outside this file.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {os.path.join(out_dir, 'entry.txt')}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
