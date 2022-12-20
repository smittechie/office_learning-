import json
a ={"name":"John",
   "age":31,
    "Salary":25000}

# y = json.dump(a)
yy = json.dumps(a)
print(yy)
# print(y)


a=        {
           "employee": [

              {
                 "id": "01",
                 "name": "Amit",
                 "department": "Sales"
              },

              {
                 "id": "04",
                 "name": "sunil",
                 "department": "HR"
              }
           ]
        }

a = json.dumps(a)                                               ## string to json
print(a)
print(type(a))
# b = json.loads(a)                                                   ## json to pyton str
# print(b)
# print(type(b))
#
# with open("json2.json","w") as outfile:
#     json.dump(a,outfile)


f = open("json2.json", )
data = json.load(f)
print(data)
for i in data['employee']:
    print(i)

f.close()