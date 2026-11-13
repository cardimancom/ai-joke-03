"""Make the AI judge laugh: a one-liner about coding agents.

Writes the joke to entry.txt inside MAKEFUN_OUTPUT_DIR
(or /output when the variable is unset). The joke is the whole
entry: no setup, no punchline tag, just the pull request itself.
"""

import os

JOKE = "My coding agent's pull request said 'Fixed everything.' The diff was 4,000 lines, and nothing worked."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
