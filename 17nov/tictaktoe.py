from random import choice

userinput = int(input("enter the number betweenn 0-8 :"))

lst = []
lst.append(userinput)

computerinput = choice([i for i in range(0,9) if i not in lst])
print(computerinput)
def count():
      


dic = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8"}





print(f" {dic[0]}  {dic[1]}  {dic[2]} \n "
      f"{dic[3]}  {dic[4]}  {dic[5]} \n "
      f"{dic[6]}  {dic[7]}  {dic[8]}")