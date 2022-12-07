##  Sort Nested keys by Value

test_dict = {'Nikhil': {'English': 5, 'Maths': 2, 'Science': 14},
             'Akash': {'English': 15, 'Maths': 7, 'Science': 2},
             'Akshat': {'English': 5, 'Maths': 50, 'Science': 20}}

res = {key : dict(sorted(val.items(), key = lambda ele: ele[1]))for key, val in test_dict.items()}

print(str(res))

this =dict()
for i,j in test_dict.items():
    a= sorted(j.items(),key=lambda ele:ele[1])
    this.update(dict.fromkeys(i.split(),a))
print(this)