


import pygame
pygame.init()
screen=pygame.display.set_mode((500,610))
screen.fill("white")
pygame.display.set_caption("Match Words Game")
font=pygame.font.SysFont("Comic Sans",30)
text=font.render("Matching Words Game",True,"blue")
screen.blit(text,(60,30))

temple_run=pygame.image.load("Match Words 2/yamal2.jpg")
screen.blit(temple_run,(60,85))

candy_crush=pygame.image.load("Match Words 2/mbappe2.jpg")
screen.blit(candy_crush,(80,230))

ludo=pygame.image.load("Match Words 2/messi2.jpg")
screen.blit(ludo,(60,330))

subway=pygame.image.load("Match Words 2/ronaldo2.jpg")
screen.blit(subway,(60,430))

font=pygame.font.SysFont("Comic Sans",20)
text4=font.render("Cristiano Ronaldo",True,"blue")
screen.blit(text4,(300,150))

font=pygame.font.SysFont("Comic Sans",20)
text3=font.render("Lamine Yamal",True,"red")
screen.blit(text3,(300,250))

font=pygame.font.SysFont("Comic Sans",20)
text1=font.render("Lionel Messi",True,"green")
screen.blit(text1,(300,450))

font=pygame.font.SysFont("Comic Sans",20)
text2=font.render("Kylian Mbappe",True,"yellow")
screen.blit(text2,(300,350))
pygame.display.update()


run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0),(pos),10,0)
            pygame.display.update()
        elif i.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,"blue",(pos),(pos2),10)
            pygame.draw.circle(screen,("blue"),(pos2),10,0)
            
    pygame.display.update()



