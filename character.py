
class animal:
    def __init__(self,type,hp,attack):
        self.type = type
        self.hp = hp
        self.attack = attack

        

class player:
    def __init__(self,name1,hp1,attack1,inv, health):
        self.name1 = name1
        self.hp1 = hp1
        self.attack1 = attack1
        self.inv = inv
        self.health = health
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move (self, direction):
        if direction == "up":
            self.y += 1
        elif direction == "down":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
        elif direction == "right":
            self.x += 1



class enemy: 
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Items:
    def __init__(self,title,heal,boost):
        self.title = title
        self.heal = heal
        self.boost = boost
        

class inventory:
    def __init__(self, good):
        self.good = good