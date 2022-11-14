print("\n example 1 \n")
'''''public '''

class A:

    def __init__(self):
        self.a = 2

    def Base(self):
        print("abc")

    def Derived(self):
        print("dervied")
        c= self.a
        print(c)

b = A()
d = A()
b.Base()
b.Derived()
b.a
print(d.a)



'''''practice question '''
print("\n example 2 \n")


class Foo:
    static_var = 'every instance has access'

    def __init__(self,name):
        self.instance_var = 'I am %s' % name

    def printAll(self):
        print ('self.instance_var = %s' % self.instance_var)
        print ('self.static_var = %s' % self.static_var)
        print ('Foo.static_var = %s' % Foo.static_var)

f1 = Foo('f1')
f1.printAll()
f1.static_var = 'Shadowing static_var'
f1.printAll()

print("\n")

f2 = Foo('f2')
f2.printAll()
Foo.static_var = 'modified class'

print("\n")
f1.printAll()
f2.printAll()



'''''practice question '''
print("example 3")


a = (1,2,3,[6,7,8],9)
print(a)
print(a[3])
a[3][1]=22
print(a[3])             # can change the internal element of list in tuple


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("\n example 4 \n")
''''' Protected '''''

class Base:
    def __init__(self):
        self._a = 2


class Derived:
    def __init__(self):
        Base.__init__(self)
        print("calling protected member  of base class ",self._a)

        #modify the protected variable
        self.__a = 3
        print("Calling modified protected member outside class: ",self._a)
class Check:
    def __init__(self):
        self.b=5


obj3=Check()
obj1= Base()
obj2 = Derived()

print("Accessing protected member of obj1: ",obj1._a)
print("Accessing protected member of obj2:",obj2._a)
