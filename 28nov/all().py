''' The all() function returns True if all elements in the given iterable are true. If not, it returns False.'''



boolean_list = ['True', 'True', 'True']                          #here string so true elses

# check if all elements are true
result = all(boolean_list)
print(result)


boolean_list = [True, 'True', 'True']                         # of not string then ehe value is od

# check if all elements are true
result = all(boolean_list)
print(result)




# empty iterable
l = []
print(all(l))                                              # empty iterable is True in all()


