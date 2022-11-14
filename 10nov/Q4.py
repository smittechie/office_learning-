#WAP to check the username and password is correct. If the entered value match with the static values then print appropriate message

'''''Static values :
Username = [admin, quixom, trootech]
Password = [admin123, quixom123, trootech123]
    Ex. 
Input1: 
Enter user name : admin (user acceptable)
Enter password : admin (user acceptable)
Output:
Username and password is incorrect.

Input2:
Enter user name : admin (user acceptable)
Enter password : admin123 (user acceptable)
Output:
	Login successfully.
'''''

Username = ["admin", "quixom", "trootech"]
Password = ["admin123", "quixom123", "trootech123"]
val = dict(zip(Username,Password))
print(val)

n= int(input("user you want to check "))
d ={}
for i in range(n):
    a = input("enter username : ").split()
    b = input("Enter password : ").split()
    d[a[0]]=b[0]
#print(d)

for x in val.items():
    print(type(x))
    if d == y:
        print("matched ")
    else:
        print("not matched ")
        break

# d= {}
# a = input("enter username : ")
# b = input("Enter password : ")
# d[a]=b
# print(d)




'''''method 2'''''
# a = input("enter username : ")
# for key in Username:
#     if key == a:
#         b = str(input("Enter password : "))
#         for value in Password:
#             if value == b:
#                 print("matched")
#             else:
#                 print("password wrong")
#             break
#     else:
#         print("username wrong")
#     break
#
