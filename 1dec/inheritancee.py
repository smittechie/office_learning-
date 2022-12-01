class Person(object):
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self.name)

    def isEmployee(self):
        print( False )

class emp(Person):
    def isEmployee(self):
        return print(True)

a= Person("alan")
a.isEmployee()
a.show()


b = emp(120000)
b.show()
b.isEmployee()


print("-"*50,"multi-level","-"*50)

class Base(object):
    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age = age

    def getage(self):
        return self.age

class Grandchild(Child):
    def __init__(self,name, age,address):
        Child.__init__(self, name, age)
        self.address = address

    def getaddress(self):
        return self.address

obj = Grandchild("smit",12,"adi")
print(obj.getname(),obj.getage(),obj.getaddress())


print("-"*50,"multiple","-"*50)

class A:
    def __init__(self):
        self.str1 = "Trootech"
        print("Accessed class A")

class B:
    def __init__(self):
        self.str2 = "Business"
        print("Accessed class B")


class Dervied :
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Derived")

    def pristr(self):
        print(self.str1,self.str2)

objj= Dervied()
objj.pristr()