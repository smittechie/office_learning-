# def scope_test():
#     def do_local():
#         spam = "do local "
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = " do non local"
#
#     def do_global():
#         global spam
#         spam = "do global"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)

def fun1():
    x = "john"
    def fun2():
        nonlocal x
        x = "cena"
    fun2()
    return x
print(fun1())


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r)


# class Dog:
#     food = "magrain"
#
#     def __init__(self,breed,color):
#         self.breed = breed
#         self.color = color
#
#
# d = Dog('labra','mudy')
# print(d.breed)
# print(d.food)


""" 28 oct """


# class student:
#     school = "Universal Public School"
#     batch = "2020-2021"
#
#     def __init__(self, name, std, roll_no):
#         self.nm = name
#         self.std = std
#         self.rl_no = roll_no
#
#     def getData(self):
#         print("Student name: ", self.nm)
#         print("Standard: ", self.std)
#         print("Roll number: ", self.rl_no)
#
#     # def setData(self, name, std, roll_no):
#     #     self.nm = name
#     #     self.std = std
#     #     self.rl_no = roll_no
#
#
# print("The school name is: ", student.school)
# print("The batch year is: ", student.batch, "\n")
#
# stud = student("Om", "4th", 9)
# stud.getData()
# print()  # to print a new line in between
# stud_1 = student("Hari", "5th", 14)
# stud_1.getData()



######example

# class Student:
#
#
#     name = "jane"
#     std = "6th"
#
#
# student1 = Student()  # object
#
# print(student1.name)





# example
# class Dog:
#      def __init__(self):
#          self.legs =4
#
# tomita = Dog()
# print(tomita.legs)


# single level inheritance

# class Dog:
#
#     def speak(self):
#         print("labradore")
#
# class Dogs(Dog):
#     def bark(self):
#         print("barking")
#
# a=Dogs()
# print(a.bark())
# print(a.speak())
# d=Dog()
# print(d.speak())





#constructor base  inhertance
# class Dog:
#     def __init__(self):
#         self.AB = "abc"
#     def speak(self):
#         print("labradore")
#
# class Dogs(Dog):
#     def __init__(self):
#         self.CD = "def"
#     def bark(self):
#         print("barking")
#
# class Dog3(Dogs,Dog):
#     def __init__(self):
#         self.EF = "ghi"
#     def pet(self):
#         print("trueeee")
#
#
# a=Dog3()
# print(a.EF())
# print(a.speak())
# print(a.pet())






#multi level inheritance
# class Dog:
#     def speak(self):
#         print("labradore")
#
# class Dogs(Dog):
#     def bark(self):
#         print("barking")
#
# class Dog3(Dogs):
#     def pet(self):
#         print("trueeee")
#
#
# a=Dog3()
# print(a.bark())
# print(a.speak())





#multiple inheritance
# class calculation1 :
#     def addition(self,a,b):
#         return a+b
#
# class calculation2:
#     def mutlplication(self,a,b):
#         return a*b
#
# class calulation3(calculation1,calculation2) :
#     def division(self,a,b):
#         return a/b
#
# x = calulation3()
# print(x.addition(5,8))
# print(x.mutlplication(8,7))



""" Method overriding """

# class Bank:
#     def roi(self):
#         return 10
#
# class sbi:
#     def roi(self):
#         return 7
#
# class icici:
#     def roi(self):
#         return 8
#
# a = Bank()
# b= sbi()
# c = icici()
# print(a.roi())
# print(b.roi())
# print(c.roi())



# class person(obj):
#
#     #constructor
#     def __init__(self):
#         self.name = name
#         self.id = id
#
#     def Display(self):
#         print(self.name ,self.id)
#
# emp= person("satyam",35)
# rint(emp)