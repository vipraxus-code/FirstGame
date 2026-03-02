import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * game.settings.alien.sprite_scale_x, self.image.get_width() * game.settings.alien.sprite_scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = 85
        self.rect.y = 85
        self.x = float(self.rect.x)