# squares = [ 1,23,4,5,34,6]
# print(squares)
# print(squares[0])                                                 # here items are accessed
# print(squares[-1])                                          # indexing return a item
# print(squares[:-3])                                        #slicing return a list
# print(squares[:])                                         #slice returns a shallow copy of the list
# squares+=[36, 49, 64, 81, 100]
# print(squares)


# cubes = [1,8,27,65,125]                              #lsit is mutable type
# # cubes[3]=64                                        #replacing wrong value
# #print(cubes)
# cubes.append(216)                                   # can add element by using append at end
# print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters[2:5]=["1","2","3"]                         # assigning new value through slicing
# print(letters)
# letters[2:5]=[]
# print(letters)
# letters[:] = []                                        # delete the elements  through slicing
# print(letters)

print(len(letters))                                  # len used to know length

#nested list
e = [1,2,3,4]
f = ["a","b","c","d"]
x = [e, f]
print(x)
