import sys
from stats import get_book_text
from stats import count_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def main():
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    words_list = book_text.split()
    print(f"Found {len(words_list)} total words")

    print("--------- Character Count -------")
    count_dict = count_characters(book_text)
    def sort_on(dict):
        return dict['count']

    char_list = []
    for char in count_dict:
        if char.isalpha():
            char_list.append({'letter': char, 'count': count_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    for char_dict in char_list:
        print(f"{char_dict['letter']}: {char_dict['count']}")
main()
