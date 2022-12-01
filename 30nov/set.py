## a set cannot have mutable elements like lists, sets or dictionaries as its elements.


my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# my_set = {1.0, "Hello", (1, 2, 3),[2,3,4,5]}
# print(my_set)                                      # cannot have list in the set

my_set = {1.0, "Hello", (1, 2, 3),(2,3,4,5,6)}
print(my_set)
# my_set = {1.0, "Hello", {1, (2,3,4), 3},(2,3,4,5,6)}
# print(my_set)                                             # cannot have  set  as it can be mutable


#set cannot have duplicate

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we cannot access the element in set as it is unordered
# print(my_set[0])


# we can add in set
# my_set.add({1,1,2,3,4,5,77,8,99,6})               # we can add only one item with the help of set
# print(my_set)

my_set.add(1)               # we can add only one item with the help of set
print(my_set)


my_set.update({1,1,2,3,4,5,77,8,99,6})               # we can add only one item with the help of set
print(my_set)

# my_set.update((1,1,2,3,4,5,77,8,99,6))               # we cannot add set tuple in the set
# print(my_set)


my_set = {1, 3, 4, 5, 6}
my_set.discard(2)                              # it will not give and error
my_set.remove(3)                                   # remove the specific item
print(my_set)


#pop()   # remove the arbitary item in the set
#clear() for claering the set

print(my_set.pop())
print(my_set.clear())

print("--"*50)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


a= A.copy()
print(a)

print(A.union(B))
print(A|B)                               #  "|"  == union

# any one can be true here A will be printed
print(A or B)

print(A and B)      # last option is true then last one is printed



# intersection  ==  " & "   " intersection "
# it will print coommon element inn the set
print(A & B)
print(A.intersection(B))

# set difference  A-B

# set symmetric diff  a-b- ab(common)

## add 1 item and update add the iterable

# mremebership operation
print(1 in A)
print(1 not in A)



