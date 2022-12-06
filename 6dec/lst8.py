## Remove Consecutive K element records

lst= [1,1,2,3,4,2,1,3,4,5,6,7,8,8,2]
n = int(input("Enter the given  number :"))
# b = str(lst)
# lst2= b.split(",",4)
# print(lst2)



end = len(lst)
for i in range(0, end,n):
    x = i
    print(lst[x:x+n])

