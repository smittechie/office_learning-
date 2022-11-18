import random

animal_list=["tiger","dolphin","eagle","lion"]
activties =["swim","fly","run","jump","drag","walk"]
attributes = {
    "tiger":["run","jump","drag","walk"],
    "dolphin":["swim","drag"],
    "eagle":["fly","walk"],
    "lion":["run","jump","drag","walk"]
}
count = 0
def input_fun():
    a = input("Do you want to play the game Y or N :- ").casefold()
    if a == "y":
        pass
    else:
        print("wrong input please try again :")
        input_fun()
input_fun()


for i in random.sample(animal_list,k=len(animal_list)):
    for j in activties:
        a = input(f" {i} can do this {j} ?   y or n :- ")
        if j in attributes[i]:
            count+=1
        else:
            count-=1


print(count)

if count >= 20:
    print("pass")
else:
    print("fail")
