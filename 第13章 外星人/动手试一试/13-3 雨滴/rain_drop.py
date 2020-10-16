import pygame

import game_functions as gf
from settings import Settings
from drop import Drop


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raining")
    drop = Drop(ai_settings, screen)
    while True:
        gf.check_events()
        screen.fill(ai_settings.bg_color)
        drop.update()
        drop.blitme()
        pygame.display.flip()


run_game()