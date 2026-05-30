


import pygame
import random
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill("black")

pygame.display.set_caption("Pac-man game")
class Pacman:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=0.5
        self.radius=20
    
    def draw(self):
        pygame.draw.circle(screen,"yellow",(self.x,self.y),self.radius)
    
    def move(self,keys):
        if keys[pygame.K_UP]:
            self.y-=self.speed
        
        elif keys[pygame.K_DOWN]:
            self.y+=self.speed
        
        elif keys[pygame.K_LEFT]:
            self.x-=self.speed
        
        elif keys[pygame.K_RIGHT]:
            self.x+=self.speed

def main():
    pacman=Pacman(200,200)
    while True:

        screen.fill("black")

        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                run=False

        keys=pygame.key.get_pressed()
        pacman.move(keys)
        pacman.draw()
        pygame.display.update()

main()