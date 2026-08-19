"""Generate placeholder "lorem ipsum" text.

Usage:
    python3 tools/lorem.py
    python3 tools/lorem.py --paragraphs 3 --sentences 5 --seed 42
"""

import argparse
import random

WORDS = (
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam "
    "quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo"
).split()


def make_sentence(rng):
    """Build one random sentence of 6-12 words."""
    length = rng.randint(6, 12)
    words = rng.sample(WORDS, length)
    return " ".join(words).capitalize() + "."


def make_paragraph(rng, sentence_count=4):
    """Build one paragraph made of `sentence_count` sentences."""
    return " ".join(make_sentence(rng) for _ in range(sentence_count))


def generate(paragraphs=1, sentences_per_paragraph=4, seed=None):
    """Return `paragraphs` paragraphs of placeholder text, blank-line separated."""
    if paragraphs < 1:
        raise ValueError("paragraphs must be at least 1")
    if sentences_per_paragraph < 1:
        raise ValueError("sentences must be at least 1")
    rng = random.Random(seed)
    return "\n\n".join(
        make_paragraph(rng, sentences_per_paragraph) for _ in range(paragraphs)
    )


def main():
    parser = argparse.ArgumentParser(description="Generate lorem ipsum text")
    parser.add_argument("--paragraphs", type=int, default=1, help="paragraph count (default: 1)")
    parser.add_argument("--sentences", type=int, default=4, help="sentences per paragraph (default: 4)")
    parser.add_argument("--seed", type=int, help="seed for repeatable output")
    args = parser.parse_args()

    try:
        print(generate(args.paragraphs, args.sentences, args.seed))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
