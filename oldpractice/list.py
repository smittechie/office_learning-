import copy

#lst =["sita","seeta" ,"gita","geeta", "nany" , "penny" ]
# lst.append("aayu")                                  #element is added
# print(lst)
# print(len(lst))                                     #length is calculated

# lst2 = ["harsh","harsha" , "akash" , "akasha"]
# lst.extend(lst2)
# print(lst)

# lst.insert(5,"nanu")
# print(lst)                                 #here the item will be addded in between  , first parameter is index number
#
# lst.remove("penny")
# print(lst)                                # it removes the given item which we have passed


#lst.pop()                                   #last item removed
#print(lst)

# lst.clear()                                # equivalent to delete
# print(lst)

# print(lst.index("gita"))                   # index is returned  which ever first found
# print(lst.index("seeta",1,5))               #item to be founnd , start , end

#print(lst.count("sita"))                   # print the number of occurance of the element

#lst.sort(reverse=True)     #here list  is sorted   revrese for reverse  , and key for sorting criteria


# lst.reverse()                           #reverse the list
# print(lst)
#print(lst[::-1])

#lst.copy()

#lst = [1,3,5,4,6,7]
# lst2=lst
# lst2[0]=2
# print(lst)
# print(lst2)

# lst2 = copy.deepcopy(lst)                            #deep copy makes a new memeory to store items
# print(lst , lst2)
# lst2[3]=99
# print(lst , lst2)


#list comprehension
#vec = [-4 , -2 ,0, 2 , 4]
# print([x * 2  for x in vec])                          # create a new list with the values doubled
# print([x for x in vec if x>=0 ])                     # filter the list to exclude negative numbers
# print([abs(x) for x in vec])                          # apply a function to all the elements
# print([pow(x,2) for x in vec])                          # call a method on each element
# print([(x,x**2) for x  in vec ])                      # create a list of 2-tuples like (number, square)
#print([x, x**2 for x in range(6)])      #the tuple must be parenthesized, otherwise an error is raised
# vec = [[1,2,3],[4,5,6],[7,8,9]]
# print([x for elm in vec for x in elm ])     #flatten a list using a listcomp with two 'for'

# del
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]                                    # here why not in print
# print(a)


"//////////////////////////////////////////////////////////////////////////////"
lst = [1,2]
lst2=[3,4]

#mistake
# len1=len(lst)
# len2=len(lst2)
# for i in range(0,len1):
#     for j in range(0,len2):
#         c=tuple(lst[i] ,lst2[j])
#         print(c)

##//// Method1

# x=[]
# for i in lst:
#     for j in lst2:
#         #c=tuple(i ,j)
#         if i != j:
#             x.append((i,j))                             #here append takes only one variable so "(i,j)"
# print(x)



##//////// method 2

# x= []
# y=[]
# for i in lst:
#     for j in lst2:
#          x.append(i)
#          x.append(j)
# print(x)

# for i in range(0,len(x),2):
#     y.append((x[i],x[i+1]))
# print(y)


#mistake
# for i in range(0,len(x),2):
# #     k=x[i]
# #     print(k)
#     y.append((i,i+1))
# print(y)


#list comprehensiion method

w=[(i,j) for i in lst for j in lst2 if i != j ]
print(w)
#output = [(1,3),(1,4),(2,3),(2,4)]


"////////////////////////////////////////////////////////////////////////"




