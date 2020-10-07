import pygame


class Timor():
    def __init__(self, screen):
        """初始化Timor并设置其初始位置"""
        self.screen = screen
        # 加载Timor图像
        self.image = pygame.image.load('images/timor.bmp')
        # 获取Timor外接矩形
        self.rect = self.image.get_rect()
        # 获取屏幕外接矩形
        self.screen_rect = screen.get_rect()
        # 将Timor放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制Timor"""
        self.screen.blit(self.image, self.rect)