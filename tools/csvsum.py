"""Print summary statistics for one column of a CSV file.

Usage:
    python3 tools/csvsum.py data.csv --column score
    cat data.csv | python3 tools/csvsum.py --column 2
"""

import argparse
import csv
import sys


def summarize(values):
    """Return count, sum, mean, min and max for a list of numbers."""
    if not values:
        raise ValueError("no numeric values found")
    return {
        "count": len(values),
        "sum": sum(values),
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }


def column_values(rows, column):
    """Extract numeric values for a column given its name or 1-based index."""
    header = rows[0]
    if isinstance(column, int):
        if not 1 <= column <= len(header):
            raise ValueError(f"column index {column} is out of range")
        name = header[column - 1]
        index = column - 1
    else:
        if column not in header:
            raise ValueError(f"column {column!r} not found in header")
        name = column
        index = header.index(column)

    values = []
    for row in rows[1:]:
        try:
            values.append(float(row[index]))
        except (ValueError, IndexError):
            continue  # skip empty or non-numeric cells
    return name, values


def read_rows(text):
    """Parse CSV text into a list of rows."""
    return [row for row in csv.reader(text.splitlines()) if row]


def main():
    parser = argparse.ArgumentParser(description="Summarize a CSV column")
    parser.add_argument("file", nargs="?", help="CSV file (default: stdin)")
    parser.add_argument("--column", required=True, help="column name or 1-based index")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8", newline="") as handle:
            rows = [row for row in csv.reader(handle) if row]
    else:
        rows = read_rows(sys.stdin.read())

    try:
        name, values = column_values(rows, int(args.column) if args.column.isdigit() else args.column)
        stats = summarize(values)
    except ValueError as error:
        parser.error(str(error))

    print(f"column: {name}")
    for key in ("count", "sum", "mean", "min", "max"):
        print(f"{key}: {stats[key]:g}")


if __name__ == "__main__":
    main()
