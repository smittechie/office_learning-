### Print all Possible Combinations from the three Digits


lst = [2,3,4]

for i in lst:
    for j in lst:
        for k in lst:
            if i == j == k :
                continue
            else:
                print(i,j,k)
print("--"*50)
for i in lst:
    for j in lst:
        for k in lst:
            if (i != j and j != k and i != k):
                print(i,j,k)