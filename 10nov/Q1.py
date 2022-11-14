#WAP to Find the element that are occur more than once in given string and count the number of elements :

a='aarrarnc'
num = list(set(a))
c=len(num)
print(c)

for i in num:
    print(i,a.count(i))
