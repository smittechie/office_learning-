class Parent:
    def __init__(self,name):
        self.name = name

    def Job(self):
        return "I do a government job "

class Child1(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def School(self):
        return f'{self.name} is in DPS school'

class Grandchild(Child1):
    def __init__(self,name,age,hobby):
        super().__init__(name,age)
        self.hobby = hobby

    def printname(self):
        print(self.name,self.age,self.hobby)


a = Parent("Mukesh")
# print(a.name)
# print(a.Job())

b1= Child1('Mike',18)
print(b1.age)
print(b1.School())
print(b1.Job())

c= Grandchild("Amit",25,"sleeping")
c.printname()
print(c.School())
print(c.Job())












# class Child2():
#     def __init__(self,name,age):
#         super.__init__(name)
#         self.age = age
#
#     def School(self):
#         print("DPS school")


# b2= Child2("Nike",18)
# print(b2.age)
# print(b2.School())