from .args import parse_args
from .read import read_input
from .convert_chapters import convert

def main():
    args = parse_args()
    input_path = args.input

    chapters = read_input(input_path)
    convert(chapters)
    print(f"Read {len(chapters)} chapters from {input_path}")
