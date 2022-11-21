## WAP to create a matrix n*n with all value is 1 and replace the all diagonal elements with “#”


# n = int(input("enter the nuimber ; "))
# a = [[j for j in range(n) ] for i in range(n)]
# print(a)

import numpy as np

A =np.array([[1, 2, 3],
    [4, 5, 6],
    [7 ,8, 9]], dtype= str)

np.fill_diagonal(A,"#")
print(A)
