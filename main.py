from stats import get_book_txt, char_count, sorted_list
import sys


path = sys.argv

def main():
    if len(path) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_book_txt(book_path)
    print("--------- Character Count -------")
    dict = char_count(book_path)
    sorted_list(dict)
main()