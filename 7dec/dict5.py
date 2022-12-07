## Dictionary with maximum count of pairs

test_list = [{"gfg": 2, "best" : 4},
             {"gfg": 2, "is" : 3, "best" : 4},
             {"gfg": 2}]
temp = 0
index = -1
count = 0
for item in test_list:
    index += 1
    if len(item) > count:
        count =len(item)
        temp = index
    else:
        pass
print("the index having largest pair is  " ,temp)