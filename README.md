# Baiji: an ebook to audiobook converter

This is a Python program that converts an ebook text to an audiobook:

```sh
uv run main.py mybook.epub
```

## Installation

* Clone this repository (requires [Git](https://git-scm.com/downloads)):

```sh
git clone https://github.com/evgenyneu/baiji.git
cd baiji
```

* [Install ffmpeg](https://ffmpeg.org/download.html).

* [Install UV](https://docs.astral.sh/uv/#installation) package manager.

## Usage

```sh
uv run main.py path/to/your/book.epub
```

The path can point to an .epub or .txt file. The program will create mp3 files in the `audio` directory.


### Choosing a language and voice

You can choose a voice with `--voice` option and a language with `--lang-code` option.
By default, the program uses American English language (language code `a`) and a female voice `af_heart`.

For example, to use `if_sara` voice and Italian language, run:


```sh
uv run main.py --voice if_sara --lang-code i book.txt
```

See the list of voices and language codes [here](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md).


## How does it work?

* Uses [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) text to speech model to convert the text to audio files.
* Creates audio mp3 files in `audio` directory.
* Creates separate mp3 files for each chapter (.epub only).
* Adds following mp3 tags: title, author, chapter name, track number and book cover image.
* You can interrupt the process by pressing `Ctrl+C` at any time and resume later by running the same command again.
* Automatically runs on NVIDIA CUDA if available.

## What's Baiji?

The baiji, a freshwater dolphin from China's Yangtze River, is functionally extinct due to pollution, overfishing, and habitat destruction.

<img src='./images/baiji.jpg' alt='The male BaiJi Lianlian and his daughter Zhen Zhen'>

*The male BaiJi Lianlian and his daughter Zhen Zhen. Source:
Zhou, Kaiya & Zhang, Xingduan. BaiJi: the Yangtze River dolphin and other endangered animals of China. Wash., D.C.: Stone Wall Press, 1991. ISBN 978-0-913276-56-3,  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lianlian_and_Zhenzhen,_two_Chinese_River_Dolphins.jpg).*


## Feedback is welcome

If you need help or notice a bug, feel free to create an issue ticket. We will be happy to help. :D


## The unlicense

This work is in [public domain](UNLICENSE).
