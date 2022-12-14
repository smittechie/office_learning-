# tel = {}
# print(type(tel))
tel ={ 'jack':4092,'john': 9642,'snow':6302}            #method 1 to create dict
# print(tel)
# tel['arya']=8520                        #adding element in the dictionary
# print(tel)
# del tel['john']
# print(tel)
# print(list(tel))
# print('arya' in tel)
# print('snow' not in tel )

#dictionary comprehension                         # methodo 2 to create a list
# a= {x : x**2 for x in range(10)}
# print(a)

#using type constructor
# a = dict([("a",520),("b",3210),("c",430)])
# print(a)
# a= dict(one=1,two=2,three=3)
# print(a)
# a = dict(zip([1,2,3],["one","two","three"]))
# print(a)

a = dict({"to":2,"thrie":3,"char":4})
# print(a)
# print(list(a))                                         # list return all the keys
# print(len(a))                                           # give  the number of list in dictionary
# print(a["char"])
#
# a["to"]=22                                           # to change the value of the value by using key
# print(a)

# del a["to"]
# print(a)                                           #deleted an item
# a["to"]=2
# print(a)                                            # added an item

# print("to" in a )
# print("to" not in a )

# a.clear()
# print(a)

# a.copy()                                  # return a shallow copy
# print(a)

# print(a.get("to"))                        # takes a key and return back the value

# print(a.items())
# print(a.keys())
# print(a.pop("to"))                          # pop will delete the value
# print(a)
# print(a.popitem())                              # last item deleted
# print(a)
# v=dict(reversed(list(a.items())))
# print(v)                             # reversed is done  by converting in list then reversed thelist and then dicrt

# a.setdefault("to",3)                         # if the key already exists then it will show the old value else new value
# print(a)
#
# a.update({"panch":5})                           # overriding can be done and new items can be added
# print(a)

# print(a.values())
# print(a.keys())
# print(a.items())

# print(a.fromkeys())              #The fromkeys() method returns a dictionary with the specified keys and the specified value.
                                 #dict.fromkeys(keys, value)
"""
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)"""


## Looping Techniques DICTIONARY

# got = {"ya":2,"snow":3}
# for k,v in got.items():
#     print(k,v)



# # enumerate function
# l1= ["eat","sleep","code"]
# l2="Trootech"
# print(list(enumerate(l1)))
# print(list(enumerate(l2)))

# for x in enumerate(l1):
#     print(x)
#
# for count, x in enumerate(l1,200):
#     print(count,x)
#
# for count , x in enumerate(l1):
#     print(x)
#     print(count)

# for i ,v in enumerate(l1):
#     print(i,v)



# a = {"to":2,"thrie":3,"char":4}
#
# b = {"to":3,"thrie":3,"char":4}
#
# a.append(b)
# print(a)
# b["to"]=2
# # b.update(["sixx":6])
# print(b)
# print(b)
# print(a.values())
# del b
# print()


# a= "qwerty"
# leng= len(a)
# for i in range(0,leng//2):
#     if a[i] == a[leng-1-i]:
#
#         print("pallindrome")
#     else:
#         print("not")
#
# b = a[-1]
# if a ==b:
#     print("yes")
# else:
#     print("no")



"""  18   Oct """


a = {"too":2,"thrie":3,"char":4,"five":5}

b = {"to":3,"thrie":3,"char":4,"six":6}

#method 1
# dict2= a.update(b)
# print(a)

#method 2
# def funct(a,b):
# 	abc={**a,**b}
# 	return abc
# print(funct(a,b))

#method 3
# def funct(a,b):
# 	abc=a|b                                 #a or b
# 	return abc
# print(funct(a,b))


#method 4
# Driver code
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
#
# for i in dict2.keys():
# 	dict1[i] = dict2[i]
# print(dict1)
# print(dict2)


""" Q:- Sort Python Dictionaries by Key or Value"""

# a=list(set(a.keys()))
# print(a)
# print(type(a))
# b=sorted(a)
# print(b)


fruits = ['apple', 'banana', 'cherry']

fruits.remove('orange')

print(fruits)












""" keyword arguments and non keywords arguments """
# def myFun(*argv):                                      # non- keywords arguments
#     for arg in argv:
#         print(arg)
#
#
# myFun("hello","amdavad","gujarat")


# def myFun2(*nums):
#     sum=0
#
#     for n in nums:
#         sum = sum + n
#
#     print("Sum",sum)
# myFun2(2,3,4,5,6,7)
# myFun2(1298,786,67,898,8,567)
# myFun2(867,675,5656,65,4545,565757)


# def intro(**data):
#     print("the data type is ",type(data))
#
#     for keys,value in data.items():
#         print('the value of {} is {}'.format(keys,value))
#
#
# intro(only=1,one=2,ounce=3,of=4,oats=5)
# intro(banana=6,bashes=7,bimari=8)


# def myFun(**data):
#     print("the type of datatype is",type(data))
#
#     for key,value in data.items():
#         print("%s == %s" %(key,value))
#
#
# myFun(first="value",second="can",third="be",fourth="chnageable")



""" Example 1 """
# def myFun(arg1, arg2, arg3):
# 	print("arg1:", arg1)
# 	print("arg2:", arg2)
# 	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)

# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)

""" Example 2 """
# def data(*args,**kwargs):
# 	print("args",args)
# 	print("kwargs",kwargs)
#
# data("dfsa","kdfjkf","djflkdjf","jdfehf",one=1,two=2,three=3,four=4,five=5)



