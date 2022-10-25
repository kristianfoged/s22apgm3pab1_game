class Gamekeeper:
    # level
    # counter
     # round
    # targets
    # hits
    # clock_ticker

    def __init__(self,round):
        self.level=0
        self.addlevel=1
        self.counter=1
        self.factor=-1
        self.round=round
        self.addround=1       
        self.addhit=1
        self.targets=0
        self.addtarget=2
        self.shots=0
        self.addshots=1
        self.hits=0
        self.clock_ticker=0
        self.add_clock_tick=1
        self.round_countdown = 0
        self.round_countdown_starter = 100
        self.blue_skeet_active = 0
        self.red_skeet_active = 0
        self.dummy_skeet_active = 0
        self.shots_aviable=0
        self.addshots_aviable=1

    def modifscore(self):
        self.counter = self.counter + self.factor

    def modiflevel(self):
        self.level = self.level + self.addlevel

    def modifround(self):
        self.round = self.round + self.addround

    def modiftargets(self):
        self.targets = self.targets + self.addtarget

    def modifhits(self):
        self.hits = self.hits + self.addhit 
        self.round_countdown = self.round_countdown_starter/2 # genstart tælleren ved hit

    def modifhits_blue(self):
        self.hits = self.hits + self.addhit 
        self.blue_skeet_active = 0
        self.round_countdown = self.round_countdown_starter/2 # genstart tælleren ved hit

    def modifhits_red(self):
        self.hits = self.hits + self.addhit 
        self.red_skeet_active = 0
        self.round_countdown = self.round_countdown_starter/2 # genstart tælleren ved hit

    def modifstarting_blue(self):
        self.blue_skeet_active = 1
        
    def modifstarting_red(self):
        self.red_skeet_active = 1

    def modifstarting_dummy(self):
        self.dummy_skeet_active = 1

    def modif_startingshots(self):
        self.shots_aviable = 2

    def modifterminating_blue(self):
        self.blue_skeet_active = 0

    def modifterminating_red(self):
        self.red_skeet_active = 0

    def modifterminating_dummy(self):
        self.dummy_skeet_active = 0       

    def modifshots(self):
        self.shots = self.shots + self.addshots
        self.shots_aviable = self.shots_aviable - self.addshots_aviable/2

    def modifclockticker(self):
        self.clock_ticker = self.clock_ticker + self.add_clock_tick

    # ligger extra tid til for hver runde
    def modifroundcountdown(self):
        self.round_countdown = self.round_countdown_starter 

    # tager løbende tid af klokken
    def modifrunningcountdown(self):
        self.round_countdown = self.round_countdown - (self.clock_ticker)

    def modifnewgame(self):
        self.level=0
        self.addlevel=1
        self.counter=1
        self.factor=-1
        self.round=round
        self.addround=1       
        self.addhit=1
        self.targets=0
        self.addtarget=2
        self.shots=0
        self.addshots=1
        self.hits=0
        self.clock_ticker=0
        self.add_clock_tick=1
        self.round_countdown = 0
        self.round_countdown_starter = 100
        self.blue_skeet_active = 0
        self.red_skeet_active = 0
        self.shots_aviable=0
        self.addshots_aviable=1

    
    def to_main(self):
        if self.shots == 5:
            active = False

    def gameover(self):
        retval=False
        if self.round == 27:
            retval=True
        return(retval)