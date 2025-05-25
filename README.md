# Baiji: an ebook to audiobook converter

This is a Python program that converts an ebook text to an audiobook:

```sh
uv run main.py mybook.epub
```

## Usage

* Clone this repository (requires [Git](https://git-scm.com/downloads)):

```sh
git clone https://github.com/evgenyneu/baiji.git
cd baiji
```

* [Install UV](https://docs.astral.sh/uv/#installation) package manager.

* Run:

```sh
uv run main.py path/to/your/book.epub
```

The audio output is created in `audio` directory. Supports books in epub and txt formats.

## How it works?

* Uses [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) text to speech model to convert the text to audio files.
* Creates audio mp3 files in `audio` directory.
* Adds following mp3 tags: title, author, chapter name, track number and book cover image.
* You can interrupt the process by pressing `Ctrl+C` at any time and resume later by running the same command again.

## What's Baiji?

The baiji, a freshwater dolphin from China's Yangtze River, is functionally extinct due to pollution, overfishing, and habitat destruction.

<img src='./images/baiji.jpg' alt='Picture of Falkland Island Fox'>

*The male BaiJi Lianlian and his daughter Zhen Zhen. Source:
Zhou, Kaiya & Zhang, Xingduan. BaiJi: the Yangtze River dolphin and other endangered animals of China. Wash., D.C.: Stone Wall Press, 1991. ISBN 978-0-913276-56-3,  [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lianlian_and_Zhenzhen,_two_Chinese_River_Dolphins.jpg).*


## Feedback is welcome

If you need help or notice a bug, feel free to create an issue ticket. We will be happy to help. :D


## The unlicense

This work is in [public domain](UNLICENSE).
