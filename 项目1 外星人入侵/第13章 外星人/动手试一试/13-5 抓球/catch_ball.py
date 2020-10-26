import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf


def run_game():
    """游戏初始化"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Catch Ball')
    # 创建雪人和雪球组
    snowmen = Group()
    snowballs = Group()
    gf.create_snowball(ai_settings, screen, snowballs)
    gf.create_snowman(ai_settings, screen, snowmen)

    # 游戏主循环
    while True:
        gf.check_events(snowmen)
        gf.update_snowmans(snowmen)
        gf.update_balls(ai_settings, screen, snowmen, snowballs)
        gf.update_screen(ai_settings, screen, snowmen, snowballs)


run_game()