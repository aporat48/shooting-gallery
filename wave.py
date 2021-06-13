import pygame as pg
from  config import *
import os
line1 = pg.Surface((WIDTH,WAVE_H))
line2 = pg.Surface((WIDTH,WAVE_H))
line3 = pg.Surface((WIDTH,WAVE_H))
def load_image(name):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(main_dir, "data", name)
    img = pg.image.load(path).convert()
    img.set_colorkey((184,61,186))
    return img

def wave_3_lines(line,img,linew):
    line.fill((pg.Color('lightblue')))        
    for i in range(5):
            x = i * (WAVE_W - 15 ) -  5
            line.blit(img,(x,0))
    wave_rect = line.get_rect()
    wave_rect.y = linew
    return wave_rect
