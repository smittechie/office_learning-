# add list in the set

sett = {"Yellow", "Orange", "Black"}
lst = ["Blue", "Green", "Red"]
sett.remove("Black")
print(sett)

lst = set(lst)

sett.update(lst)
print(sett)