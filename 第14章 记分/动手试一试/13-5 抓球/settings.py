class Settings():
    """游戏的所有设置类"""
    def __init__(self):
        """设置初始化"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 149, 183, 186
        # 雪人设置
        self.snowman_speed_factor = 0.8
        # 雪球设置
        self.snowball_drop_speed_factor = 0.6
