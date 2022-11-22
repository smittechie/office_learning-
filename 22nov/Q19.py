'''Modify the program 14 and expected output must be like mentioned below. (accept only odd number)
Output 1:
# , 1 #
1 ,# ,1
#, 1 ,#
'''

import numpy as np
A= np.array([[1,2,3],
            [4,5,6],
            [7,8,9]],dtype=str)
np.fill_diagonal(np.fliplr(A),"#")
np.fill_diagonal(A,"#")
print(A)