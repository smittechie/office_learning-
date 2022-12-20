from datetime import date ,datetime
from datetime import timedelta

fmt = "%H:%M"
count = 0
def fun1():
    while True:
        store_start_time = input("please enter the start time of store in HH:MM :-")
        time_validation = store_start_time.split(":")
        if 0<=int(time_validation[0])<=24 and 0<=int(time_validation[1])<=60  :
            return store_start_time
        else:
            print("wrong input")
# fun1()

def fun2():
    while True:
        store_close_time = input("please enter the end time of store in HH:MM :-")
        time_validation = store_close_time.split(":")
        if 0<=int(time_validation[0])<=24 and 0<=int(time_validation[1])<=60 :
                return store_close_time
        else:
            print("wrong input")
a=fun1()
b=fun2()


store_start_time =datetime.strptime(a,fmt)
store_close_time =datetime.strptime(b,fmt)

store_start_time_f =store_start_time.strftime("%H:%M")
store_close_time_f =store_close_time.strftime("%H:%M")


print("---------------Welcome to my store---------------- \n")

def fun3():
    while True:
        time_cal = input(f"My store timing is {store_start_time_f} to {store_close_time_f} \n"
                  "please enter the time you want to book in HH:MM :- ")
        time_validation = time_cal.split(":")
        if 0 <= int(time_validation[0]) <= 24 and 0 <= int(time_validation[1]) <= 60:
            return time_cal
        else:
            print("wrong input")
time_cal= fun3()
time_cal = time_cal.split(":")
fmt = "%H:%M"
time  =datetime.strptime(a,fmt)
time =time.strftime("%H:%M")
print(f'you have booked for "{time}" hours:minutes')

total_min = int(time_cal[0])*60 + int(time_cal[1])*1                           ## input time in minute
print(total_min)                                                                                                             #testing
store_time_cal =store_close_time - store_start_time
seconds = store_time_cal.total_seconds()
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
store_time = int(hours)*60 + int(minutes)*1
print("total store time is ",store_time,"minutes")                                                                            #store time in minute


updated = store_start_time +timedelta(minutes=(total_min))
updated =updated.strftime("%H:%M")

if total_min>store_time:
    print(f"time exceeds please enter under {store_time} minute time")
else:
    print(f"your slot is booked from {store_start_time_f} to  {updated} \n")


a=  store_time // total_min -1
print("The number of remaining slots are ",a ,"\n")

count=0
while a >count:
    old_time= updated
    updated = datetime.strptime(updated, fmt)
    updated = updated + timedelta(minutes=(total_min))
    updated = updated.strftime("%H:%M")
    print("remaining slots are from ",old_time,"to ",updated)
    count +=1

