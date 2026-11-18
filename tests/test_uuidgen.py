import unittest
import uuid

from tools.uuidgen import generate_uuids


class GenerateUuidsTests(unittest.TestCase):
    def test_count(self):
        self.assertEqual(len(generate_uuids(5)), 5)
        self.assertEqual(len(generate_uuids(1)), 1)

    def test_valid_uuid4(self):
        parsed = uuid.UUID(generate_uuids(1)[0])
        self.assertEqual(parsed.version, 4)

    def test_rejects_zero(self):
        with self.assertRaises(ValueError):
            generate_uuids(0)


if __name__ == "__main__":
    unittest.main()
