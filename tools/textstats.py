"""Quick text statistics: reading time and most-used words.

Usage:
    python3 tools/textstats.py README.md
    cat article.txt | python3 tools/textstats.py
"""

import argparse
import math
import re
import sys
from collections import Counter

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "is", "it",
    "on", "for", "with", "as", "at", "by", "this", "that", "be",
}

READING_WPM = 200


def reading_time(text, wpm=READING_WPM):
    """Return the estimated reading time in minutes."""
    words = len(text.split())
    if words == 0:
        return 0
    return max(1, math.ceil(words / wpm))


def top_words(text, limit=5):
    """Return the `limit` most common non-stopwords as (word, count) pairs."""
    words = re.findall(r"[a-z']+", text.lower())
    words = [word for word in words if word not in STOPWORDS]
    return Counter(words).most_common(limit)


def sentence_count(text):
    """Rough sentence count based on '.', '!' and '?' marks."""
    return max(1, sum(text.count(mark) for mark in ".!?"))


def main():
    parser = argparse.ArgumentParser(description="Text statistics")
    parser.add_argument("file", nargs="?", help="file to analyze (default: stdin)")
    parser.add_argument("--top", type=int, default=5, help="how many top words to show")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as handle:
            text = handle.read()
    else:
        text = sys.stdin.read()

    minutes = reading_time(text)
    sentences = sentence_count(text)
    print(f"reading time: ~{minutes} min  sentences: ~{sentences}")
    for word, count in top_words(text, args.top):
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
