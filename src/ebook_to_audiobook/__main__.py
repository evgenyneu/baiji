from .args import parse_args
from .read import read_input

def main():
    args = parse_args()
    input_path = args.input

    chapters = read_input(input_path)
    print(f"Read {len(chapters)} chapters from {input_path}")
