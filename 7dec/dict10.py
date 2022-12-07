## Maximum record value key in dictionary

test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}

summ =0
index = 0
for i,j in test_dict.items():
    a = sum(j.values())
    if summ <a:
        summ =a
        index =  i
print(index)