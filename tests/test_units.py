import unittest

from tools.units import convert


class ConvertTests(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.106856, places=4)
        self.assertAlmostEqual(convert(1, "ft", "in"), 12.0, places=6)

    def test_mass(self):
        self.assertAlmostEqual(convert(1, "kg", "lb"), 2.2046244, places=4)
        self.assertEqual(convert(500, "g", "kg"), 0.5)

    def test_temperature(self):
        self.assertEqual(convert(100, "c", "f"), 212.0)
        self.assertEqual(convert(32, "f", "c"), 0.0)
        self.assertAlmostEqual(convert(0, "k", "c"), -273.15, places=6)

    def test_same_unit_returns_value(self):
        self.assertEqual(convert(42, "km", "KM"), 42)

    def test_incompatible_units_raise(self):
        with self.assertRaises(ValueError):
            convert(1, "kg", "mi")


if __name__ == "__main__":
    unittest.main()
