import sys
import pygame


def check_keydown_events(event):
    """响应按键"""
    print(event.key)


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def update_screen(ai_settings, screen):
    # 更新屏幕上的图像，并切换到新屏幕
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 让最近绘制的屏幕可见
    pygame.display.flip()