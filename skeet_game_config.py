import pygame
font_size = 50
font_name = "couriernew"
white=(250,250,250)
default = (0,0,0)
upper_corner_x = 0
upper_corner_y = 0
round_seconds_to = 1
get_rect_divisor = 2
black=(0,0,0)
width=1200
height=800
bottombarheight     =200
bottombar_ypos      = height - bottombarheight
clock_value         = 120
height_playfield    = height - bottombarheight
textobj_interval    = 50
textobj_xpos        = 725
textobj_targets_pos = (textobj_xpos,bottombar_ypos)
textobj_hits_pos    = (textobj_xpos,bottombar_ypos+textobj_interval*1) 
textobj_seconds_pos = (textobj_xpos,bottombar_ypos+textobj_interval*2) 
textobj_score_pos   = (textobj_xpos,bottombar_ypos+textobj_interval*3)
game_title_text = ('SUMMER GAMES 1984 SKEET SHOOTING') 
start_command_text  = ('Press s to start')
game_over_text = ('Game over')
textobj_start_pos =  (400,400)
textobj_game_title_pos =  (110,100)
delta_x=int(width/10)
delta_y=int(height_playfield /10)
xpos_bird=width-delta_x
ypos_bird=height_playfield-delta_y

# faste positioner på de to skeet-tårne
xpos_skeet_blue=55
ypos_skeet_blue=300
xpos_skeet_red=1151
ypos_skeet_red=330
speed_skeet=1
speed_skeet_blue=1
starting_round = 1

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

