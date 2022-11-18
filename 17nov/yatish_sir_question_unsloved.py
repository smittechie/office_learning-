import random

animal_list=["tiger","dolphin","eagle"]
activties =["swim","fly","run","jump"]


tiger = ["run","jump"]
dolphin = ["swim"]
eagle = ["fly"]

count = 0

a = input("Do you want to paly the game Y or N").casefold()
if a == "y":
    pass
else:
    quit()

for i in random.sample(animal_list,k=len(animal_list)):
    for j in activties:
        a = input(f" {i} can do this {j} ?   y or n :- ")
        for k in i == tiger or dolphin or eagle:
            if j == k :
                count +=1
            # else:
            #     count-=1

print(count)

if count >= 20:
    print("pass")
else:
    print("fail")
