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
            self._update_aliens()
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
        coliisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        for alien in self.aliens.sprites():                           # DEBUG
            pygame.draw.rect(self.screen, (0, 255, 0), alien.rect, 2) # DEBUG
        
        pygame.display.flip()

    def _create_fleet(self):
        alien = Alien(self)
        current_x = alien.rect.x
        current_y = alien.rect.y
        while current_y < (self.settings.screen_height - alien.image.get_height() * 3):
            while current_x < (self.settings.screen_width - alien.image.get_width()):
                self._create_alien(current_x, current_y)
                current_x += alien.image.get_width() * 1.5
            current_x = alien.rect.x
            current_y += alien.image.get_height() * 1.5

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien.drop_speed
        self.settings.alien.fleet_direction *= -1