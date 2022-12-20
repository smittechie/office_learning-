from random import randint 
import random

welcome_message = """
          Welcome to 'Pig', a dice game!
   
    In this game, a user and a computer opponent
    roll a 6-sided die each round. If the value of
    the die is a 1, the player that rolled the 1 loses
    all of their points. Otherwise, the player gets the
    value of the die added to their points. The first
    player to reach 30 points wins!
"""
print(welcome_message)

User_Dice_Rolled = 0
User_Dice_Rolled_Points = 0
Computer_Dice_Rolled = 0
Computer_Dice_Rolled_Points = 0
Total_turn = 10

count =0
while count<1:
    a = input("want to play the game :type 'Y' OR 'N' :-").upper()
    if a == "Y":
        print("lets play")
        count+=1
    elif a == "N":
        print("Thanks for your time")
        quit()
    else :
        print("Wrong input ")

def user_turn():
    num = random.randint(1,6)
    return num
def Computer_turn():
    num = random.randint(1,6)
    return num

# while Computer_Dice_Rolled_Points | User_Dice_Rolled_Points >= 30:
while User_Dice_Rolled < Total_turn:
    User_score =user_turn()
    if User_score != 1:
        User_Dice_Rolled_Points =User_Dice_Rolled_Points+User_score
        User_Dice_Rolled +=1
        # print(User_Dice_Rolled_Points,"User",User_score)
    elif User_score == 1 :
        User_Dice_Rolled_Points = 0
        User_Dice_Rolled += 1
        # print("We got 1 on user side")
print("User total points are : ",User_Dice_Rolled_Points)

while Computer_Dice_Rolled < Total_turn:
    Computer_score = Computer_turn()
    if Computer_score != 1:
        Computer_Dice_Rolled_Points = Computer_Dice_Rolled_Points+ Computer_score
        Computer_Dice_Rolled += 1
        # print(Computer_Dice_Rolled_Points,"Comp",Computer_score)
    elif Computer_score == 1:
        Computer_Dice_Rolled_Points = 0
        Computer_Dice_Rolled += 1
        # print("1 from computer")
print("Computer total score is :",Computer_Dice_Rolled_Points)


if User_Dice_Rolled_Points > Computer_Dice_Rolled_Points:
    print(f"User win the game with {User_Dice_Rolled_Points - Computer_Dice_Rolled_Points} points")
elif Computer_Dice_Rolled_Points > User_Dice_Rolled_Points:
    print(f"Computer has win the game with {Computer_Dice_Rolled_Points - User_Dice_Rolled_Points} points ")

elif Computer_Dice_Rolled_Points == User_Dice_Rolled_Points:
    print("Its a tie")
    pass





# a = user_turn()
# b = Computer_turn()
# lst =[user_turn(),Computer_turn()]
# # lst =[a,b]
# c = random.sample(lst,k=1)
# print(c)

# def Userr(c):
#     User_Dice_Rolled_Points=0
#     User_Dice_Rolled = 0
#     for ele in c:
#         if ele ==1:
#             User_Dice_Rolled_Points =0
#         else:
#             if User_Dice_Rolled <=6 and User_Dice_Rolled_Points<30:
#                 User_Dice_Rolled_Points += ele
#                 User_Dice_Rolled +=1
#         print(User_Dice_Rolled_Points)
# Userr(c)