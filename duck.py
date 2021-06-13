import pygame as pg
from  config import *
import random
import os
class Duck(pg.sprite.Sprite):
    scale = 1
    def __init__(self,id):
        super().__init__()
        self.image1 = self.load_image('duck-right1.png')
        self.image2 = self.load_image('duck-left1.png')
        (_,_,w,h) =self.image1.get_rect()
        # self.image = pg.Surface((w,h))
        self.image = self.image1
        self.rect = self.image.get_rect()
        # print(self.rect.center)
        self.speed = random.randint(2,7)
        self.id = id
        if self.id == 0:
            self.rect.y = LINE1
            Duck.scale = 1
        elif self.id == 1:
            self.rect.y = LINE2
            Duck.scale = 1
        else:
            self.rect.y = LINE3
            Duck.scale = 1
        # self.tx,self.ty = self.rect.center   
        # print(self.rect.center)   
        # self.ty += 13 
        # self.Target = pg.draw.ellipse(self.image,((0,0,0)),self.rect)    
        # self.Target = pg.draw.circle(self.image,((0,0,0)),(self.tx,self.ty),25)    


    def move(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH + 10 :
            self.speed = -self.speed
            self.image =self.image2
        if self.rect.right < -10 :
            self.speed = -self.speed
            self.image = self.image1
    
    def update(self):
        self.move()

    def draw(self):
        print('draw')

    def load_image(self,name):
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        path = os.path.join(main_dir, "data", name)
        img = pg.image.load(path).convert()
        img.set_colorkey((184,61,186))
        img = pg.transform.scale(img,(int(DUCK_H * Duck.scale),int(DUCK_W * Duck.scale))) 
        return img
