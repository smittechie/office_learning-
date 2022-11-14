#WAP to split a list every Nth element.

lst = [2,3,5,6,7,8,9,0,3,5,6,7,8,9,0]

#a = int(input("enter the steps  "))
# b= []
#lent = len(lst)

# def fun1(S,step):
#     return [S[i::2] for i in range(step)]
# print(fun1(lst,2))


lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
s = []
n = 3
for x in range(n):
    s.append(lst[x::n])
    print(s)