
#n = int(input())
# for i in range(0,n):
#         print(i*i)

# x=1
# while x <= n:
#     print(x**2)
#     x+=1






"\\\\\\Leap Year Or Not\\\\\\"
# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         return True
#     if year % 100 == 0:
#         if year % 400:
#             return True
#         else:
#             return False
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


# if __name__ == '__main__':
#     n = int(input())

# method 1
    # s = ''
    # for i in range(1, n + 1):
    #     s += str(i)
    #
    # print(s)

# method 2
    # elements=[i for i in range(0,n)]
    # print(elements)
    # print("".join(map(str,elements)))


# list1=[1,4,"Gitam",6,"college"]
# list2=[]  # creates an empty list
# list3=list((1,2))
# print(list1)
# print(list2)
# print(list3)





""" strings """

# def swap_case(s):
#     new = ""
#     update=""
#     for letter in s:
#         if letter == letter.upper():
#             update = letter.lower()
#             new+=update
#         elif letter== letter.lower():
#             update = letter.upper()
#             new+= update
#     return new
# # if __name__ = '__main__':
# s = input("enrter your name: ")
# #s = input()
# result = swap_case(s)
# print(result)


