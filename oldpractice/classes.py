class Mobile:
    def __init__(self):
        self.Model="Apple14Pro"
    def show_model(self):
        print('Model:',self.Model)

Apple=Mobile()
print(Apple)

class Mobile2:
    def __init__(self,m):
        self.model= m
    def Show_model(self):
        print("Model",self.model)

Apple2=Mobile2(" Apple 14 pro max")
print(Apple2.Show_model())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("-"*80)
print("Example 1 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class MyClass(object):
    def show(self):
        print("I am good")

obj1=MyClass()
obj1.show()



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("-"*80)
print("Example 2 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class MyClass:
    def show(self):
        print("I am good")

obj1=MyClass()
obj1.show()


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("-"*80)
print("Example 3 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''examaple 3'''''
class Mobile:
    def __init__(self):
        self.model ="3s prime"

    def Myphone(self):
        print("My phone is of redmi",self.model)

a = Mobile()
a.Myphone()
print(a.model)
a.model="Apple15pro"
print(a.model)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("-"*80)
print("Example 4 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''examaple 4'''''

class Mobile:
    def __init__(self,m):
        self.model=m

    def Phone(self,Model):
        self.version=Model
        print("the model is ",self.model ,"the version is ",self.version)

a = Mobile("420")
a.Phone("X2")
print(id(a))

b =Mobile("520")
b.Phone("q7")
print(id(b))

c =Mobile("620")
c.Phone("R8")
print(id(c))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("*" *50 )
print("Example 5 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@staticmethod
def f1(x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g
a=C()
c=a.f(5,4)
print(c)

print(__name__)