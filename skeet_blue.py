import numpy as np
from random import randint

import pygame.transform

class Skeet_blue():
    # attributter - egenskaber
#Skeet_blue;Skeet_red;Position;Target_sum
    # konstruktør - jordemoder, en speciel metode
    # bird = {"xpos": xpos, "ypos": ypos, "link": link_bird, "counter": counter, "name": "test", "speed": speed}
    def __init__(self,xpos_skeet_blue,ypos_skeet_blue,skeet_blue_image,speed_skeet):
        self.xpos_skeet = xpos_skeet_blue
        self.ypos_skeet = ypos_skeet_blue
        self.image_skeet = skeet_blue_image
        self.speed_skeet = speed_skeet
    # metoder - handlinger
    # standard inventory: Getters and Setters

    def SetXpos(self,xpos_skeet):
        self.xpos_skeet+self.speed_skeet

    def SetYpos(self,ypos_skeet):
        self.ypos_skeet=self.ypos_skeet

    def move(self):
        self.xpos_skeet = self.xpos_skeet+self.speed_skeet

    def blitme(self, screen):
        screen.blit(self.image_skeet, (self.xpos_skeet,self.ypos_skeet))