import pygame

from settings import Settings
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个游戏对象
    pygame.init()
    # 实例化Settings类，
    ai_settings = Settings()
    # 使用settings属性设置屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("KEYDOWN")
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen)


run_game()