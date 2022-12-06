# Modify the tuple

tuple1 = (11, [22, 33], 44,{3,4,5}, 55)
tuple1[1].append(25)
print(tuple1)
tuple1[1].pop()
tuple1[1].pop()
tuple1[1].pop()
print(tuple1)
tuple1[3].pop()
print(tuple1)
tuple1[3].pop()
print(tuple1)

#items cannot be changed but mutable things can be manipulated