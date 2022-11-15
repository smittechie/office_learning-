from random import randint
hero_life = 0
villian_life = 0

def inc_hero_life(life):
    global hero_life
    hero_life+= life

def dec_hero_life(life):
    global hero_life
    hero_life-= life

def inc_villian_life(life):
    global villian_life
    villian_life+= life

def dec_villian_life(life):
    global villian_life
    villian_life-= life


def get_all_superheros():
    # Super_heros
    IRONMAN = {"name" : "Ironman", "attack_power" :  250, "life" : 1000}
    BLACKWIDOW = {"name" : "Blackwidow", "attack_power" : 250, "life" : 1000}
    SPIDERMAN = {"name" : "Spiderman", "attack_power" : 250, "life" : 1000}
    HULK = {"name" : "Hulk", "attack_power" : 250, "life" : 1000}
    Superheros = [IRONMAN, BLACKWIDOW, SPIDERMAN, HULK]
    return Superheros
def get_superhero(index):
    superhero = get_all_superheros()
    if index <= len(superhero):
        return superhero[index]
    else:
        return None

def get_all_supervillian():
    #Super_villian
    THANOS = {"name" : "Thanos", "attack_power" : 1500, "life" : 1500}
    REDSKULL = {"name" : "Redskull ", "attack_power" : 300, "life" : 800}
    PROXIMA = {"name" : "Proxima", "attack_power" : 320, "life" : 800}
    Supervillians = [THANOS,REDSKULL,PROXIMA]
    return Supervillians

def get_supervillains(index):
    supervillan = get_all_supervillian()
    if index <= len(supervillan):
        return supervillan[index]
    else:
        return None

def attack():
    for attack_number in range(3):
        hero_index = randint(0,3)
        villian_index = randint(0,2)

        current_hero = get_superhero(hero_index)
        current_villain = get_superhero(villian_index)

        if current_villain and current_hero:
            simulate_attack(attack_number, current_villain,current_hero)
        else:
            print("their is no hero and villian to fight ")

def simulate_attack(attack_number , current_villian , current_hero):
    #set life
    inc_hero_life(current_hero['life'])
    inc_villian_life(current_villian['life'])
    print(
        f"Attack :{attack_number} =>{current_hero['name']} is going to fight with {current_villian['name']}"
          )
    #reduce life
    dec_hero_life(current_villian['attack_power'])
    dec_villian_life(current_hero['attack_power'])

def winorloss():
    WIN_MSG= "You sucessfully saved zorton "
    LOST_MSG  = "Avengers are killed Zorton is captured "

    #Win and loose
    if hero_life >= villian_life:
        print(WIN_MSG)
    else:
        print(LOST_MSG)

def main():
    attack()
    winorloss()
main()