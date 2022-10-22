import numpy as np
from random import randint

import pygame.transform


class Bird():
    # attributter - egenskaber

    # konstruktør - jordemoder, en speciel metode
    # bird = {"xpos": xpos, "ypos": ypos, "link": link_bird, "counter": counter, "name": "test", "speed": speed}
    def __init__(self,xpos,ypos,link,name,speed,direction,widthbounce):
        self.xpos=xpos
        self.ypos=ypos
        self.link=link
        self.name=name
        self.speed=speed
        self.direction=direction
        self.widthbounce=widthbounce
    # metoder - handlinger
    # standard inventory: Getters and Setters

    def SetXpos(self,xpos):
        self.xpos=xpos

    def SetYpos(self,ypos):
        self.ypos=ypos

    def move(self):
        if self.xpos >= 0 and self.xpos <= self.widthbounce:
            self.direction=self.direction*-1
            self.xpos = self.xpos - self.speed
        # sjov flaskende
        #self.xpos=self.xpos-np.sin(self.ypos*0.6)-((randint(1,4))/4)
        # jævn flok
        #self.xpos = self.xpos - np.sin(self.speed * 0.6) - ((randint(1, 4)) / 4)
        # test1
        #self.xpos = self.xpos - np.sin(self.speed * ((randint(1, 4)) / 4)) - ((randint(1, 4)) / 4)

        # test2
        #self.xpos=self.xpos-np.sin(self.ypos*((randint(1, 4)) / 4))-((randint(1,4))/4)

    def moveup(self):
         self.ypos=self.ypos-+np.sin((self.xpos*0.7))

    def blitme(self, screen):
        screen.blit(self.link, (self.xpos,self.ypos))