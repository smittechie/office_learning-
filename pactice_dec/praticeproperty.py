class Student:
    def __init__(self,name,grade):
        self.name= name
        self.grade =grade

    @property
    def msg(self):
        return self.name+" grade is  "+self.grade

    @msg.setter
    def msg(self,msg):
        sent = msg.split(" ")
        self.name=sent[0]
        self.grade=sent[-1]


stud1= Student("Amit","8")
print(stud1.name)
print(stud1.msg)
print(stud1.grade)

stud1.name= "Amuliya "
print(stud1.msg)
stud1.msg ="Amit grade is 9"                        #here after setter we are using the msg as an sttribute
print(stud1.msg)




