class Settings():
    """存储所有设置参数的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (255, 255, 255)
        self.rocket_speed_factor = 1.5
