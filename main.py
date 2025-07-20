from stats import get_book_text
def main():
    book_text = get_book_text("books/frankenstein.txt")
    words_list = book_text.split()
    print(f"{len(words_list)} words found in the document")

main()
