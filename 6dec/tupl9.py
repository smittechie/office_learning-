##  Sum of tuple elements

tup = (5, 20, 3, 7, 6, 8)
items = list(tup)
ans = sum(items)
print(ans)

tupl = ([7, 8], [9, 1], [10, 7])
a=sum(list(map(sum,list(tupl))))
print(a)