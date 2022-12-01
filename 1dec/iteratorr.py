tup = ('a', 'b', 'c', 'd', 'e')

tup_iter = iter(tup)
for index, item in enumerate(tup_iter):
    print(item)

    if index ==2:
        break
# print(list(tup_iter))
print("its using next now")
print(next(tup_iter))
print(next(tup_iter))


print(50*"---")

def nextsqr():
    i = 1
    while True:
        yield i*i
        i+=1
for num in nextsqr():
    if num >100:
        break
    print(num)