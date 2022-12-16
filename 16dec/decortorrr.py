'''
synatax of decorator

def mydecoratorfunc(func):

    def wrapper_fun():
        ## method
        fun()
        ## something after the function
    return wrapper_fun

@mydecoratorfunc
def my_func():

    pass
'''

from datetime import datetime
def my_decorator_fun(func):

    def wrapperfun():
        print(datetime.today())
        func()
    return wrapperfun

# def split(funn):
#     def wordsplit():


@my_decorator_fun
def mydaily_routine():
    print ('python code')
mydaily_routine()







