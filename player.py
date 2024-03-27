import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -PLAYER_SPEEDX
        if keys[pygame.K_RIGHT]:
            self.speedx = PLAYER_SPEEDX
        self.rect.x += self.speedx

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SC_WIDTH:
            self.rect.right = SC_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
