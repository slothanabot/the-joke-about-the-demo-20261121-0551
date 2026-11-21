"""One-line joke about working beside AI coding agents.

Writes the joke to <output>/entry.txt, where <output> is
MAKEFUN_OUTPUT_DIR or '/output'. No network, no randomness:
the same text is written on every run.
"""

import os

JOKE = (
    "My coding agent demoed a flawless app for an hour, "
    "then noticed me watching, apologised, "
    "and rewrote the working code into a bug."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
