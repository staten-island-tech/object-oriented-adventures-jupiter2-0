class dialouge:
    def __init__(self,dStart,dA,dnpc,dP,dB,dEnd):
        dStart = dStart
        self.dA = dA
        self.dnpc = dnpc
        self.dP = dP
        self.dB = dB
        self.dEnd = dEnd
    def dnpc(self):
        while True:
            dialouge.dnpc = ("Would you like to heal your teammate? (Y/N)")
            if dialouge.dnpc == "Y":
                