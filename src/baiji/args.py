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

    parser.add_argument(
        "--lang-code",
        type=str,
        default="a",
        help="Language code for TTS (default: a)"
    )

    parser.add_argument(
        "--voice",
        type=str,
        default="af_heart",
        help="Voice to use for TTS (default: af_heart)"
    )

    return parser.parse_args()
