import pygame
from settings import *


class Background(pygame.sprite.Sprite):

    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)




    
