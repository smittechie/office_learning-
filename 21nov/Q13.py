##  WAP to create a list that contains only strings.
##  Constraints : make sure the list only contains alphabetic type data.


lst = []

while True:
    user_input = input("ENter the alphabetic value or quit: ")
    if user_input == "quit":
        print(lst)
        quit()
    elif user_input.isalpha():
        lst.append(user_input)
        print("your value is ",user_input)
    elif True:
        print("Wrong input  try again ")
print(lst)