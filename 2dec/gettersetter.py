class Employee:
    def __init__(self,name,lname):
        self.name = name
        self.lname =lname
        #self.email= f"{name}.{lname}@gmail.com"

    def explain(self):
        return f"the employee is {name} {lname}"

    @property
    def email(self):
        return f"{self.name}.{self.lname}@gmail.com"

harsha = Employee("Harsha","patel")

# print(harsha.explain())
print(harsha.email)
harsha.name="venkariya"
print(harsha.email)

