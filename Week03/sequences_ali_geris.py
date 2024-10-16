def remove_duplicates(input_list):
    """Tekrarlanan elemanları çıkar."""
    return list(dict.fromkeys(input_list))

def list_counts(input_list):
    """Listedeki elemanların tekrar sayısı."""
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

def reverse_dict(input_dict):
    return {value: key for key, value in input_dict.items()}
