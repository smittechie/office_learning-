#Counting the frequencies in a list using dictionary in Python

Input = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

freq={}
for item in Input:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]= 1
print(freq)

