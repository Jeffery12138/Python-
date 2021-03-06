import pygame

from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket")
    # 创建一艘火箭
    rocket = Rocket(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)


run_game()