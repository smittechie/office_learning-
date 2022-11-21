## WAP to function that accept two arguments dict and name of keys . And return the list of list from those value

test_dic = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 10},
        {'student_id': 2, 'name': 'Lula Powell', 'class': 12}]

def fun1(test_dic,list_of_keys):
        for i in test_dic:
                print([i[list_of_keys[0]],i[list_of_keys[1]]])


fun1(test_dic,["name", "student_id"])




















# def fun1(test_dic,["name”, "class"]):
#         a = [("name","class") for "name" in test_dic for "class" in test_dic]
#         print(a)
# fun1(test_dic,['name','class'])

# def fun1(test_dic,["name”, "class"]):
#         for i in test_dic :
#         y=[(x,y) for x in i['name'] for y in i['class']]
#         # print(test_dic[0]['name'])
#         print(y)