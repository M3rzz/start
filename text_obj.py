import pygame
from settings import *

class Text_Obj:

    def __init__(self, x, y, score, screen):
        self.x = x
        self.y = y
        self.score = score
        self.screen = screen
        self.font = pygame.font.SysFont('arial', 32)
        

    def update(self, score):
        self.score = score
        self.text = self.font.render(str(self.score), True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.x, self.y)

    def draw(self):
        self.screen.blit(self.text, self.text_rect)
