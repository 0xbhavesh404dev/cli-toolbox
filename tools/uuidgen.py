"""Generate random UUIDs (version 4) from the command line.

Usage:
    python3 tools/uuidgen.py
    python3 tools/uuidgen.py --count 5
"""

import argparse
import uuid


def generate_uuids(count):
    """Return a list of `count` UUID4 strings."""
    if count < 1:
        raise ValueError("count must be at least 1")
    return [str(uuid.uuid4()) for _ in range(count)]


def main():
    parser = argparse.ArgumentParser(description="Generate random UUIDs")
    parser.add_argument("--count", type=int, default=1, help="how many UUIDs (default: 1)")
    args = parser.parse_args()

    try:
        for value in generate_uuids(args.count):
            print(value)
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
