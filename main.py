import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

#import functions

from stats import get_num_characters
from stats import get_num_words
from stats import sort_characters

# convert book into string

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_string = get_book_text(str(sys.argv[1]))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {str(sys.argv[1])}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_string)} total words")
    print("--------- Character Count -------")
    dictionary_list = sort_characters(get_num_characters(book_string))
    for dict in dictionary_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
        else:
            pass
    print("============= END ===============")
main()