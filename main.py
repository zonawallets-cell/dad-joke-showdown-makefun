#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun, program/v1).

Writes one original dad joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure stdlib only (os). The joke is a single text of at most 200 characters,
punchline at the end, no line breaks, byte-identical on every run.
"""

import os

JOKE = "What's for dinner, Dad? \"Leftovers.\" Again? \"Yes \u2014 a re-peat performance.\""


def validate(text):
    """Enforce the gate; return a list of problems (empty = valid).

    Gate: UTF-8, 1-200 chars, no line breaks, not only whitespace.
    """
    problems = []
    if not isinstance(text, str):
        return ["not a string"]
    if not 1 <= len(text) <= 200:
        problems.append("length %d outside 1-200" % len(text))
    if not text.strip():
        problems.append("only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("contains a line break")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("not UTF-8 encodable: %s" % exc)
    return problems


def main():
    problems = validate(JOKE)
    if problems:
        raise SystemExit("joke failed validation: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print("wrote %d chars to %s" % (len(JOKE), path))


if __name__ == "__main__":
    main()
