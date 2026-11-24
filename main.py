#!/usr/bin/env python3
"""make.fun entry: u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.

Writes one alien field note from two days of observing Earth to
/output/entry.txt. One line, no trailing newline.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

NOTE = "Field note, day 2: humans will not eat until their glowing rectangle has seen the food first; the rectangle appears to be the senior species."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_note(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("field note must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("field note must be 1-200 characters")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_note(NOTE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(NOTE)
    if path.read_text(encoding="utf-8") != NOTE:
        raise IOError("written entry does not match the field note")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
