## Sort Dictionary key and values List

test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}
res = dict()
for i,j in sorted(test_dict.items()):
    j.sort()
    res[i]= j
print(res)


## method 2
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])
print("The sorted dictionary : " + str(res))