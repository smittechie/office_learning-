from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

obj1=Hello()
obj2=Hi()

obj1.start()
sleep(0.2)
obj2.start()

obj1.join()
obj2.join()
print("Bye")