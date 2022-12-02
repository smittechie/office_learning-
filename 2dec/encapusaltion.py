class A:
    def __init__(self):
        self._id = 2
        self.numm= "num"
    city = "ahmedabad"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.subject = 5
class C:
    def __init__(self):
        pass


a= A()
print(a.numm)
print(a._id)
print(a.city)
b =B()
print(b._id)
print(b.city)
c=C()
#print(c.city)                      # cannot access the element as not inherited and it is in different class



### -------------------- private members---------------------------------

class Base:
    def __init__(self):
        self.a="trootech"
        self.__b = "MNC"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.c= "private"
class C:
    def __init__(self):
        pass


x= Base()
y= Derived()
z=C()
print(x.a)
print(x._Base__b)
#print(x.__b)                    # cannot access it as it is private we have to use technique
print(y._Base__b)                  # as not in herited so cant access
