import json

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
                        "     y or n :- ").lower()
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
            data = {self.name:[{
                                "bike": 50,
                                "balance":self.balance}]}
            return data
        elif front_output == "b":
            self.account_balance = taxi
            data = {self.name: [{
                                 "taxi": 100,
                                 "balance":self.balance}]}
            return data


    def json_update(self):
        cancel =""
        print("cancel printing",cancel)
        count = 0
        while cancel != "n":
            import json
            # count = 0
            print("initail count ",count)
            if count == 0:
                with open('data3.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f,indent=4)
                    # f.write(",")
                    f.close()
                    count+=1
                    cancel = input("want to cancel or continue y or n :->")
                    if cancel =="n":
                        continue
                    print("updated count",count)
                    self.frontend()
                # self.json_update()

            else:
                with open('data3.json','r+') as file1:
                    print("Aaa")

                    file_data = json.load(file1)
                    # file_data.write(",")
                    print(file_data)

                    file_data[self.name].append(data)
                    file1.seek(0)
                    json.dump(file_data, file1, indent = 2)
                    # file_data.close()
                self.frontend()
                #self.json_update()

obj = Banking("Smit",10000000)
obj2 = Banking("amit",10000)
# data = obj.calulation()
# obj.json_update()
data = obj2.calulation()
print(data)
obj2.json_update()


a = input("ask  do you want to show the balance "
          "y or n :-")
if a == "y" :
    print("Your balance is ",obj2.account_balance)
else:
    print("thank you dear customer ")


def showjson():
    with open('data3.json','r') as f1:
        aceess_data  = json.load(f1)
        for i in aceess_data["amit"]:
            print(i)

val = input("do you want to see the log :-> ")
if val == "y":
    showjson()
else:
    print("Thank you")