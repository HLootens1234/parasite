import pygame
from Config import *

#Init
pygame.init()
clock=pygame.time.Clock()

# Open window
displaySurface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Parasite")

isGameRunning = True
while isGameRunning:
    #Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isGameRunning = False
    pygame.display.flip()
    clock.tick(60)

# Close pygame
pygame.quit()