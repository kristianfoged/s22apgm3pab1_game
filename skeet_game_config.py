import pygame
font_size = 50
font_name = "couriernew"
white=(250,250,250)
default = (0,0,0)
upper_corner_x = 0
upper_corner_y = 0
waiting_posx = -1
waiting_posy = -1
round_seconds_to = 1
get_rect_divisor = 2
shots_counter_divisor = 2
black=(0,0,0)
width=1200
height=800
bottombarheight     =200
bottombar_ypos      = height - bottombarheight
clock_value         = 60
height_playfield    = height - bottombarheight
textobj_interval    = 50
textobj_xpos1        = 100
textobj_xpos2        = 700

textobj_round_pos           = (textobj_xpos1,bottombar_ypos)
textobj_shots_pos           = (textobj_xpos1,bottombar_ypos+textobj_interval*1)
textobj_countdown_pos       = (textobj_xpos1,bottombar_ypos+textobj_interval*2)
textobj_shot_aviable_pos    = (textobj_xpos1,bottombar_ypos+textobj_interval*3)

textobj_targets_pos = (textobj_xpos2,bottombar_ypos)
textobj_hits_pos    = (textobj_xpos2,bottombar_ypos+textobj_interval*1) 
textobj_seconds_pos = (textobj_xpos2,bottombar_ypos+textobj_interval*2) 




game_title_text = ('SUMMER GAMES 1984 SKEET SHOOTING') 
start_command_text  = ('Press s to start')
quit_command_text  = ('Press q to quit')
game_over_text = ('Game over')

textobj_start_pos =  (400,400)
textobj_quit_pos =  (400,600)
textobj_game_title_pos =  (110,100)
delta_x=int(width/10)
delta_y=int(height_playfield /10)
xpos_bird=width-delta_x
ypos_bird=height_playfield-delta_y

# faste positioner på de to skeet-tårne
start_xpos_skeet_blue = (55)
start_ypos_skeet_blue = (300)
xpos_skeet_blue= 55
ypos_skeet_blue= 300
start_xpos_skeet_red = (1151)
start_ypos_skeet_red = (330)
xpos_skeet_red=1151
ypos_skeet_red=330
speed_skeet=4
speed_skeet_blue=4
speed_skeet_red=4
starting_round = 0

# init load images
bg=pygame.image.load("resources/skeet3.png")
bar=pygame.image.load("resources/black_bar.png")
bird=pygame.image.load("resources/bird.png")
skeet_blue_image=pygame.image.load("resources/skeet_blue.png")
skeet_blue_hit=pygame.image.load("resources/skeet_blue_hit.png")
skeet_red_image=pygame.image.load("resources/skeet_red.png")
croshair=pygame.image.load("resources/crosshair.png")
startbut=pygame.image.load("resources/start.png")
startscreen=pygame.image.load("resources/start_screen.png")

