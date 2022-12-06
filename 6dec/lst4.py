## Test if List contains elements in Range

lst = [4, 5, 6, 7, 3, 9]
start = int(input("enter the starting number :"))
end = int(input("enter the ending number :"))
while start<end:
    break
else:
    print("start is smaller then end ")
    quit()
lst2= []

for i in range(start,end):
    if i in lst:
        lst2.append(i)
print(lst2)