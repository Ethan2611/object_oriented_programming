


import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
class Circle():
    def __init__(self,radius,colour,pos,width):
        self.radius=radius
        self.colour=colour
        self.pos=pos
        self.width=width
        self.screen=screen
    

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.width)


red_circle=Circle(40,"red",(100,100),10)
green_circle=Circle(40,"green",(400,100),20)

run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    red_circle.draw()
    green_circle.draw()
    pygame.display.update()
