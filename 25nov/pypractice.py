def def1():
    lst = {10:132,21:343,3:233,4:34,5:343}
    print(set(lst))                               # set gives the answer in the sequence
    #print(dict(lst))
#def1()


from abc import ABC , abstractmethod
class Computer(ABC):                                                             # here we have to write abc to make it abstract clas
    @abstractmethod
    def process(self):                        #basically we are giving the structure only
        pass                                # here we doesn't define the body just type pass
    def bugging(self):
        print("solving bugs ")            ### concrete method =--> method inside abstract method os called concrete method


class Programmer(Computer):
    def Solving(self):
        print("solving problems ")            ### concrete method

    def process(self):
        print("trying to acess ")

# obj1= Computer()
# obj1.process()

obj2= Programmer()
obj2.bugging()