import json

name = "amit"
with open('data3.json', "r+") as f:
    data = json.loads(f.read())
    data1 = {"bike":500}
if data:
    names = []
    for i in data:
        names.extend(i.keys())

    if name in names:
        for i in data:
            print(i[name][0]['bike'])
            if i[name][0]['bike']:
                print("inside")
                i[name][0]['bike'] += data1['bike']


with open('data3.json', "r+") as f:
    f.write(json.dumps(i))
