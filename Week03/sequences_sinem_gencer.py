def remove_duplicates(mylist):
  newlist = []
  for item in mylist:
    if item not in newlist:
      newlist.append(item)
  return newlist

def list_counts(mylist):
    duplicated_items = {}
    for item in mylist:
        if item not in duplicated_items:
            duplicated_items[item] = 1
        else:
            duplicated_items[item] += 1
    return duplicated_items

def reverse_dict(mydict):
    newdict = {}
    for key, value in mydict.items():
        newdict[value] = key
    return newdict
