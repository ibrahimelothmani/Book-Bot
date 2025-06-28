import sys
from stats import count_words, count_letters, sort_letters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    filepath = sys.argv[1]
    with open(filepath) as f:
        return f.read()


def main():
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count_words(get_book_text())} total words")
    print(f"--------- Character Count -------")
    for letter, count in sort_letters(count_letters(get_book_text())):
        if letter.isalpha():
            print(f"{letter}: {count}")
    print(f"============ END ===============")


main()

