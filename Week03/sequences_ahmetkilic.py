def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def list_counts(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def reverse_dict(d):
    reversed_result = {}
    for key, value in d.items():
        if value not in reversed_result:
            reversed_result[value] = key
        else:
            reversed_result[value] = [reversed_result[value], key]

    return reversed_result
