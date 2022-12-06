### Remove all the occurrences of an element from a list


list_1 = [1,1,2,3,4,2,1,3,4,5,6,7,8,8,2]
lst2= []
for i in list_1:
    if i not in lst2:
        lst2.append(i)
    else:
        pass
        # lst2.remove(i)               # remove the repeated element of the list
print(lst2)



#remove the given element from the list
value = int(input("enter the given item to be deleted "))
lst2= []
for i in list_1:
    if value != i:
        lst2.append(i)
    else:
        pass
print(lst2)