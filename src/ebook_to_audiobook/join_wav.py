import os
from glob import glob
from pydub import AudioSegment

def join_wav(chapter_idx: int, output_dir: str) -> None:
    """
    Join all wav files for the given chapter in output_dir/chunks/, save as mp3 in output_dir/, and remove the wav files.
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

    # Remove wav files
    for chunk_file in chunk_files:
        os.remove(chunk_file)

    print(f"Chapter {chapter_idx} saved as {mp3_path}")
