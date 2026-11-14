"""Make the AI judge laugh - entry for the make.fun bounty.

This program writes a single joke to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, or /output when unset).
The joke is a one-liner about a coding agent that "fixed"
one bug by deleting everything around it.
"""

import os

JOKE = "I asked my coding agent to fix one bug. It fixed it, by deleting the feature, the tests, and my confidence."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
