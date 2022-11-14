# def mains():
#     print("hello")
#     print(__name__)
#
# if __name__=="__main__":
#     mains()



from namefunpracticedemo import *


def fun1():
    main()
    print("from fun1")


def fun2():
    print("from fun2")


def main2():
    fun1()
    fun2()

main2()
print(__name__)