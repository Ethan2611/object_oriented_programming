


import pygame
import os
from pygame.locals import*
pygame.mixer.init()
pygame.init()
screen=pygame.display.set_mode((1000,700))
bg=pygame.image.load("Space Invaders/space_bg.png")

def draw_window():
    screen.blit(bg,(0,0))
    pygame.display.update()




run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    draw_window()
    pygame.display.update()