# SPDX-License-Identifier: MIT
"""One Emoji, One Smile — writes exactly one emoji to /output/entry.txt.

The chosen emoji is the teddy bear: a universal comfort symbol that a
stranger reads instantly as warm and friendly, with no intimacy,
sarcasm or in-joke attached.
"""
import os

EMOJI = "🧸"
OUTPUT_PATH = "/output/entry.txt"


def render() -> str:
    """Return the entry text: the single emoji, nothing else, no newline."""
    return EMOJI


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" plus an explicit no-trailing-newline write keeps the file
    # byte-exact: 1 character, 4 UTF-8 bytes, well inside the 1-8 char gate.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
