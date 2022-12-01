# sea_creatures = ['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone']
# for x in range(1,4):
#     sea_creatures += ['fish']
#     print(sea_creatures)


# sea_creatures =['shark', 'octopus', 'blobfish', 'mantis shrimp', 'anemone', 'yeti crab']
# del sea_creatures[1]
# print(sea_creatures)
#
# del sea_creatures[1:4]
# print(sea_creatures)


# odd = [2, 4, 6, 8]
# odd[1:4] = [3, 5, 7]                         #replacing the value
# print(odd)

# add one item with append and many item with extend



# Demonstration of list insert() method
# odd = [1, 9]
# odd.insert(1,3)
# print(odd)
#
# odd[2:2] = [5, 7]
# print(odd)


# del can delete anything from index to range of index
# remove for given item
#pop to remove item at given index

my_list = ['p','r','o','b','l','e','m']
#del my_list                                            # del remove item completely
# my_list.pop(5)                                         # element if
# print(my_list)



##  list.index(element, start, end)

# animals = ['cat', 'dog', 'rabbit', 'horse']
# index = animals.index('dog')                                 # we have to pass the element
# print(index)



# create a list
numbers = [2, 3, 5, 2, 11, 2, 7]
count = numbers.count(2)
print('Count of 2:', count)