# Create Nested Dictionary using given List

test_dict = {'Gfg' : 4, 'best' : 9}
test_list = [8,2]

for i  in test_list:
    a= zip(test_list,test_dict.items())
    print(dict(a))
