


import pygame
import time
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Mother's day card")
width=500
height=500
screen.fill("black")


image1=pygame.image.load("Mothers day animation/flowers.jpg")
image1=pygame.transform.scale(image1,(width,height)) #adjusting the size of the image per the window width and hegight

run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    font=pygame.font.SysFont("Arial",30)
    
    screen.blit(image1,(0,0))
    
    pygame.display.update()
    time.sleep(2)

    image2=pygame.image.load("Mothers day animation/hearts.png")
    image2=pygame.transform.scale(image2,(width,height))
    font=pygame.font.SysFont("Arial",30)
    
    screen.blit(image2,(0,0))
    
    pygame.display.update()
    time.sleep(2)

    image3=pygame.image.load("Mothers day animation/sweetest_mom.jpg")
    image3=pygame.transform.scale(image3,(width,height))
    font=pygame.font.SysFont("Arial",30)
    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(2)




