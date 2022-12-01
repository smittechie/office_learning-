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
