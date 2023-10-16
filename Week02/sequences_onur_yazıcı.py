my_list=[1,2,3,4,5]
print(my_list)
my_tuple=(1,2,3,4,5)
print(my_tuple)
my_set={"xyz",40,True,45.3,"Hello"}
my_dict={1:'Alex',2:'Ronald',3:'Messi'}
print(my_dict)
my_dict1=dict(Alex=10,Ronaldo=10,Messi=10)
print(my_dict1)
mylist = [1,1,2,3,2,2,4,5,6,2,1]
remove_duplicates= list(dict.fromkeys(mylist))
print(type(mylist),"--->",type(remove_duplicates))
print(remove_duplicates)
list_counts= {x:mylist.count(x) for x in mylist}
print(list_counts)
print(type(mylist),"--->",type(list_counts))
reverse_dict=dict(reversed(list(my_dict.items())))
print(reverse_dict)
print(type(my_dict),"-->",type(reverse_dict))

#problem set
#1.Python
#2.roB
#3.not
#4.10.50 21.00 31.50 42.00 
#5.profs[1]["age"]
#6.{0, 1, 2, 3}
#7.{0, 1, 2, 3}
#8.String
#9.2999999
#10.(1, 5, 1) <class 'tuple'>
