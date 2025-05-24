from typing import List
import os
from kokoro import KPipeline
import torch
import soundfile as sf
import time

def convert(chapters: List[str]) -> None:
    kokoro_pipe = KPipeline(lang_code='a')

    for chapter_idx, chapter in enumerate(chapters, 1):
        convert_single_chapter(chapter, chapter_idx, kokoro_pipe)
        return

def convert_single_chapter(text: str, chapter_idx: int, kokoro_pipe: KPipeline) -> None:
    """
    Convert a single chapter to audio chunks using Kokoro TTS and save each chunk as a .wav file.
    Splits the chapter into segments by single newlines and processes each segment independently.
    """
    os.makedirs('output/chunks', exist_ok=True)
    segments = split_into_segments(text)

    for segment_num, segment in enumerate(segments, 1):
        convert_segment(segment, chapter_idx, segment_num, kokoro_pipe)

def convert_segment(segment: str, chapter_idx: int, segment_num: int, kokoro_pipe: KPipeline) -> None:
    """
    Convert a text segment to audio using Kokoro TTS and save as a .wav file.
    """
    generator = kokoro_pipe(segment, voice='af_heart')

    for chunk_idx, (graphemes, phonemes, audio_chunk) in enumerate(generator, 1):
        chunk_path = f'output/chunks/chunk_{chapter_idx:04d}_{segment_num:04d}_{chunk_idx:04d}.wav'
        audio_array = audio_chunk.cpu().numpy() if torch.is_tensor(audio_chunk) else audio_chunk
        sf.write(chunk_path, audio_array, 24000)


def split_into_segments(text: str, min_length: int = 500) -> list[str]:
    """
    Split text by single newlines into segments, but join segments together if they are shorter than min_length.
    Returns a list of segments, each at least min_length characters (unless at the end).
    """
    raw_segments = [seg.strip() for seg in text.split('\n') if seg.strip()]
    segments = []
    buffer = ""

    for seg in raw_segments:
        if not buffer:
            buffer = seg
        else:
            buffer += "\n" + seg

        if len(buffer) >= min_length:
            segments.append(buffer)
            buffer = ""

    if buffer:
        segments.append(buffer)

    return segments
