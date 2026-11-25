"""Two Days of Quiet Dread — writes the winning review comment to /output/entry.txt.

The comment approves the PR (LGTM ... Merging.) while carrying quiet
existential dread: the tests are green, the sun will still die, but the
deploy happens first. Flat tone, understatement, no exclamation.
"""

import os

ENTRY = "LGTM. The tests are green, the sun will still die, but not before this deploys. Merging."


def validate(text: str) -> None:
    """Gate: 1-140 chars, a single line, not only whitespace (UTF-8)."""
    if not text or text != text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    if len(text) > 140:
        raise SystemExit(f"gate failed: entry is {len(text)} chars, max 140")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
