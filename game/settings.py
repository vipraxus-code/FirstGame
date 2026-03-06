class Settings:
    def __init__(self):
        self.screen_width: int = 1920
        self.screen_height: int = 1080
        self.bg_color: int = (192, 192, 192)
        self.fps: int = 180
        self.caption: str = "SPACE SHIP"
        self.ship: Settings = SettingsShip()
        self.alien: Settings = SettingsAlien()

class SettingsAlien:
    def __init__(self):
        self.start_position: int = 85
        self.sprite_scale_x: float = 0.192
        self.sprite_scale_y: float = 0.192
        self.speed: int = 1
        self.drop_speed: int = 10
        self.fleet_direction: int = 1 # 1=right, -1=left

class SettingsShip:
    def __init__(self):
        self.default_speed: int = 3
        self.bullet_speed: float = 5.0
        self.bullet_width: int = 10
        self.bullet_height: int = 30
        self.bullet_color: int = (255, 0, 255)