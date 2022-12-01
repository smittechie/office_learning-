''' The any() function returns True if any element of an iterable is True. If not, it returns False '''


boolean_list = ['True', 'False', 'True']
print(any(boolean_list))

##syntax
# any(iterable)


d = {'0': 'False'}              #in dictionary keys are considered
print(any(d))


d = {0: 'False'}                #interger having 0 value in key is  considered false
print(any(d))