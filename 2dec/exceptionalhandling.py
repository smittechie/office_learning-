# try :
#     a= 5/0
#
# except ArithmeticError:
#     print("you have an error")
# else:
#     print("sucess")
#



# try:
# 	a = 10/0
# 	print (a)
# except BaseException:
# 		print ("This statement is raising an arithmetic exception.")
# else:
# 	print ("Success.")



###custom exception

class Error(Exception):
    pass
class Noteligible(Error):
    pass
age = int(input("enter your age for gov exam :"))
try:
    if age < 20:
        print("yot are not eligible ")
    else:
        raise Noteligible
except Noteligible:
    print("you are  eligible to work ")

