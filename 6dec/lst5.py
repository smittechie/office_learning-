####  check if the list contains three consecutive common numbers

lst= [1, 1, 1, 64, 23, 64, 22, 22, 22]

for i in range(len(lst)):
    if lst[i] == lst[i-1] == lst[i-2]:
        print(lst[i])

for i in range(len(lst)-2):
    if lst[i] == lst[i + 1] and lst[i + 1] == lst[i + 2]:
        print(lst[i])