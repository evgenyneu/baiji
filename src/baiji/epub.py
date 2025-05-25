from typing import List

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from .transform_text import normalize_text


def epub_to_chapters(path: str) -> List[str]:
    """
    Extract chapters from an EPUB file.
    Returns a list of strings, each string is a chapter's text.
    Removes <header>, <footer>, <nav>, and <sup> tags from each chapter.
    Paragraphs are separated by blank lines.
    Skips chapters that are empty or only whitespace.
    """
    book = epub.read_epub(path)
    chapters = []

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            content = item.get_content()
            soup = BeautifulSoup(content, 'html.parser')

            # Remove unwanted tags
            for tag in soup(['header', 'footer', 'nav', 'sup']):
                tag.decompose()

            # Extract headers and paragraphs
            text_parts = []

            # Get headers first
            for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                text = header.get_text(separator='\n')
                text_parts.append(text)

            # Then get paragraphs
            paragraphs = [p.get_text() for p in soup.find_all('p') if p.get_text()]
            text_parts.extend(paragraphs)

            if text_parts:
                text = '\n\n'.join(text_parts)
            else:
                text = soup.get_text(separator='\n', strip=True)

            # Skip chapters that are empty or only whitespace
            if text and text.strip():
                text = normalize_text(text)
                chapters.append(text)

    return chapters
