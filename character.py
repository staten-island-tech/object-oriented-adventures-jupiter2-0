
class Animal:
    def __init__(self,type,hp,attack):
        self.type = type
        self.hp = hp
        self.attack = attack

        
class Player:
    def __init__(self,name,hp,attack, health):
        self.name = name
        self.hp1 = hp
        self.attack1 = attack
        self.health = health

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
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack 


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