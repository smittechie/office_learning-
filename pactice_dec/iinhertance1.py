class Parent:
    def __init__(self,name):
        self.name = name

    def Job(self):
        return "I do a government job "



class Child:
    def __init__(self,age):
        self.age = age

    def School(self):
        print("Hebron school")

a = Parent("Mukesh")
print(a.name)
print(a.Job())

b= Child(18)
print(b.age)
print(b.School())