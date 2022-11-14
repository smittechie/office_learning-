#WAP to find empty list from given list and also find the index of empty list

lst = [[], [2], [40, 0], [], [3,3]]
# count= 0
indexx= []
for i in lst:
        if i:
            indexx.append(lst.index(i))
total_items = len(lst)
c = [i for i in range(total_items) if i not in indexx]
d = len(c)

print(f"Total empty list is {d} and indexes of empty list are {c} ")



#print(c)


#(home->google->abc_video->hrportal)

# pallendrom
# fubbnioseries
# range function (using genrator)
# factorial - simple or using reccusion

# range_(1, 5)
