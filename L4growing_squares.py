import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
screen.fill("black")

class Square():
    def __init__(self, size, colour, pos, width):
        self.size = size
        self.colour = colour
        self.pos = pos
        self.width = width
        self.screen = screen
    
    def draw(self):
        rect = pygame.Rect(self.pos[0] - self.size//2,
                           self.pos[1] - self.size//2,
                           self.size,
                           self.size)
        pygame.draw.rect(self.screen, self.colour, rect, self.width)

    def grow(self, r):
        self.size = self.size + r
        rect = pygame.Rect(self.pos[0] - self.size//2,
                           self.pos[1] - self.size//2,
                           self.size,
                           self.size)
        pygame.draw.rect(self.screen, self.colour, rect, self.width)

blue_square = Square(40, "blue", (250,250), 0)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            blue_square.draw()

        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            blue_square.grow(10)

    pygame.display.update()