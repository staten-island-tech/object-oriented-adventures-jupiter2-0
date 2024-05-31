class companion:
    def __init__(self,type,hp,attack):
        self.type = type
        self.hp = hp
        self.attack = attack

    def battle(self, enemy):
        pass

class Player:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory

    def move(self, direction, grid_size):
        pass


class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, companion):
        pass

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

class Nurse:
    def heal(self, companion):
        companion.health = 100 


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



