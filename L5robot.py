import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

# Rectangle Class
class Rectangle():
    def __init__(self, colour, rect, width=0):
        self.colour = colour
        self.rect = rect  # (x, y, width, height)
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, self.rect, self.width)


# Robot Parts
head = Rectangle("grey", (200, 50, 100, 100))

left_eye = Rectangle("white", (220, 70, 20, 20))
right_eye = Rectangle("white", (260, 70, 20, 20))

body = Rectangle("blue", (180, 150, 140, 150))

left_arm = Rectangle("grey", (130, 160, 50, 20))
right_arm = Rectangle("grey", (320, 160, 50, 20))

left_leg = Rectangle("grey", (200, 300, 30, 80))
right_leg = Rectangle("grey", (270, 300, 30, 80))


# Game Loop
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    screen.fill("black")  # clear screen

    # Draw Robot
    head.draw()
    left_eye.draw()
    right_eye.draw()
    body.draw()
    left_arm.draw()
    right_arm.draw()
    left_leg.draw()
    right_leg.draw()

    pygame.display.update()

pygame.quit()