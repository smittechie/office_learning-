from collections import Counter

# Remove_duplicate_values_across_Dictionary_Values


test_dict = {'Manjeet' : [1, 4, 5, 6],
            'Akash' : [1, 8, 9],
            'Nikhil': [10, 22, 4],
            'Akshat': [5, 11, 22]}

# count_values = test_dict.values()
# print(count_values)
# a= []
# for i in count_values:
#     for j in i:
#         if j not in a:
#             a.append(j)
#         else:
#             pass
# print(a)
#
# for i in count_values:
#     for j in i:
#         if j in a:
#             a.remove(j)
#         else:
#             pass
# print(count_values)

ab=[]
c=[]
for k,v in test_dict.items():
    for i in v:
        if i in ab:
            c.append(i)
        if i not in ab:
            ab.append(i)


for k,v in test_dict.items():
    print([i for i in v if i not in c])






# a =["a","a",'c','c','d','d','e']
# d= {}
# for item in a:
#   if item in d:
#       d[item]+=1
#   else:
#       d[item]=1
#
# # b = dict.fromkeys(a)
# print(d)