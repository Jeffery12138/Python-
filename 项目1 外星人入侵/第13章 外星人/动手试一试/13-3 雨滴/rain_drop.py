import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raining")
    # 创建雨滴编组
    drops = Group()
    # 创建雨滴阵列
    gf.create_rain(ai_settings, screen, drops)
    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_drops(drops)
        gf.update_screen(ai_settings, screen, drops)


run_game()