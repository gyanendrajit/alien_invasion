class Settings:
    """A class to store all settings for Alien INvasion"""

    def __init__(self):
        """INitialize the game's settings"""
        #screen settings
        self.screen_width= 1200
        self.screen_height=800
        self.bg_color=(255,255,255)
        self.ship_speed = 1.5
        self.ship_limit=3
        self.bullet_speed =1
        self.bullet_width =1

        self.bullet_height= 15
        self.bullet_color = (0,0,0)
        self.alien_speed=2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        