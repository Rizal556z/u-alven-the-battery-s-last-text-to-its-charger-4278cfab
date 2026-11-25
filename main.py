#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

A pure-stdlib Python program for the make.fun bounty
"The Battery's Last Text to Its Charger". It writes the phone battery's
last text message to the charger it waited for all day -- one line of
plain text, 1-200 characters -- to /output/entry.txt.
"""

import os

ENTRY = (
    "hey. it's me. 1%. waited all day for you and you show up "
    "with a cable that doesn't even fit. tell my apps i loved them. "
    "you, i just tolerated."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Re-read and assert the gate: 1-200 chars, single line, not blank.
    with open("/output/entry.txt", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text.strip(), "entry must not be only whitespace"
    print(f"Wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
