from .args import parse_args
from .epub import epub_to_chapters
import os


def main():
    args = parse_args()
    input_path = args.input

    if input_path.lower().endswith('.epub'):
        chapters = epub_to_chapters(input_path)
        os.makedirs('output/chapters', exist_ok=True)
        for idx, chapter in enumerate(chapters, 1):
            chapter_path = f'output/chapters/chapter_{idx:04d}.txt'
            with open(chapter_path, 'w', encoding='utf-8') as f:
                f.write(chapter)
        print(f"Extracted {len(chapters)} chapters from {input_path} and saved to output/chapters/")
    else:
        print(f"Input file: {input_path}")
