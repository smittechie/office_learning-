#sets methods
# add(add  the elements at the end of set),
# clear(delete the whole list),
# copy(copy the set ),
#discard( remove the specific item ),
# difference (gives the difference between two sets),
# remove(delete the items),
# pop(will remove the random item from the set ),
# intersection(gives common element from both the set )
#symetric difference (roemoves the common lement from the set )
#isdisjoint(check whater the set has common elements ir not)
#update(update the set with iterable items )
#union(returns a set containing the union of sets)



""""" sets questions """""


def q1():
    ''''' Add a list of elements to a set '''''

    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    sample_set.update(sample_list)
    print(sample_set)
#q1()


def q2():
    ''''' Return a new set of identical items from two sets '''''
    '''''Get Only unique items from two sets'''''

    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    a= set1.intersection(set2)
    b = set1.symmetric_difference(set2)
    print(a)
    print(b)
#q2()

def q3():
    '''''Check if two lists have at-least one element common'''''

    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]
    a = set(a)
    b = set(b)
    print(a.isdisjoint(b))
#q3()

def q4():
    '''''program to count number of vowels using sets in given string'''''
    a = set("python")
    count = 0
    for i in a:
        if i in ["a","e","i","o","u"]:
            count+=1
    print(count)
#q4()

def q5():
    '''''Concatenated string with uncommon characters '''''
    S1 = "aacdb"
    S2 = "gafd"
    set1= set(S1)
    set2= set(S2)
    uncommon = list(set1^set2)
    print(''.join(uncommon))
#q5()


def q6():
    '''''Check if a given string is binary string or not'''''
    #approach 1
    str= "101010"
    value= ["0","1"]
    count = 0
    for item in str:
        if item in value:
            count+=1
        else:
            print("no")
        if count== len(str):
            print("yes")

    #approach 2
    '''''by using set'''''
    str= "1010110101"
    set1= set(str)
    value = {"0","1"}
    if set1 == value or set1== {"0"} or set1 == {"1"}:
        print("yes")
    else:
        print("no")
q6()