a="Python"
#a[1]="l"                                  ##TypeError: 'str' object does not support item assignment
# a[0:2]="ly"                              #TypeError: 'str' object does not support item assignment
#print(a)

# a="j"+a[1:]                  #other string should be created because string is immutable
# print(a)

# """fibonnaci  series """
# a , b = 0,1
# while a< 10:
#     a,b = b,a+b
#     print(a)


"""4. More Control Flow Tools"""
#
# x = int(input("Please enter an integer: "))
#
# if x< 0 :
#     print("ists a negative number")
# elif 0<=0<10:
#     print("between 0-10")


# print(range(0,10))

# alphabet = ['a', 'b', 'c']
# integers = [1, 2, 3]
# n=list(zip(alphabet, integers))
# print(n)




# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'
#
# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
#
# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")



### defining function
# def fib(n):
#     a , b = 0 , 1
#     while a < n :
#         print(a)
#         a , b = b , a+b
#     print()
#
# fib(2000)
#
# f = fib
# f(5000)


from collections import ChainMap

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4,'a': 1}
# d3 = {'e': 5, 'f': 6}

# Defining the chainmap
# c = ChainMap(d1, d2, d3)
#
# print(c)
#
# a=c.maps
# print(a)
# print(list(c.keys()))
# print(list(c.values()))






# nums = [1, 2, 3]
# nums.extend((4, 5, 6))
# print(nums)

#
# my_list = ['geeks', 'for', 6, 0, 4, 1]
# my_list.extend('geeks')
# my_list.extend(['geeks'])
# print (my_list)


from collections import Counter
# a = Counter("amit")                    #string so one by one
# print(a)
# a = Counter(["amit"])                      # list so one
# print(a)
#
# a = Counter({"amit":5,"deep":7,"pathak":9})
# print(a)
#
# a = Counter(a=12,f=34,s=64)
# print(a)
#
# print(a['a'])                            #acessinf element if not found then return 0



# a = Counter("trootech")
# for i in a.elements():
#     print(i , end="")

# a = Counter("trootech")
# print(a.most_common(2))
# print(sorted(a.elements()))           #sorted is used to acess the element


# a = Counter(amit=5,deep=7,patha=9)
# b = Counter(amit=15,deep=75,pathak=-9)
# a.subtract(b)
# print(a)
# a.total()
# print(a)

# lst1=[1,2,3,4,5]
# a= [x  for x in lst1]
# print(a)

# a = [x for x in range(1200,2000,130)]
# print(a)

# lst1=[44,54,64,74,104]
# a = [y+6 for y in lst1]
# print(a)

# lst1=[2, 4, 6, 8, 10, 12, 14]
# a = [i**2 for i in lst1]
# print(a)


"""27 oct """

"""extra  question not to print error while accessing the elements """
# mydict={"a":2,"c":4}
# print(mydict.get("b"))
# print(mydict.fromkeys("b"))


"""sets """
my_set= {1,2,3,4,5,6}
# print(my_set)
# my_set=set([1,2,4,5,6,7,6,8,5,4])                      # no duplicate allowed
# print(my_set)
#
# my_set=set([1,2,4,5,6,hi:45,6,8,5,4])                #mutalble things not allowed
# print(my_set)

# a = {}
# print(type(a))
#
# a = set()
# print(type(a))
#
# my_set= {1,2,3,4,5,6}
#
# my_set.discard(2)
# print(my_set)

# my_set=set("Hello World")
# print(my_set)
# print(my_set.pop())              # removes random elements as unordered

# myset= {(1,2,3,4,4)}                         #here the question is why tuple
# print(myset)
# myset= set()
# print(myset)


# myset = set([1,3,4,5])
# print(myset)
# myset = set((9,3,4,5))
# print(myset)
# myset = set({9,3,4,5})
# print(myset)



# set operations

a = {1,2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
# print(a|b)                           # a or b , a unioin b    , gives all the elements once
# print(a)
#print(a.union(b))


# print(a&b)                          #gives elements that are common
# print(a.intersection(b))


# print(a-b)
# print(a.difference(b))              # gives a - b

# print(a^b)                                  #xor
# print(a.symmetric_difference(b))                # removes the common elements

# a.add(9)
# print(a)
#
# a.discard(9)                           # removes the elements  or gives no error
# print(a)

# print(a.isdisjoint(b))                 # True , two sets have null intersection
# c={1,2}
# print(c.issubset(a))
# print(c.issuperset(a))

# print(a)
# x= a.pop()
# print(x)
# print(a)
#                                                      # pop is not recommended in set
# print(b)
# print(b.pop())
# print(b)


# print(a)
# a.remove(1)                         #raise error if not found
# print(a)

#update() method can take any number of arguments.        eg:A.update(B, C, D)
# anything can be updated like list tuple  set dictionary also   answer will be in set and no duplicate


# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
#
#
# import fibo
# print(fibo.fib(5000))


# for i , v in enumerate(['tic', 'tac', 'toe']):
#     print(i,v)
#


a = {1,2, 3, 4, 5}
print(a.discard("z"))