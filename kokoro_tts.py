#!/usr/bin/env python3
"""
Kokoro-82M TTS - Fast High-Quality Text-to-Speech

Prerequisites:
- Install espeak-ng: brew install espeak-ng
- Run with: PYTORCH_ENABLE_MPS_FALLBACK=1 uv run python kokoro_tts.py
"""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'

import time
import torch
import soundfile as sf
from pydub import AudioSegment
import numpy as np
from kokoro import KPipeline

# Set environment variable for Apple Silicon compatibility

print(f"MPS available: {torch.backends.mps.is_available()}")

# Initialize Kokoro pipeline
print("Loading Kokoro-82M TTS model...")
start_load = time.time()
kokoro_pipe = KPipeline(lang_code='a')
end_load = time.time()
print(f"Kokoro-82M loaded in {end_load - start_load:.2f} seconds")

# Generate speech - audiobook test with longer text
text = """In the quiet village of Willowbrook, nestled between rolling hills and ancient oak trees, lived a young librarian named Clara who possessed an extraordinary gift. Every evening, as the sun painted the sky in shades of amber and rose, she would discover that the books in her care began to whisper their stories aloud. The leather-bound volumes would creak open by themselves, and the characters within would step out from their pages, bringing tales of adventure, romance, and mystery to life in the dimly lit library halls.

Clara had inherited this magical library from her grandmother, who had warned her that with great knowledge comes great responsibility. The stories that escaped the books each night weren't merely entertainment—they were living memories of human experience, hopes and dreams that had been carefully preserved in ink and paper for generations. As Clara learned to navigate this enchanted world, she realized that she had become the guardian not just of books, but of the very essence of storytelling itself, ensuring that these precious narratives would continue to inspire and guide future generations through the darkness of uncertainty."""

print("Generating audio...")
start_time = time.time()
generator = kokoro_pipe(text, voice='af_heart')

# Get all audio chunks from the generator
audio_chunks = []
for i, (graphemes, phonemes, audio_chunk) in enumerate(generator):
    audio_chunks.append(audio_chunk)
    print(f"Processed chunk {i+1}: {len(audio_chunk)} samples")

# Concatenate all audio chunks
audio_data = torch.cat(audio_chunks, dim=0)

end_time = time.time()

print(f"Audio generated in {end_time - start_time:.2f} seconds")
print(f"Audio shape: {audio_data.shape}")

# Save audio
os.makedirs("output", exist_ok=True)

wav_file = "output/kokoro_output.wav"
mp3_file = "output/kokoro_output.mp3"

audio_array = audio_data.cpu().numpy() if torch.is_tensor(audio_data) else np.array(audio_data)
audio_normalized = audio_array.squeeze() / np.max(np.abs(audio_array.squeeze()))

sf.write(wav_file, audio_normalized, 24000)
audio_segment = AudioSegment.from_wav(wav_file)
audio_segment.export(mp3_file, format="mp3")

print(f"Audio saved as {mp3_file}")
print(f"Duration: {len(audio_segment)/1000:.2f} seconds")
print("⚡ Kokoro-82M TTS: Perfect balance of speed and quality!")
