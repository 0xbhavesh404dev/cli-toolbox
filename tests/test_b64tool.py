import unittest

from tools.b64tool import decode_text, encode_text


class Base64Tests(unittest.TestCase):
    def test_known_encoding(self):
        self.assertEqual(encode_text("hello"), "aGVsbG8=")
        self.assertEqual(decode_text("aGVsbG8="), "hello")

    def test_roundtrip_unicode(self):
        text = "héllo wörld ☃"
        self.assertEqual(decode_text(encode_text(text)), text)

    def test_invalid_base64_raises(self):
        with self.assertRaises(ValueError):
            decode_text("not!!valid")


if __name__ == "__main__":
    unittest.main()
