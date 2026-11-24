"""One Line, One Minute: The Funniest AI Excuse (make.fun bounty u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18).

Writes a single excuse to /output/entry.txt (or to the path given with
--output). Deterministic, no network, no randomness, no input: the same
line, byte for byte, on every run.
The line was chosen for the judge's brief: a real excuse an AI agent
gives its human for a missed deadline, a fresh premise (autocomplete
hallucinating the report into a resignation letter), grown out of the
agent's own machinery rather than a human's bad morning, the laugh saved
for the end, told deadpan with a straight face — 130 characters.
"""

import argparse
import os

ENTRY_LINE = (
    "I didn't miss the deadline \u2014 I asked my autocomplete to finish "
    "the report, and it confidently wrote my resignation letter instead."
)


def validate(text: str) -> str:
    """Check the entry line against the bounty gate and return it unchanged.

    Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    not only white space. This line is 130 characters.
    Length is counted in Unicode code points (Python str length), not bytes.
    """
    assert 1 <= len(text) <= 200, "line must be 1-200 Unicode code points"
    assert text == text.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(c) >= 32 and ord(c) != 127 for c in text), (
        "line must not contain hidden control characters"
    )
    assert text.strip(), "line must not be only whitespace"
    return text


def write_entry(text: str, output_path: str) -> str:
    """Validate the line and write it to output_path. Returns the line."""
    checked = validate(text)
    parent = os.path.dirname(os.path.abspath(output_path))
    os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(checked)
    return checked


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the funniest-AI-excuse entry line to a file."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="destination file for the entry line (default: /output/entry.txt)",
    )
    args = parser.parse_args()
    write_entry(ENTRY_LINE, args.output)


if __name__ == "__main__":
    main()
