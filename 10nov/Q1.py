#WAP to Find the element that are occur more than once in given string and count the number of elements :

a='aarrarnc'
# num = list(set(a))
# c=len(num)
# print(c)

sum = 0
repeated_element = []
for i in num:
    if a.count(i) >1:
        repeated_element.append(i)
    if 1 < a.count(i):
        sum += a.count(i)
print(f"the repeated value are{repeated_element}and their sum is ",sum)
    # print(i,a.count(i))
