"""Sort files in a folder into subfolders by file type.

Usage:
    python3 tools/organize.py ~/Downloads
"""

import argparse
import shutil
from pathlib import Path

CATEGORY_BY_EXT = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "documents": {".pdf", ".txt", ".md", ".doc", ".docx", ".csv"},
    "audio": {".mp3", ".wav", ".flac", ".ogg"},
    "video": {".mp4", ".mov", ".mkv", ".webm"},
    "archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
}


def category_for(suffix):
    """Map a file extension like '.jpg' to its folder name."""
    suffix = suffix.lower()
    for category, extensions in CATEGORY_BY_EXT.items():
        if suffix in extensions:
            return category
    return "other"


def organize(directory):
    """Move every file in `directory` into a type-based subfolder.

    Returns a dict of category -> number of files moved.
    """
    directory = Path(directory)
    moved = {}
    for entry in sorted(directory.iterdir()):
        if not entry.is_file():
            continue
        category = category_for(entry.suffix)
        target_dir = directory / category
        target_dir.mkdir(exist_ok=True)
        shutil.move(str(entry), str(target_dir / entry.name))
        moved[category] = moved.get(category, 0) + 1
    return moved


def main():
    parser = argparse.ArgumentParser(description="Organize files into subfolders by type")
    parser.add_argument("directory", help="folder to organize")
    args = parser.parse_args()

    moved = organize(args.directory)
    if not moved:
        print("Nothing to move.")
        return
    for category, count in sorted(moved.items()):
        print(f"{category}: {count} file(s)")


if __name__ == "__main__":
    main()
