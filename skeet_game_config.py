import pygame


no_of_targets = 3
no_of_rounds = 4
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


font_size = 50
font_name = "couriernew"
white=(250,250,250)
default = (0,0,0)
upper_corner_x = 0
upper_corner_y = 0
waiting_posx = -1
waiting_posy = -1
out_of_sight_posx_left = -200
out_of_sight_posx_right = width + 200
out_of_sight_posx_right_dummy = width*1.7

# lerduernes bane er et 2grads polinomie f(x) = ax2 + bx + c 
# konstantleddet leveres via udgangspunktet, som er tårnenes højde, hvilket kommer fra flowet
flight_power  = 2

flight_red_a_high = 21
flight_red_a_low = 15
flight_blue_a_high = 20
flight_blue_a_low = 14
flight_a_divisor = -10000000

flight_red_b_high = 21
flight_red_b_low = 17
flight_blue_b_high = 9
flight_blue_b_low = 7
flight_b_divisor = 10

flight_red_a  = -0.0000015 # lerduen falder når den kommer længere frem
flight_red_b  = 1.9 # rød har en stigende bane
flight_blue_a = -0.0000015
flight_blue_b = 0.8 # blå har en flad bane



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

# Placering af elementer på start/slutskæmr
textobj_game_title_pos =  (110,100)
textobj_start_pos =  (400,250)
textobj_quit_pos =  (400,350)
textobj_endscore_targets_pos =  (400,500)
textobj_endscore_hits_pos =  (400,600)


delta_x=int(width/10)
delta_y=int(height_playfield /10)
xpos_bird=width-delta_x
ypos_bird=height_playfield-delta_y
speed_bird=3
# faste positioner på de to skeet-tårne
start_xpos_skeet_blue = (55)
start_ypos_skeet_blue = (300)
xpos_skeet_blue= 55
ypos_skeet_blue= 300
start_xpos_skeet_red = (1151)
start_ypos_skeet_red = (330)
xpos_skeet_red=1151
ypos_skeet_red=330
speed_skeet=(6)
speed_skeet_blue=5
speed_skeet_red=5
starting_round = 0

start_xpos_skeet_dummy = (1)
#start_ypos_skeet_dummy = (1100)
xpos_skeet_dummy= 1
#ypos_skeet_dummy= 1100

# init load images
bg=pygame.image.load("resources/skeet3.png")
bar=pygame.image.load("resources/black_bar.png")
bird=pygame.image.load("resources/bird.png")
skeet_blue_image=pygame.image.load("resources/skeet_blue.png")
skeet_blue_hit=pygame.image.load("resources/skeet_blue_hit.png")
skeet_red_image=pygame.image.load("resources/skeet_red.png")
croshair=pygame.image.load("resources/crosshair.png")
#startbut=pygame.image.load("resources/start.png")
startscreen=pygame.image.load("resources/start_screen.png")

# values for gamekeeper

zero_value = 0