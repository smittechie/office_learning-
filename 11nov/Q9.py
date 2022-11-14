#WAP to separate the different type of data type value in different list

input = ["test", 23, ["e","r"], (3,4), 3.4 ,24 ]

d ={}
for i in input:
    if type(i) not in d:
        d.update({type(i):i})
    # if type(i) in d:
    #     d[type(i)].append(i)                             # check

print(d)

