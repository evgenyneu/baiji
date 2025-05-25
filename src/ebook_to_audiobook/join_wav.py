import os
from glob import glob
from pydub import AudioSegment
import shutil
from mutagen.id3 import ID3, TIT2, TPE1, TALB

def join_wav(chapter_idx: int, output_dir: str, metadata: dict) -> None:
    """
    Join all wav files for the given chapter in output_dir/chunks/, save as mp3 in output_dir/,
    set ID3 metadata (title, author, album), and remove the wav files.
    """
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

    # Set ID3 metadata
    tags = ID3()
    tags.add(TIT2(encoding=3, text=f"Chapter {chapter_idx}"))
    tags.add(TPE1(encoding=3, text=metadata.get('author', 'Unknown')))
    tags.add(TALB(encoding=3, text=metadata.get('title', '')))
    tags.save(mp3_path)

    # Remove the entire chunks directory and its contents
    shutil.rmtree(chunks_dir, ignore_errors=True)

    print(f"Chapter {chapter_idx} saved as {mp3_path}")
