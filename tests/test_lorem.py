import unittest

from tools.lorem import generate


class GenerateTests(unittest.TestCase):
    def test_paragraph_count(self):
        text = generate(paragraphs=3)
        self.assertEqual(len(text.split("\n\n")), 3)

    def test_seed_makes_output_repeatable(self):
        self.assertEqual(generate(seed=42), generate(seed=42))
        self.assertNotEqual(generate(seed=42), generate(seed=43))

    def test_sentence_count(self):
        paragraph = generate(paragraphs=1, sentences_per_paragraph=6)
        self.assertEqual(paragraph.count("."), 6)

    def test_invalid_counts_raise(self):
        with self.assertRaises(ValueError):
            generate(paragraphs=0)
        with self.assertRaises(ValueError):
            generate(sentences_per_paragraph=0)


if __name__ == "__main__":
    unittest.main()
