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
        pass
np1 = npc("Nurse")
np2 = npc("Merchant")
np3 = npc("8")


class player:
    def __init__(self,name1,hp1,attack1,inv):
        self.name1 = name1
        self.hp1 = hp1
        self.attack1 = attack1
        self.inv = inv

        pass

class Boss:
    def __init__(self,name2,hp2,attack2):
        self.name2 = name2
        self.hp2 = hp2
        self.attack2 = attack2

        pass

class inventory:
    def __init__(self,Items):
        self.Items = Items
        pass

class Items:
    def __init__(self,title,heal,boost):
        self.title = title
        self.heal = heal
        self.boost = boost
        pass
