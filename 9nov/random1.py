
'''''import random
There are various functions associated with the random module are:

random()
randrange()
seed()
randint()
uniform()
choice()
shuffle '''''

import random
i=1
while i<10:
    print(random.random())
    if i==5:
        break
    i+=1

'''''Example 2 '''''
print("Example 2")

i=1
while i<10:
    random.seed(10)
    print(random.random())
    if i==5:
        break
    i+=1
