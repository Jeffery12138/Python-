class Settings():
    """所有设置的类"""
    def __init__(self):
        """设置的初始化"""
        # 屏幕的设置
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = 0, 0, 0
        # 雨滴设置
        self.drop_speed_factor = 1