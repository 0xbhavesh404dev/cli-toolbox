import unittest

from tools.palette import hex_to_rgb, rgb_to_hex, shade


class HexToRgbTests(unittest.TestCase):
    def test_six_digit(self):
        self.assertEqual(hex_to_rgb("#0080ff"), (0, 128, 255))

    def test_three_digit_expands(self):
        # CSS style: each digit is doubled, so 08f -> 0088ff
        self.assertEqual(hex_to_rgb("08f"), (0, 136, 255))

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            hex_to_rgb("#12345")


class RgbToHexTests(unittest.TestCase):
    def test_roundtrip(self):
        self.assertEqual(rgb_to_hex((0, 128, 255)), "#0080ff")

    def test_clamps_out_of_range(self):
        self.assertEqual(rgb_to_hex((-5, 128, 300)), "#0080ff")


class ShadeTests(unittest.TestCase):
    def test_half_white(self):
        self.assertEqual(shade("#ffffff", 0.5), "#808080")

    def test_dark_stays_dark(self):
        self.assertEqual(shade("#000000", 2.0), "#000000")

    def test_clamps_each_channel(self):
        # channels clamp individually, never normalize toward white
        self.assertEqual(shade("#e63946", 3.0), "#ffabd2")


if __name__ == "__main__":
    unittest.main()
