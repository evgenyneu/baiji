# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Environment Setup
```bash
# Install dependencies and create virtual environment
uv sync

# Activate environment
source .venv/bin/activate

# Start Jupyter notebook server
uv run jupyter notebook
```

### Development Workflow
```bash
# Run all notebooks to test TTS models
uv run jupyter nbconvert --execute bark_tts.ipynb
uv run jupyter nbconvert --execute vits_tts.ipynb
```

## Project Purpose

The purpose is to evaluate TTS models, with intent of using them to generate audiobook from a ebook text. Thus the models needs to be able to be fast but still have good quality. The balance of speed and quality is important.

Each TTS model has its own notebook, and the notebook is used to evaluate the model.


### TTS Model Implementations

**Bark TTS (`bark_tts.ipynb`)**:
- High-quality, human-like speech generation
- Uses `suno/bark-small` model via transformers pipeline
- Runs on CPU due to MPS compatibility issues with PyTorch
- Slow generation (~40-90 seconds) but best quality
- Outputs to `output/bark_output.mp3`

**VITS TTS (`vits_tts.ipynb`)**:
- Fast generation optimized for Apple Silicon MPS GPU
- Uses `facebook/mms-tts-eng` model (40M parameters)
- Much faster (~10 seconds) with good quality
- Outputs to `output/vits_output.mp3`

**Kokoro TTS (`kokoro_tts.py`)**:
- By FAR the best quality, and the fastest.
- We will use this model from now on.
- Needs to be run with `PYTORCH_ENABLE_MPS_FALLBACK=1` environment variable:

```sh
PYTORCH_ENABLE_MPS_FALLBACK=1 uv run python kokoro_tts.py
```




### Output Structure

All generated audio files are saved in the `output/` directory as both WAV and MP3 formats. Audio is normalized to prevent clipping before saving.

## Apple Silicon Considerations

- Bark TTS requires CPU execution due to MPS dtype compatibility issues
- VITS TTS leverages MPS GPU acceleration effectively
-- Kokoro uses MPS very well.
- Set `PYTORCH_ENABLE_MPS_FALLBACK=1` environment variable for better compatibility

## Code style guidelines

- Code needs to be simple, and readaible, we use KISS principle.
- No need for unnecessary comments or print outs. Code needs to be self explanatory.
- In Jupiter notebooks, don't write gigantic cells, but organize neatly into smalelr cells which user can run sequentially.
