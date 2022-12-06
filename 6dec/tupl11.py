## Multiply Adjacent elements

test_tup = (1, 5, 7, 8, 10)

result = tuple( i*j for i , j in zip(test_tup,test_tup[1:]))
print(result)