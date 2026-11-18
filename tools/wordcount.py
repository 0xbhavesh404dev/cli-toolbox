"""Count lines, words and characters of a file or stdin.

Usage:
    python3 tools/wordcount.py README.md
    cat README.md | python3 tools/wordcount.py
"""

import argparse
import sys


def count_text(text):
    """Return line, word and character counts for `text`."""
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def main():
    parser = argparse.ArgumentParser(description="Count lines, words and characters")
    parser.add_argument("file", nargs="?", help="file to count (default: stdin)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()

    counts = count_text(text)
    print(f"lines: {counts['lines']}  words: {counts['words']}  characters: {counts['characters']}")


if __name__ == "__main__":
    main()
