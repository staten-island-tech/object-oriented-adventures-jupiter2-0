<<<<<<< HEAD

class Player:
    def __init__(self,name):
        self.name = name

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.inventory = Inventory()

    def move(self, direction):
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1

    def get_position(self):
        return self.x, self.y
    


class npc:
    def __init__(self, name, dialogue):
        self.name = name 
        self.dialogue = dialogue



class Items:
    def __init__(self,name,heal,boost):
        self.name = name
        self.heal = heal
        self.boost = boost
        
=======
import json
>>>>>>> vicky

class Inventory:
    def __init__(self):
        self.items = []
        self.potions = 5

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        return self.items

    def use_potion(self, companion):
        if self.potions > 0:
            print(f"Using potion on {companion.name}")
            companion.hp = min(companion.hp + 20, companion.max_hp)
            self.potions -= 1
        else:
            print("No potions left!")

class Companion:
    def __init__(self, name, attacks, hp):
        self.name = name
        self.attacks = attacks
        self.hp = hp
        self.max_hp = hp

<<<<<<< HEAD


import random 
class companion:
    def __init__(self, name, health=100, attack=10, defense=5):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        print(f"{self.name} takes {actual_damage} damage.")

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)


class Enemy():
    def __init__(self, name, health=50, attack=8, defense=3):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        print(f"{self.name} takes {actual_damage} damage.")

    def attack_player(self, companion):
        damage = random.randint(1, self.attack)
        print(f"{self.name} attacks {companion.name} for {damage} damage.")
        companion.take_damage(damage)




class Battle(companion, Enemy):
    def __init__(self, companion, enemy):
        self.companion = companion
        self.enemy = enemy

    def start_battle(self):
        print(f"A battle between {self.companion.name} and {self.enemy.name} begins!")

        while self.companion.is_alive() and self.enemy.is_alive():
            self.companion.attack_enemy(self.enemy)
            if self.enemy.is_alive():
                self.enemy.attack_player(self.player)
            else:
                print(f"{self.enemy.name} is defeated!")

            if self.companion.is_alive():
                print(f"{self.companion.name}'s health: {self.companion.health}")
                print(f"{self.enemy.name}'s health: {self.enemy.health}")
            else:
                print(f"{self.companion.name} is defeated!")




class buyer:
    def __init__(self, name, budget):
        self.name = name 
        self.budget = budget
        
    def buy(self, seller, good, price):
        if self.budget >= price:
            self.budget -= price
            seller.sell(good, price)

class seller:
    def __init__(self,name, iven, price):
        self.name = name
        self.iven = iven 
        self.price = price

    def sell(self, good, price):
        if good in self.iven:
            self.iven.remove(good)


class Buyer:
    def __init__(self, name, budget):
        self.name = name 
        self.budget = budget
        
    def buy(self, seller, good, price):
        if self.budget >= price:
            self.budget -= price
            seller.sell(good, price)

class Seller:
    def __init__(self,name, iven, price):
        self.name = name
        self.iven = iven 
        self.price = price

    def sell(self, good, price):
        if good in self.iven:
            self.iven.remove(good)
""" class dialogue:
    def __init__(self,Nurse1,Merchant1,Violet1,dB,dEnd):
        self.dnpc = Nurse1
        self.Merchant1 = Merchant1
        self.Violet1 = Violet1
        self.dB = dB
        self.dEnd = dEnd
    pass """
=======
    def attack(self, move):
        if move in self.attacks:
            return self.attacks[move]
        else:
            return 0

class Player:
    def __init__(self, name, start_x, start_y):
        self.name = name
        self.x = start_x
        self.y = start_y
        self.inventory = Inventory()
        self.companion = None

    def move(self, direction, map):
        if direction == 'up' and self.y > 0 and map[self.y - 1][self.x] != '[ ]':
            self.y -= 1
        elif direction == 'down' and self.y < len(map) - 1 and map[self.y + 1][self.x] != '[ ]':
            self.y += 1
        elif direction == 'left' and self.x > 0 and map[self.y][self.x - 1] != '[ ]':
            self.x -= 1
        elif direction == 'right' and self.x < len(map[0]) - 1 and map[self.y][self.x + 1] != '[ ]':
            self.x += 1
        else:
            print("You can't move in that direction!")

    def get_position(self):
        return self.x, self.y

class Nurse:
    def __init__(self, position):
        self.position = position
        self.dialogue = "Welcome to the Nurse's Station! I will heal your companion."

    def heal(self, companion):
        print(self.dialogue)
        companion.hp = 50

class Boss:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.attacks = attacks

    def attack(self, move):
        if move in self.attacks:
            return self.attacks[move]
        else:
            return 0

def load_companions():
    with open('companion.json', 'r') as f:
        return [Companion(**companion) for companion in json.load(f)]
>>>>>>> vicky
