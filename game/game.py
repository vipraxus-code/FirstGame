import sys
import pygame
from time import sleep
from game.settings import Settings
from game.obj.gamestats import GameStats
from game.obj.ship import Ship
from game.obj.bullet import Bullet
from game.obj.alien import Alien
from game.obj.button import Button


class Game:
    """Main game loop/controller."""
    def __init__(self):
        """Initializes game state."""
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = False
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Runs the game loop."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

    def _update_bullets(self):
        """Updates bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_colissions()

    def _check_bullet_alien_colissions(self):
        """Handles collisions between bullets and aliens."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_events(self):
        """Handles all events."""
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
        """Handles keydown events."""
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
        if event.key == pygame.K_p:
            self._play_button_pressed()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Handles keyup events."""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_w:
            self.ship.moving_top = False
        if event.key == pygame.K_s:
            self.ship.moving_bottom = False

    def _check_mousewheel_events(self, event):
        """Handles mouse wheel events."""
        if event.y > 0:
            if self.ship.speed < 10:
                self.ship.speed += 1
        if event.y < 0:
            if self.ship.speed > 1:
                self.ship.speed -= 1
   
    def _check_mousebutton_events(self, event):
        """Handles mouse button events."""
        mouse_pos = pygame.mouse.get_pos()
        if event.button == 2:
            self.ship.speed = self.ship.default_speed
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self._play_button_pressed()

    def _play_button_pressed(self):
        self.stats.reset_stats()
        self.game_active = True
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Fires a bullet."""
        if self.game_active:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Draws the frame."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for alien in self.aliens.sprites():                                                         # DEBUG
            pygame.draw.rect(self.screen, (0, 255, 0), alien.rect, 2)                               # DEBUG
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _create_fleet(self):
        """Creates alien fleet."""
        alien = Alien(self)
        current_x = alien.rect.x
        current_y = alien.rect.y
        while current_y < (self.settings.screen_height - alien.image.get_height() * 5):
            while current_x < (self.settings.screen_width - alien.image.get_width()):
                self._create_alien(current_x, current_y)
                current_x += alien.image.get_width() * 1.5
            current_x = alien.rect.x
            current_y += alien.image.get_height() * 1.5

    def _create_alien(self, x_position, y_position):
        """Creates one alien."""
        new_alien = Alien(self)
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Updates aliens."""
        self._check_fleet_edges()
        self.aliens.update()
        ship_hit = False
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            ship_hit = True
        else:
            if self._check_aliens_bottom():
                ship_hit = True
        if ship_hit:
            self._ship_hit() 

    def _check_fleet_edges(self):
        """Checks if fleet touches screen edges."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.settings.aliens.drop_speed += 5
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Changes direction and drops the fleet."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.aliens.drop_speed
        self.settings.aliens.fleet_direction *= -1

    def _ship_hit(self):
        """Handles ship hitting"""
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            print(self.stats.ships_left)                                                            # DEBUG
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        """Hits ship if any alien reaches bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                return True