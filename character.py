class companion:
    def __init__(self,type,hp,attack):
        self.type = type
        self.hp = hp
        self.attack = attack

    def battle(self, enemy):
        pass


class Player():
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.inventory = Inventory()
        self.companions = []

    def move(self, direction, maze):
        if direction == 'up' and self.y > 0 and maze[self.y - 1][self.x] != '[ ]':
            self.y -= 1
        elif direction == 'down' and self.y < len(maze) - 1 and maze[self.y + 1][self.x] != '[ ]':
            self.y += 1
        elif direction == 'left' and self.x > 0 and maze[self.y][self.x - 1] != '[ ]':
            self.x -= 1
        elif direction == 'right' and self.x < len(maze[0]) - 1 and maze[self.y][self.x + 1] != '[ ]':
            self.x += 1

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_player(self, companion):
        pass


class Nurse:
    def heal(self, companion):
        companion.hp = 100 


import random 
class Battle(companion):
    def take_damage(self, damage):
        companion.health -= damage

    def is_alive(self):
        return companion.health > 0

    def attack_enemy(companion, enemy):
        damage = random.randint(1, companion.attack)
        enemy.damage(damage)
        print(f"{companion.name} attacks {enemy.name} for {damage} damage!")

    def battle(companion, enemy):
        print(f"Battle begins between {companion.name} and {companion.name}!")

        while companion.is_alive() and enemy.alive():
            companion.attack_enemy(companion)
            if enemy.alive():
                companion.attack_enemy(companion)

        if companion.is_alive():
            print(f"{companion.name} wins the battle!")
        else:
            print(f"{enemy.name} wins the battle!")



class Inventory:
    def __init__(self):
        self.items = []
        self.potions = 3

    def add_item(self, item):
        self.items.append(item)

    def use_potion(self, character):
        if self.potions > 0:
            self.potions -= 1
            character.health += 20
            print(f"{character.name} used a potion and gained 20 HP. Current health: {character.health}")
        else:
            print("No more potions left!")

    def show_inventory(self):
        return self.items, self.potions

