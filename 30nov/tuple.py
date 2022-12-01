tempTuple = ('Welcome', 'to', 'interview', 'bit.', 'Have', 'a', 'great', 'day', [1, 2, 3])
print(tempTuple[0])                             # tuple is ordered

#print(tempTuple[0].remove())         # we cannot remove item

# print(tempTuple.pop())


print(tempTuple[2])                # we can access the element in the tuple
print(tempTuple[-2])               #negative indexing

print(tempTuple[2:5])
print(tempTuple[2:55])         # range we can find  if range exists then it will

print(tempTuple[:4])

#we cannot change the tuple but we can turn it into list and then we can change

#unpack the tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

(green, tropic, *red) = fruits
print(green)
print(tropic)
print(red)

third_tupele = fruits + tempTuple
print(third_tupele)

print(third_tupele.count("apple"))
print(third_tupele.index("mango"))