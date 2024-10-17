def remove_duplicates(lst):
    seen = []
    result = []
    for x in lst:
        if x not in seen:
            seen.append(x)
            result.append(x)
    return result

def list_counts(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(dct):
    reversed_dict = {}
    for k, v in dct.items():
        reversed_dict[v] = k
    return reversed_dict
