# class Fruit:
#     def __init__(self,name):
#         self._name = name                  #wanted to be private
#
#     def get_name(self):
#         print("getting the name ")
#         return self._name
#     def set_name(self,newname):
#         print("setting the name ")
#         self._name = newname
#
# if __name__=='__main__':
#     fruit =Fruit('Banana')
#     # print(fruit._name)
#     fruit.set_name("Orange")
#     print(fruit.get_name())
#


class Fruit:
    def __init__(self,name):
        self._name = name                  #wanted to be private

    @property
    def fruit_name(self):
        print("getter is accessed ")
        return self._name

    @fruit_name.setter
    def fruit_name(self,value):
        print("acessing setter")
        self._name = value

    @fruit_name.deleter
    def fruit_name(self):
        print(f'"{self._name}" was deleted ')


if __name__=='__main__':
    fruit =Fruit('Banana')
    print(fruit.fruit_name)
    fruit.fruit_name="Orange"
    del fruit.fruit_name