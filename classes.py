class dialouge:
    def __init__(self,dStart,dA,dnpc,dP,dB,dEnd):
        dStart = dStart
        self.dA = dA
        self.dnpc = dnpc
        self.dP = dP
        self.dB = dB
        self.dEnd = dEnd

class battle:
    def __init__(self,):
        pass

class animal:
    def __init__(self,type,hp,attack):
        self.type = type
        self.hp = hp
        self.attack = attack

        pass

class npc:
    def __init__(self,name):
        self.name = name
        self.dialouge = dialouge

        pass

class player:
    def __init__(self,name1,hp1,attack1,inv):
        self.name1 = name1
        self.hp1 = hp1
        self.attack1 = attack1
        self.inv = inv
    def __init__(self, x, y):
        self.x = x
        self.y = y

        pass

class enemy: 
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack


class Boss:
    def __init__(self,name2,hp2,attack2):
        self.name2 = name2
        self.hp2 = hp2
        self.attack2 = attack2

        pass

class Items:
    def __init__(self,title,heal,boost):
        self.title = title
        self.heal = heal
        self.boost = boost
        pass


