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

def reversed_dict(d):
    reversed_dict={}
    for k,v in d.items():
        if v not in reversed_dict:
            reversed_dict[v]=k

        else:
            reversed_dict[v] = [reversed_dict[v], k]

    return reversed_dict
