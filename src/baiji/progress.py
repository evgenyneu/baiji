import json
import os

def save_progress(chapter_idx: int, segment_idx: int, output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)

    progress = {
        "chapter_idx": chapter_idx,
        "segment_idx": segment_idx
    }

    with open(os.path.join(output_dir, 'progress.json'), 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2)

def read_progress(output_dir: str) -> tuple[int | None, int | None]:
    """
    Read the current progress from output_dir/progress.json.
    Returns (chapter_idx, segment_idx) if the file exists, otherwise (None, None).
    """
    path = os.path.join(output_dir, 'progress.json')
    if not os.path.exists(path):
        return None, None

    with open(path, 'r', encoding='utf-8') as f:
        progress = json.load(f)
        return progress.get('chapter_idx'), progress.get('segment_idx')
