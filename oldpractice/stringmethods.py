# # print("yes")
# tax = 202.10 / 2
# price = 11.23565
# a = price* tax
# print(a)
# print(round(a,2))
#
#
#
# #floor function fractioanl part
# print(17 // 2)
#
# #return reminder
# a=14%4
# print(a)
#
# #power function
#
# a= 3 ** 4
# print(a)
#
# #round function   (by default zero )  round(number,digits)
#
# x = 3545.23545
# print(round(x,4))
#
#
#
#
#
# ##  Strings
#
# # comments
# """"   each and everthing in between is comments  """
# # double slash also as
#
# #escape sequence
#
# print('doesn\'t' )     #slash to escape next block
# print("doesn't" )   # we can use single quotes inside  and double quotes outside
# print('"Isn\'t," they said.')    # here print will remove the slash in the output while idle will not
# print("C:\some\name")
# print(r"C:\some\name")    #here we used r i.e= raw string method
#
#
# #string conacatination  (+)
# a = "fdfdsf"
# b = "jsdfhs"                         #############      question solved    #can we add 2 obj
# print( a + b)
#
# a = 'i m ' 'groot'
# print(a)
#
# #  to break long strings:
# text = ('Put several strings within parentheses'
# 'to have them joined together.')                                 ##  question solved
#
# print(text)
#
# # String indexing
# yasureweareright = 5
# jhedjan = 10
#
# eg = yasureweareright                 # variable ko variable mei store kiya hai yaha
# eg2 = jhedjan                         # define nahi kiya hai ki ye hai kya variable hai ya string
#
# print(eg+eg2)
#
#
# eg = 'yasureweareright'
# print(eg[5])
# print(eg[-5])
# print(eg[5:-5])
# print(eg[-5:])
# print(eg[::-1])
#
# #  string length
# s = "i am groooot "
# print(len(s))
#

# string Methods
str = "i am Groooooot "
print(str.capitalize())              # here first block is converted into capital
print (str.casefold())              # all word will be in small case
print(str.center(16))                           # here mmovement is done after the length of the string  exceds
print(str.count("o",4,12))            # here first which string ypu hve to count and then from where ,then to where
print(str.endswith("m",2,8))           # true or false will be returned

str2 = "i \t am \t Groooooot "
print(str2.expandtabs(3))           # expand tabs requires  \t   and then the space you required  should be pass inparameter

print(str.find("o"))                # this gives the postion of the letter which ever first found
print(str.find("o", 8,10))

print('Py' in 'Python')

print(str +'{}'.format('good'))

a = {'x': "good", 'y': 'example'}
# Use of format_map() function
print('{x} {y}'.format_map(a))                     # this is used for mapping of dictonary

print(str.index('am',2,17))            #same as find but raises value error
str3 = "iamGroooooot 45"
print( str3.isalnum())             #check the alphnmeric string wheather their is one number or not else return false
str3 = "iamGroooooot"
print( str3.isalpha())              # check for alphabet only
print(str3.isascii())              # return true if the value is inncluded in ascii
print(str3.isdecimal())            #strict decimal is checked if not then false
str3 = "a34343"
print((str3.isdigit()))             #check for digit
print("/n")
print(str.isidentifier())
print(str2.isidentifier())
print(str3.isidentifier())
print("")
str4 = "IamGroooooot"
print(str4.islower())                # check wheather the string has all lower case or not
print(str4.isnumeric())
print(str4.isprintable())
print()
print(str4.isspace())              # check all the whitespaces if their then true
print(str4.istitle())              #check the title type style ie first cahrcater should be capital
print(str4.isupper())              # all should br upper cse then only true else false
str5 = [ "hi", "hello" ,"saru" ,"saras"]
print(",".join(str5))
str6 = "ya sure"
print(str6.ljust(7,"k"))                # same here jitne ki dtring hai usk baad operation q ho raha hai
str6= "  I   am  Grootttttttt    "
print(str6.islower())                     # return  T or F according to; condition
print(str6.lstrip())                   # left side trimm
str7 ="thhiiskrk"
print(str7.partition("iis"))            #breaks the string into part which ever we want to seprate
print(str7.removeprefix("thh"))        #prefix mens first removed 1st prefix
print(str7.removesuffix("krk"))        #suffix means last part
print(str7.replace("h","r"))           #replacing string having h with r
print(str7.replace("h","r",1))         #same ab above just hov many time we have to change is mentioned
print(str.rfind("o"))                  # gives the right most postion or the last most
print(str.rindex("o"))                 #same as r find just return the error value if not found
print()

print(str.rjust(50,"0"))              #right side swift is done
print(str.rpartition('o'))            # partion breaks string in 3 parts and this will give the right most answer
print(str6.rstrip())                  # strip the right most part of the string
print()
print(str.split("o",maxsplit=2))      #split the string by passing the parameter
print()

str8 = "ya \n man \n we \n are \n right "
print(str8.splitlines())
print(str8.startswith("y",0,7))           #string which starts with is searched  snd T or F is returened

str9 ='abcddcba D'
print(str9.strip('ac'))                  # strip means removing of prefix and suffic only not in middle of it
print(str9.swapcase())                    # convert upper into lower and vice versa
print(str9.title())                       #here first and after whitespace  are converted into capital
print(str9.upper())                      # copy & make string in upper case
print(str9.zfill(15))                  # zerofill fill the empty space in the string

str10 = "yayauarealwaysright"
a = "nono"
b = "yaya"
tablee= str10.maketrans(a,b)                           # we have to use maketrans to make the swap and then
print("traslation string:", str10.translate(tablee))    # here we will translate the string
