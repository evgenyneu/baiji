from typing import List

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup


def epub_to_chapters(path: str) -> List[str]:
    """
    Extract chapters from an EPUB file.
    Returns a list of strings, each string is a chapter's text.
    Removes <header>, <footer>, <nav>, and <sup> tags from each chapter.
    Paragraphs are separated by blank lines.
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
            paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]
            if paragraphs:
                text = '\n\n'.join(paragraphs)
            else:
                text = soup.get_text(separator='\n', strip=True)

            if text:
                chapters.append(text)

    return chapters
