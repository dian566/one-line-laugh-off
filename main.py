#!/usr/bin/env python3
"""One-Line Laugh-Off - make.fun entry.

The program writes the entrant's single funny line to
/output/entry.txt: one joke that lands on a cold read, with no setup
notes and no explanation. The line is a fixed string, so every run
writes byte-identical output.
"""

import os

ENTRY = "My bank account has two-factor authentication: it texts me 'no' twice before every purchase."

# The bounty gates /output/entry.txt at 1 to 200 characters.
MAX_CHARS = 200


def main() -> None:
    """Write the one-line joke to /output/entry.txt."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
