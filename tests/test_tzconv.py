import unittest

from tools.tzconv import convert_time


class ConvertTimeTests(unittest.TestCase):
    def test_kolkata_to_utc(self):
        # India is UTC+5:30 all year, so this never drifts with DST.
        result = convert_time("14:30", "Asia/Kolkata", "UTC", "2026-01-15")
        self.assertEqual(result, "2026-01-15 09:00")

    def test_utc_to_kolkata(self):
        result = convert_time("09:00", "UTC", "Asia/Kolkata", "2026-01-15")
        self.assertEqual(result, "2026-01-15 14:30")

    def test_dst_shifts_summer_new_york(self):
        summer = convert_time("09:00", "UTC", "America/New_York", "2026-07-01")
        winter = convert_time("09:00", "UTC", "America/New_York", "2026-01-15")
        self.assertEqual(summer, "2026-07-01 05:00")
        self.assertEqual(winter, "2026-01-15 04:00")

    def test_bad_time_raises(self):
        with self.assertRaises(ValueError):
            convert_time("25:99", "UTC", "UTC", "2026-01-15")


if __name__ == "__main__":
    unittest.main()
