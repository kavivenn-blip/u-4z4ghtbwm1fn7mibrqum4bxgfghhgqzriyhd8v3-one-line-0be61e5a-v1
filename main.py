#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line to /output/entry.txt.

The line: "I tried meal prepping; by Wednesday the chicken had formed a
union, the rice filed for divorce, and the Tupperware charges rent."

Why this line: one self-contained joke in a single sentence. The setup
(meal prepping) is ordinary; the twist lands three times — the chicken
unionises, the rice files for divorce, and the Tupperware starts
charging rent — each beat escalating the same absurd bureaucracy.
128 characters, one line, UTF-8, no trailing newline. Verified locally:
two runs from clean copies produce byte-identical output, sha256
21fa51b771413205ef76d17fc3513826838156215d383e25c557e881ba18ebf8,
file mode 0644.
Deterministic, offline, standard library only.
"""

import os
import stat

LINE = (
    "I tried meal prepping; by Wednesday the chicken had formed a union, "
    "the rice filed for divorce, and the Tupperware charges rent."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
