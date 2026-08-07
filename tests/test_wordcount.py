import unittest

from tools.wordcount import count_text


class CountTextTests(unittest.TestCase):
    def test_simple_string(self):
        counts = count_text("hello world\nfoo")
        self.assertEqual(counts, {"lines": 2, "words": 3, "characters": 15})

    def test_empty_string(self):
        self.assertEqual(count_text(""), {"lines": 0, "words": 0, "characters": 0})

    def test_single_line_no_newline(self):
        self.assertEqual(count_text("one two three")["lines"], 1)

    def test_trailing_newline(self):
        self.assertEqual(count_text("a\nb\n")["lines"], 2)


if __name__ == "__main__":
    unittest.main()
