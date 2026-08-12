import tempfile
import unittest
from pathlib import Path

from tools.organize import category_for, organize


class CategoryForTests(unittest.TestCase):
    def test_known_categories(self):
        self.assertEqual(category_for(".jpg"), "images")
        self.assertEqual(category_for(".PDF"), "documents")
        self.assertEqual(category_for(".zip"), "archives")

    def test_unknown_goes_to_other(self):
        self.assertEqual(category_for(".xyz"), "other")


class OrganizeTests(unittest.TestCase):
    def test_moves_files_into_folders(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "photo.jpg").write_text("fake")
            (root / "notes.txt").write_text("fake")
            (root / "blob.xyz").write_text("fake")

            moved = organize(root)

            self.assertTrue((root / "images" / "photo.jpg").exists())
            self.assertTrue((root / "documents" / "notes.txt").exists())
            self.assertTrue((root / "other" / "blob.xyz").exists())
            self.assertFalse((root / "photo.jpg").exists())
            self.assertEqual(moved["images"], 1)

    def test_ignores_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "already_a_folder").mkdir()
            moved = organize(root)
            self.assertEqual(moved, {})


if __name__ == "__main__":
    unittest.main()
