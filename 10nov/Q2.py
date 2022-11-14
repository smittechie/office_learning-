#WAP to Capitalize first character in given string and also capitalize each word first letter in string : (at least 2 solution are required)
'''''
Ex :
Input : “hello word”
Output : Hello Word
input : today is a great day
Output: Today Is A Great Day
'''''
a = str(input("enter the letter with space"))
d =[]
str1=""
for ele in a:
    c=ele.title()
    d.append(c)
print(str1.join(d))