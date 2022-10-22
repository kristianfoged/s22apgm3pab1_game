import sys
##import pyautogui
from random import randint
import pygame 
import pandas as pd


# samme bibliotek
from gamekeeper import Gamekeeper
from bird import Bird
from skeet_game_config import *

# import list
df_game_rounds = pd.read_csv(r'game_rounds.csv')

# import variables

#define variables
##white=(250,250,250)
##default = (0,0,0)
##upper_corner_x = 0
##upper_corner_y = 0
#round_seconds_to = 1
#black=(0,0,0)
#width=1200
#height=800
#bottombarheight     =200
#bottombar_ypos      = height - bottombarheight
#clock_value         = 120
#height_playfield    = height - bottombarheight
#textobj_interval    = 50
#textobj_xpos        = 725
#textobj_targets_pos = (textobj_xpos,bottombar_ypos)
#textobj_hits_pos    = (textobj_xpos,bottombar_ypos+textobj_interval*1) 
#textobj_seconds_pos = (textobj_xpos,bottombar_ypos+textobj_interval*2) 
#textobj_score_pos   = (textobj_xpos,bottombar_ypos+textobj_interval*3) 

game_title_text = ('SUMMER GAMES 1984 SKEET SHOOTING') 
start_command_text  = ('Press s to start')
game_over_text = ('Game over')
textobj_start_pos =  (400,400)
textobj_game_title_pos =  (110,100)

delta_x=int(width/10)
delta_y=int(height_playfield /10)

xpos_bird=width-delta_x
ypos_bird=height_playfield-delta_y


xpos_skeet_blue=55
ypos_skeet_blue=300
speed_skeet_blue=1
#start_xpos_skeet_blue =(56)
#start_ypos_skeet_blue =(320)

speed_bird=randint(1,4)


croshair_pos_round1 = (400,400)


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
skeet_blue_image=pygame.image.load("resources/skeet_blue.png")
skeet_blue_hit=pygame.image.load("resources/skeet_blue_hit.png")

skeet_red=pygame.image.load("resources/skeet_red.png")
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.png")
startscreen=pygame.image.load("resources/start_screen.png")

skeets_blue=[]

# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(width/2,height/2))
bird_rect=bird.get_rect(center=(xpos_bird,ypos_bird))
skeet_blue_rect=skeet_blue_image.get_rect(center=(xpos_skeet_blue/2,ypos_skeet_blue/2))

#skeet_blue_rect=bird.get_rect(center=(xpos_skeet_blue,ypos_skeet_blue))

active = False

#start the loop
while True:
    if mygamekeep.gameover():
        active = False
        #screen.fill(black)
        screen.blit(startscreen,(upper_corner_x,upper_corner_y))
        textobj_start=myfont.render(game_over_text,(default),(white))
        screen.blit(textobj_start,(textobj_start_pos))  
        pygame.quit()
        sys.exit()
    else:



        # start counting seconds
        if active:
            mygamekeep.modifclockticker()
                    # initialisere skeets
        # check events with for-loop
        croshair_rect=croshair.get_rect(center = pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #what should happen? - bird
                if croshair_rect.colliderect(bird_rect):
                    mygamekeep.modifscore()
                    xpos_bird=width
                    # random ypos for bird
                    ypos_bird=randint(0,height_playfield)
                 #what should happen? - skeet blue
                if croshair_rect.colliderect(skeet_blue_rect):
                    mygamekeep.modifhits()
                    xpos_skeet_blue=-100
                    ypos_skeet_blue=-100


            if event.type == pygame.MOUSEMOTION:
                pass
                ##croshair_rect=croshair.get_rect(center = event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    active=not active
        #put background on screen
        screen.blit(bg,(upper_corner_x,upper_corner_y))
        screen.blit(bar,(upper_corner_x,bottombar_ypos))
        textobj_targets=myfont.render(f'TARGETS:    {mygamekeep.targets}',(default),(white))
        textobj_hits=myfont.render(f'HITS:       {mygamekeep.hits}',(default),(white))
        textobj_seconds=myfont.render(f'SECONDS:    {round((mygamekeep.clock_ticker/clock_value),round_seconds_to)}',(default),(white))
        textobj_score=myfont.render(f'Evil score: {mygamekeep.counter}',(default),(white))
        screen.blit(textobj_targets,(textobj_targets_pos)) 
        screen.blit(textobj_hits,(textobj_hits_pos)) 
        screen.blit(textobj_seconds,(textobj_seconds_pos))        
        screen.blit(textobj_score,(textobj_score_pos)) 

        # startskærm
        if not active:
            screen.blit(startscreen,(0,0))
            
            textobj_game_title  =myfont.render(game_title_text,(default),(white))
            textobj_start       =myfont.render(start_command_text,(default),(white))
            screen.blit(textobj_start,(textobj_start_pos)) 
            screen.blit(textobj_game_title,(textobj_game_title_pos)) 
        # modify moving objects
        else :   
            bird_rect = bird.get_rect(center=(xpos_bird, ypos_bird))
            skeet_blue_rect = bird.get_rect(center=(xpos_skeet_blue, ypos_skeet_blue))
            xpos_skeet_blue=xpos_skeet_blue+1
            #skeet_blue_dict["xpos_blue"]=skeet_blue_dict["xpos_blue"]+skeet_blue_dict["speed_blue"]
            #put paint stuff on screen
            # put counter on screen

 
            screen.blit(bird,bird_rect)
            screen.blit(skeet_blue_image,skeet_blue_rect)
            screen.blit(croshair,croshair_rect)
            
        #update screen
        pygame.display.update()
    #tick the clock
        clock.tick(clock_value)
        
     