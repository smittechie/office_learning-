
''''' Topic: Duck typing
Duck typing, where the type or the class of an object is less important than the method it defines.
we do not check types at all. Instead, we check for the presence of a given method or attribute.'''''


class Bird:
    def fly(self):
        print("fly eith wings")

class Airplane:
    def fly(self):
        print("fly with fuel ")

class Fish:
    def swim(self):
        print("swims in sea ")

for obj in Bird(),Airplane():
    obj.fly()                                       # object should have that method

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''Operator Overloading'''''
#Program illustrate how  to overload an binary + operator

class A:
    def __init__(self,a):
        self.a = a

    #adding two objects  #maniooulate the magic function
    def __add__(self, other):
        return self.a + other.a

obj1=A(1)
obj2=A(2)
obj3=A("Trootech")
obj4=A(" Quixom")
print(obj1 + obj2)
print(obj3 + obj4)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''Method Overloading(No) and Method Overriding

 Method Overriding allows a subclass or child class to provide a specific implementation of a method 
 that is already provided by one of its super-classes or parent classes.'''''

class A:
    def show(self):
        print("in show A")

class B(A):
    def show(self):
        print("in show B")

obj1= B()
obj1.show()
