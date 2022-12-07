str = "SmitPatel"
str.casefold()
length = len(str)
firststr = str[:length//2]
secondstr =str[length//2:]

count = 0
exception ="aeiou"
for item in firststr:
    if item in exception:
        count += firststr.count(item)
print("vowels on first half are total :",count)

count = 0
for item in secondstr:
    if item in exception:
        count +=secondstr.count(item)
print("vowels on second half are total :",count)


print("--"*50)

count = 0
for i in range(0,length//2):
    if str[i] in exception:
        count+= 1
print("vowels on first half are total :- ",count)

count =0
for i in range(length//2,len(str)):
    if str[i] in exception:
        count+= 1
print("vowels on second half are total:- ", count)



print("--"*50)

for i in str[0:length//2]:
    if i in exception:
        print("first half is :",i)
for i in str[:length//2:-1]:
    if  i in exception:
        print("second half :", i)


