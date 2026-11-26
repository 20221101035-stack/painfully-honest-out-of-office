#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office entry for make.fun.

Writes one original out-of-office auto-reply to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

TEXT = (
    "Thank you for your email. I'm on leave until Monday, having run out of "
    "enthusiasm somewhere around unread message 300, and I'll reply in the "
    "order they arrived \u2014 with a fresh pot of coffee."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
