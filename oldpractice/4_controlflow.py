
#  fibonnaci number
# a , b = 0 , 1
# while a < 10 :
#     print(a)
#     a , b = b , a+b

# # if statement
# x = int(int(input("enter any number:")))
#
# if x<0:
#     print("less than 0 ")
# elif x == 0 :
#     print("ya zero")
# elif x==1:
#     print("grater than zero")
# else:
#     print("more")

#range
# for i in range(6):
#     print(i)

# for i in range(6,22):                  # range(start, end , steps)
#     print(i)

# for i in range(6,22,2):                  # range(start, end , steps)
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i ,a[i])



#break

# for i in range(2,10):
#     for j in range(2,i):
#         if i%j == 0:
#             print(i ,'equals',j ,'*',i//j)
#             break
#     else:
#          print(i , 'is the prime number')

# continue

# for i in range(2,20):
#     if i % 2 == 0:
#         print("even")
#         continue
#     print("odd")


#MATCH  statement
trythis = str(input("enter the number between 1-5  \n" ))
match trythis:
    case "1":
        print("you are first")
    case "2":
        print("you are second")
    case "3" | "4" | "5":
        print("ehh ok ")


#functons 4.8


