


import pygame
import time
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("birthday greeting card")
width=500
height=500
screen.fill("black")


image1=pygame.image.load("BirthdayL5/present.jpg")
image1=pygame.transform.scale(image1,(width,height)) #adjusting the size of the image per the window width and hegight

run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    font=pygame.font.SysFont("Arial",30)
    text=font.render("Wishing you a bright future!",True,"blue")
    screen.blit(image1,(0,0))
    screen.blit(text,(45,75))
    pygame.display.update()
    time.sleep(2)

    image2=pygame.image.load("BirthdayL5/card.jpg")
    image2=pygame.transform.scale(image2,(width,height))
    font=pygame.font.SysFont("Arial",30)
    text=font.render("Happy Birthday",True,"black")
    text2=font.render("Wishing you a great day!",True,"red")
    screen.blit(image2,(0,0))
    screen.blit(text,(175,100))
    screen.blit(text2,(125,250))
    pygame.display.update()
    time.sleep(2)

    image3=pygame.image.load("BirthdayL5/cake.jpg")
    image3=pygame.transform.scale(image3,(width,height))
    font=pygame.font.SysFont("Arial",30)
    text=font.render("Happy Birthday",True,"black")
    text3=font.render("Hip Hip Hooray",True,"red")
    screen.blit(image3,(0,0))
    screen.blit(text3,(175,75))
    pygame.display.update()
    time.sleep(2)

