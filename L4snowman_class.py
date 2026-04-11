


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



small_circle=Circle(40,"white",(100,100),0)
medium_circle=Circle(60,"white",(100,200),0)
big_circle=Circle(80,"white",(100,300),0)
left_eye_circle=Circle(10,"black",(75,90),0)
right_eye_circle=Circle(10,"black",(120,90),10)
button_circle=Circle(10,"black",(100,200),0)
run=True
while run:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
    small_circle.draw()
    medium_circle.draw()
    big_circle.draw()
    left_eye_circle.draw()
    right_eye_circle.draw()
    pygame.display.update()
