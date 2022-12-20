
class Banking :
    Transaction_log = {}
    Expense=0

    def __init__(self,name,account_balance ):
        self.name = name
        self.balance = account_balance

    def frontend(self):
        print("-----  Welcome to Citadel LLC  -----")

        print("Welcome to Citadel LLC :", self.name)

        print("Your balance is ", self.balance)

        ask_out = input("want to go out \n"
                        "y or n :- ").lower()
        if ask_out == "n":
            quit()
        choice_ride = input("print what you want to ride on \n"
                            "a = bike\n"
                            "b = taxi :->")
        return choice_ride


    @property
    def account_balance(self):
        return self.balance

    @account_balance.setter
    def account_balance(self, value):
        self.balance=self.balance-value


    def calulation(self):
        bike = 50
        taxi = 100
        front_output = self.frontend()
        if front_output =="a":
            self.account_balance= bike
            data = {self.name:[{"bike": 50}]}
            return data
        elif front_output == "b":
            self.account_balance = taxi
            data = {self.name: [{"taxi": 100}]}
            return data



# obj = Banking("Smit",10000000)
obj2 = Banking("amit",10000)

data = obj2.calulation()
print(data)


import json
with open('data.json', 'w') as f:
    json.dump(data, f,indent=4)

a = input("ask  do you want to show the balance "
          "y or n :-")
if a == "y" :
    print("Your balance is ",obj2.account_balance)
else:
    print("thank you dear customer ")



def showjson():
    f = open('data.json','r',encoding='utf-8-sig')
    aceess_data  = json.load(f)
    for i in aceess_data["amit"]:
        print(i)

val = input("do you want to see th e log :-> ")
if val == "y":
    showjson()
else:
    print("Thank you")