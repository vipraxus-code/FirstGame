import pygame

class Ship:
    """Player ship."""
    def __init__(self, game):
        """Initializes the player ship."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("game/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = self.default_speed = game.settings.ship.default_speed
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        """Draws the ship."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moves the ship."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.speed
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed