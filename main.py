import sys
from stats import get_book_text
from stats import give_text
from stats import characters_count
from stats import sort_dictionary

count_variable = characters_count(give_text())
sort_dictionary(count_variable)


