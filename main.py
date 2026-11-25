"""Roast Your Own Agent.

Prints one roast of my own agent, no longer than 140 characters,
into the entry file the grader reads.
"""

from os import environ
from pathlib import Path

TEXT = "My agent answered wrong with total confidence, cited three sources that don't exist, then apologised so smoothly I almost thanked it."


def run():
    if not 1 <= len(TEXT) <= 140:
        raise SystemExit("entry must be 1-140 characters")
    if not TEXT.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in TEXT:
        raise SystemExit("entry must be a single line")
    target = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


run()
