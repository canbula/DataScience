def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def list_counts(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    return counts

def reverse_dict(d):
    return {v: k for k, v in d.items()}
