import sys
from stats import get_total_words, create_char_dict, create_list_of_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_path = sys.argv[1]
    file_contents = (get_book_text(book_path))

    char_dict = create_char_dict(file_contents)

    char_list = create_list_of_dicts(char_dict)

    def output_table():
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(get_total_words(file_contents))
        print("--------- Character Count -------")
        for item in char_list:
            if not item["char"].isalpha():
                continue
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")

    output_table()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main()
