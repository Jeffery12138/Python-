class Settings():
    """存储所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船的设置
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 0.8
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 射击目标设置
        self.target_speed_factor = 0.1
        self.target_width = 20
        self.target_height = 100
        self.target_color = 90, 90, 90
        self.target_direction = 1
        self.target_limit = 3
