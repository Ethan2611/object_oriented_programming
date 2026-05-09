


import pygame
pygame.init()
from pygame.locals import *
screen=pygame.display.set_mode((800,800))
screen.fill("black")
space=pygame.image.load("Rocket conrtol/space2.png")
rocket=pygame.image.load("Rocket conrtol/rocket4.png")
rocketx=200
rockety=200


run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==K_UP:
                rockety=rockety-10
        
            if i.key==K_DOWN:
                rockety=rockety+10
            
            if i.key==K_LEFT:
                rocketx=rocketx-10
            
            if i.key==K_RIGHT:
                rocketx=rocketx+10
    

    rockety=rockety+0.1
    screen.blit(space,(0,0))        
    screen.blit(rocket,(rocketx,rockety))
    

    pygame.display.update()



