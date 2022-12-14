# def fib(n):    # write Fibonacci series up to n
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
#
# def fib2(n):   # return Fibonacci series up to n
#     result = []
#     a, b = 0, 1
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result


# a = [x if x%2==0 else x+1  for x in range(10) ]
# print(a)
#
#
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)



# a= "W*lco*eto*ung*e"
# b="emjl"
# for i in a :
#     if i == "*":
#         a=a.replace(i,b[0],1)
#         b= b.replace(b[0],"")
#         print(a)
# print(a)


c = [i for j in "emjl" for i in "W*lco*eto*ung*e"  if i == "*" i=j   ]
print(c)


# c = [i for i in "W*lco*eto*ung*e" if i == "*"  ]
# print(c)
#
# c = [i for i in "W*lco*eto*ung*e"  ]
# print(c)