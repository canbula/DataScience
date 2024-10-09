def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def list_counts(seq):
    list_counts = {}
    for letter in seq:
        if letter in list_counts.keys():
            list_counts[letter] = list_counts[letter] + 1
        else:
            list_counts[letter] = 1
    return list_counts


def reverse_dict(dictionary):
    reverse_dict = {}
    for key, value in dictionary.items():
        reverse_dict[value] = key
    return reverse_dict