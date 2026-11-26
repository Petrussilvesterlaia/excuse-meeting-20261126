#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes a single one-line excuse to /output/entry.txt.
Deterministic, self-contained: reads nothing outside this file.
"""

ENTRY = "Sorry, I can't make it \u2014 my calendar booked me into a meeting about why I have too many meetings."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text: str) -> str:
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = validate_entry(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
