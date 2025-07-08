import pygame
from config import *

#Init
pygame.init()
clock = pygame.time.Clock()

# Open window
displaySurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Parasite")

button_images = [
    pygame.image.load('assets/Heart1.png'),
    pygame.image.load('assets/Heart2.png'),
    pygame.image.load('assets/Heart3.png'),

]

for i in range(len(button_images)):
    button_images[i] = pygame.transform.smoothscale(button_images[i], (BUTTON_RADIUS*2, BUTTON_RADIUS*2))

class CircularButton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        pygame.draw.circle(surface, (80, 80, 80), self.rect.center, BUTTON_RADIUS)
        surface.blit(self.image, self.rect)


buttons = []
for i in range(3):
    x = WINDOW_WIDTH - BUTTON_RADIUS - 20
    y = (BUTTON_RADIUS + BUTTON_SPACING) * i + BUTTON_RADIUS + 40
    buttons.append(CircularButton(x, y, button_images[i]))



isGameRunning = True
while isGameRunning:
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                isGameRunning = False

    displaySurface.fill((20, 20, 30))

    for button in buttons:
        button.draw(displaySurface)


    pygame.display.flip()
    clock.tick(60)

# Close pygame
pygame.quit()