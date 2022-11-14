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
superheros = [IRONMAN,BLACKWIDOW,SPIDERMAN,HULK]
supervillians = [THANOS,REDSKULL,PROXIMA]


IRONMAN_ATTACK_POWER  = 250
BLACKWIDOW_ATTACK_POWER  = 180
SPIDERMAN_ATTACK_POWER  = 260
HULK_ATTACK_POWER  = 300

hero_life  = 0
villian_life = 0

Win_msg ="Avengers are the winner "
Lost_msg = "Thanos win "

for attack in range (3):
    hero_index = randint(0,3)
    vilian_index = randint(0,2)

    current_hero = superheros[hero_index]
    current_villian = supervillians[vilian_index]

    #life
    hero_life += current_hero['Life']
    villian_life += current_villian['Life']

    print(
        f" Attack : {attack} =>{current_hero['name']}is going to fight with {current_villian['name']}"
    )

    #fight

    hero_life -= current_villian['attack_power']
    villian_life -= current_hero['attack_power']


print("="*50)

#Win and loose
if hero_life >= villian_life:
    print(Win_msg)
else:
    print(Lost_msg)