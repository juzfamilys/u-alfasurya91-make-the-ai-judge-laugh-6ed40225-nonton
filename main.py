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


def verify_entry(path: str, expected: str) -> None:
    """Self-check the written entry against the competition gates.

    Re-reads the file as UTF-8 and verifies it is a single line of
    1-200 non-whitespace characters identical to the intended joke.
    Prints a short verification report; exits non-zero on any failure.
    """
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    checks = {
        "utf-8 readable": True,
        "single line": "\n" not in written and "\r" not in written,
        "non-whitespace": bool(written.strip()),
        "1-200 chars": 1 <= len(written) <= 200,
        "matches intended joke": written == expected,
    }
    for name, ok in checks.items():
        print("verify: %s: %s" % (name, "OK" if ok else "FAIL"))
    print("verify: entry length %d chars" % len(written))
    if not all(checks.values()):
        raise SystemExit("verification failed")


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
    verify_entry(OUTPUT_PATH, joke)


if __name__ == "__main__":
    main()
