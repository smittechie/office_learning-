def fib(n):
    a , b= 0,1
    while a <n:
        print(a,end=' ')
        a , b = b , a+b
    print()


def fib2(n):
    count=[]
    a , b = 0, 1
    while a < n:
        count.append(a)
        a, b = b, a + b
    return count

