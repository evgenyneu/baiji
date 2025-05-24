import json
import os

def save_progress(chapter_idx: int, segment_idx: int) -> None:
    os.makedirs('output', exist_ok=True)

    progress = {
        "chapter_idx": chapter_idx,
        "segment_idx": segment_idx
    }

    with open('output/progress.json', 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2)
