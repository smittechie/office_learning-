'''''iter() Example'''''

string="Trootech"
a=iter(string)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))




''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''topic : Generators '''''


''''Generator-Function '''
def simplegenerator():
    yield 1
    yield 2
    yield 3

for value in simplegenerator():
    print(value)


''''' Generator-Object'''''
a =simplegenerator()
print(next(a))
print(next(a))



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Example 3 \n")
'''''iterator '''''


class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val =self.num
            self.num += 1
            return val
        else:
            raise StopIteration

obj1 = TopTen()
for i in obj1:
    print(i)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Example 4 \n")
'''''Generator '''''

def Gen():
    yield 5

obj1= Gen()
print(obj1.__next__())


#program to write top 10 perfect square
def Gen2():

    n= 1
    while n<10:
        sq=n*n
        yield sq
        n+=1

obj1= Gen2()
print(obj1.__next__())
print(obj1.__next__())
print(obj1.__next__())
print(obj1.__next__())
for i in obj1:
    print(i)

