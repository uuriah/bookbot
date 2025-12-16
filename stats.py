def get_total_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def create_char_dict(file_contents):
    char_dict = {}
    for char in file_contents.lower():
        if char not in char_dict:
            char_dict[char] = char_dict.get(char, 0) + 1
        else:
            char_dict[char] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def create_list_of_dicts(char_dict):
    char_counts = []

    for key, val in char_dict.items():
        my_dict = {"char":key, "num":val}
        char_counts.append(my_dict)

    char_counts.sort(reverse=True, key=sort_on)
    return char_counts
