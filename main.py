import pygame
from pygame import Vector2

from Scenes.Game import Game
from Scenes.MainMenu import MainMenu
from utils.utils import utils

utils.currentScreen = MainMenu()

while True:
    utils.screen.fill((23, 23, 23), (0, 0, utils.width, utils.height))
    utils.initDeltaTime()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            utils.currentScreen.onMouseDown(Vector2(mousex,mousey))
        if event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = pygame.mouse.get_pos()
            utils.currentScreen.onMouseUp(Vector2(mousex,mousey))
        if event.type == pygame.KEYDOWN:
            utils.currentScreen.onKeyDown(event.key)

    utils.currentScreen.update()
    utils.currentScreen.draw()

    pygame.display.flip()
