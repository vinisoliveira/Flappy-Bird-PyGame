import pygame
from pygame.locals import *

SCREEN_W = 400
SCREEN_H = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BACKGROUND = pygame.image.load('\assets\background-day.png')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.display.update()