class Trootech:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name
        print(self.name)


obj = Trootech("Harsh")
print(obj.name)
obj.get_name()
obj.set_name("amit")

