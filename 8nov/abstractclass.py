'''''A class is called an Abstract class if it contains one or more abstract methods.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes may not be instantiated,
and its abstract methods must be implemented by its subclasses'''

from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod
    def Gun(self):
        pass
    def Area(self):
        print("Concrete Method")

class Child(Father):
    def Gun(self):
        print("child class")
        print("Defining Abstract Meethod")

obj1=Child()
obj1.Gun()
obj1.Area()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Program 2 ")


class Defence(ABC):
    @abstractmethod
    def Area(self):
        pass
    def Gun(self):
        print("A.K-47")

class Army(Defence):
    def Area(self):
        print("Land area")

class AirForce(Defence):
    def Area(self):
        print("Air area")

class Navy(Defence):
    def Area(self):
        print("Sea area")

army= Army()
airforce=AirForce()
navy=Navy()


print()
army.Area()
army.Gun()
print()
airforce.Area()
airforce.Gun()
print()
navy.Area()
navy.Gun()