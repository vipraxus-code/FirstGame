class Settings:
    def __init__(self):
        self.screen_width: int = 1920
        self.screen_height: int = 1080
        self.bg_color: int = (192, 192, 192)
        self.fps: int = 180
        self.caption: str = "SPACE SHIP"
        self.ship: Settings = SettingsShip()


class SettingsShip:
    def __init__(self):
        self.default_speed: int = 3
        self.bullet_speed: float = 5.0
        self.bullet_width: int = 3
        self.bullet_height: int = 15
        self.bullet_color: int = (255, 0, 0)