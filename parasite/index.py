
import pygame
from Config import *

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


start_bg = pygame.image.load('assets/Parasite.png').convert()
start_bg = pygame.transform.scale(start_bg,(WINDOW_WIDTH,WINDOW_HEIGHT))

#font for "press to start"
font = pygame.font.SysFont(None, 50)
text = font.render('Press SPACE to start', True, (255,255,255))
text_rect = text.get_rect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT-100))

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

#Used for start screen
gameStarted = False

isGameRunning = True
while isGameRunning:
    displaySurface.fill((0,0,0))
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        elif event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                isGameRunning = False

        if not gameStarted and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameStarted = True

    displaySurface.fill((20, 20, 30))

    if not gameStarted:
        displaySurface.blit(start_bg, (0, 0))
        displaySurface.blit(text, text_rect)

    if gameStarted:
        for button in buttons:
            button.draw(displaySurface)


    pygame.display.flip()
    clock.tick(60)

# Close pygame
pygame.quit()
