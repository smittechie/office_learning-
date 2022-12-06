## Update each element in tuple list

lst_tupl = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

"""for item in lst_tupl:
    for val in item:
        print(val+5)"""                    # tried but  fail


res = [tuple(val +5 for val in item) for item in lst_tupl]
print(res)
