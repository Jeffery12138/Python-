import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    """表示单个雨滴的类"""
    def __init__(self, ai_settings, screen):
        """初始化雨滴设置"""
        super(Drop, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载雨滴图像并获取其外接矩形
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储雨滴的位置
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制雨滴"""
        self.screen.blit(self.image, self.rect)

    def check_disappear(self):
        """如果雨滴从屏幕中消失了，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True

    def update(self):
        """向下移动雨滴"""
        self.y += self.ai_settings.drop_speed_factor
        self.rect.y = self.y
