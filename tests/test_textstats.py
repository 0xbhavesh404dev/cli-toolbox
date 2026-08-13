import unittest

from tools.textstats import reading_time, sentence_count, top_words


class ReadingTimeTests(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(reading_time(""), 0)

    def test_at_least_one_minute(self):
        self.assertEqual(reading_time("just a few words"), 1)

    def test_scales_with_length(self):
        text = " ".join(["word"] * 400)
        self.assertEqual(reading_time(text), 2)


class TopWordsTests(unittest.TestCase):
    def test_counts_and_order(self):
        top = top_words("cat cat cat dog dog bird", limit=2)
        self.assertEqual(top, [("cat", 3), ("dog", 2)])

    def test_stopwords_removed(self):
        top = top_words("the the the cat")
        self.assertEqual([word for word, _ in top], ["cat"])

    def test_case_insensitive(self):
        top = top_words("Cat CAT cat")
        self.assertEqual(top, [("cat", 3)])


class SentenceCountTests(unittest.TestCase):
    def test_counts_marks(self):
        self.assertEqual(sentence_count("One. Two! Three?"), 3)

    def test_minimum_one(self):
        self.assertEqual(sentence_count("no punctuation here"), 1)


if __name__ == "__main__":
    unittest.main()
