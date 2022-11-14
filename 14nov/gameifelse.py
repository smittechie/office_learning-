

ironman_power = 180
captianA_power = 390
thor_power = 560
hulk_power = 100

thanos_life = 1500

Win_msg="Thanos defeated "
Lost_msg = "Avengers are dead "
MSG = """
----------------------------------------------------------------------------------------------------
Zorton is under attack ,choose a pair that will attack the Thanos
1)Ironman and Blackwidow
2)Blackwidow and Spiderman
3)Spiderman and Hulk
4)Hulk and Ironman
----------------------------------------------------------------------------------------------------
"""


attack_num = 0
choice = 0
while True:
    if thanos_life <= 0 and attack_num <= 3:
        print(Win_msg)
        break
    elif attack_num > 3:
        print(Lost_msg)
        break


    print(MSG)
    choice = int(input("enter yout choice between 1-4 : "))
    if choice == 1:
        print("Ironman and Blackwidow is attacking Thanos")
        thanos_life = thanos_life - captianA_power - ironman_power
        attack_num +=1
    elif choice == 2:
        print("Blackwidow and Spiderman is attacking Thanos")
        thanos_life = thanos_life - captianA_power - thor_power
        attack_num +=1
    elif choice == 3:
        print("Spiderman and Hulk are attacking Thanos")
        thanos_life = thanos_life - thor_power - hulk_power
        attack_num +=1
    elif choice ==4 :
        print("Hulk and Ironman are attacking Thanos")
        thanos_life = thanos_life - hulk_power - ironman_power
        attack_num +=1
