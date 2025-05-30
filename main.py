#!/usr/bin/env python3
import sys
from stats import get_num_words, get_chars_dict, get_sorted_chars_dicts


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)
    sorted_chars_dicts = get_sorted_chars_dicts(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in sorted_chars_dicts:
        print(f"{d['char']}: {d['count']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
