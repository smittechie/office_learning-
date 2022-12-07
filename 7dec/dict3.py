## Code to demonstrate working of Extract Key's Value, if Key Present in List and Dictionary

# initializing list
test_list = ["Gfg", "is", "Good", "for", "Geeks"]

# initializing Dictionary
test_dict = {"Gfg": 2, "is": 4, "Best": 6}

K ="Best"
result = None
if all(K in sub for sub in [test_dict,test_list]):
    result = test_dict[K]
print(str(result))




''' Failed '''
# for i in test_list:
#     if i == test_dict.keys():
#         print(test_dict[i])
#     else:
#         # print(i)
#         pass