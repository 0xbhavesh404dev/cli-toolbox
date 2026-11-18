import unittest

from tools.csvsum import column_values, read_rows, summarize


SAMPLE = "name,score\nalice,10\nbob,30\ncarol,\n"


class SummarizeTests(unittest.TestCase):
    def test_stats(self):
        stats = summarize([10.0, 30.0])
        self.assertEqual(stats["count"], 2)
        self.assertEqual(stats["sum"], 40.0)
        self.assertEqual(stats["mean"], 20.0)
        self.assertEqual(stats["min"], 10.0)
        self.assertEqual(stats["max"], 30.0)

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            summarize([])


class ColumnValuesTests(unittest.TestCase):
    def setUp(self):
        self.rows = read_rows(SAMPLE)

    def test_by_name_skips_bad_cells(self):
        name, values = column_values(self.rows, "score")
        self.assertEqual(name, "score")
        self.assertEqual(values, [10.0, 30.0])

    def test_by_index(self):
        name, values = column_values(self.rows, 2)
        self.assertEqual(values, [10.0, 30.0])

    def test_unknown_column_raises(self):
        with self.assertRaises(ValueError):
            column_values(self.rows, "nope")


if __name__ == "__main__":
    unittest.main()
