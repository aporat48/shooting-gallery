import pygame,sys

pygame.init()
size = width,height = [600,400]
speed = [1,1]
BLACK = 0,0,0
screen = pygame.display.set_mode(size)
#game name
pygame.display.set_caption("pygame squash")
#Import the picture path of the ball, which can be customized
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #Mobile Way
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #background color
    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    #Refresh
    pygame.display.update()