def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def give_text():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    return text

from stats import words

from stats import characters_count


words(give_text())
count_variable = characters_count(give_text())

print(count_variable)

