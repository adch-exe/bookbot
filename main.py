def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def give_text():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    return text

from stats import words

words(give_text())
