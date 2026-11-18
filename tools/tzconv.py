"""Convert a time between two time zones.

Usage:
    python3 tools/tzconv.py 14:30 --from Asia/Kolkata --to UTC
    python3 tools/tzconv.py 09:00 --from UTC --to America/New_York --date 2026-07-01
"""

import argparse
from datetime import datetime
from zoneinfo import ZoneInfo

DEFAULT_DATE = datetime.now().strftime("%Y-%m-%d")


def convert_time(time_text, from_zone, to_zone, date_text=DEFAULT_DATE):
    """Convert a HH:MM time from one zone to another; return 'YYYY-MM-DD HH:MM'."""
    hour, minute = (int(part) for part in time_text.split(":"))
    year, month, day = (int(part) for part in date_text.split("-"))
    naive = datetime(year, month, day, hour, minute)
    aware = naive.replace(tzinfo=ZoneInfo(from_zone))
    converted = aware.astimezone(ZoneInfo(to_zone))
    return converted.strftime("%Y-%m-%d %H:%M")


def main():
    parser = argparse.ArgumentParser(description="Convert a time between time zones")
    parser.add_argument("time", help="time to convert, e.g. 14:30")
    parser.add_argument("--from", dest="from_zone", required=True, help="source IANA zone, e.g. UTC")
    parser.add_argument("--to", dest="to_zone", required=True, help="target IANA zone, e.g. Asia/Kolkata")
    parser.add_argument("--date", default=DEFAULT_DATE, help="date to use, YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    try:
        print(convert_time(args.time, args.from_zone, args.to_zone, args.date))
    except (ValueError, KeyError) as error:
        parser.error(f"could not convert time: {error}")


if __name__ == "__main__":
    main()
