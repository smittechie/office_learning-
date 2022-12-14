
"""\\\\\\\\\\\\\\ map function \\\\\\\\\\\\\\\\ """
"\\map(fun,iter)\\"                                  #it will pass all the items to the function while filter() will pass only filter 1


# def doublenumber(n):
#     return n*2
# lst=[1,2,3,4,5,6]
# lst2 = map(doublenumber,lst)
# print(list(lst2))



# l = ['sat', 'bat', 'cat', 'mat']
# lst2=map(list,l)
# print(list(lst2))



# lst=[2,3,4,5,6]
# def square(lst):
#     return lst * lst
# lst2 = map(square,lst)
# #print(lst2)
# squared_number = list(lst2)
# print(squared_number)



# def calculatesquare(n):
#     return n * n
#
# lst=[2,3,4,5]
# lst3 =map(calculatesquare,lst)
# lst = set(lst3)
# print(lst)


# Passing Multiple Iterators to map() Using Lambda
# num1 = [4, 5, 6]
# num2 = [5, 6, 7]
# num3 = list(map(lambda x,y:(x+x,y+y),num1,num2))
# print(num3)



"""\\\\\\\\\\\\\\ lambda function \\\\\\\\\\\\\\\\/ """

""" lambda function syntax 
      lambda arguments : expresions"""

# double = lambda x:x*2
# print(double(6))


#Example use with filter()
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# newlist= list(filter(lambda x:(x%2==0),my_list))
# print(newlist)


# lst= [23,234,3434343,64,2323,5,45,23]
# neulist=list(filter(lambda x:(x%8==0) , lst ))
# print(neulist)



# by using map
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x:x*2,my_list))
# print(new_list)



""" #hash code program"""
#wrong attempt
# n= input()
# print (hash(tuple([int(i) for i in input().split()])))

# if __name__ == '__main__':
#     _ = input()
#     print(hash(tuple(map(int, input().split()))))


"""list comprehension  """

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
#     print([[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z!=n ])



"""Nested list """
# matrix = []
# n= 5
# for i in range(n):
#     matrix.append([])
#     for j in range(n):
#         matrix[i].append(j)
#
# print(matrix)
#

#same with nested list comprehension
# matrix =[(i,j) for i in range(5) for j in range(5) ]
# print(matrix)
# matrix =[[i for i in range(5) ]for j in range(5) ]                  #one line code
# print(matrix


#Example 2:
#flatternlist program
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattern_list = []
# for sublist in matrix:
#     for item in sublist:
#         flattern_list.append(item)
# print(flattern_list)

#same with nested list
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatternlist  =[]
# flatternlist  =[item for sublist in matrix for item in sublist]
# print(flatternlist)


#Example 3:
# planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
# flatten_planets = []
# for sublist in planets:
#     for planet in sublist:
#         if len(planet) < 6:
#             flatten_planets.append(planet)
#
# print(flatten_planets)


"""Zip function """

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")
#
# x = zip(a, b)
# print(tuple(x))
#


#Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# x = filter(None,list1)
# print(tuple(x))



#Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)