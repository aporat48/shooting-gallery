import pygame as pg
import  math
from  config import *
import random
import os
missed = 0
class Bullet(pg.sprite.Sprite):
    def __init__(self,p,x,y):
        global missed
        super().__init__()
        # self.image = pg.draw.circle(screen,((254,114,0)),(100,100),10)
        self.image = pg.Surface((10,10))
        self.image.fill((254,114,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed = 20
        self.plt = p.last_point
        self.pl3 = p.pl3
        angle = (math.atan2(self.plt.y- self.pl3.y, self.plt.x-self.pl3.x ))
        self.dx = math.cos(angle)* self.speed
        self.dy = math.sin(angle)* self.speed
        self.x = x
        self.y = y

    def update(self):
        global missed
        self.x += self.dx
        self.y += self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        if self.rect.bottom < 0:
            missed += 1
            self.kill()
                
    
    def draw(self):
        print('draw')

    

    
