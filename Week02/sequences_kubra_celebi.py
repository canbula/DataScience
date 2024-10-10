from collections import defaultdict

def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

def list_counts(lst):
    counts = defaultdict(int)
    for item in lst:
        counts[item] += 1
    return dict(counts)

def reverse_dict(dct):
    return {v: k for k, v in dct.items()}
