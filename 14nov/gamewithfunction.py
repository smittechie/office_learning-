
from random import randint


#----------------------------------Life--------------------------------------------------
#Helper varaiblr
hero_life = 0
villian_life = 0

def inc_hero_life(life):
    """increse  hero life """

    global hero_life
    hero_life += life

def dec_hero_life(life):
    """decrese  hero life """

    global hero_life
    hero_life -= life

def inc_villian_life(life):
    """increse  villian life """

    global villian_life
    villian_life += life


def dec_villian_life(life):
    """decrese  villian life """

    global villian_life
    villian_life -= life



#------------------------------------Superheros------------------------------------------
def get_all_superheros():
    IRONMAN = {"name" : "Ironman", "attack_power" :  250, "life" : 1000}
    BLACKWIDOW = {"name" : "Blackwidow", "attack_power" : 250, "life": 1000}
    SPIDERMAN = {"name" : "Spiderman", "attack_power" : 250, "life" : 1000}
    HULK = {"name" : "Hulk", "attack_power" : 250, "life" : 1000}
    Superheros = [IRONMAN,BLACKWIDOW,SPIDERMAN,HULK]
    return Superheros

def get_superhero(index):
    superheros = get_all_superheros()
    if index <len(superheros):
        return superheros[index]
    else:
        return None

#----------------------------------Villians --------------------------------------------------------------
def get_all_supervillians():
    THANOS = {"name": "Thanos", "attack_power": 1500, "life": 1500}
    REDSKULL = {"name": "Redskull ", "attack_power": 300, "life": 800}
    PROXIMA = {"name": "Proxima", "attack_power": 320, "life": 800}
    Supervillians = [THANOS, REDSKULL, PROXIMA]
    return Supervillians

def get_supervillian(index):
    supervillians = get_all_supervillians()
    if index <len(supervillians):
        return supervillians[index]
    else:
        return None


def attack():
    for attack_num in range(3):
        # each  iteration get a new hero and supervillian
        hero_index = randint(0, 3)
        villian_index = randint(0, 2)

        # helper varialble
        superhero = get_superhero(hero_index)
        supervillian = get_supervillian(villian_index)

        if superhero and supervillian:
            #attack
            simulate_attack(attack_num,superhero,supervillian)
        else:
            print("Error ! No superhero or suoervillian to fight ")

def simulate_attack(attack_num , superhero,supervillian):
    # set life
    inc_hero_life(superhero["life"])
    inc_villian_life(supervillian["life"])

    print(
        f"Attack : {attack_num + 1} => {superhero['name']} is going to fight with {supervillian['name']}"
    )

    # attack
    dec_hero_life(supervillian["attack_power"])
    dec_villian_life(superhero["attack_power"])

def winorloose():
    WIN_MSG = "You sucessfully saved zorton "
    LOST_MSG = "Avengers are killed Zorton is captured "

    print("="*50)

    #Win and loose
    if hero_life >= villian_life:
        print(WIN_MSG)
    else:
        print(LOST_MSG)


def main():
    attack()
    winorloose()


main()