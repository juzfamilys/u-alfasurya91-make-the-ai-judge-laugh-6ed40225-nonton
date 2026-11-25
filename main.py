#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

Writes a single original joke about office life (one line, under
200 characters) to /output/entry.txt for the make.fun bounty
u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Pure Python standard library only; no dependencies.
"""

import os

JOKE = "My boss praised my work-life balance, then booked a 7 a.m. meeting to discuss it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    joke = JOKE.strip()
    if not joke:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in joke:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(joke) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(joke)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)
    print("wrote %d characters to %s" % (len(joke), OUTPUT_PATH))


if __name__ == "__main__":
    main()
