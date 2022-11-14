class Computers:
    def Comp1(self):
        print("i5","intel","gen12")


'''''device1=Computers()
     Computers.Comp1(device1)
     #this is the old method of class calling'''''
device1=Computers()
device1.Comp1()


print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Example 1 '''''
class Car:

    wheels ='4'                                  # class variable

    def __init__(self):
        self.mil =10
        self.com ="amw"                       #instance variable

car1=Car()
car2 = Car()

print(car1.mil,car2.com)
print(car2.wheels)
car2.wheels=5
print(car2.wheels)
car2.mil =20
print(car2.mil)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Example 2 '''''
print("class method and static method")
class Student:

    school ="Trootech"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def aveerage(self):
        print(self.m2+self.m1+self.m3/3)

    @classmethod
    def info(cls):
        return cls.school                                # class method

    @classmethod
    def average(cls,m1,m2,m3):
        return cls(m1,m2,m3)

    @staticmethod
    def getinfo():                                      # static method
        print("checking the static method ")


obj3=Student.average(20,30,40)
obj3.aveerage()

obj1=Student(20,23,65)
print(obj1.m1)
obj2=Student(12,21,42)
print(obj2.aveerage())
print(Student.info())
print(Student.getinfo())


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Example 3 '''''

print("Example 3 :inner class method")



class Students:
    def __init__(self,rollno,marks):
        self.rollno=rollno
        self.marks = marks
        self.lap =self.Laptop()


    def show(self):
        print(self.rollno,self.marks)

    class Laptop:
        def __init__(self):
            self.company = "HP"
            self.ram = "8 GB"
        def show(self):
            print(self.ram,self.company)

obj1= Students(10,99)
obj2= Students(10,98)
obj1.show()


lap1 = Students.Laptop()
lap1.show()



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Example 4 '''''
print("Example 4 \n")

'''''Inheritance'''''

class A:
    def fun1(self):
        print("Function 1 is working ")
    def fun2(self):
        print("Function 2 is working ")

class B(A):
    def fun3(self):
        print("Function 3 is working")
    def fun4(self):
        print("Function 4 is working ")

class C(B):
    def fun5(self):
        print("Functioin 5 working")

obj1= A()
print(obj1.fun2())

obj2 =B()
print(obj2.fun1())

obj3=C()
print(obj3.fun5())


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Example 5 '''''
print("Example 5 \n")
'''''Constructor in Inheritance'''''

class A:
    def __init__(self):
        print("in A init")
    def fun1(self):
        print("Function 1-A is working ")
    def fun2(self):
        print("Function 2 is working ")

class B:
    def fun1(self):
        print("Function 1-B is working")
    def fun4(self):
        print("Function 4 is working ")
    def __init__(self):
        print("in B  init ")
#obj1= B()

class C(A,B):
    def __init__(self):
        super().__init__()                                     # Method Resolution Order
        print("In C init")

obj3 = C()
obj3.fun1()
