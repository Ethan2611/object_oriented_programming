


import pygame
pygame.init()
from pygame.locals import *
screen=pygame.display.set_mode((800,800))
screen.fill("black")
sky=pygame.image.load("Superman game/sky.jpg")
superman=pygame.image.load("Superman game/superman3.png")
superx=200
supery=200


run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==K_UP:
                supery=supery-10
        
            if i.key==K_DOWN:
                supery=supery+10
            
            if i.key==K_LEFT:
                superx=superx-10
            
            if i.key==K_RIGHT:
                superx=superx+10
    

    supery=supery+0.1
    screen.blit(sky,(0,0))        
    screen.blit(superman,(superx,supery))
    

    pygame.display.update()



