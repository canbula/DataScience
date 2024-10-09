def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


def list_counts(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts


def reverse_dict(dct):
    reversed_dict = {}
    for key, value in dct.items():
        reversed_dict[value] = key
    return reversed_dict
