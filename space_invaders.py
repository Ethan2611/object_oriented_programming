


import pygame
import os
from pygame.locals import*
pygame.mixer.init()
pygame.init()
screen=pygame.display.set_mode((1000,700))
bg=pygame.image.load("Space Invaders/space_bg.png")
pygame.display.set_caption("Space Invaders")
ship1=pygame.image.load("Space Invaders/ship_1.png")
ship2=pygame.image.load("Space Invaders/ship_2.png")
red_ship=pygame.transform.rotate(pygame.transform.scale(ship1,(60,40)),270)
yellow_ship=pygame.transform.rotate(pygame.transform.scale(ship2,(60,40)),90)

def draw_window():
    screen.blit(bg,(0,0))
    screen.blit(red_ship,(red.x,red.y))
    screen.blit(yellow_ship,(yellow.x,yellow.y))
    pygame.display.update()

def red_ship_movement(keypress,red):
    if keypress[pygame.K_LEFT]:
        red.x-=1
    if keypress[pygame.K_RIGHT]:
            red.x+=1
    if keypress[pygame.K_UP]:
            red.y-=1
    if keypress[pygame.K_DOWN]:
            red.y+=1



def yel_ship_movement(keypress,yellow):
    if keypress[pygame.K_a]:
        yellow.x-=1
    if keypress[pygame.K_d]:
            yellow.x+=1
    if keypress[pygame.K_w]:
            yellow.y-=1
    if keypress[pygame.K_s]:
            yellow.y+=1
def handle_bullets(yellow_bullet,red_bullet,yellow,red):
      for i in red_bullet:
            i.x=i.x-5
      for i in yellow_bullet:
        i.x=i.x+5
red=pygame.Rect(900,300,60,90)
yellow=pygame.Rect(100,300,60,90)
red_bullet=[]
yellow_bullet=[]


run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_RSHIFT:
                 bullet=pygame.Rect(red.x+red.width,red.y+red.height//2-2,10,5) #creating the bullet from the place where the ship is
                 red_bullet.append(bullet)#appending it into the empty list
    keypress=pygame.key.get_pressed() #tracks which keyboard key is pressed
    red_ship_movement(keypress,red) #calling the function
    yel_ship_movement(keypress,yellow)
    handle_bullets(yellow_bullet,red_bullet,yellow,red)
    draw_window()

    pygame.display.update()