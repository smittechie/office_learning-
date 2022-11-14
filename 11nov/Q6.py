#WAP to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''''Input : 'The lyrics are not that poor! 'The lyrics are poor!' 
Output: 'The lyrics are good! The lyrics are poor!
'''''

import re
a = "The lyrics are not that poor! The lyrics are poor!"
length= len(a.split())
b = ""
# for i in a.split():
#     b+=i+" "
#     if i=="not":
#         c=b.replace(i,"")
#         print(c)

# c = re.findall("not.*poor",a)
# print(c)
c = re.findall("not.*poor",a)
print(c)
# d = re.findall(r"\bnot".r"poor\b",a)
# print(d)

