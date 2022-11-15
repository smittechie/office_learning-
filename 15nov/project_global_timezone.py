from datetime import datetime
import pytz

# time = input("Enter  time in :->>  Day/Month/year Hour:Minutes:Seconds :")
# time_object =datetime.strptime(time,"%d/%m/%y %H:%M:%S")
# print(time_object)


zones = pytz.all_timezones
zones = list(zones)
print(zones)
country= []
continent = []
other = []

# for i, value in enumerate(zones):
#     if "/" in value:
#         ab = value.split("/")
#         continent.append(ab[0])
#         country.append(ab[1])
#     else:
#         other.append(value)
#
# continent= list(set(continent))
# print(country)
# print(continent)
# print(other)


seoulTime = pytz.timezone('Asia/Seoul')
timeinseoul = datetime.now(seoulTime)
print(timeinseoul)





