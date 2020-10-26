import sys
import pygame
from time import sleep

from bullet import Bullet
from target import Target


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, play_button, ship, targets, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, targets, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(ai_settings, screen, stats, play_button, ship, targets, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        # 清空外星人列表和子弹列表
        targets.empty()
        bullets.empty()
        reset_target_direction(ai_settings)
        # 创建一个新的目标，并让飞船居中
        create_target(ai_settings, screen, targets)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, ship, targets, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for target in targets.sprites():
        target.draw_target()
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, targets, bullets):
    """更新子弹的位置，并删除以消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.left > ai_settings.screen_width:
            bullets.remove(bullet)
    check_bullet_target_collisions(ai_settings, screen, targets, bullets)


def check_bullet_target_collisions(ai_settings, screen, targets, bullets):
    """响应子弹和目标的碰撞"""
    # 删除发生碰撞的子弹和目标
    collisions = pygame.sprite.groupcollide(bullets, targets, True, True)
    if len(targets) == 0:
        # 删除现有的所有子弹，并创建一个新的目标
        bullets.empty()
        # 重置target_direction
        reset_target_direction(ai_settings)
        create_target(ai_settings, screen, targets)


def change_target_direction(ai_settings):
    """改变目标方向"""
    ai_settings.target_direction *= -1


def reset_target_direction(ai_settings):
    """重置目标方向"""
    ai_settings.target_direction = 1


def check_target_edges(ai_settings, targets):
    """有目标到达边缘时采取相应措施"""
    for target in targets.sprites():
        if target.check_edges():
            change_target_direction(ai_settings)
            break


def create_target(ai_settings, screen, targets):
    """创建一个目标"""
    target = Target(ai_settings, screen)
    targets.add(target)


def miss_target(ai_settings, screen, stats, ship, targets, bullets):
    """相应错失目标事件"""
    if stats.chance_left > 0:
        # 将stats.chance_left减1
        stats.chance_left -= 1
        # 清空目标列表和子弹列表
        targets.empty()
        bullets.empty()
        # 创建一个新的目标，并把飞船放置在屏幕中央
        create_target(ai_settings, screen, targets)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_targets_top(ai_settings, screen, stats, ship, targets, bullets):
    """检查是否有外星人到达屏幕顶端"""
    for target in targets.sprites():
        if target.rect.top <= 0:
            target.reset_target_direction()
            miss_target(ai_settings, screen, stats, ship, targets, bullets)
            break


def update_targets(ai_settings, screen, stats, ship, targets, bullets):
    """检查是否有目标到达屏幕边缘，并更新目标位置"""
    check_target_edges(ai_settings, targets)
    targets.update()
    # 检查是否有外星人到达了顶端
    check_targets_top(ai_settings, screen, stats, ship, targets, bullets)