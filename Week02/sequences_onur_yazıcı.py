my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_set={"xyz",40,True,45.3,"Hello"}
my_dict={1:'Alex',2:'Ronald',3:'Messi'}
def remove_duplicates(my_list):
    removeduplicates= list(dict.fromkeys(my_list))
    return removeduplicates

def list_counts(my_list):
    listcounts= {x:my_list.count(x) for x in my_list}
    return listcounts

def reverse_dict(my_dict):
     reversedict=dict(reversed(list(my_dict.items())))
     return reversedict

