import sys
import pygame
from pygame.event import event_name
from settings import Settings
from ship import Ship


class Game:
    def  __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEWHEEL:
                    if event.y > 0:
                        if self.ship.speed < 10:
                            self.ship.speed += 1
                    elif event.y < 0:
                        if self.ship.speed > 1:
                            self.ship.speed -= 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 2:
                        self.ship.speed = self.ship.default_speed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.ship.moving_right = True
                    if event.key == pygame.K_a:
                        self.ship.moving_left = True
                    if event.key == pygame.K_w:
                        self.ship.moving_top = True
                    if event.key == pygame.K_s:
                        self.ship.moving_bottom = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.ship.moving_right = False
                    if event.key == pygame.K_a:
                        self.ship.moving_left = False
                    if event.key == pygame.K_w:
                        self.ship.moving_top = False
                    if event.key == pygame.K_s:
                        self.ship.moving_bottom = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run_game()