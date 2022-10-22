import sys
from random import randint
import pygame
#from pyrsistent import T
from gamekeeper import Gamekeeper
from bird import Bird

#define variables
white=(250,250,250)
default = (0,0,0)
round_seconds_to = 1
black=(0,0,0)
width=1200
height=800
bottombarheight=200
clock_value = 120
height_playfield = height - bottombarheight

delta_x=int(width/10)
delta_y=int(height_playfield /10)

xpos_bird=width-delta_x
ypos_bird=height_playfield-delta_y

xpos_skeet_blue=200
ypos_skeet_blue=500

speed_bird=randint(1,4)
speed_skeet_blue=1


pygame.init()
#set screen
screen=pygame.display.set_mode((width,height))
# font for text
# myfont = pygame.font.SysFont("rockwellextrabold",50)
myfont = pygame.font.SysFont("couriernew",50)


# init clock from time
clock=pygame.time.Clock()

# init gamekeeper
mygamekeep = Gamekeeper(1)
# init load images
bg=pygame.image.load("resources/skeet3.png")
bar=pygame.image.load("resources/black_bar.png")
bird=pygame.image.load("resources/bird.png")
skeet_blue=pygame.image.load("resources/skeet_blue.png")
skeet_red=pygame.image.load("resources/skeet_red.png")
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.png")
startscreen=pygame.image.load("resources/start_screen.png")
# create rects around stuff you want to target

croshair_rect = croshair.get_rect(center=(width/2,height/2))
bird_rect=bird.get_rect(center=(xpos_bird,ypos_bird))
#skeet_blue_rect=bird.get_rect(center=(xpos_skeet_blue,ypos_skeet_blue))

#  create rect
active = False
counter = 1
level = 1
gamedict={"level":0, "round":1,"targets":0,"hits":0,"clock_ticker":0,"seconds":0}
#start the loop
while True:
    if mygamekeep.gameover():
        active = False
        #screen.fill(black)
        screen.blit(startscreen,(0,0))
        textobj_start=myfont.render(f'Game over',(0,0,0),(255,255,255))
        screen.blit(textobj_start,(400,400))  
        pygame.quit()
        sys.exit()
    else:
        # start counting seconds
        if active:
            mygamekeep.modifclockticker()
        # check events with for-loop
        croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #what should happen?
                if croshair_rect.colliderect(bird_rect):
                    mygamekeep.modifscore()
                    xpos_bird=width
                    # random ypos for bird
                    ypos_bird=randint(0,height_playfield)
            if event.type == pygame.MOUSEMOTION:
                pass
                #croshair_rect=croshair.get_rect(center = event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    active=not active
        #put background on screen
        screen.blit(bg,(0,0))
        screen.blit(bar,(0,600))
        textobj_targets=myfont.render(f'TARGETS:    {mygamekeep.targets}',(default),(white))
        textobj_hits=myfont.render(f'HITS:       {mygamekeep.hits}',(default),(white))
        textobj_seconds=myfont.render(f'SECONDS:    {round((mygamekeep.clock_ticker/clock_value),round_seconds_to)}',(default),(white))
        textobj_score=myfont.render(f'Evil score: {mygamekeep.counter}',(default),(white))
        screen.blit(textobj_targets,(700,600)) 
        screen.blit(textobj_hits,(700,650)) 
        screen.blit(textobj_seconds,(700,700))        
        screen.blit(textobj_score,(700,750)) 

        if not active:
            screen.blit(startscreen,(0,0))
            textobj_start=myfont.render(f'Press s to start',(0,0,0),(255,255,255))
            screen.blit(textobj_start,(400,400)) 
           
        # modify moving objects
        else :   
            bird_rect = bird.get_rect(center=(xpos_bird, ypos_bird))
            #put paint stuff on screen
            # put counter on screen
 
            screen.blit(bird,bird_rect)
            screen.blit(croshair,croshair_rect)
            
        #update screen
        pygame.display.update()
    #tick the clock
        clock.tick(clock_value)
        #print(gamedict["seconds"])
      