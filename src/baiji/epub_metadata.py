from typing import Dict
import os
from ebooklib import epub

def extract_metadata(input_path: str) -> Dict[str, str]:
    """
    Extract book title and author from an EPUB or TXT file.
    For EPUB, use metadata fields. For TXT, use filename as title and 'Unknown' as author.
    Returns a dict with 'title' and 'author'.
    """
    if input_path.lower().endswith('.epub'):
        book = epub.read_epub(input_path)
        title = 'Unknown'
        author = 'Unknown'

        title_list = book.get_metadata('DC', 'title')
        if title_list:
            title = title_list[0][0]

        author_list = book.get_metadata('DC', 'creator')
        if author_list:
            author = author_list[0][0]

        return {'title': title, 'author': author}

    # For TXT files
    base = os.path.basename(input_path)
    name, _ = os.path.splitext(base)
    return {'title': name, 'author': 'Unknown'}
