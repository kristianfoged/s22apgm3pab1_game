import sys
##import pyautogui
from random import randint
import pygame 
import pandas as pd
# samme bibliotek
from gamekeeper import Gamekeeper
from bird import Bird
from skeet import Skeet
# importer variable
from skeet_game_config import *
# import list
df_game_rounds = pd.read_csv(r'game_rounds.csv')
df_shooting_position = pd.read_csv(r'shooting_positions.csv')


speed_bird=randint(1,4)



pygame.init()
#set screen
screen=pygame.display.set_mode((width,height))
# font for text
myfont = pygame.font.SysFont(font_name,font_size)
# init clock from time
clock=pygame.time.Clock()
# init gamekeeper - styrer optælling
mygamekeep = Gamekeeper(starting_round)
skeets_blue=[]
skeets=[]
# create rects around stuff you want to target
croshair_rect = croshair.get_rect(center=(width/get_rect_divisor,height/get_rect_divisor))
bird_rect=bird.get_rect(center=(xpos_bird,ypos_bird))
skeet_blue_rect=skeet_blue_image.get_rect(center=(xpos_skeet_blue/get_rect_divisor,ypos_skeet_blue/get_rect_divisor))
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
            screen.blit(startscreen,(upper_corner_x,upper_corner_y))
            textobj_game_title  =myfont.render(game_title_text,(default),(white))
            textobj_start       =myfont.render(start_command_text,(default),(white))
            screen.blit(textobj_start,(textobj_start_pos)) 
            screen.blit(textobj_game_title,(textobj_game_title_pos)) 
        # modify moving objects
        else :   
            for number in range(25):
                xpos_skeet = xpos_skeet_blue
                ypos_skeet = ypos_skeet_blue
                speed_skeet = speed_skeet
                skeet_col = "blue"
                image_skeet = skeet_blue_image
                skeet = Skeet(xpos_skeet,ypos_skeet,skeet_col,image_skeet,speed_skeet)
                skeets.append(skeet)
            
            
            bird_rect = bird.get_rect(center=(xpos_bird, ypos_bird))
            skeet_blue_rect = bird.get_rect(center=(xpos_skeet_blue, ypos_skeet_blue))
            xpos_skeet_blue=xpos_skeet_blue+1
            #skeet_blue_dict["xpos_blue"]=skeet_blue_dict["xpos_blue"]+skeet_blue_dict["speed_blue"]
            #put paint stuff on screen

            screen.blit(bird,bird_rect)
            screen.blit(skeet_blue_image,skeet_blue_rect)
            screen.blit(croshair,croshair_rect)
            
        #update screen
        pygame.display.update()
    #tick the clock
        clock.tick(clock_value)
        #print(pygame.mouse.get_pos())
        print(skeets)
     