from collections import Counter
##count unique values inside a list

lst = [1, 2, 2, 5, 8, 4, 4, 8]

#method1
a = set(lst)
print(len(a))

#method2
b = Counter(lst)
print(len(b.keys()))

# mehod3
lst2= []
count = 0
for i in lst:
    if i not in lst2:
        count+=1
        lst2.append(i)
print(count)