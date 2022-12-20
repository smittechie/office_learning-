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

def break_time():
    while True:
        ask_break_time = input("please enter the break time of store in HH:MM :-")
        break_validation = ask_break_time.split(":")
        if 0<=int(break_validation[0])<=24 and 0<=int(break_validation[1])<=60 :
                return ask_break_time
        else:
            print("wrong input")


a=fun1()
b=fun2()
c= break_time()

store_start_time =datetime.strptime(a,fmt)
store_close_time =datetime.strptime(b,fmt)
ask_break_time =datetime.strptime(c,fmt)


store_start_time_f =store_start_time.strftime("%H:%M")
store_close_time_f =store_close_time.strftime("%H:%M")
ask_break_time_f =ask_break_time.strftime("%H:%M")


## time formatting

break_cal = c.split(":")                                                                      ## break of time  format
breakk_time  =datetime.strptime(c,fmt)
breakk_time =breakk_time.strftime("%H:%M")
print(f'Break time is  "{breakk_time}" hours:minutes')
total_break_min = int(break_cal[0])*60 + int(break_cal[1])*1                                    #break time in minutes
print("Break in minutes ",total_break_min)


print("---------------Welcome to my store---------------- \n")

def Booking_time():
    while True:
        time_cal = input(f"My store timing is {store_start_time_f} to {store_close_time_f} \n"
                  "please enter the time you want to book in HH:MM :- ")
        time_validation = time_cal.split(":")
        if 0 <= int(time_validation[0]) <= 24 and 0 <= int(time_validation[1]) <= 60:
            return time_cal
        else:
            print("wrong input")
time_cal= Booking_time()
time_cal = time_cal.split(":")
fmt = "%H:%M"
time  =datetime.strptime(a,fmt)
time =time.strftime("%H:%M")
print(f'you have booked for "{time}" hours:minutes')


total_min = int(time_cal[0])*60 + int(time_cal[1])*1                                            ## booking slot time in minute


store_time_cal =store_close_time - store_start_time                                             ## total store open time in time-format
seconds = store_time_cal.total_seconds()
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
store_time = int(hours)*60 + int(minutes)*1

'''validation '''
if store_time < total_break_min :
    print("Break time is big then the  store time ")
    quit()
elif store_time < total_min:
    print("Booking time is greater then store time ")
    quit()
print("total store time is ",store_time,"minutes")                                                       #store time in minute


updated_datetime = store_start_time +timedelta(minutes=(total_min))
time_updated =updated_datetime.strftime("%H:%M")
updated_datetime+=timedelta(minutes=(total_break_min))                                       ## 1900-01-01 11:00:00
updated_string = updated_datetime.strftime("%H:%M")


if total_min>store_time:
    print(f"time exceeds please enter under {store_time} minute time")
else:
    print(f"your slot is booked from {store_start_time_f} to  {time_updated} \n")



total_slot=  (store_time // (total_min + total_break_min)) -1
print("The number of remaining slots are ", total_slot ,"\n")
print("Total break is  ",total_break_min," minutes ",'\n')

count=0
while total_slot >count:
    old_time= updated_string
    updated_string = datetime.strptime(updated_string, fmt)
    updated_string = updated_string + timedelta(minutes=(total_min))                          #+timedelta(minutes=(total_break_min))
    time_updated = updated_string.strftime("%H:%M")
    print("remaining slots are from ",old_time,"to ",time_updated)
    updated_string += timedelta(minutes=(total_break_min))
    updated_string = updated_string.strftime("%H:%M")
    count +=1