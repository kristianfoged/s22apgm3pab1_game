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
        self.shots=0
        self.addshots=1
        self.hits=0
        self.clock_ticker=0
        self.add_clock_tick=1
        self.round_countdown = 0
        self.round_countdown_starter = 300
  
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

    def modifshots(self):
        self.shots = self.shots + self.addshots

    def modifclockticker(self):
        self.clock_ticker = self.clock_ticker + self.add_clock_tick

    # ligger extra tid til for hver runde
    def modifroundcountdown(self):
        self.round_countdown = self.round_countdown + self.round_countdown_starter 

    # tager løbende tid af klokken
    def modifrunningcountdown(self):
        self.round_countdown = self.round_countdown - (self.clock_ticker/600)


    def to_main(self):
        if self.shots == 5:
            active = False
       

    def gameover(self):
        retval=False
        if self.shots == 30:
            retval=True
        return(retval)