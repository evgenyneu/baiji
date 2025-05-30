import os
from glob import glob
from pydub import AudioSegment
import shutil
from .mp3_tags import set_mp3_tags

def join_wav(chapter_idx: int, output_dir: str, metadata: dict, total_chapters: int, cover_path: str = None) -> None:
    chunks_dir = os.path.join(output_dir, 'chunks')
    os.makedirs(output_dir, exist_ok=True)
    pattern = os.path.join(chunks_dir, 'chunk_*.wav')
    chunk_files = sorted(glob(pattern))

    if not chunk_files:
        print(f"No chunks found for chapter {chapter_idx}")
        return

    combined = AudioSegment.empty()

    for chunk_file in chunk_files:
        audio = AudioSegment.from_wav(chunk_file)
        combined += audio

    mp3_path = os.path.join(output_dir, f'chapter_{chapter_idx:04d}.mp3')
    combined.export(mp3_path, format='mp3', bitrate='64k')

    set_mp3_tags(
        mp3_path=mp3_path,
        chapter_idx=chapter_idx,
        total_chapters=total_chapters,
        metadata=metadata,
        cover_path=cover_path
    )

    shutil.rmtree(chunks_dir, ignore_errors=True)
