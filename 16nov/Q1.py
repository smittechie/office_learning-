from collections import Counter

# Remove all duplicates words from a given sentence

Input = "Python is great and Java is also great"

def Q1():
    Input = "Python is great and Java is also great"
    Input= Input.split()

    uniquee = Counter(Input)

    s = " ".join(uniquee.keys())
    print(s)
Q1()

def Q2():
    Input = "Python is great and Java is also great"
    uniiquee= set(Input.split())
    uniiquee  = " ".join(uniiquee)
    print(uniiquee)
Q2()

def Q3():
    Input = "Python is great and Java is also great"
    words = Input.split()
    dicti= dict.fromkeys(words)
    uniquee = " ".join(dicti.keys())
    print(uniquee)
Q3()

