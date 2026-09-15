import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 15

    def attack(self):
        damage= 10
        Crit = 5
        if random.randint(1, 6) == 4:
            return Crit+damage
        else:
            return damage 
          
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
         return self.health > 0