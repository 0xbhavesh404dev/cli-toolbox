import unittest

from tools.dice import parse_expression, roll


class ParseExpressionTests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse_expression("3d6"), (3, 6, 0))

    def test_defaults_to_one_die(self):
        self.assertEqual(parse_expression("d20"), (1, 20, 0))

    def test_modifier(self):
        self.assertEqual(parse_expression("2d10+3"), (2, 10, 3))
        self.assertEqual(parse_expression("d8-1"), (1, 8, -1))

    def test_case_insensitive(self):
        self.assertEqual(parse_expression("4D6"), (4, 6, 0))

    def test_rejects_garbage(self):
        with self.assertRaises(ValueError):
            parse_expression("banana")
        with self.assertRaises(ValueError):
            parse_expression("0d6")
        with self.assertRaises(ValueError):
            parse_expression("1d1")


class RollTests(unittest.TestCase):
    def test_results_in_range(self):
        for value in roll(50, 6):
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 6)

    def test_returns_requested_count(self):
        self.assertEqual(len(roll(7, 20)), 7)


if __name__ == "__main__":
    unittest.main()
