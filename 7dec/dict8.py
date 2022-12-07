## Convert Lists of List to Dictionary

test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

result = dict()
for item in test_list:
    result[tuple(item[:2])] = tuple(item[2:])
print(result)