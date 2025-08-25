def words(text):
    num_words = text.split()
    total = len(num_words)
    print(f"{total} words found in the document")

def characters_count(text):
    lowercase = text.lower()
    char_dictionary = {}
    
    for i in lowercase:
        if i not in char_dictionary:
            char_dictionary[i] = 1
        else:
            char_dictionary[i] += 1
    return char_dictionary