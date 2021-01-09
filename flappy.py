import pygame
from pygame.locals import *

SCREEN_W = 400
SCREEN_H = 600

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load('assets/bluebird-upflap.png').convert_alpha(),
            pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),
            pygame.image.load('assets/bluebird-downflap.png').convert_alpha()]

        self.current_image = 0

        self.image = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_W / 2
        self.rect[1] = SCREEN_H / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BACKGROUND = pygame.image.load('assets/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_W, SCREEN_H))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()

    bird_group.draw(screen)
    
    pygame.display.update()