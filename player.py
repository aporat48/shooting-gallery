import sys, math
import  pygame as pg 
from bullet import *
from config import *
class Player():
    ah = 100
    ax = WIDTH /2
    ay = HEIGHT - ah
    pl3 = pg.Vector2(ax, ay + ah/2)
    pl4 = pg.Vector2(ax, ay - ah/2)
    last_point = pg.Vector2(pl4)

    def aim_arrow(self,ang):
        vec = pg.Vector2(Player.last_point - Player.pl3)
        w = vec.rotate(ang) 
        Player.last_point = Player.pl3 + w
        return Player.last_point

    def shoot(self):
       rect = pg.Rect(Player.last_point,(0,0))    
       bullet = Bullet(self,rect.centerx,rect.top)
       return(bullet)
   
    def draw():
        pass