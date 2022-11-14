'''''dictionary methods'''''

# clear(deletes the item )
#.keys(gives the keys)
#.fromkeys(gives a new dictionary )
#.get(will not give an error, we have to give a key ,and if it is not their we can access it wihout error )
#pop(removes the specific items from the dictionary)
#.popitem(deletes the last item from the dictionary )
#.items(gives the items)
#.values(gives the values of the key
#.copy(gives the copy of the item )
#.update (update tthe value)
#setdefault(if key not their then it will update key with none)



'''''Practice questions'''
def methodpractice():
    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }

    #x = car.get("cars",456)
    #x = car.setdefault("yeaar")
    car.update({"year": "Whiite"})
    x=car.items()

    print(x)
    print(car)
#methodpractice()


def q1():
    '''''Convert two lists into a dictionary'''''
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    a=dict(zip(keys,values))
    print(a)

    extradict=dict()
    for i in range(len(keys)):
        extradict.update({keys[i]:values[i]})
    print(extradict)
#q1()


def q2():
    '''''Merge two Python dictionaries into one'''''
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict1.update(dict2)
    print(dict1)

    #method2
    dict3= {**dict1,**dict2}
    print(dict3)
#q2()

def q3():
    '''''Print the value of key ‘history’ from the below dict'''''

    sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
    print(sampleDict["class"]["student"]["marks"]["history"])

#q3()


def q4():
    '''''Create a dictionary by extracting the keys from a given dictionary'''''
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    a=list(sample_dict.keys())
    b = dict()
    for i in range(0,len(a),2):
        b.update({a[i]:a[i+1]})
    print(b)
#q4()


def q5():
    '''''Rename key of a dictionary'''''
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    sample_dict['location']=sample_dict.pop('city')
    print(sample_dict)
#q5()

def q6():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    print(min(sample_dict, key=sample_dict.get))
#q6()

def q7():
    test_str = 'Trootech best for freshers'
    lookp_dict = {"best": "good and better", "Trootech": "all CS aspirants"}

    #split the string
    a = test_str.split()
    print(a)
    lst=[]
    for i in a:
        b=lookp_dict.get(i,i)
        lst.append(b)
    res =''.join(lst)
    print(str(res))
q7()