import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Creates alien fleet."""
    def __init__(self, game):
        """Iniatializes alien fleet."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load("game/images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.settings.aliens.sprite_scale_x, self.image.get_height() * self.settings.aliens.sprite_scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = self.settings.aliens.start_position
        self.x = float(self.rect.x)

    def update(self):
        """Updates alien fleet."""
        self.x += (self.settings.aliens.speed * self.settings.aliens.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Checks if alien fleet collides edges of the screen."""
        return (self.rect.right >= self.settings.screen_width) or (self.rect.left <=0)