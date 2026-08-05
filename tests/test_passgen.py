import string
import unittest

from tools.passgen import build_charset, generate_password


class GeneratePasswordTests(unittest.TestCase):
    def test_length_is_respected(self):
        self.assertEqual(len(generate_password(24)), 24)
        self.assertEqual(len(generate_password(4)), 4)

    def test_short_length_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_password(3)

    def test_symbols_by_default(self):
        password = generate_password(64)
        self.assertTrue(any(char in build_charset() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_no_symbols_mode(self):
        password = generate_password(64, use_symbols=False)
        allowed = set(string.ascii_letters + string.digits)
        self.assertTrue(set(password) <= allowed)

    def test_random_passwords_differ(self):
        self.assertNotEqual(generate_password(16), generate_password(16))


if __name__ == "__main__":
    unittest.main()
