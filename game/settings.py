class Settings:
    """General game settings"""
    def __init__(self):
        """Main settings"""
        self.screen_width: int = 1920
        self.screen_height: int = 1080
        self.bg_color: int = (192, 192, 192)
        self.fps: int = 180
        self.caption: str = "SPACE SHIP"
        self.ship: SettingsShip = SettingsShip()
        self.aliens: SettingsAliens = SettingsAliens()
        self.speedup_scale: float = 1.1
class SettingsAliens:
    """Aliens settings"""
    def __init__(self):
        self.start_position: int = 85
        self.sprite_scale_x: float = 0.192
        self.sprite_scale_y: float = 0.192
        self.default_speed = 1
        self.speed: float = 1
        self.drop_speed: int = 5
        self.fleet_direction: int = 1

class SettingsShip:
    """Ship settings"""
    def __init__(self):
        self.ships_limit: int = 3
        self.default_speed: int = 3
        self.bullet_speed: float = 10.0
        self.bullet_width: int = 20
        self.bullet_height: int = 30
        self.bullet_color: int = (255, 0, 255)