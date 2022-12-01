from datetime import date

class Person:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    @classmethod
    def datewithyear(cls,name,birthyear):
        return cls(name, date.today().year - birthyear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


    @classmethod
    def addtionafun(cls,name,hobbies,):
        print(f"{name} likes to {hobbies}")


person = Person("Major Ram",29)
person.display()

person = Person.datewithyear("Major shiyam",1988)
person.display()

person =Person.addtionafun("Lt. aghora" ,"watch sunset")
