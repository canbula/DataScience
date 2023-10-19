my_list=[1,2,3,3,4,5,5,5,6]
my_tuple=("suleyman","dogan","codeco","soft","software","engineer")
my_set={1,2,3,4,5,6,7,8,9,10}
my_dict={"name":"suleyman","surname":"dogan","age":23,"job":"software engineer","company":"Codeco Soft"}



def remove_duplicates(remove_list):
    return list(set(remove_list))

def list_counts(counts_list):
    return {i:counts_list.count(i) for i in counts_list}


def reverse_dict(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
            new_dict[value]=key

    return new_dict

