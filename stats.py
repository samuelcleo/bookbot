def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents
