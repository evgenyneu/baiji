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

    parser.add_argument(
        "--save-txt",
        action="store_true",
        help="Save chapter text files debugging"
    )

    return parser.parse_args()
