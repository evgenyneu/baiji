"""
Text transformation utilities for baiji.
"""
import re

def roman_to_arabic(roman: str) -> str:
    """
    Converts a Roman numeral to an Arabic number.
    Example: "I" -> "1", "II" -> "2", "III" -> "3"
    """
    roman = roman.upper()
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman)):
        if i > 0 and roman_nums[roman[i]] > roman_nums[roman[i-1]]:
            result += roman_nums[roman[i]] - 2 * roman_nums[roman[i-1]]
        else:
            result += roman_nums[roman[i]]
    return str(result)

def convert_chapter_numbers(text: str) -> str:
    """
    Converts Roman numerals in chapter titles to Arabic numbers.
    Example: "Chapter I" -> "Chapter 1", "chapter II" -> "chapter 2"
    """
    pattern = r'(?i)(chapter\s+)([IVX]+)'
    return re.sub(pattern, lambda m: m.group(1) + roman_to_arabic(m.group(2)), text)

def normalize_text(text: str) -> str:
    """
    Normalizes text by joining lines within paragraphs.
    Treats two or more consecutive newlines as paragraph breaks.
    Joins lines within a paragraph with a space.
    Converts Roman numerals in chapter titles to Arabic numbers.

    This is needed because many ebooks have lines break for each line of text
    in a paragraph, which will create pauses in the text-to-speech output.
    """
    text = convert_chapter_numbers(text)
    paragraphs = re.split(r'\n{2,}', text)
    normalized_paragraphs = []
    for paragraph in paragraphs:
        lines = [line.strip() for line in paragraph.splitlines()]
        normalized_paragraph = ' '.join(line for line in lines if line)
        normalized_paragraphs.append(normalized_paragraph)
    return '\n\n'.join(normalized_paragraphs)
