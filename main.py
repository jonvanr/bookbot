import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        book_text = f.read()

    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    character_count = count_characters(book_text)
    sorted = sort_characters(character_count)
    for i in range(len(sorted)):
        print(f"{sorted[i]['char']}: {sorted[i]['num']}")
    

main()
