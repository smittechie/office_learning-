def fun1(name, age):
    print(f'heyy you {name} Your age is {age}')

#fun1("rahul",23)

def fun2(*args):
    for i in args:
        print(i)
#fun2(12,121,484,65,26)


def calculation(a,b):
    return print(a+b , a-b)
#calculation(40,30)

def show_employee(name,*args):
    if args == ():
        args = 9000
        print(name,args)

#show_employee("ben")


def show_employe(name,salary=9000):
    print(name,salary)
#show_employe("ben")


def twoparameters(a,b):
    def add():
        return a+b
    return print(add()+5)
#twoparameters(5,3)

def recursive(num):
    if num :
        return num +recursive(num -1)
    else:
        return 0
a= recursive(5)
print(a)