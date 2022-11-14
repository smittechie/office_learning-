''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 1 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner
@smart_div
def div(a,b):
    print(a/b)

#div =smart_div(div)
div(2,4)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 2 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def decor(num):
    def inner():
        a = num()
        add = a+5
        return add
    return inner


def num():
    print("this is main function")
    return 10

num = decor(num)
print(num())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 3 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1

def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used= hello_decorator(function_to_be_used)
function_to_be_used()