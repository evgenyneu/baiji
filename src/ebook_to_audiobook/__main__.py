import warnings
# Suppress pytorch warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

from .args import parse_args
from .read import read_input
from .convert_chapters import convert
from .output_path import output_path
from .cover_image import extract_cover_image
from .epub_metadata import extract_metadata

def main():
    args = parse_args()
    input_path = args.input

    out_dir = output_path(input_path)
    cover_path = extract_cover_image(input_path=input_path, output_dir=out_dir)

    metadata = extract_metadata(input_path=input_path)
    chapters = read_input(path=input_path)

    convert(
        chapters=chapters,
        output_dir=out_dir,
        metadata=metadata,
        cover_path=cover_path
    )

    print(f"Audio files saved to {out_dir}")
    print("We are done")
