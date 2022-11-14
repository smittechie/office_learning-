def Derived(fun):
    def inner(a,b):
        d= fun(a,b)
        e= d +a+b
        return e
    return inner
@Derived
def Base(a,b):
    return a * b
a=Base(5,4)
print(a)
