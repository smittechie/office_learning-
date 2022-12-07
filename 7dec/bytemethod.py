#The bytes() method returns an immutable bytes object initialized with the given size and data.

str = "Trootechh is very good for me "

abc = bytes(str,'utf -8')
print(abc)                                   # it converts items into immutable byte object


size = 5
a = bytes(size)
print(a)