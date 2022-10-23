import sys
##import pyautogui
from random import randint
import pygame 
import pandas as pd
# samme bibliotek
from gamekeeper import Gamekeeper
from bird import Bird
from skeet_blue import Skeet_blue
# importer variable
from skeet_game_config import *
# import list
df_game_rounds = pd.read_csv(r'game_rounds.csv')
df_shooting_position = pd.read_csv(r'shooting_positions.csv')

Blue_skeets=[]

speed_bird=3

pygame.init()
#set screen
screen=pygame.display.set_mode((width,height))
# font for text
myfont = pygame.font.SysFont(font_name,font_size)
# init clock from time
clock=pygame.time.Clock()
# init gamekeeper - styrer optælling
mygamekeep = Gamekeeper(starting_round)

# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(width/get_rect_divisor,height/get_rect_divisor))
bird_rect=bird.get_rect(center=(xpos_bird,ypos_bird))
skeet_blue_rect=skeet_blue_image.get_rect(center=(xpos_skeet_blue/get_rect_divisor,ypos_skeet_blue/get_rect_divisor))
#skeet_blue_rect=bird.get_rect(center=(xpos_skeet_blue,ypos_skeet_blue))
active = False

xpos_skeet_blue
ypos_skeet_blue


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
                    mygamekeep.modifshots()
                    mygamekeep.modifroundcountdown()
                    xpos_skeet_blue=5
                    ypos_skeet_blue=50
                    speed_skeet_blue=0
                else:
                    mygamekeep.modifshots()
                 #what should happen? - skeet blue
                if croshair_rect.colliderect(skeet_red_rect):
                    mygamekeep.modifhits()
                    mygamekeep.modifshots()
                    mygamekeep.modifroundcountdown()
                    xpos_skeet_red=25
                    ypos_skeet_red=85
                    speed_skeet_red=0
                else:
                    mygamekeep.modifshots()
            if event.type == pygame.MOUSEMOTION:
                pass
                ##croshair_rect=croshair.get_rect(center = event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    active=not active
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        #put background on screen
        screen.blit(bg,(upper_corner_x,upper_corner_y))
        screen.blit(bar,(upper_corner_x,bottombar_ypos))
        textobj_targets=myfont.render(f'TARGETS:    {mygamekeep.targets}',(default),(white))
        textobj_hits=myfont.render(f'HITS:       {mygamekeep.hits}',(default),(white))
        textobj_seconds=myfont.render(f'SECONDS:    {round((mygamekeep.clock_ticker/clock_value),round_seconds_to)}',(default),(white))
        textobj_shots=myfont.render(f'SHOTS:      {round((mygamekeep.shots/shots_counter_divisor))}',(default),(white))
        textobj_round=myfont.render(f'ROUND:      {mygamekeep.level}',(default),(white))
        textobj_countdown=myfont.render(f'COUNTDOWN:  {round(mygamekeep.round_countdown)}',(default),(white))


        screen.blit(textobj_targets,(textobj_targets_pos)) 
        screen.blit(textobj_hits,(textobj_hits_pos)) 
        screen.blit(textobj_seconds,(textobj_seconds_pos))        
        screen.blit(textobj_shots,(textobj_shots_pos)) 
        screen.blit(textobj_round,(textobj_round_pos)) 
        screen.blit(textobj_countdown,(textobj_countdown_pos)) 

        # startskærm
        if not active:
            screen.blit(startscreen,(upper_corner_x,upper_corner_y))
            textobj_game_title  =myfont.render(game_title_text,(default),(white))
            textobj_start       =myfont.render(start_command_text,(default),(white))
            textobj_quit       =myfont.render(quit_command_text,(default),(white))
            screen.blit(textobj_start,(textobj_start_pos)) 
            screen.blit(textobj_quit,(textobj_quit_pos)) 
            screen.blit(textobj_game_title,(textobj_game_title_pos)) 
        # modify moving objects
        else :   
            bird_rect = bird.get_rect(center=(xpos_bird, ypos_bird))
            skeet_red_rect = skeet_red_image.get_rect(center=(xpos_skeet_red, ypos_skeet_red))
            skeet_blue_rect = skeet_blue_image.get_rect(center=(xpos_skeet_blue, ypos_skeet_blue))
           #skeet_blue_rect = skeet_blue_image.get_rect(center=(xpos_skeet_blue, ypos_skeet_blue))
            #put paint stuff on screen
            xpos_bird=xpos_bird-speed_bird
            xpos_skeet_red = xpos_skeet_red - speed_skeet_red
            xpos_skeet_blue = xpos_skeet_blue + speed_skeet_blue
            screen.blit(bird,bird_rect)
            screen.blit(skeet_red_image,skeet_red_rect)
            screen.blit(skeet_blue_image,skeet_blue_rect)
            screen.blit(croshair,croshair_rect)
            mygamekeep.modifrunningcountdown()
            if mygamekeep.round_countdown <= 0:
                speed_skeet_blue = speed_skeet
                xpos_skeet_blue = start_xpos_skeet_blue
                ypos_skeet_blue = start_ypos_skeet_blue
                xpos_skeet_blue = xpos_skeet_blue + speed_skeet_blue
                mygamekeep.modifroundcountdown()
                    

        #update screen
        pygame.display.update()
    #tick the clock
        clock.tick(clock_value)
        
        #print(pygame.mouse.get_pos())