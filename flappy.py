import pygame
from pygame.locals import *

SCREEN_W = 400
SCREEN_H = 600
SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

GROUND_WIDTH = 2 * SCREEN_W
GROUND_HEIGHT = 100

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load('assets/bluebird-upflap.png').convert_alpha(),
            pygame.image.load('assets/bluebird-midflap.png').convert_alpha(),
            pygame.image.load('assets/bluebird-downflap.png').convert_alpha()]

        self.speed = SPEED
        self.current_image = 0

        self.image = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
        self_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_W / 2
        self.rect[1] = SCREEN_H / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image]

        #Update Height
        self.rect[1] += self.speed
        self.speed += GRAVITY

    def bump(self):
        self.speed = -SPEED

class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
        self_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = SCREEN_H - GROUND_HEIGHT

    def update(self):
        self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])


pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BACKGROUND = pygame.image.load('assets/background-day.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_W, SCREEN_H))

bird_group = pygame.sprite.Group()
bird = Bird()
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH * i)
    ground_group.add(ground)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0, 0))

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        new_ground = Ground(GROUND_WIDTH - 20)
        ground_group.add(new_ground )

    bird_group.update()
    ground_group.update()

    bird_group.draw(screen)
    ground_group.draw(screen)

    pygame.display.update()

    if pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask):
        #GAME OVER
        input()
        break