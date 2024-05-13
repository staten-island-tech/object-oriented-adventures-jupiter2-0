import random


def take_damage(self, damage):
        self.halth -= damage

def alive(self):
        return self.health < 0
    
def attack(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage")
    
def battle(player, enemy):
        print("Battle begins")

def take_damage():
    