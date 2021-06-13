import os,random
import pygame as pg
from pygame.constants import K_LEFT, K_RIGHT
from  config import *
from player import *
from duck import *
import wave
total = 0
pg.init()
font = pg.font.Font('freesansbold.ttf', 32)
all_sprites = pg.sprite.Group()
all_bullets = pg.sprite.Group()
def display_score():
    text = font.render('total: ' + str(total) + '  misses: ' + str(missed), True, pg.Color('black')) #,pg.Color('blue'))
    textRect = text.get_rect()
    textRect.center = (200,HEIGHT-50)
    return (text, textRect) 

def check_collide():
    global total
    col_list = pg.sprite.groupcollide(all_sprites, all_bullets, True, True)
    if col_list:
        total += 1
def main():
    global misses
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    duck = Duck(0)
    all_sprites.add(duck)
    duck = Duck(1)
    all_sprites.add(duck)
    duck = Duck(2)
    all_sprites.add(duck)
    pg.time.wait(30)
    duck = Duck(0)
    all_sprites.add(duck)
    duck = Duck(1)
    all_sprites.add(duck)
    duck = Duck(2)
    all_sprites.add(duck)
    img = wave.load_image('wave.png')
    wave_rect_line1 = wave.wave_3_lines(wave.line1,img,LINE1W)
    wave_rect_line2 = wave.wave_3_lines(wave.line2,img,LINE2W)
    wave_rect_line3 = wave.wave_3_lines(wave.line3,img,LINE3W)
    player = Player()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullet = player.shoot()
                    all_bullets.add(bullet)
                    # print(bullet.missed)
 

        key = pg.key.get_pressed()
        if key[K_LEFT]: player.last_point = player.aim_arrow(-4)      
        elif key[K_RIGHT]: player.last_point = player.aim_arrow(4)      

        screen.fill((pg.Color('lightblue')))
        screen.blit(wave.line1, (wave_rect_line1))
        screen.blit(wave.line2, (wave_rect_line2))
        screen.blit(wave.line3, (wave_rect_line3))
        all_sprites.update()
        all_bullets.update()
        
        check_collide()
        all_sprites.draw(screen)
        all_bullets.draw(screen)
        pg.draw.line(screen, pg.Color('red'),(player.pl3),(player.last_point), width=4)
        text, textRect = display_score()
        screen.blit(text, textRect)
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
