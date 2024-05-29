
class Animal:
    def __init__(self,type,hp,attack):
        self.type = type
        self.hp = hp
        self.attack = attack

        
class Player:
    def __init__(self,name,hp,attack, health, alive):
        self.name = name
        self.hp1 = hp
        self.attack = attack
        self.health = health
        self.alive = alive

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


class Enemy: 
    def __init__(self, name, health, attack, alive, damage):
        self.name = name
        self.health = health
        self.attack = attack 
        self.alive = alive
        self.damage = damage

class Items:
    def __init__(self,name,heal,boost):
        self.name = name
        self.heal = heal
        self.boost = boost
        

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.items:
                print(f"- {item}")


import random 
class Battle(Player):
    def take_damage(self, damage):
        Player.health -= damage

    def is_alive(self):
        return Player.health > 0

    def attack_enemy(Player, enemy):
        damage = random.randint(1, Player.attack)
        Enemy.damage(damage)
        print(f"{Player.name} attacks {Enemy.name} for {damage} damage!")

    def battle(player, enemy):
        print(f"Battle begins between {Player.name} and {Player.name}!")

        while player.is_alive() and Enemy.alive():
            player.attack_enemy(player)
            if Enemy.alive():
                player.attack_enemy(player)

        if player.is_alive():
            print(f"{Player.name} wins the battle!")
        else:
            print(f"{Enemy.name} wins the battle!")

