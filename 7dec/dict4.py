##  Remove keys with substring values

test_dict = {1: 'Gfg is best for geeks', 2: 'Gfg is good', 3: 'I love Gfg'}
sub_list = [ 'love','good']

#method 1
res = dict()
for key, val in test_dict.items():
   if not any(ele in val for ele in sub_list):
       res[key] = val

print(str(res))



# method 2
lst= []
for key,item in test_dict.items():
    for ele in item.split():
        if ele in sub_list:
            lst.append(key)
del test_dict[lst[0]]
del test_dict[lst[1]]
print(test_dict)