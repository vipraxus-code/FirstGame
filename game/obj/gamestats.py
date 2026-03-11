class GameStats:
    """Track various game statistics"""
    def __init__(self, game):
        """Initializes game statistics"""
        self.settings = game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Resets game statistics"""
        self.ships_left = self.settings.ship.ships_limit
        self.settings.aliens.speed = self.settings.aliens.default_speed