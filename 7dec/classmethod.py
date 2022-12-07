## The classmethod() method returns a class method for the given function.

from datetime import date

class Child:

    def __init__(self, name,age):
        self.age = age
        self.name = name

    @classmethod
    def birthyearoffather(cls,name,birthyear):
        return cls(name , date.today().year -birthyear)

    def show(self):
        print(self.name+"'s age is :"+ str(self.age))
obj1 = Child("Anil",18)
obj2 = Child.birthyearoffather("Rinku",1970)
obj2.show()