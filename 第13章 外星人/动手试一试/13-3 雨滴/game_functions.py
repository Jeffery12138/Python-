import pygame
import sys


def check_keydown_events(event):
    """检查按键事件"""
    if event.key == pygame.K_q:
        sys.exit()


def check_events():
    """检查鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.K_DOWN:
            check_keydown_events(event)