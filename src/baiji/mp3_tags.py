from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, APIC
import os

def set_mp3_tags(mp3_path: str, chapter_idx: int, total_chapters: int, metadata: dict, cover_path: str = None) -> None:
    """
    Set ID3 tags for an MP3 file: title (Chapter N), artist, album, track number (N/total), and optionally embed cover image.
    cover_path: path to cover image (jpg), or None to skip.
    """
    tags = ID3()
    tags.add(TIT2(encoding=3, text=f"Chapter {chapter_idx}"))
    tags.add(TPE1(encoding=3, text=metadata.get('author', 'Unknown')))
    tags.add(TALB(encoding=3, text=metadata.get('title', '')))
    tags.add(TRCK(encoding=3, text=f"{chapter_idx}/{total_chapters}"))

    if cover_path and os.path.isfile(cover_path):
        with open(cover_path, 'rb') as img:
            tags.add(APIC(
                encoding=3,  # UTF-8
                mime='image/jpeg',
                type=3,  # Cover (front)
                desc='cover',
                data=img.read()
            ))

    tags.save(mp3_path)
