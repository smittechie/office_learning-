''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("Example 1 \n")
'''''simple try and except '''''
try:
    b=4 + spam * 3
    print(b)
except  NameError as e:
    print(e)


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 2 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

''''' many exceptions '''
try:
    # b=4 + spam * 3

    #'2' + 2

    10 * (1 / 0)

except NameError:
    print("Oops!  That was no valid number.  Try again..")
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print('"can only concatenate str (not "int") to str."')


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 3 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''Raising Exceptions¶ '''''
# x = -1
#
# if x < 0:
#   raise Exception("Sorry, ")


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 4 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def divide(x, y):
    try:
        result =x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Yeah ! Your answer is :", result)
    finally:
        print('This is always executed')

divide(3, 2)
print()
divide(3, 0)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print("--"*50)
print("Example 5 \n")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a = 5
b = 0

try:
    print("File open")
    print(a/b)
except Exception as e:
    print(e)
finally:
    print("File close")

