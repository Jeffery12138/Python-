import pygame


class Timor():
    def __init__(self, screen):
        """初始化Timor并设置其初始位置"""
        self.screen = screen
        # 加载Timor图像并获取其外接矩形
        self.image = pygame.image.load("images/timor.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # 将每个新Timor都放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制Timor"""
        self.screen.blit(self.image, self.rect)
