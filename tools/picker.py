"""Pick a random item from a list, or flip a coin.

Usage:
    python3 tools/picker.py pizza pasta salad
    python3 tools/picker.py --pick 2 alice bob carol
    python3 tools/picker.py --coin
"""

import argparse
import random


def pick(items, rng=None):
    """Return one random item from `items`."""
    if not items:
        raise ValueError("need at least one item to pick from")
    rng = rng or random
    return rng.choice(items)


def pick_many(items, count, rng=None):
    """Return `count` distinct random items from `items`."""
    if count < 1:
        raise ValueError("count must be at least 1")
    if count > len(items):
        raise ValueError("cannot pick more items than exist")
    rng = rng or random
    return rng.sample(items, count)


def flip(rng=None):
    """Return 'heads' or 'tails'."""
    rng = rng or random
    return rng.choice(["heads", "tails"])


def main():
    parser = argparse.ArgumentParser(description="Random picker / coin flip")
    parser.add_argument("items", nargs="*", help="items to choose from")
    parser.add_argument("--pick", type=int, default=1, metavar="N", help="pick N items (default: 1)")
    parser.add_argument("--coin", action="store_true", help="flip a coin instead")
    parser.add_argument("--seed", type=int, help="random seed for repeatable runs")
    args = parser.parse_args()

    rng = random.Random(args.seed) if args.seed is not None else random

    if args.coin:
        print(flip(rng))
        return
    if not args.items:
        parser.error("give some items to pick from (or use --coin)")

    try:
        if args.pick == 1:
            print(pick(args.items, rng))
        else:
            chosen = pick_many(args.items, args.pick, rng)
            print(", ".join(chosen))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
