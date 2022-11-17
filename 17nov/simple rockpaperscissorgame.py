import random

def game():
    user_input= input("Choose one thing:- rock , paper , scissor or quit :- ").casefold()
    #values used in game
    print(user_input)
    game_values = ["rock", "paper", "scissor"]

    #values computer is going to select
    computer_pick  = random.choice(game_values)

    if user_input == "quit":
        quit()
    elif user_input == computer_pick:
        print("both have slected the same item ")
        game()
    elif user_input == 'rock' and computer_pick == 'scissor':
        print("user win ")
        game()
    elif user_input == 'paper' and computer_pick == 'rock':
        print("user win ")
        game()
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("user win ")
        game()
    else :
        print("you lost")
        game()

game()