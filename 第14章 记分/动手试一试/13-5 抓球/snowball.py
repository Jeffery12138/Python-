import pygame
from pygame.sprite import Sprite
from random import randint


class SnowBall(Sprite):
    """表示单个雪球的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(SnowBall, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载雪球并获取其外接矩形
        self.image = pygame.image.load('images/snowball.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = randint(0, int(self.ai_settings.screen_width - self.rect.width))
        # 存储雪球的准确位置
        self.y = float(self.rect.y)

    def update(self):
        """雪球下落"""
        self.y += self.ai_settings.snowball_drop_speed_factor
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制雪人"""
        self.screen.blit(self.image, self.rect)