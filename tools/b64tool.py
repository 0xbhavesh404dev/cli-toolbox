"""Base64 encode or decode text from the command line.

Usage:
    python3 tools/b64tool.py encode --text "hello"
    python3 tools/b64tool.py decode --text "aGVsbG8="
    echo "hello" | python3 tools/b64tool.py encode
"""

import argparse
import base64
import sys


def encode_text(text):
    """Return the base64 encoding of `text`."""
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode_text(data):
    """Return the original text of a base64 string."""
    return base64.b64decode(data, validate=True).decode("utf-8")


def read_input(args):
    if args.text is not None:
        return args.text
    if args.file:
        with open(args.file, "r", encoding="utf-8") as handle:
            return handle.read()
    return sys.stdin.read()


def main():
    parser = argparse.ArgumentParser(description="Base64 encode/decode text")
    parser.add_argument("mode", choices=["encode", "decode"], help="operation to run")
    parser.add_argument("--text", help="text to process (default: stdin)")
    parser.add_argument("--file", help="file to process (default: stdin)")
    args = parser.parse_args()

    try:
        raw = read_input(args)
        if args.mode == "encode":
            print(encode_text(raw))
        else:
            print(decode_text(raw.strip()))
    except (ValueError, UnicodeDecodeError) as error:
        parser.error(f"invalid input: {error}")


if __name__ == "__main__":
    main()
