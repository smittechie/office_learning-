# class A:
#     @classmethod
#     def dob(cls, age):
#         if age < 18:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def date(age):
#         if age < 18:
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def mix(dob):
#         print(A.date(dob))
#         print(A.dob(dob))
#         return "a"
#
#     def mix2(self, dob):
#         print(self.date(dob))
#         print(self.dob(dob))
#
#
# class B(A):
#     var = A.mix(15)
#
#
# obj = A()
# print(obj.dob(21))
# print(obj.date(21))
# A.mix(87)
#
# print("*" * 50)
# obj.mix2(16)
#
# print(B.var)
# b=B()
# var2 = b.mix2(52)
#
# print("--"*50)
#
# var3 = b.date(52)
# print(var3)












class Employee:
    def __init__(self,first, last):
        self.first = first
        self.last = last
        # self.email = self.first+"."+self.last +"@gmail.com "
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {} '.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first ,last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first= None
        self.last= None

a= Employee("harsh", "patel")
# print(a.first)
# print(a.email)
# print(a.fullname)

a.fullname = "amit patel"              ## we cannot set the value of fullname  but after setter we can use
print(a.first)
print(a.email)
print(a.fullname)

# del a.fullname
# del a.first











