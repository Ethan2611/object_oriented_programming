


import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill("white")
class Circle():
    def __init__(self,radius,colour,pos,width):
        self.radius=radius
        self.colour=colour
        self.pos=pos
        self.width=width
        self.screen=screen
    

    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.width)


blue_circle=Circle(40,"blue",(100,100),10)
yellow_circle=Circle(40,"yellow",(150,125),10)
black_circle=Circle(40,"black",(200,100),10)
green_circle=Circle(40,"green",(250,125),10)
red_circle=Circle(40,"red",(300,100),10)
run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    blue_circle.draw()
    black_circle.draw()
    yellow_circle.draw()
    green_circle.draw()
    red_circle.draw()
    pygame.display.update()
