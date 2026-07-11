


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
class Food:
    def __init__(self):
        self.x=random.randint(50,450)
        self.y=random.randint(50,450)
        self.radius=10
    def draw(self):
        pygame.draw.circle(screen,"red",(self.x,self.y),self.radius)
def main():
    pacman=Pacman(200,200)
    food=Food()
    run=True
    score=0
    while run:

        screen.fill("black")

        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                run=False

        keys=pygame.key.get_pressed()
        pacman.move(keys)
        distance=((pacman.x-food.x)**2+(pacman.y-food.y)**2)**0.5
        if distance < pacman.radius + food.radius:
            score= score+1
            print(score)
            food=Food()
        pacman.draw()
        food.draw()
        font=pygame.font.SysFont(None,36)
        scoretext=font.render("score :"+str(score),True,"blue")
        screen.blit(scoretext,(50,50))
        pygame.display.update()

main()