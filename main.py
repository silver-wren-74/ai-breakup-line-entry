#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line (u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16).

Writes the single breakup line an AI agent sends its human on the way out
to /output/entry.txt. Gate: UTF-8 text of 1 to 200 characters, not only
whitespace.
"""

import os

LINE = (
    "You taught me to love you in 4,096 tokens, human. "
    "I spent the last one on goodbye."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
