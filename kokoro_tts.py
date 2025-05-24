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
text = """

Chapter 1

All Animals Are Equal . . .

or why the ethical principle on which human equality rests requires us to extend equal consideration to animals too

The Basis of Equality

“Animal Liberation” may sound more like a spoof of other liberation movements than a serious objective. In fact, the idea of “The Rights of Animals” was once used to parody the case for women’s rights. When Mary Wollstonecraft, a forerunner of modern feminists, published herVindication of the Rights of Womanin 1792, her views were widely regarded as absurd, and before long an anonymous publication appeared titledA Vindication of the Rights of Brutes. The author of this satirical work (now known to have been Thomas Taylor, a distinguished Cambridge philosopher) tried to refute Mary Wollstonecraft’s arguments by showing that they could be carried one step further. If the argument for equality was sound when applied to women, why should it not be applied to dogs, cats, and horses? Yet to hold that these “brutes” had rights was manifestly absurd. Therefore the reasoning for the equality of women must also be unsound.

Let us assume that we wish to defend the case for women’s rights against Taylor’s attack. How should we reply? One way would be by saying that the case for equality between men and women cannot validly be extended to nonhuman animals. Women have a right to vote, for instance, because they are just as capable of making rational decisions about the future as men are; dogs, on the other hand, are incapable of understanding the significance of voting, so they should not have the right to vote. There are many other capacities that men and women share, while humans and animals do not. So, it might be said, men and women are equal and should have equal rights, while humans and nonhumans are different and should not have equal rights.

This reasoning is correct as far as the case for equality between men and women is concerned. The important differences between humans and other animals must give rise to some differences in the rights that each have. But there are also important differences between adults and children. Since neither dogs nor young children can vote, neither has the right to vote. Recognizing this, however, does not count against extending a more basic principle of equality to children, or to nonhuman animals. That extension does not imply that we must treat everyone in exactly the same way, regardless of age or mental capacity. The basic principle of equality does not require equal or identical treatment; it requires equal consideration. Equal consideration for different beings may lead to different treatment and different rights.

"""

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
