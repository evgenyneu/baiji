from .args import parse_args

def main():
    args = parse_args()
    print(f"Input file: {args.input}")
