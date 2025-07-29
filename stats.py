def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents

def count_characters(text):
    char_count = {}

    # Convert text to lowercase to avoid duplicates
    text = text.lower()

    # Count each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
