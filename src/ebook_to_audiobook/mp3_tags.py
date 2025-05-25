from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK

def set_mp3_tags(mp3_path: str, chapter_idx: int, total_chapters: int, metadata: dict) -> None:
    """
    Set ID3 tags for an MP3 file: title (Chapter N), artist, album, and track number (N/total).
    """
    tags = ID3()
    tags.add(TIT2(encoding=3, text=f"Chapter {chapter_idx}"))
    tags.add(TPE1(encoding=3, text=metadata.get('author', 'Unknown')))
    tags.add(TALB(encoding=3, text=metadata.get('title', '')))
    tags.add(TRCK(encoding=3, text=f"{chapter_idx}/{total_chapters}"))
    tags.save(mp3_path)
