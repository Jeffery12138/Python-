import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("STAR FLEET")
    # 创建一个用于存储星星的编组
    stars = Group()
    # 创建外星人群
    gf.create_star_fleet(ai_settings, screen, stars)
    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, stars)


run_game()