import pygame
from constants import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width=BLOCK.width, height=BLOCK.height, color=None):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((width, height))
        self.image=pygame.image.load(GREY_TILE)
        self.image = pygame.transform.smoothscale(self.image, (BLOCK.width, BLOCK.height))
        self.color = color
        self.selected = False
        self.type = "block"

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

    def update(self):
        pass

