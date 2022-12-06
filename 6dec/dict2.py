# Swapping Hierarchy in Nested Dictionaries

test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
             'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}

result = dict()
for i , j in test_dict.items():
    # print(i , j)
    for j,k in j.items() :
            # print(j, k)
        if j not in result:
            temp = dict()
        else:
            temp =result[j]
        temp[i]=k
        result[j]=temp
print(str(result))