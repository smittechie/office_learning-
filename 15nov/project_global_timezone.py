from datetime import datetime
import pytz
import json


# data on which the timezone function is going to use
people_data = {"Trootech":[{
  "emp_name": "Deep_pathak",
  "emp_number" : "12345",
  "emp_joining_time":'2022:11:16 23:15:54'                # EST -0500
  },
{
  "emp_name": "Smit_kumar_patel",
  "emp_number":"54321",
  "emp_joining_time":'2022:11:16 22:16:48'              # CST -0600
  }]}



fmt="%Y:%m:%d %H:%M:%S"                                   # %Z %z

user_input = input("Select the employee \n"
      "a = Deep_pathak\n"
      "b = Smit_kumar_patel :")



def retrive_time(obj):
    if user_input == "a":
      a_obj= people_data["Trootech"][0]['emp_joining_time']
      return a_obj
    elif user_input == "b":
      b_obj = people_data["Trootech"][1]['emp_joining_time']
      print(b_obj)
      return b_obj


def time_parsed(time_from_data):
    date = datetime.strptime(time_from_data, fmt)
    print("Time after data retrived and parsed :",date)
    return date
def convert_timezone(parsed_time):
    user_input_timezone = input("Enter the timezone you want the time in\n"
                                "US/Central\n"
                                "Asia/Seoul\n"
                                "Europe/London\n"
                                "Europe/Oslo :->")
    #current local time
    naive = datetime.now()
    print("current local time of system  : ", naive)

    #time retrived by the data
    us_local =pytz.timezone(f'{user_input_timezone}')
    print(f"{user_input_timezone} local time   :",datetime.now(us_local))

    # converting time
    us_local = parsed_time.astimezone(pytz.timezone(f'{user_input_timezone}'))
    print("After comparing time from\ndata "
          f"with {user_input_timezone} local time ", us_local)



if __name__ == "__main__":
    time_from_data= retrive_time(user_input)
    parsed_time =time_parsed(time_from_data)
    convert_timezone(parsed_time)








# time = input("Enter  time in :->>  Hour:Minutes:Seconds :")
# time_object =datetime.strptime(time,"%H:%M:%S")             #convert string to date time object
# time_object=time_object.strftime("%H:%M:%S")                #formatting of date time object
# print(time_object)



# zones = pytz.all_timezones
# zones = list(zones)
# print(zones)


# seoulTime = pytz.timezone('Asia/Seoul')
# timeinseoul = datetime.now(seoulTime)
# print(timeinseoul)



# data on which the timezone function is going to use
people_data = {"Trootech":[{
  "emp_name": "Deep_pathak",
  "emp_number" : "12345",
  "emp_joining_time":'04/04/21 09:31:22'
  },
{
  "emp_name": "Smit_kumar_patel",
  "emp_number":"54321",
  "emp_joining_time":'05/04/21 09:00:42'
  }]}

c=people_data["Trootech"][0]['emp_name']



print(50*"--")
# converting different timezones

# local = datetime.now(pytz.utc)
# print("local DateTime:", local.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
#
# us_local = local.astimezone(pytz.timezone('US/Central'))
# print("US Central DateTime:",us_local.strftime("%Y:%m:%d %H:%M:%S %Z %z"))
#
# now_tokyo= datetime.now(pytz.timezone("Asia/Tokyo"))
# print("tokyo Date time::",now_tokyo)






# now = datetime.now()
# print(now)
# now_utc= datetime.now(pytz.utc)          # for standard timezone
# print("utc",now_utc)
# now_utc= datetime.now(pytz.UTC)          #both are same
#
# now_usa= datetime.now(pytz.timezone('US/Central'))
# print("us time::",now_usa)
#
# soeul = datetime.now(pytz.timezone('Asia/Seoul'))
# print("seoul  DateTime", soeul)
#
# # TimeZone Information Using tzinfo
# print("Time zone",soeul.tzname())
# print("UTC off set :",soeul.utcoffset())
# print("daylight  standard tiem :",soeul.dst())
#
#



#
# print(50*"--")
# #Working with Local Timezones
#
# fmt = '%Y-%m-%d %H:%M:%S %Z%z'
# tz_india = pytz.timezone('Asia/Kolkata')
# print(tz_india)
# ist_local = tz_india.localize(datetime.now())
# print("Indian Standard Time::", ist_local.strftime(fmt))
#


# country= []
# continent = []
# other = []
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
