import datetime

#Get Current Date and Time
print(datetime.datetime.now())
x = datetime.datetime(2022,11,15)
print(x)

p= datetime.time(21,54,45,0)
print(p)


#Get Current Date
date_object = datetime.date.today()
print(date_object)

#Get the Current Time of a Timezone with datetime

import pytz
zones  = pytz.all_timezones
print(zones)

from datetime import datetime
#time in a given city
seoulTime = pytz.timezone('Asia/Seoul')
print(seoulTime)
timeinseoul = datetime.now(seoulTime)
currenttimeinSeoul = timeinseoul.strftime("%H:%M:%S")
print("The current time in Seoul  is:", currenttimeinSeoul)



#datetime.date Class

from datetime import date
d = date(2022,11,12)
print(d)

d = date.today()
print(d)


print(50*"--")
today= date.today()
print("Day",today.day)
print("Month",today.month)
print("Year",today.year)



print(50*"--")

from datetime import time

a = time()
print(a)

#time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

a = time(17, 30, 46)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond )

print(50*"--")

#datetime.datetime
from datetime import datetime
a = datetime(2020,3,8)
print(a)

b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)


print(50*"--")
#datetime.timedelta

from datetime import datetime , date
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)

t3 = t1 - t2
print(t3)
print("type of t3 =", type(t3))

#Difference between two timedelta objects
from datetime import timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1- t2
print(t3)                                                            # here it will  adjust by default all the date and time


print(50*"--")


# Printing negative timedelta object
from datetime import timedelta

t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2

print("t3 =", t3)
print("t3 =", abs(t3))


print(50*"--")

#Time duration in seconds

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("a",t.total_seconds())




print(50*"--")
print(50*"--")
print(50*"--")
#Python format datetime

from datetime import  datetime

now = datetime.now()
print(type(now))

t = now.strftime("%H:%M:%S")
print(t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1: ",s1)


#strptime()
date_string = "21 June, 2018"
print("date_string",date_string)

date_object = datetime.strptime(date_string,"%d %B, %Y")
print("date_object", date_object)