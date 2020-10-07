import pygame


class Rocket():
    def __init__(self, ai_settings, screen):
        """初始化火箭并设置其初始位置"""
        self.ai_settings = ai_settings
        self.screen = screen
        # 加载火箭图像
        self.image = pygame.image.load('images/rocket.bmp')
        # 获取火箭外接矩形
        self.rect = self.image.get_rect()
        # 获取屏幕外接矩形
        self.screen_rect = screen.get_rect()
        # 将火箭放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 在火箭的属性centerx和centery中储存小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """根据移动标志调整火箭的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor
        # 根据centerx和centery更新火箭rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)