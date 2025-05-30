def get_num_words(text):
    return len(text.split())


def get_chars_dict(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on_count(dict):
    return dict["count"]


def get_sorted_chars_dicts(chars_dict):
    sorted_chars_dicts = []
    for char, count in chars_dict.items():
        if char.isalpha():
            sorted_chars_dicts.append({"char": char, "count": count})
    sorted_chars_dicts.sort(key=sort_on_count, reverse=True)
    return sorted_chars_dicts
