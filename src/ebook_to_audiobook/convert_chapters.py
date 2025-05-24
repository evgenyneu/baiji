from typing import List
import os
from kokoro import KPipeline
import torch
import soundfile as sf
import time

def convert(chapters: List[str]) -> None:
    kokoro_pipe = KPipeline(lang_code='a')

    for idx, chapter in enumerate(chapters, 1):
        convert_single_chapter(chapter, idx, kokoro_pipe)
        return

def convert_single_chapter(text: str, idx: int, kokoro_pipe: KPipeline) -> None:
    """
    Convert a single chapter to audio chunks using Kokoro TTS and save each chunk as a .wav file.
    """
    os.makedirs('output/chunks', exist_ok=True)
    generator = kokoro_pipe(text, voice='af_heart')

    for chunk_num, (graphemes, phonemes, audio_chunk) in enumerate(generator, 1):
        chunk_path = f'output/chunks/chunk_{idx:04d}_{chunk_num:04d}.wav'
        audio_array = audio_chunk.cpu().numpy() if torch.is_tensor(audio_chunk) else audio_chunk
        sf.write(chunk_path, audio_array, 24000)
