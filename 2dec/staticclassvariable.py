class Student:
    strem = "CSE"

    def __init__(self,name, age ):
        self.name = name
        self.age = age

obj1= Student("Amit",25)
obj2 = Student("K.T",26)
print(obj1.name)
print(obj2.name)
print(obj2.age)
print(obj1.age)
print(obj1.strem)
print(obj2.strem)
obj2.strem="computer"                          # for overall class we have to change the  variable with the help of class name
print(obj2.strem)
print(obj1.strem)
print()