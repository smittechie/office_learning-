'''''Public '''''

class A:
    def xyz(self):
        print("hi")

class B:
    def abc(self):
        print("Hello")
        obj3 = A()
        obj3.xyz()

obj1=A()
obj1.xyz()

obj2 = B()
obj2.abc()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("example 2 \n")
'''''Protected'''''

class A:
    def _xyz(self):
        print("hi")

class B(A):
    def abc(self):
        print("Hello")

class C:
    def check(self):
        pass

obj1=A()
obj1._xyz()                 #private can access it's value by its own object

obj2 = B()
obj2.abc()                  # child class can access the value of parent class in private
obj2._xyz()                   # accessed

obj3 = C()
#obj3._xyz()                    # can't acess giving an error



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("example 3 \n")
'''''Private'''''

class A:
    def __xyz(self):
        print("hi")
    def check(self):
        a = A()
        a.__xyz()

obj1= A()
#obj1.__xyz()                          # can't access outside of class
#obj1.xyz()

obj1.check()                      # can be access  within the class    (indirectly done)
obj1._A__xyz()                    # another way to acess the private function