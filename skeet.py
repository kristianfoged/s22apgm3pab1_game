import numpy as np
from random import randint

import pygame.transform

class Skeet():
    # attributter - egenskaber
#Skeet_blue;Skeet_red;Position;Target_sum
    # konstruktør - jordemoder, en speciel metode
    # bird = {"xpos": xpos, "ypos": ypos, "link": link_bird, "counter": counter, "name": "test", "speed": speed}
    def __init__(self,xpos_skeet,ypos_skeet,skeet_col,image_skeet,speed_skeet):
        self.xpos_skeet = xpos_skeet
        self.ypos_skeet = ypos_skeet
        self.skeet_col = skeet_col 
        self.image_skeet = image_skeet
        self.speed_skeet = speed_skeet
    # metoder - handlinger
    # standard inventory: Getters and Setters

    def SetXpos(self,xpos_skeet):
        self.xpos_skeet=xpos_skeet

    def SetYpos(self,ypos_skeet):
        self.ypos_skeet=ypos_skeet

    def blitme(self, screen):
        screen.blit(self.link, (self.xpos_skeet,self.ypos_skeet))