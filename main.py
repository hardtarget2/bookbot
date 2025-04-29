# Imports Word_count function from the stats.py file
import sys
from stats import word_count
from stats import charecter_count
from stats import report_char_num

def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    num_char = charecter_count(book_text)
    report = report_char_num(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in report:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")
    
main()