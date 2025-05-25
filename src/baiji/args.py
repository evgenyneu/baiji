import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert ebook text to audiobook using Kokoro TTS."
    )

    parser.add_argument(
        "input",
        type=str,
        help="Path to input .txt or .epub file"
    )

    return parser.parse_args()
