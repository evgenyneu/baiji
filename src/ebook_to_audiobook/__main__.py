from .args import parse_args
from .read import read_input
from .convert_chapters import convert
from .output_path import output_path

def main():
    args = parse_args()
    input_path = args.input

    out_dir = output_path(input_path)
    chapters = read_input(input_path)
    convert(chapters, out_dir)
    print(f"Audio files saved to {out_dir}")
    print("We are done")
