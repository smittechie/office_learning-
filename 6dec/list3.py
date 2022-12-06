### List product excluding duplicates

lst = [1, 3, 5, 6, 3, 5, 6, 1]

new_lst = list(set(lst))
print(new_lst)

def product(new_lst):
    a= 1
    for i in new_lst:
        a *= i
    return a
print(product(new_lst))