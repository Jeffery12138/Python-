import pygame


class Rocket():
    def __init__(self, ai_settings, screen):
        """初始化火箭并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载火箭图像并获取其外接矩形
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 将每艘新火箭放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # 在飞船的属性x/y中存储小数值
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的x/y值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.rocket_speed_factor
        # 根据self.x/y的值更新rect对象
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)