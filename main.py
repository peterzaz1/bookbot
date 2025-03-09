import sys
from stats import *


def get_book_text(file_path: str) -> str:
    print(f"Analyzing book found at {file_path}...")
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path: str = sys.argv[1]

    if not book_path.startswith("./"):
        book_path = "./" + book_path
    

    print("============ BOOKBOT ============")
    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_of_words: int = get_number_of_words(text)
    print(f"Found {num_of_words} total words")

    num_of_chars: dict[str, int] = get_character_count(text)


    print("--------- Character Count -------")
    sorted_chars: dict[str,int] = get_sorted_characters(num_of_chars)
    for k,v in sorted_chars.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")
    

main()




