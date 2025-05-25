from typing import List
from .epub import epub_to_chapters
import re


def normalize_text(text: str) -> str:
    """
    Normalizes text by joining lines within paragraphs.
    Treats two or more consecutive newlines as paragraph breaks.
    Joins lines within a paragraph with a space.
    """
    paragraphs = re.split(r'\n{2,}', text)
    normalized_paragraphs = []
    for paragraph in paragraphs:
        lines = [line.strip() for line in paragraph.splitlines()]
        normalized_paragraph = ' '.join(line for line in lines if line)
        normalized_paragraphs.append(normalized_paragraph)
    return '\n\n'.join(normalized_paragraphs)


def read_input(path: str) -> List[str]:
    """
    Reads the input file and returns a list of chapter strings.
    For .epub, returns chapters. For .txt, returns a list with one element (the file content).
    """
    if path.lower().endswith('.epub'):
        return epub_to_chapters(path)
    elif path.lower().endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
            normalized_text = normalize_text(text)
            return [normalized_text]
    else:
        raise ValueError("Unsupported file type. Only .epub and .txt are supported.")
