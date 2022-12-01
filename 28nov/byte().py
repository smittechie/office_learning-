#  The bytes() method returns an immutable bytes object initialized with the given size and data.
'''  byte return an object which is immutable  '''


string = "Python is interesting."
arr = bytes(string, 'utf-8')
print(arr)


size = 5
arr = bytes(size)
print(arr)
