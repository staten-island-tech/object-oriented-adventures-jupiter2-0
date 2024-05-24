class dialogue:
    def __init__(self,dA,dnpc,dB,dEnd):
        
        self.dA = dA
        self.dnpc = dnpc
        self.dB = dB
        self.dEnd = dEnd
    pass
class map:
    def __init__(self,Map):
        self.Map = Map
        pass

class battle:
    def __init__(self,take_damage,alive,take_dmg,attack):
        self.take_damage = take_damage
        self.alive = alive
        self.take_dmg = take_dmg
        self.attack = attack
        pass

class animal:
    def __init__(self,type,hp):
        self.type = type
        self.hp = hp
        self.battle = battle

        pass

class npc:
    def __init__(self,name):
        self.name = name
        self.dialouge = dialogue

        pass

class player:
    def __init__(self,name1,hp1,attack1,inv,health,move):
        self.name1 = name1
        self.hp1 = hp1
        self.attack1 = attack1
        self.inv = inv
        self.health = health
        self.move = move
    def __init__(self, x, y):
        self.x = x
        self.y = y

        pass

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
        pass

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

