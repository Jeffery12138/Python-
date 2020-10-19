import pygame
from pygame.sprite import Sprite
from random import randint


class Target(Sprite):
    """表示射击目标的类"""
    def __init__(self, ai_settings, screen):
        """初始化射击目标并初始化其位置"""
        super(Target, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # 在(0, 0)处创建一个子弹的矩阵，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.ai_settings.target_width, self.ai_settings.target_height)
        self.rect.right = self.screen_rect.right
        self.rect.top = randint(0, int(self.screen_rect.bottom - self.rect.height))
        # 存储用小数表示的目标位置
        self.y = float(self.rect.y)
        self.color = self.ai_settings.target_color
        self.speed_factor = self.ai_settings.target_speed_factor

    def update(self):
        """向下移动目标"""
        # 更新表示目标位置的小数值
        self.y += (self.speed_factor * self.ai_settings.target_direction)
        # 更新表示目标rect的位置
        self.rect.y = self.y

    def draw_target(self):
        """在屏幕上绘制目标"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        """如果目标位于屏幕底端就返回True"""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True

    def reset_target_direction(self):
        """重置目标移动方向"""
        self.ai_settings.target_direction = 1