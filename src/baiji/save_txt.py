import os
from typing import List


def save_chapter_texts(chapters: List[str], output_dir: str) -> None:
    """
    Save each chapter's text to a separate file in output_dir/txt/.
    Files are named chapter_001.txt, chapter_002.txt, etc.
    """
    txt_dir = os.path.join(output_dir, 'txt')
    os.makedirs(txt_dir, exist_ok=True)

    for i, chapter in enumerate(chapters, 1):
        chapter_path = os.path.join(txt_dir, f'chapter_{i:03d}.txt')
        with open(chapter_path, 'w', encoding='utf-8') as f:
            f.write(chapter)

    print(f"== TXT files saved to {txt_dir}")
