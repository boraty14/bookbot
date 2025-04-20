def get_num_words(context):
    return len(context.split())

def get_num_chars(context):
    char_counts = {}
    for char in context:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts

def get_report(char_counts):
    char_list = []
    for char in char_counts:
        char_list.append((char,char_counts[char]))
    char_list.sort(key=lambda item: item[1], reverse=True)
    return char_list
