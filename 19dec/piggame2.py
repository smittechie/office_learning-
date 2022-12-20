from random import randint
import random
# global User_Dice_Rolled_Points ,Computer_Dice_Rolled_Points

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


count = 0
while count < 1:
    a = input("want to play the game :type 'Y' OR 'N' :-").upper()
    if a == "Y":
        print("lets play")
        count += 1
    elif a == "N":
        print("Thanks for your time")
        quit()
    else:
        print("Wrong input ")


def user_turn():
    num = random.randint(1, 6)
    return num


def Computer_turn():
    num = random.randint(1, 6)
    return num


def comp():
    global Computer_Dice_Rolled_Points
    global Computer_Dice_Rolled
    # while Computer_Dice_Rolled < Total_turn:

    while Computer_Dice_Rolled < Total_turn:
        a = input("Computer wants to play  'y' or 'n' :-")
        if a == "y":
            Computer_score = Computer_turn()
            if Computer_score != 1:
                Computer_Dice_Rolled_Points = Computer_Dice_Rolled_Points + Computer_score
                Computer_Dice_Rolled += 1
                # print(Computer_Dice_Rolled_Points,"Comp",Computer_score)
            elif Computer_score == 1:
                Computer_Dice_Rolled_Points = 0
                Computer_Dice_Rolled += 1
                # print("1 from computer")
            print(Computer_Dice_Rolled_Points,"compurter point  ")
        elif a =="n":
            user()
    # return Computer_Dice_Rolled_Points


def user():
    # while Computer_Dice_Rolled_Points | User_Dice_Rolled_Points >= 30:
    global User_Dice_Rolled
    global User_Dice_Rolled_Points
    while  User_Dice_Rolled < Total_turn:
        a = input("User wants play 'y' or 'n' :-")
        if a == "y":
            User_score = user_turn()
            if User_score != 1:
                User_Dice_Rolled_Points = User_Dice_Rolled_Points + User_score
                User_Dice_Rolled += 1
                # print(User_Dice_Rolled_Points,"User",User_score)
            elif User_score == 1:
                User_Dice_Rolled_Points = 0
                User_Dice_Rolled += 1
                # print("We got 1 on user side")
            print("user current points",User_Dice_Rolled_Points)

        elif a == "n":
            comp()
    # return User_Dice_Rolled_Points

user()

print("User total points are : ", User_Dice_Rolled_Points)
print("Computer total score is :", Computer_Dice_Rolled_Points)



if User_Dice_Rolled_Points > Computer_Dice_Rolled_Points:
    print(f"User win the game with {User_Dice_Rolled_Points - Computer_Dice_Rolled_Points} points")
elif Computer_Dice_Rolled_Points > User_Dice_Rolled_Points:
    print(f"Computer has win the game with {Computer_Dice_Rolled_Points - User_Dice_Rolled_Points} points ")

elif Computer_Dice_Rolled_Points == User_Dice_Rolled_Points:
    print("Its a tie")
