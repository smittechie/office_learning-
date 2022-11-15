
answer = ["d","a","d","b","d"]
right_answer = 0
user_input= input("Do tpu; want to play the game?   y/n ")
if user_input == "y":
    print("Lets start\n",
          "*"*50)

    print("Question 1 \n"
          "What is the maximum length of a Python identifier?\n"
          "a = 32\n"
          "b = 16\n"
          "c = 128\n"
          "d = No fixed length is specified.")
    user_answer = input(":")
    if user_answer == answer[0]:
        right_answer+=1
    else:
        print("Wrong Answer:\n"
        "No fixed length is specified by default for a Python identifier.")

    print("*"*50)
    print("Question 2 \n"
        "What will be the output of the following code snippet?\n"
        "print(2**3 + (5 + 6)**(1 + 1))\n"
          "a = 129\n"
          "b = 8\n"
          "c = 121\n"
          "d = None of the above ")
    user_answer = input(":")
    if user_answer == answer[1]:
        right_answer += 1
    else:
        print("Wrong Answer:\n"
        "The above code will print 129 by following the BEDMAS rule of operator precedence.")

    print("*" * 50)
    print("Question 3 \n"
          '''What will be the datatype of the var in the below code snippet?
            var = 10
            print(type(var))
            var = "Hello"
            print(type(var))'''
          "a = str and int\n"
          "b = int and int \n"
          "c = str and str\n"
          "d = int nd str  ")
    user_answer = input(":")
    if user_answer == answer[2]:
        right_answer += 1
    else:
        print("Wrong Answer:\n"
              "Initially var stores 10, and so is of type int. After that it stores “Hello” which is of type string.")

    print("*" * 50)
    print("Question 4 \n"
          "How is a code block indicated in Python?"
          "a = Brackerts\n"
          "b = Indentation\n"
          "c = Keys\n"
          "d = None of the above ")
    user_answer = input(":")
    if user_answer == answer[3]:
        right_answer += 1
    else:
        print("Wrong Answer:\n"
              "A python code block is indicated through the use of indentation.")

    print("*" * 50)
    print("Question 5 \n"
          "What will be the output of the following code snippet?"
        '''a = [1, 2, 3]
           a = tuple(a)
           a[0] = 2
           print(a)\n'''
          "a = [2,2,3]\n"
          "b = (2,2,3)\n"
          "c = (1,2,3)\n"
          "d = Error ")
    user_answer = input(":")
    if user_answer == answer[4]:
        right_answer += 1
    else:
        print("Wrong Answer:\n"
              "Since we convert a to a tuple and then try to change its content, we will get an error since tuples are immutable.")


    print(f"{right_answer}  out of 5 is right")


