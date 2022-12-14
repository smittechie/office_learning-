
class A:
    @classmethod
    def dob(cls, age):
        if age < 18:
            return True
        else:
            return False
    @staticmethod
    def date(age):
        if age < 18:
            return True
        else:
            return False

    def mix(date,dob):
        print(obj.date(date))
        print(obj.dob(dob))
        return "a"

    def mix2(self,date,dob):
        print(self.date(date))
        print(self.dob(dob))


obj = A()
# print(obj.dob(21))
# print(obj.date(21))
A.mix(87,17)

print("*"*50)
obj.mix2(16,17)









# print(A.dob(21))
# print(A.date(21))