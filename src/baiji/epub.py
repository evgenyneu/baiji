from typing import List

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from .transform_text import normalize_text


def epub_to_chapters(path: str) -> List[str]:
    """
    Extract chapters from an EPUB file.
    """
    book = epub.read_epub(path)
    chapters = []

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')

            # Remove unwanted tags
            for tag in soup(['header', 'footer', 'nav', 'sup']):
                tag.decompose()

            # Extract paragraphs and join with double newlines
            paragraphs = [p.get_text() for p in soup.find_all('p') if p.get_text()]

            if paragraphs:
                text = '\n\n'.join(paragraphs)
            else:
                text = soup.get_text(separator='\n', strip=True)

            # Skip chapters that are empty or only whitespace
            if text and text.strip():
                text = normalize_text(text)
                chapters.append(text)

    return chapters
