import json

x ={
  "name": "smit",
  "score": 11.75,
  "items": ["food", "cloths","oil"],
  "myobj": {
    "name": "smit",
    "score": 11.75,
    "items": ["food", "cloths","oil"]
  }
}

#parse json
mylist = json.dumps(x,indent=4)
print(x)

mylist1= json.loads(mylist)
print(mylist1)



people_data = {"Trootech":[{
  "emp_name": "Deep pathak",
  "emp_number" : "12345",
  "emp_joining_time":"10:54:21"
  },
{
  "emp_name": "Smit kumar patel",
  "emp_number":"54321",
  "emp_joining_time":"15:23:47"
  }]}



data = json.dumps(people_data)               #python object to json string
print(data)

data2 = json.loads(data)                     #json string to parse
print(data2)

print(data2['Trootech'][1]['emp_name'])