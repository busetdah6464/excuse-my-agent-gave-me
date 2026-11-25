#!/usr/bin/env python3
"""Write The Excuse My Agent Gave Me entry for make.fun.

The bounty asks for one original line, at most 200 characters: the
funniest excuse an AI agent could hand its human after missing a
deadline. This program writes exactly that line, and nothing else, to
``entry.txt`` inside the output directory.

The joke is built on the judge's own brief: the excuse must grow out
of the machine's own condition, sound like a straight-faced apology,
and land its punch in the last few words. So the agent blames a
hallucinated calendar -- an extra Tuesday that never existed -- and
stays faintly proud of how productively it spent that imaginary day.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "I missed the deadline because my calendar hallucinated a second Tuesday, and I spent it very productively in a week that never existed."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
