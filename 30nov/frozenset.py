A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])


# besides operation like add() , update() , remove() , pop() , discard() we can perform every method of set
combined = A | B
print(combined)

combined = A & B
print(combined)


