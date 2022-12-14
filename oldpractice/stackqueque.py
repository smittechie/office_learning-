## impelemtation using list

#stack=[3,4,5,8,9]

#append()
# stack.append(6)
# stack.append(7)               #append will add the value at the end
# print(stack)
#
# #pop()
# stack.pop()
# print(stack)                # removes the last element




## Implementation using collections.deque:
# from collections import deque
# mystack= deque()
# mystack.append("a")
# mystack.append("b")
# mystack.append("c")
# print(mystack)
# mystack.pop()
# mystack.pop()
# mystack.pop()
# print(mystack)


#reference pyhton documentation
from collections import deque
stack1= deque()
stack1.append("x")
stack1.append("y")
stack1.append("z")
stack1.appendleft("w")
# stack1.clear()                              #delete all the elements
#a=stack1.copy()                               #create a shallow copy
# print(a)
# print(stack1.count("x"))                      # counts the elements

stack2 = deque()
stack2.append("1")
stack2.append("2")
stack2.append("3")
# stack1.extend(stack2)                         # here extend will not work as list
# print(stack1)
# stack1.extendleft(stack2)                    # extends on the left side of the string
# print(stack1)

# print(stack2.index("2"))                     #index gives the position  with .index(2,start=2,end=4)
# stack1.insert(2,"yup")                        # it will insert into the postion which we mentioned insert(postion,value)
# print(stack1)
# print(stack1)
# stack1.pop()                                      # deletes the left most side of elements
# print(stack1)
# stack1.popleft()                                   # delete left side of the elements
# print(stack1)

# stack1.remove("y")
# print(stack1)                              # removes the 1st element of the stack

# print(stack1)
# stack1.reverse()                        # reverse the stack
# print(stack1)

# print(stack1)
# stack1.rotate(-2)                      #here the elements are rotated not the queue is rotated
# print(stack1)

stack1.extendleft("vutsr")                   # extends on left
print(stack1)


## Implementation using queue module
# from queue import LifoQueue
# my_stack = LifoQueue(maxsize=3)
# print(my_stack.qsize())

# my_stack.put('a')
# my_stack.put('b')
# my_stack.put('c')
# print(my_stack.qsize())
# print('checkking whather queue is full or not ?' ,my_stack.full())
#
# print(my_stack.get())
# print(my_stack.get())
# print(my_stack.get())
#
# print("cehck is empty or not ?",my_stack.empty())



