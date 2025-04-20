from stats import get_num_words
from stats import get_num_chars
from stats import get_report
def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    word_count = get_num_words(file_contents)
    char_counts = get_num_chars(file_contents)
    # print(get_num_chars(file_contents))
    report = get_report(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_count in report:
        if not char_count[0].isalpha():
            continue
        print(f"{char_count[0]}: {char_count[1]}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

    
main()