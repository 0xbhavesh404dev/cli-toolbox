import random
import unittest

from tools.picker import flip, pick, pick_many


class PickerTests(unittest.TestCase):
    def setUp(self):
        self.rng = random.Random(42)

    def test_pick_returns_member(self):
        items = ["a", "b", "c"]
        self.assertIn(pick(items, self.rng), items)

    def test_pick_rejects_empty(self):
        with self.assertRaises(ValueError):
            pick([], self.rng)

    def test_pick_many_distinct(self):
        chosen = pick_many(["a", "b", "c", "d"], 3, self.rng)
        self.assertEqual(len(chosen), 3)
        self.assertEqual(len(set(chosen)), 3)

    def test_pick_many_too_many(self):
        with self.assertRaises(ValueError):
            pick_many(["a"], 2, self.rng)

    def test_flip_sides(self):
        self.assertIn(flip(self.rng), {"heads", "tails"})


if __name__ == "__main__":
    unittest.main()
