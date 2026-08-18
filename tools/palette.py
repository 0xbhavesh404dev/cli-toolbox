"""Generate lighter and darker shades of a hex color.

Usage:
    python3 tools/palette.py #e63946
    python3 tools/palette.py e63946 --factors 0.5 1.0 1.5
"""

import argparse

MIN_CHANNEL, MAX_CHANNEL = 0, 255


def hex_to_rgb(hex_color):
    """Turn '#0080ff' (or '08f') into an (r, g, b) tuple."""
    text = hex_color.lstrip("#")
    if len(text) == 3:
        text = "".join(char * 2 for char in text)
    if len(text) != 6:
        raise ValueError(f"invalid hex color: {hex_color!r}")
    return tuple(int(text[index:index + 2], 16) for index in (0, 2, 4))


def rgb_to_hex(rgb):
    """Turn an (r, g, b) tuple back into a '#rrggbb' string."""
    return "#" + "".join(f"{max(MIN_CHANNEL, min(MAX_CHANNEL, channel)):02x}" for channel in rgb)


def shade(hex_color, factor):
    """Scale every channel of a color by `factor`, clamped to 0-255."""
    rgb = hex_to_rgb(hex_color)
    scaled = tuple(int(round(channel * factor)) for channel in rgb)
    return rgb_to_hex(scaled)


def shades(hex_color):
    """Return five shades of a color, from dark to light."""
    return [shade(hex_color, factor) for factor in (0.4, 0.7, 1.0, 1.3, 1.6)]


def main():
    parser = argparse.ArgumentParser(description="Generate color shades")
    parser.add_argument("color", help="hex color like #e63946 or e63946")
    parser.add_argument("--factors", type=float, nargs="*", help="custom scale factors")
    args = parser.parse_args()

    try:
        results = [shade(args.color, factor) for factor in args.factors] if args.factors else shades(args.color)
    except ValueError as error:
        parser.error(str(error))

    for color in results:
        print(color)


if __name__ == "__main__":
    main()
