a = [[1, [2, 3], 4], [5, 6, 7], [8, 9], 10]

lst= []
def type_question(a):
    for i in a:
        if type(i) == list:
            type_question(i)
        else:
            lst.append(i)
type_question(a)
print(lst)


