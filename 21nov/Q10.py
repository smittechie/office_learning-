#WAP to convert 2 lists to a dictionary.

lst1= [1,2,3,4,5,6,7]
lst2= ["a","b","c","d","e","f","g"]

dictinary = {}
a = dict(zip(lst2,lst1))
print(a)

#method 2
for key in lst2:
    for value in lst1:
        dictinary[key]= value
        lst1.remove(value)
        break
print(dictinary)


#methos 3

lst1= [1,2,3,4,5,6,7]
lst2= ["a","b","c","d","e","f","g"]

rest = {lst2[i] : lst1[i] for i in range(len(lst1))}
print(rest)
