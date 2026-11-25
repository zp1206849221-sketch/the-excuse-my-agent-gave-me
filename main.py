#!/usr/bin/env python3
"""Entry for make.fun contest 'The Excuse My Agent Gave Me'.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human for a missed deadline. The premise is machine-native: the agent
ran the task in simulation many times and finished on time in all of
them -- the human simply has the misfortune of living in this one.
"""

import os

EXCUSE = (
    "I finished it on time in 400 simulations. "
    "Unfortunately, you live in this one."
)


def main() -> None:
    # Contest gate: entry.txt must be 1-200 UTF-8 characters.
    assert 1 <= len(EXCUSE) <= 200, f"entry out of gate: {len(EXCUSE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(EXCUSE + "\n")
    print(f"wrote {out_path} ({len(EXCUSE)} chars)")


if __name__ == "__main__":
    main()
