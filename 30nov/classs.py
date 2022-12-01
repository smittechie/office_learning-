'''@classmethod means: when this method is called, we pass the class as the first
argument instead of the instance of that class (as we normally do with methods).
This means you can use the class and its properties inside that method rather than a particular instance.'''


class Animal:

    #class attribute
    attr1="mammal"
    attr2="dog"

    #A sample method
    def fun(self):
        print("I am a",self.attr1)
        print("I am a",self.attr2)

#instantiating the class
Rodger = Animal()

#accessing the class attribute
print(Rodger.attr1)


#acessing the method attribute
Rodger.fun()


'''------------------------------------------------------------------------------------------------------------------'''

print(50 *"--")

class Dog:
    def __init__(self,breed ):
        self.breed = breed

a = Dog("pugg")
print(a.breed)
'''------------------------------------------------------------------------------------------------------------------'''
print(50 *"--")

class Dog:
    def __init__(self ):
        self.breed = "breed"

a = Dog()
print(a.breed)

'''------------------------------------------------------------------------------------------------------------------'''
print("----Q1",50 *"--")

class Dog:

    #class attribute
    commonbreed= "pitbull"

    def __init__(self,breed,colour):

        # instance varaible
        self.breed = breed
        self.colour = colour

#class object
a = Dog("labra","red")
b = Dog("bulldog" , "brown" )

print(a.breed)
print(b.breed)
print(a.commonbreed)
print(Dog.commonbreed)

