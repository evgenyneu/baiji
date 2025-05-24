from typing import List

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup


def epub_to_chapters(path: str) -> List[str]:
    """
    Extract chapters from an EPUB file.
    Returns a list of strings, each string is a chapter's text.
    """
    book = epub.read_epub(path)
    chapters = []

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text(separator='\n', strip=True)

            if text:
                chapters.append(text)

    return chapters
