import pygame
import sys
from time import sleep

from snowball import SnowBall
from snowman import SnowMan


def check_keydown_events(event, snowmen):
    """响应按键"""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        for snowman in snowmen.sprites():
            snowman.moving_right = True
    elif event.key == pygame.K_LEFT:
        for snowman in snowmen.sprites():
            snowman.moving_left = True


def check_keyup_events(event, snowmen):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        for snowman in snowmen.sprites():
            snowman.moving_right = False
    if event.key == pygame.K_LEFT:
        for snowman in snowmen.sprites():
            snowman.moving_left = False


def check_events(snowmen):
    """检查按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snowmen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, snowmen)


def check_snowman_snowball_collisions(ai_settings, screen, snowmen, snowballs):
    """响应雪人和雪球的碰撞"""
    # 如果接到雪球，就删除这个雪球，新建一个新的雪球
    collisions = pygame.sprite.groupcollide(snowmen, snowballs, False, True)
    if len(snowballs) == 0:
        # 如果没有雪球，就新建一个雪球
        create_snowball(ai_settings, screen, snowballs)


def not_catch_snowball(ai_settings, stats, screen, snowmen, snowballs):
    """响应接到了雪球"""
    if stats.chance_left > 0:
        # 将snowmen_left减1
        stats.chance_left -= 1
        snowballs.empty()
        # 创建一个新的雪球
        create_snowball(ai_settings, screen, snowballs)
        # 将雪人置于屏幕中央
        for snowman in snowmen.sprites():
            snowman.center_screen()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False


def check_snowballs_bottom(ai_settings, stats, screen, snowmen, snowballs):
    """检查是否有雪球掉到了屏幕底端"""
    screen_rect = screen.get_rect()
    for snowball in snowballs.sprites():
        if snowball.rect.bottom >= screen_rect.bottom:
            # 像接到雪球一样处理
            not_catch_snowball(ai_settings, stats, screen, snowmen, snowballs)
            break


def update_balls(ai_settings, stats, screen, snowmen, snowballs):
    """更新雪球的位置"""
    # 检查是否有雪球到达屏幕底端
    check_snowballs_bottom(ai_settings, stats, screen, snowmen, snowballs)
    # 检测雪人和雪球的碰撞
    check_snowman_snowball_collisions(ai_settings, screen, snowmen, snowballs)
    snowballs.update()


def update_screen(ai_settings, screen, snowmen, snowballs):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    snowmen.draw(screen)
    snowballs.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def create_snowball(ai_settings, screen, snowballs):
    """创建雪球"""
    snowball = SnowBall(ai_settings, screen)
    snowballs.add(snowball)


def create_snowman(ai_settings, screen, snowmen):
    """创建雪人"""
    snowman = SnowMan(ai_settings, screen)
    snowmen.add(snowman)


def update_snowmen(snowmen):
    """更新雪人的位置"""
    for snowman in snowmen.sprites():
        snowman.update()