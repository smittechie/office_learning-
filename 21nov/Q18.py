#WAP for  function that accept the function and list values as parameters and return the appropriate answer.
'''Accepted function are : [sum , len , average , custom  function ]
Constraints : Custom function that check value is palindrome or not
'''

lst= ["aa", 2334, "4343"]
# sum1 = 0
def summ(lst):
    sum1 =0
    for j in lst:
        if type(j) == int:
            for i in str(j):
                sum1+=int(i)
            print(f"The sum of {j} is : ",sum1)

        else:
            print(f"{j}:wrong data type")

def length(lst):
    for j in lst:
        print(f"lenth of {j} is ",len(str(j)))


def averagee(lst):
    sum1 = 0
    lengthh= 0
    for j in lst:
        if type(j) == int:
            for i in str(j):
                sum1 += int(i)
                lengthh= lengthh+1
            print(f"The average  of {j} is : ", sum1/lengthh)
        else:
            print(f"{j}:wrong data type")


def custom(lst):
    for i in lst:
        if type(i) == str:
            answer= i == i[::-1]
            print(f"the string is: {answer} : a Palindrome ")
        else:
            print("Invalid datatype")



if __name__ == "__main__":
    custom(lst)
    averagee(lst)
    length(lst)
    summ(lst)



