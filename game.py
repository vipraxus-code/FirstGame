import sys
import pygame
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
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.ship.rect.x += 5
                    elif event.key == pygame.K_a:
                        self.ship.rect.x -= 5
                    elif event.key == pygame.K_s:
                        self.ship.rect.y += 5
                    elif event.key == pygame.K_w:
                        self.ship.rect.y -= 5

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run_game()
    