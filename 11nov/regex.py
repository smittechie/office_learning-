#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

import re

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*"*50,"search example","*"*50)
#search method
#returns a Match object if there is a match.
#If there is more than one match, only the first occurrence of the match will be returned:
# return None
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")                                      # return the values in the object form



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n","*"*50,"findall example","*"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n","*"*50,"split() Function example","*"*50)
#The split() function returns a list where the string has been split at each match:
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

txt = "The rain in Spain"
x = re.split("\s",txt)         #split(parttern, string ,maxsplit )
print(x)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n","*"*50,"sub() Function example","*"*50)
#The sub() function replaces the matches with the text of your choice:
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

txt = "The rain in Spain"
x = re.sub("\s","*",txt)                   #re.sub(item to repalce,item who will replace, string, occurance)
print(x)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n","*"*50,"Metacharacters","*"*50)
#Metacharacters are characters with a special meaning:
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''
[] =          gives a set of character                                                                          "[a-m]"  
\  =          Signals a special sequence (can also be used to escape special characters)                         "\d"
               anyr=thinf which is different in the string can be found 
               
.  =          Any character (we can pass any character in between                                               "he..o"
^  =            Starts with                                                                                     "^hello"
$  =        	Ends with	                                                                                    "planet$"
*  =        	Zero or more occurrences	                                                                     "he.*o"
+ =	            One or more occurrences	                                                                         "he.+o"
? =         	Zero or one occurrences                                                                          "he.?o"
| =            	Either or	                                                                                     "falls|stays"

'''''