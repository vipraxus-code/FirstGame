import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = self.default_speed = game.settings.default_speed
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += self.speed
        if self.moving_left:
            self.rect.x -= self.speed
        if self.moving_top:
            self.rect.y -= self.speed
        if self.moving_bottom:
            self.rect.y += self.speed
        