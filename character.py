import json

class Inventory:
    def __init__(self):
        self.items = []
        self.potions = 5

    def add_item(self, item):
        self.items.append(item)

    def show_inventory(self):
        return self.items

    def use_potion(self, character):
        if self.potions > 0:
            self.potions -= 1
            character.health += 20
            if character.health > 50:  
                character.health = 50
            print(f"{character.name} used a potion and gained 20 HP. Current health: {character.health}")
        else:
            print("No more potions left!")

class Companion:
    def __init__(self, name, attacks, hp):
        self.name = name
        self.attacks = attacks
        self.hp = hp
        self.max_hp = hp

    def attack(self, move):
        if move in self.attacks:
            return self.attacks[move]
        else:
            return 0

class Player:
    def __init__(self, start_x, start_y):
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
        companion.hp = companion.max_hp

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
