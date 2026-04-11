


import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill("black")
class Circle():
    def __init__(self,radius,colour,pos,width):
        self.radius=radius
        self.colour=colour
        self.pos=pos
        self.width=width
        self.screen=screen
    

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.width)

    def grow(self,r):
        self.radius=self.radius+r
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.width)
        
blue_circle=Circle(20,"blue",(250,250),0)



















run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            blue_circle.draw()
        elif i.type==pygame.MOUSEBUTTONUP:
            screen.fill("white")
            blue_circle.grow(10)
    pygame.display.update()