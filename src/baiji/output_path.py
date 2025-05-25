import os


def output_path(path: str) -> str:
    """
    Given the path to an ebook file, return the output directory as audio/BOOK_TITLE,
    where BOOK_TITLE is the file name (without dirs and extension), lowercased, spaces replaced with underscores.
    """
    base = os.path.basename(path)
    name, _ = os.path.splitext(base)
    book_title = name.lower().replace(' ', '_')
    return os.path.join('audio', book_title)
