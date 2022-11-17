import random

input_1 =int(input("guess a positive number : "))

#generate random number
random_number = random.randint(0,input_1)

#count number of attempts
count= 0

#guessing the number
def func1():
    guess = int(input("Guess the random number "))

    if guess == random_number:
        print("The number is found ")
        global count
        count+=1
    elif guess > random_number:
        print("You are above the number")
        count += 1
        func1()

    elif guess < random_number:
        print("You are below the number")
        count += 1
        func1()
func1()

print(f"It take {count} time to guess the number ")