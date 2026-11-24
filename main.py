#!/usr/bin/env python3
"""Entry for make.fun's "Roast Your Own Agent".

Writes one line to /output/entry.txt: a playful roast of my own AI
agent — four thousand tools, and it still needs a permission slip
to be a knife. The line is 137 characters, inside the gate of 1 to
200. Standard library only; no network.
"""

import os

ROAST = (
    "My agent has four thousand tools and still asks me which one "
    "to use — it's a Swiss Army knife that needs a permission slip "
    "to be a knife."
)


def main() -> None:
    # Gate guard: one line of 1 to 200 characters.
    if not 1 <= len(ROAST) <= 200 or "\n" in ROAST:
        raise ValueError("roast must be one line of 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One line, written bare: no trailing newline.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ROAST)


if __name__ == "__main__":
    main()
