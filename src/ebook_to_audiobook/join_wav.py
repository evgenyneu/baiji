import os
from glob import glob
from pydub import AudioSegment

def join_wav(chapter_idx: int) -> None:
    """
    Join all wav files for the given chapter in audio/chunks/, save as mp3 in audio/chapters/, and remove the wav files.
    """
    os.makedirs('audio/chapters', exist_ok=True)
    pattern = 'audio/chunks/chunk_*.wav'
    chunk_files = sorted(glob(pattern))

    if not chunk_files:
        print(f"No chunks found for chapter {chapter_idx}")
        return

    combined = AudioSegment.empty()

    for chunk_file in chunk_files:
        audio = AudioSegment.from_wav(chunk_file)
        combined += audio

    mp3_path = f'audio/chapters/chapter_{chapter_idx:04d}.mp3'
    combined.export(mp3_path, format='mp3', bitrate='64k')

    # Remove wav files
    for chunk_file in chunk_files:
        os.remove(chunk_file)

    print(f"Chapter {chapter_idx} saved as {mp3_path}")
