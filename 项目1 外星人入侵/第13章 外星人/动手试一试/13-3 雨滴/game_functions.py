import pygame
import sys

from drop import Drop


def check_keydown_events(event):
    """检查按键事件"""
    if event.key == pygame.K_q:
        sys.exit()


def check_events():
    """检查鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def get_number_drops_x(ai_settings, drop_width):
    """计算每行可容纳多少个雨滴"""
    available_space_x = ai_settings.screen_width - 2 * drop_width
    number_drops_x = int(available_space_x / (2 * drop_width))
    return number_drops_x


def get_number_drops_y(ai_settings, drop_height):
    """计算每列可容纳多少个雨滴"""
    available_space_y = ai_settings.screen_height - 2 * drop_height
    number_drops_y = int(available_space_y / (2 * drop_height))
    return number_drops_y


def create_drop(ai_settings, screen, drops, number_drop_x, number_drop_y):
    """创建一个雨滴，并把它放在当前行"""
    drop = Drop(ai_settings, screen)
    drop_width = drop.rect.width
    drop_height = drop.rect.height
    drop.x = drop_width + 2 * drop_width * number_drop_x
    drop.rect.x = drop.x
    drop.y = drop_height + 2 * drop_height * number_drop_y
    drop.rect.y = drop.y
    drops.add(drop)


def create_rain(ai_settings, screen, drops):
    """创建雨滴阵列"""
    # 创建一个雨滴，并计算屏幕可容纳多少雨滴
    drop = Drop(ai_settings, screen)
    number_drops_x = get_number_drops_x(ai_settings, drop.rect.width)
    number_drops_y = get_number_drops_y(ai_settings, drop.rect.height)
    # 创建雨滴阵列
    for number_drop_x in range(number_drops_x):
        for number_drop_y in range(number_drops_y):
            create_drop(ai_settings, screen, drops, number_drop_x, number_drop_y)


def update_drops(drops):
    """更新雨滴位置"""
    drops.update()


def update_screen(ai_settings, screen, drops):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 重绘所有外星人
    drops.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()
