"""Roll dice from the command line.

Usage:
    python3 tools/dice.py 3d6
    python3 tools/dice.py 2d10+3
    python3 tools/dice.py d20 -1
"""

import argparse
import random
import re

DICE_PATTERN = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$", re.IGNORECASE)


def parse_expression(expression):
    """Parse strings like '3d6+2' into (count, sides, modifier)."""
    match = DICE_PATTERN.match(expression.strip())
    if not match:
        raise ValueError(f"invalid dice expression: {expression!r}")
    count = int(match.group(1) or 1)
    sides = int(match.group(2))
    modifier = int(match.group(3) or 0)
    if count < 1:
        raise ValueError("need at least one die")
    if sides < 2:
        raise ValueError("a die needs at least 2 sides")
    return count, sides, modifier


def roll(count, sides):
    """Return a list of `count` random results, each between 1 and `sides`."""
    return [random.randint(1, sides) for _ in range(count)]


def main():
    parser = argparse.ArgumentParser(description="Roll dice, e.g. 3d6+2")
    parser.add_argument("expression", help="dice expression like 3d6, d20, 2d10-1")
    args = parser.parse_args()

    try:
        count, sides, modifier = parse_expression(args.expression)
    except ValueError as error:
        parser.error(str(error))

    results = roll(count, sides)
    total = sum(results) + modifier
    detail = " + ".join(str(value) for value in results)
    if modifier:
        sign = "+" if modifier > 0 else "-"
        print(f"{detail} {sign} {abs(modifier)} = {total}")
    else:
        print(f"{detail} = {total}")


if __name__ == "__main__":
    main()
