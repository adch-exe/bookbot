import sys
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def give_text():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
        return text

def words(text):
    num_words = text.split()
    total = len(num_words)
    return total

var1 = give_text()
var2 = words(var1)

def characters_count(text):
    lowercase = text.lower()
    char_dictionary = {}
    
    for i in lowercase:
        if i not in char_dictionary:
            char_dictionary[i] = 1
        else:
            char_dictionary[i] += 1
    return char_dictionary

def sort_dictionary(char_dictionary):
    dictionary_list = []
    for char, count in char_dictionary.items():
        new_dic = {"char": char, "num": count}
        if char.isalpha():
            dictionary_list.append(new_dic)
    def sort_helper(dictionary_list):
        return dictionary_list["num"]
        
    dictionary_list.sort(reverse=True, key=sort_helper)
    
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {var2} total words")
    print("--------- Character Count -------")
    for i in dictionary_list:
        char1 = i["char"]
        char2 = i["num"]
        print (f"{char1}: {char2}")
