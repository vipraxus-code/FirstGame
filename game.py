import sys
import pygame
from settings import Settings
from obj.ship import Ship
from obj.bullet import Bullet
from obj.alien import Alien


class Game:
    def  __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEWHEEL:
                self._check_mousewheel_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousebutton_events(event)
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        if event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_w:
            self.ship.moving_top = True
        if event.key == pygame.K_s:
            self.ship.moving_bottom = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_w:
            self.ship.moving_top = False
        if event.key == pygame.K_s:
            self.ship.moving_bottom = False

    def _check_mousewheel_events(self, event):
        if event.y > 0:
            if self.ship.speed < 10:
                self.ship.speed += 1
        elif event.y < 0:
            if self.ship.speed > 1:
                self.ship.speed -= 1
        
    def _check_mousebutton_events(self, event):
        if event.button == 2:
            self.ship.speed = self.ship.default_speed

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for alien in self.aliens.sprites():
            pygame.draw.rect(self.screen, (0, 255, 0), alien.rect, 2)
        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)