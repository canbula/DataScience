my_list = [1, 1, 45, 35, 35]
my_tuple = (3, 5, 7, 9)
my_set = {"manisa", "izmir", "adana"}
my_dict = {"manisa":45, "izmir":35, "adana":1}

def remove_duplicates(source_list):
    final_list = list(set(source_list))
    return final_list

def list_counts(source_list):
    counts_dict = {}
    for element in source_list:
        if element in counts_dict:
            counts_dict[element] += 1
        else:
            counts_dict[element] = 1
    return counts_dict

def reverse_dict(input_dict):
    reversed_dict = {}
    buffer_list1 = list(input_dict.keys())
    buffer_list2 = list(input_dict.values())
    for i in range(len(buffer_list1)):
        reversed_dict[buffer_list2[i]] = buffer_list1[i]
    return reversed_dict
