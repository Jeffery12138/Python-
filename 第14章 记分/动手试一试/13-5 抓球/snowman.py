import pygame
from pygame.sprite import Sprite


class SnowMan(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化雪人并设置其初始位置"""
        super(SnowMan, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载雪人并获取其外接矩形
        self.image = pygame.image.load('images/snowman.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 将每个新雪人放置在屏幕正下方
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在雪人的属性center存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整雪人位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.snowman_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.snowman_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)