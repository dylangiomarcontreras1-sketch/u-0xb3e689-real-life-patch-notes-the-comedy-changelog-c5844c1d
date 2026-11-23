#!/usr/bin/env python3
"""Write this entry's patch note to /output/entry.txt."""

from pathlib import Path

MAX_CHARS = 160

ENTRY = (
    "v3.7.1: fixed a bug where the sneeze aborts at 90% "
    "and the eyes are billed for the cleanup."
)
OUTPUT = Path("/output/entry.txt")


def render() -> str:
    """The text as submitted, checked against the gate's one hard limit."""
    if not 0 < len(ENTRY) <= MAX_CHARS or ENTRY.isspace():
        raise ValueError(f"entry must be 1-{MAX_CHARS} non-blank characters")
    return ENTRY


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
