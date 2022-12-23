import json

class Banking :

    def __init__(self,name,account_balance,bike_value =50,car_value =100):
        self.name = name
        self.balance = account_balance
        self.bike = bike_value
        self.car = car_value
        self.data ={self.name:[{"car":self.car ,
                                "bike":self.bike ,
                                "balance":self.balance}]}
    def frontend(self):
        print("-----  Welcome to Citadel LLC  -----")
        print("Welcome to Citadel LLC :", self.name)
        print("Your balance is ", self.balance)

        # ask_out = input("want to go out \n"
        #                 "     y or n :- ").lower()
        # if ask_out == "n":
        #     self.showdata(self.data)
        #     quit()
        choice_ride = input("print what you want to ride on \n"
                            "a = bike\n"
                            "b = taxi :->")
        self.calulation(choice_ride)
        ask = input('Want to continue? ')
        if ask == 'y':
            self.frontend()
        else:
            self.showdata(self.data)
            # quit()

    @property
    def account_balance(self):
        return self.balance
    @account_balance.setter
    def account_balance(self, value):
        self.balance=self.balance-value

    @property
    def bike_value(self):
        return self.bike
    @bike_value.setter
    def bike_value(self,value):
        self.bike = self.bike + value

    @property
    def car_value(self):
        return self.car
    @car_value.setter
    def car_value(self, value):
        self.car = self.car + value

    def calulation(self, choice_ride):
        bike = 50
        car =100
        databse ={self.name}
        front_output = choice_ride
        if front_output =="a":
            self.account_balance= bike
            self.bike_value= bike
            self.data = {self.name:[{"car":self.car -100,
                                "bike":self.bike -50,
                                "balance":self.balance}]}
            print(self.data)
            with open('finaldata.json', 'a') as f:
                # json.dump(self.data, f, indent=4)
                # breakpoint()
                f.write(json.dumps(self.data,indent=4))
                f.seek(0)
                f.write(",")

            self.showdata(self.data)

        elif front_output == "b":
            self.account_balance = car
            self.car_value = car
            self.data = {self.name:[{
                                "car":self.car -100,
                                "bike": self.bike - 50,
                                "balance":self.balance}]}
            with open('finaldata.json', 'a') as f:
                # json.dump(self.data, f, indent=4)
                f.write(json.dumps(self.data ,indent=4))
                f.write(",")
                # print(file_data)

            self.showdata(self.data)


    def showdata(self,data):
         print(data)



obj = Banking("Raj",20000)
print(obj.frontend())
# print(obj.data)
#
# with open('finaldata.json','r') as f :
#     breakpoint()
#     data = f.readlines()
#     if data:
#         name = ''
#         balance = 0
#         for item in data:
#             if item == 'balance':
#                 balance = item['balance']
#                 name = item['name']
#         obj = Banking(name, balance)
#     else:
#         obj = Banking('Raj', 20000)



