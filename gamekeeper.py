class Gamekeeper:
    # level
    # counter
    # liv
    # round
    # targets
    # hits
    # seconds

    def __init__(self,numoflives):
        self.level=1
        self.counter=1
        self.liv=numoflives
        self.factor=-1
        self.round=1
        self.addround=1       
        self.addtarget=0
        self.addhit=0
        self.targets=0
        self.hits=0

    def modifscore(self):
        self.counter = self.counter + self.factor

    def modiflevel(self):
        self.level = self.level + self.factor

    def modifliv(self):
        self.liv = self.liv - self.factor

    def modifround(self):
        self.round = self.round + self.addround

    def modiftargets(self):
        self.targets = self.targets + self.addtarget

    def modifhits(self):
        self.hits = self.hits + self.addhit

    def gameover(self):
        retval=False
        if self.liv == 0:
            retval=True
        return(retval)