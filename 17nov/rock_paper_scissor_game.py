import random

def game(user_input):
    game_values = ["rock", "paper", "scissor"]

    #values computer is going to select
    computer_pick  = random.choice(game_values)

    if user_input == "quit":
        quit()
    elif user_input == computer_pick:
        print("both have slected the same item ")
        # game(user_input)
        every_input()
    elif user_input == 'rock' and computer_pick == 'scissor':
        print("user win ")
        # return game()
        every_input()
        # game(user_input)
    elif user_input == 'paper' and computer_pick == 'rock':
        print("user win ")
        # game(user_input)
        every_input()
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("user win ")
        # game(user_input)
        every_input()
    else :
        print("you lost")
        # game(user_input)
        every_input()
if __name__=="__main__":
    while True:
        def every_input():
            user_input = input("Choose one thing:- rock , paper , scissor or quit :- ")
            if user_input in ["rock", "paper", "scissor", "quit"]:
                # break
                game(user_input)
        every_input()
