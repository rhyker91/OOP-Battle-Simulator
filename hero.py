import random

class Hero:
    """The hero blueprint will be implemented later in the project."""
    def __init__(self, name):
        self.name=name
        self.health=123
        self.attack_power=21

    def attack(self):
        return random.randint(1,self.attack_power)

    def take_damage(self, damage):
        health=self.health-damage
        if health < 0:
            health-=health
        return health
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
