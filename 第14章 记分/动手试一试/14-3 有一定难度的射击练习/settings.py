class Settings():
    """存储所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 射击目标设置
        self.target_width = 20
        self.target_height = 100
        self.target_color = 90, 90, 90
        self.target_limit = 3
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 0.2
        self.bullet_speed_factor = 0.8
        self.target_speed_factor = 0.1
        self.target_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale
