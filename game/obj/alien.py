import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load("game/images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.settings.aliens.sprite_scale_x, self.image.get_height() * self.settings.aliens.sprite_scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = self.settings.aliens.start_position
        self.speed = game.settings.aliens.speed

    def update(self):
        self.rect.x += (self.settings.aliens.speed * self.settings.aliens.fleet_direction)

    def check_edges(self):
        return (self.rect.right >= self.settings.screen_width) or (self.rect.left <=0)