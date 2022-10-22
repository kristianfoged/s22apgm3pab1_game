class Gamekeeper:
    # level
    # counter
     # round
    # targets
    # hits
    # clock_ticker

    def __init__(self,round):
        self.level=1
        self.counter=1
        self.factor=-1
        self.round=round
        self.addround=1       
        self.addtarget=0
        self.addhit=1
        self.targets=0
        self.hits=0
        self.clock_ticker=0
        self.add_clock_tick=1

 
    def modifscore(self):
        self.counter = self.counter + self.factor

    def modiflevel(self):
        self.level = self.level + self.factor

    def modifround(self):
        self.round = self.round + self.addround

    def modiftargets(self):
        self.targets = self.targets + self.addtarget

    def modifhits(self):
        self.hits = self.hits + self.addhit

    def modifclockticker(self):
        self.clock_ticker = self.clock_ticker + self.add_clock_tick

    def gameover(self):
        retval=False
        if self.round == 10:
            retval=True
        return(retval)