MLB_team = dict(
   Colorado='Rockies',
   Boston='Red Sox',
   Minnesota='Twins',
   Milwaukee='Brewers',
   Seattle='Mariners'
 )

MLB_team = dict([
     ('Colorado', 'Rockies'),
     ('Boston', 'Red Sox'),
     ('Minnesota', 'Twins'),
     ('Milwaukee', 'Brewers'),
     ('Seattle', 'Mariners')
 ])



a = {"James": 95, "Jane": 98}
b = {"Matt": 85, "Ashely": 90}


# merge two dictionary
c = a|b
print(c)

res = {**a,**b}
print(res)

a = {"James": 95, "Jane": 98, "Matt": 85, "Ashely": 90}
# del a["James"]
# print(a)
#
# a.pop("Jane")
# print(a)

soerted_a = sorted(a.items(),key=lambda x:x[1])
print(dict(soerted_a))