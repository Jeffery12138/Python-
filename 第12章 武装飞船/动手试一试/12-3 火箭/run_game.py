import pygame

from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个游戏对象
    pygame.init()
    # 实例化Settings类，
    ai_settings = Settings()
    # 使用settings属性设置屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket")
    # 实例化Rocket类
    rocket = Rocket(ai_settings, screen)
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)


run_game()