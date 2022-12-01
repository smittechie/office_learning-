### constructor
#special method used to create and initialze an object of a class .
# self is reference to current instance of the class , it is created and passed automatically to the init when constructer is called

# parameterized consructor
# non parameterized consructor
# default consructor


##Parameterized Constructor in Python
class Family :
    def __init__(self,num):
        print("This is parametrized constructor")
        #instance variable
        self.number = num

    #instance metehod
    def members(self):
        print("the number of members are,",self.number)

obj = Family(10)
obj.members()


###Non-Parameterized Constructor
class Fruit :
    favourites = "Banana"
    def __init__(self):
        print("This is Non-parametrized constructor")
        #instance variable
        self.favourite= "apple"


    #instance metehod
    def members(self):
        print("the number of fruit are,",self.favourite)

obj = Fruit()
obj.members()
print(Fruit.favourites)


### Default Constructor in Python
#When you do not write the constructor in the class created, Python itself creates a constructor during the compilation of the program.

class Assignment:
    check = "its done "

    #method
    def is_done(self):
        print(self.check)

obj = Assignment()
obj.is_done()
print(Assignment.check)



print(50*"--")







class Animal:
    animals= "wild"


    #instance attribute(varaiale)
    def __init__(self,name,age):
        #iinstance variable
        self.name  = name
        self.age = age

    # def aa(self,name,age):
    #     self.name= name
    #     self.age = age
    #     return "abc"


    @classmethod
    def methodd(cls,breed):
        print(Animal.animals)
        Animal.animals=breed

    @staticmethod
    def temp(age):
        if age >10:
            print("then its adult ")
        else:
            print("not")


pug = Animal("TM",18)
# print(pug.aa("dog"))
print(pug.animals)
pug.temp(18)
pug.methodd("TM")
print(pug.animals)
