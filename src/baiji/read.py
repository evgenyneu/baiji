from typing import List
from .epub import epub_to_chapters


def read_input(path: str) -> List[str]:
    """
    Reads the input file and returns a list of chapter strings.
    For .epub, returns chapters. For .txt, returns a list with one element (the file content).
    """
    if path.lower().endswith('.epub'):
        return epub_to_chapters(path)
    elif path.lower().endswith('.txt'):
        with open(path, 'r', encoding='utf-8') as f:
            return [f.read()]
    else:
        raise ValueError("Unsupported file type. Only .epub and .txt are supported.")
