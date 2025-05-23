# Text-to-Speech with Muyan-TTS

This project demonstrates text-to-speech conversion using the Muyan-TTS model.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python package management.

### Prerequisites

Install uv if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Environment Setup

1. Create and activate a virtual environment with all dependencies:

```bash
uv sync
```

2. Activate the environment:

```bash
source .venv/bin/activate
```

3. Start Jupyter notebook:

```bash
uv run jupyter notebook
```

### Quick Start

1. Open `muyan_tts_test.ipynb` in Jupyter
2. Run all cells to test the Muyan-TTS model
3. Generated audio will be saved as `muyan_tts_output.wav`


### Usage

The notebook provides a complete example of:

- Loading the Muyan-TTS model
- Converting text to speech
- Saving audio output to file
- Playing audio in the notebook

Modify the `text` variable in the notebook to test with different input text.
