##Modification is to count the each element from a string and convert them into a dictionary.

inputt = "aarrcctret"

dictt={}
for i in inputt:
    if i not in dictt:
        dictt[i] = 1
    else:
        dictt[i]+=1
print(dictt)