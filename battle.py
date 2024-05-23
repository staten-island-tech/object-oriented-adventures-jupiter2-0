import random

def take_damage(self, damage):
        self.health -= damage

def alive(self):
        return self.health < 0
    
def attack(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage")
    
def take_dmg(player, enemy):
        player.health - attack

        