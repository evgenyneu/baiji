import pytest
from baiji.transform_text import roman_to_arabic, convert_chapter_numbers

def test_roman_to_arabic():
    assert roman_to_arabic("I") == "1"
    assert roman_to_arabic("II") == "2"
    assert roman_to_arabic("III") == "3"
    assert roman_to_arabic("IV") == "4"
    assert roman_to_arabic("V") == "5"
    assert roman_to_arabic("VI") == "6"
    assert roman_to_arabic("VII") == "7"
    assert roman_to_arabic("VIII") == "8"
    assert roman_to_arabic("IX") == "9"
    assert roman_to_arabic("X") == "10"
    assert roman_to_arabic("XI") == "11"
    assert roman_to_arabic("XII") == "12"
    assert roman_to_arabic("XIII") == "13"
    assert roman_to_arabic("XIV") == "14"
    assert roman_to_arabic("XV") == "15"

def test_roman_to_arabic_case_insensitive():
    assert roman_to_arabic("i") == "1"
    assert roman_to_arabic("ii") == "2"
    assert roman_to_arabic("iii") == "3"
    assert roman_to_arabic("iv") == "4"
    assert roman_to_arabic("v") == "5"

def test_convert_chapter_numbers():
    text = "Chapter I\nChapter II\nChapter III"
    expected = "Chapter 1\nChapter 2\nChapter 3"
    assert convert_chapter_numbers(text) == expected

def test_convert_chapter_numbers_case_insensitive():
    text = "chapter i\nChapter II\nCHAPTER III"
    expected = "chapter 1\nChapter 2\nCHAPTER 3"
    assert convert_chapter_numbers(text) == expected

def test_convert_chapter_numbers_with_spaces():
    text = "Chapter  I\nChapter  II\nChapter   III"
    expected = "Chapter  1\nChapter  2\nChapter   3"
    assert convert_chapter_numbers(text) == expected

def test_convert_chapter_numbers_no_changes():
    text = "This is a normal text without any chapter numbers"
    assert convert_chapter_numbers(text) == text

def test_convert_chapter_numbers_mixed_content():
    text = "Chapter I\nSome text here\nChapter II\nMore text\nChapter III"
    expected = "Chapter 1\nSome text here\nChapter 2\nMore text\nChapter 3"
    assert convert_chapter_numbers(text) == expected
