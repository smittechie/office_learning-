from typing import Final

IRONMAN_ATTACK_POWER :Final[int] = 250
BLACKWIDOW_ATTACK_POWER :Final[int] = 180
SPIDERMAN_ATTACK_POWER :Final[int] = 260
HULK_ATTACK_POWER :Final[int] = 300

THNAOS_LIFE:Final[int] = 1500

WIN_MSG= "You sucessfully saved zorton "
LOST_MSG  = "Avengers are killed Zorton is captured "

MSG = """
----------------------------------------------------------------------------------------------------
Zorton is under attack ,choose a pair that will attack the Thanos
1)Ironman and Blackwidow
2)Blackwidow and Spiderman
3)Spiderman and Hulk
4)Hulk and Ironman
----------------------------------------------------------------------------------------------------
"""

choice = 0
attack_num  = 0
while True:
    if THNAOS_LIFE <= 0 and attack_num <=3:
        #win
        print(WIN_MSG)
        break
    elif attack_num >3 :
        #loose
        print(LOST_MSG)
        break


    print(MSG)
    choice = int(input("Enter your choice "))
    if choice == 1:
        print("Ironman and Blackwidow is attacking Thanos")
        THNAOS_LIFE = THNAOS_LIFE- IRONMAN_ATTACK_POWER-BLACKWIDOW_ATTACK_POWER
        attack_num +=1
    elif choice == 2:
        print("Blackwidow and Spiderman is attacking Thanos")
        THNAOS_LIFE = THNAOS_LIFE- BLACKWIDOW_ATTACK_POWER - SPIDERMAN_ATTACK_POWER
        attack_num += 1
    elif choice == 3:
        print("Spiderman and Hulk are attacking Thanos")
        THNAOS_LIFE = THNAOS_LIFE - SPIDERMAN_ATTACK_POWER- HULK_ATTACK_POWER
        attack_num += 1
    elif choice == 4 :
        print("Hulk and Ironman are attacking Thanos")
        THNAOS_LIFE = THNAOS_LIFE-HULK_ATTACK_POWER-IRONMAN_ATTACK_POWER
        attack_num += 1


