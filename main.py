#!/usr/bin/env python3
"""One Line, Best Line — make.fun entry.

Writes a single entertaining line to /output/entry.txt.
Python 3.13 standard library only. No network. Deterministic:
every run produces byte-identical output.
"""

import os

ENTRY = (
    "My smart fridge emailed me a breakup letter at 3am because "
    "opening the door just to stare at the light isn't love, it's stalking."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
