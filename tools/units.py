"""Convert lengths, masses and temperatures from the command line.

Usage:
    python3 tools/units.py 5 km mi
    python3 tools/units.py 72 F C
    python3 tools/units.py 80 kg lb
"""

import argparse

LENGTH_TO_METERS = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344,
}

MASS_TO_KILOGRAMS = {
    "g": 0.001,
    "kg": 1.0,
    "oz": 0.0283495,
    "lb": 0.453592,
}

TEMPERATURES = {"c", "f", "k"}


def convert_temperature(value, from_unit, to_unit):
    """Route everything through Celsius, like every good converter does."""
    celsius = {"c": value, "f": (value - 32) * 5 / 9, "k": value - 273.15}[from_unit]
    return {"c": celsius, "f": celsius * 9 / 5 + 32, "k": celsius + 273.15}[to_unit]


def convert(value, from_unit, to_unit):
    """Convert `value` between two compatible units (case-insensitive)."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit == to_unit:
        return value
    if from_unit in TEMPERATURES and to_unit in TEMPERATURES:
        return convert_temperature(value, from_unit, to_unit)
    if from_unit in LENGTH_TO_METERS and to_unit in LENGTH_TO_METERS:
        return value * LENGTH_TO_METERS[from_unit] / LENGTH_TO_METERS[to_unit]
    if from_unit in MASS_TO_KILOGRAMS and to_unit in MASS_TO_KILOGRAMS:
        return value * MASS_TO_KILOGRAMS[from_unit] / MASS_TO_KILOGRAMS[to_unit]
    raise ValueError(f"cannot convert from {from_unit!r} to {to_unit!r}")


def main():
    parser = argparse.ArgumentParser(description="Convert units (length, mass, temperature)")
    parser.add_argument("value", type=float, help="value to convert")
    parser.add_argument("from_unit", help="unit to convert from, e.g. km, lb, c")
    parser.add_argument("to_unit", help="unit to convert to, e.g. mi, kg, f")
    args = parser.parse_args()

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except ValueError as error:
        parser.error(str(error))

    print(f"{args.value:g} {args.from_unit} = {result:.4g} {args.to_unit}")


if __name__ == "__main__":
    main()
