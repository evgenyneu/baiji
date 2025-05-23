#!/usr/bin/env python3
"""
Kokoro-82M TTS - Fast High-Quality Text-to-Speech

Prerequisites:
- Install espeak-ng: brew install espeak-ng
- Run with: PYTORCH_ENABLE_MPS_FALLBACK=1 uv run python kokoro_tts.py
"""

import time
import torch
import os
import soundfile as sf
from pydub import AudioSegment
import numpy as np
from kokoro import KPipeline

# Set environment variable for Apple Silicon compatibility
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'

print(f"MPS available: {torch.backends.mps.is_available()}")

# Initialize Kokoro pipeline
print("Loading Kokoro-82M TTS model...")
start_load = time.time()
kokoro_pipe = KPipeline(lang_code='a')
end_load = time.time()
print(f"Kokoro-82M loaded in {end_load - start_load:.2f} seconds")

# Generate speech
text = "Hello, this is Kokoro TTS. I provide fast, high-quality speech generation with only 82 million parameters."

print("Generating audio...")
start_time = time.time()
generator = kokoro_pipe(text, voice='af_heart')

# Get the audio from the generator
for i, (graphemes, phonemes, audio_data) in enumerate(generator):
    break  # We just want the first result

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