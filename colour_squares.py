


import pygame
pygame.init()
from pygame.locals import *
screen=pygame.display.set_mode((500,500))
screen.fill("black")
squarex=80
squarey=90
sqaure_wid=80
square_hi=80
pygame.display.set_caption("colour changing square")
current_colour="white"
run=True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                squarey = squarey - 20

            if i.key == K_DOWN:
                squarey = squarey + 20

            if i.key == K_LEFT:
                squarex = squarex - 20

            if i.key == K_RIGHT:
                squarex = squarex + 20
    
    if squarex <= 0:
        current_colour = "red"

    elif squarex + sqaure_wid >= 500:
        current_colour = "blue"

    elif squarey <= 0:
        current_colour = "yellow"

    elif squarey + square_hi >= 500:
        current_colour = "green"

    else:
        current_colour = "white"

    screen.fill("black")
    pygame.draw.rect(screen, current_colour,
                     (squarex, squarey, sqaure_wid, square_hi))

    pygame.display.update()
            
            


    screen.fill("black")
    pygame.draw.rect(screen,current_colour,(squarex,squarey,sqaure_wid,square_hi))
    pygame.display.update()

        


