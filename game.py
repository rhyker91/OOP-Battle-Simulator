from goblin import Goblin
from hero import Hero
import random
from time import sleep
ARENA_NAME = "The Iron Lung"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    gobline = Goblin("Kibble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{gobline.name} enters the arena with {gobline.health} health.")
    print("But no hero has answered the call... yet.")

    hero = Hero("Bart")
    print("Hero Name: ",hero.name,"| Health: ", hero.health)

    def battle(hero: Hero, enemy: Goblin):
        print('Our hero meets and enemy', "in a battle to the death!", "\nThe battle starts with a coin toss!")
        rant=random.randint(1,2)
        if rant==1:
            sleep(1)
            print("It lands on Heads... Hero attacks first!")
            sleep(1)
            gob=hero.attack()
            goblin.health -= gob
            print("Hero dealt",gob,"damge, let the fight commence!")
        else:
            sleep(1)
            print("It lands on Tails... Goblin attacks first!")
            sleep(1)
            he=goblin.attack()
            hero.health -= he
            print("Goblin dealt", he, "damage, let the fight commence!")
        while hero.is_alive() and goblin.is_alive():
            ran=random.randint(1,2)
            if ran==1:
                g=hero.attack()
                goblin.health -= g
                print("Hero Strikes the Enemy for ", g, "damage! Enemy has ", goblin.health,"remaining!")
                sleep(0.3)

            else:
                w=goblin.attack()
                hero.health -= w
                print("Enemy striked the Hero for ", w, "damage! Enemy has ", hero.health,"remaining!")
                sleep(0.3)
        if hero.health>0:
            print("Hero Wins! Health:", hero.health)
        else:
            print("Goblin Wins! Health:", goblin.health)

    battle(hero=Hero("Bart"), enemy=Goblin("Goblin"))
if __name__ == "__main__":
    main()
