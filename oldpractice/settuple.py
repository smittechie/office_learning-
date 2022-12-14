# t = 5 , 3, "hello "
# print(t)                                     # here wihtout () we can also declare tuple just we need to
#
# print(t[0])                                  #acessing tuple

#nested tuple
# u = t,(1,2,3,4,5,6,7)
# print(u)
#u[0]= 22                                     # tuple is nested

# x= t.count(5)                                # counr function    #nested tuple ma nahi caount kare
# print(x)

# x= t.index(3)                             #index gives the index of that value
# print(x)





###### set  & its methods


# Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {};

# basket = {"apple", "banana","chikoo", "apple", "pineapple", "guava" , "papaya"}
# print(basket)
#
# print("orange" in basket )

# a = set('asdfbfhfujdfnjdkfnhfdehifioewjhfsndfsdhyfioeufdfhfeohdsf')
# b= set('ehrehwfjhdsioufh')
# b= set('ehrehwfjhdsioufh')
# print(a)
# print(a-b)
# print(a&b)
# print(a^b)      #xor ++=0 --=0


# add()

basket = {"apple", "banana","chikoo", "apple", "pineapple", "guava" , "papaya"}
# basket.add("grapes")
# print(basket)

#clear()
# basket.clear()
# print(basket)                     #deletes all the values and return empty  sets

#copy()
a= basket.copy()
# print(a)                             # copy the string

#differnce
# x = basket.difference(a)                # comparae the values
# print(x)

#difference_update
# basket.add("grapes")
# print(basket)
# basket.difference_update(a)
# print(basket)                          # the difference will remain other will be deleted from the list

#discard()
# print(a)
# x  = a.discard('banana')              # remove the specific item froom  the set
# print(a)

#intersection()
# print(a, basket)
# basket.add("grapes")
# print(a, basket)                           #it will give a value to a variable
# x=a.intersection(basket)
# print(x)                                  # intersection will give common values as output


#intersection_update
# basket.add("grapes")
# a.add("oranges")                          #here update will be done on a or y which ever
# print(a, basket)
# a.intersection_update(basket)            # remove the item that are not present in one pf the set
# print(a)


#isdisjoint()
#print(a.isdisjoint(basket))               ## check is it disjoint    if dijoint then true else false


 #issubset()
# basket.add("grapes")
# #a.add("oranges")
# print(a.issubset(basket))                    # a (has all th value of basket) subset of basket


#issuperset()
# basket.add("grapes")
# print(basket.issuperset(a))              #basket (has all the value of a) is  superset of a

#pop()
# print(basket)
# basket.pop()
# print(basket)                      #pop delete the last item

#remove()
# print(basket)
# basket.remove('pineapple')
# print(basket)                          # removes the specific element

#symmetric_difference()
# basket.add("grapes")
# a.add("oranges")
# e = basket.symmetric_difference(a)                # give unique value from both of set in new set
# print(e)                                         # same wala nahi aayega sab mei se alag alag aayega


#symmetric_difference_update()
# basket.add("grapes")
# a.add("oranges")
# print(basket)
# print(a)                                           # same nikaal diya hai
# basket.symmetric_difference_update(a)                # give unique value from both of set in new set
# print(basket)

# union()
# basket.add("grapes")                           # give the union of the both the set
# a.add("oranges")
# print(basket)
# print(a)
# z = a.union(basket)
# print(z)


# update()
# basket.add("grapes")
# a.add("oranges")
# print(basket)
# print(a)
# basket.update(a)
# print(basket)                           # update a set by from both sets
