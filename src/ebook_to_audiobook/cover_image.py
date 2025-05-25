import os
import ebooklib
from ebooklib import epub

def extract_cover_image(input_path: str, output_dir: str) -> str | None:
    """
    If input_path is an .epub file, extract the cover image and save it as cover.jpg in output_dir.
    If no cover is found, do nothing.
    Returns the path to the cover image if extracted, otherwise None.
    """
    if not input_path.lower().endswith('.epub'):
        return None

    book = epub.read_epub(input_path)
    cover_item = None

    # Iterate over all image items and look for 'cover' in the name
    for item in book.get_items_of_type(ebooklib.ITEM_IMAGE):
        if 'cover' in item.get_name().lower():
            cover_item = item
            break

    if cover_item is not None:
        os.makedirs(output_dir, exist_ok=True)
        cover_path = os.path.join(output_dir, 'cover.jpg')
        with open(cover_path, 'wb') as f:
            f.write(cover_item.get_content())
        return cover_path

    return None
