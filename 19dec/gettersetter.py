class Trootech:
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):
        print("Getter metehod ")
        print(self.name)

    @get_name.setter
    def set_name(self, name):
        self.name = name
        print("setter called ")
        print(self.name)

    @get_name.deleter
    def deel(self):
        print("Deleter ")
        del self.name

obj = Trootech("Harsh")
# print(obj.name)
# obj.get_name
obj.set_name="amit"
# obj.get_name
del obj.deel