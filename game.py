from goblin import Goblin
from hero import Hero


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
    print("Hero Name: ",hero.name,"Health: ", hero.health)

if __name__ == "__main__":
    main()
