"""Generate a random password from the command line.

Usage:
    python3 tools/passgen.py
    python3 tools/passgen.py --length 24 --no-symbols
"""

import argparse
import secrets
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*-_=?"


def build_charset(use_symbols=True):
    """Return the pool of characters passwords are drawn from."""
    charset = LOWER + UPPER + DIGITS
    if use_symbols:
        charset += SYMBOLS
    return charset


def generate_password(length=16, use_symbols=True):
    """Return a random password of the requested length."""
    if length < 4:
        raise ValueError("password length must be at least 4")
    charset = build_charset(use_symbols)
    return "".join(secrets.choice(charset) for _ in range(length))


def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    parser.add_argument("--length", type=int, default=16, help="password length (default: 16)")
    parser.add_argument("--no-symbols", action="store_true", help="skip symbol characters")
    args = parser.parse_args()

    try:
        print(generate_password(args.length, use_symbols=not args.no_symbols))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
