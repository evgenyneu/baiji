from typing import List
import os
from kokoro import KPipeline
import torch
import soundfile as sf
from .progress import save_progress, read_progress
from .join_wav import join_wav
from tqdm import tqdm
from typing import Dict

def convert(
    chapters: List[str],
    output_dir: str,
    metadata: Dict[str, str],
    cover_path: str = None,
    lang_code: str = "a",
    voice: str = "af_heart"
) -> None:
    print("== Initializing text-to-speech model...")
    kokoro_pipe = KPipeline(lang_code=lang_code, repo_id='hexgrad/Kokoro-82M')
    total_chapters = len(chapters)

    # Read progress if exists
    progress = read_progress(output_dir)
    resume_chapter_idx, resume_segment_idx = progress

    if resume_chapter_idx is not None:
        print(f"== Resuming from chapter {resume_chapter_idx} segment {resume_segment_idx + 1}")

    for chapter_idx, chapter in enumerate(chapters, 1):
        # If resuming, skip chapters before the saved one
        if resume_chapter_idx is not None and chapter_idx < resume_chapter_idx:
            continue

        convert_single_chapter(
            text=chapter,
            chapter_idx=chapter_idx,
            total_chapters=total_chapters,
            kokoro_pipe=kokoro_pipe,
            start_segment_idx=resume_segment_idx,
            output_dir=output_dir,
            voice=voice
        )
        resume_segment_idx = None # Start with the first segment of the next chapter

        join_wav(
            chapter_idx=chapter_idx,
            output_dir=output_dir,
            metadata=metadata,
            total_chapters=total_chapters,
            cover_path=cover_path
        )

def convert_single_chapter(text: str, chapter_idx: int, total_chapters: int, kokoro_pipe: KPipeline, start_segment_idx, output_dir: str, voice: str) -> None:
    """
    Convert a single chapter to audio chunks using Kokoro TTS and save each chunk as a .wav file.
    Splits the chapter into segments by single newlines and processes each segment independently.
    start_segment_idx: segment index to start from (1-based)
    """
    chunks_dir = os.path.join(output_dir, 'chunks')
    os.makedirs(chunks_dir, exist_ok=True)
    segments = split_into_segments(text)

    for segment_idx, segment in enumerate(tqdm(segments, desc=f"Chapter {chapter_idx}/{total_chapters}"), 1):
        if start_segment_idx is not None and segment_idx <= start_segment_idx:
            continue

        convert_segment(segment, chapter_idx, segment_idx, kokoro_pipe, output_dir, voice)
        save_progress(chapter_idx, segment_idx, output_dir)

def convert_segment(segment: str, chapter_idx: int, segment_idx: int, kokoro_pipe: KPipeline, output_dir: str, voice: str) -> None:
    """
    Convert a text segment to audio using Kokoro TTS and save as a .wav file.
    """
    chunks_dir = os.path.join(output_dir, 'chunks')
    generator = kokoro_pipe(segment, voice=voice)

    for chunk_idx, (graphemes, phonemes, audio_chunk) in enumerate(generator, 1):
        chunk_path = os.path.join(chunks_dir, f'chunk_{chapter_idx:04d}_{segment_idx:04d}_{chunk_idx:04d}.wav')
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
