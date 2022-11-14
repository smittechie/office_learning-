# def fun1():
#     a = int(input("enter the number between 0-6: "))
#     b = 0
#     b =a+b
#     while b < 30:
#         fun1()
#     else:
#         print(a)
# fun1()
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def summation(a,sum):
    return a + sum

if __name__=="__main__":
    sum=0
    while (sum < 30):
        a = int(input("please throw the dice : "))
        sum= summation(a, sum)
    print(sum)




