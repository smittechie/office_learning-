from typing import Final
from random import randint

# Super_heros
IRONMAN = {"name" : "Ironman", "attack_power" :  250, "Life" : 1000}
BLACKWIDOW = {"name" : "Blackwidow", "attack_power" : 250, "Life" : 1000}
SPIDERMAN = {"name" : "Spiderman", "attack_power" : 250, "Life" : 1000}
HULK = {"name" : "Hulk", "attack_power" : 250, "Life" : 1000}

#Super_villian
THANOS = {"name" : "Thanos", "attack_power" : 1500, "Life" : 1500}
REDSKULL = {"name" : "Redskull ", "attack_power" : 300, "Life" : 800}
PROXIMA = {"name" : "Proxima", "attack_power" : 320, "Life" : 800}

# All Superhero and Super villains
Superheros = [IRONMAN,BLACKWIDOW,SPIDERMAN,HULK]
Supervillians = [THANOS,REDSKULL,PROXIMA]


IRONMAN_ATTACK_POWER :Final[int] = 250
BLACKWIDOW_ATTACK_POWER :Final[int] = 180
SPIDERMAN_ATTACK_POWER :Final[int] = 260
HULK_ATTACK_POWER :Final[int] = 300

#Helper varaiblr
hero_life = 0
villian_life = 0

WIN_MSG= "You sucessfully saved zorton "
LOST_MSG  = "Avengers are killed Zorton is captured "


# Attack

for attack in range(3):

    # each  iteration get a new hero and supervillian
    hero_index = randint(0,3)
    villian_index = randint(0,2)

    #helper varialble
    current_superhero = Superheros[hero_index]
    current_supervillian =Supervillians[villian_index]
    #life
    hero_life += current_superhero["Life"]
    villian_life+= current_supervillian["Life"]
    print(f"Attack : {attack +1 } => {current_superhero['name']} is going to fight with {current_supervillian['name']}")

    #attack
    hero_life -= current_supervillian["attack_power"]
    villian_life -= current_superhero["attack_power"]

print("="*50)

#Win and loose
if hero_life >= villian_life:
    print(WIN_MSG)
else:
    print(LOST_MSG)