import json

def fun1():
    x = '{ "name":"John", "age":30, "city":"New York"}'
    print(x)
    print(type(x))

    #parse x:
    y = json.loads(x)
    print(type(y))
    print(y)
#fun1()


def fun2():
    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }
    print(x)
    print(type(x))

    # convert into JSON:
    y = json.dumps(x)

    # the result is a JSON string:
    print(y)
    print(type(y))
#fun2()


def fun3():
    with open("/home/trootech/PycharmProjects/practicequestions/23nov/data.json","r") as f:
        data= json.load(f)

    print(data)
#fun3()

def fun4():
    person_dict = {'name': 'Bob',
                   'age': 12,
                   'children': None
                   }
    person_data = json.dumps(person_dict)
    print(person_data)
fun4()

def fun5():
