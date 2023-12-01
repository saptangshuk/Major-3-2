import pygame.rect
from pygame.math import Vector2

from utils.utils import utils


class GameObject:

    def __init__(self, pos, img, type = ""):
        self.pos = pos
        self.img = img
        self.vel = Vector2(0, 0)
        self.destroyFlag = False
        self.type = type

    def update(self):
        pass

    def draw(self):
        if self.vel.x < 0:
            self.img = pygame.transform.flip(self.img, True, False)
        utils.screen.blit(self.img, (self.pos.x, self.pos.y))

    def getRect(self):
        rect = pygame.rect.Rect(self.pos.x, self.pos.y, self.img.get_width(), self.img.get_height())
        return rect

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def getCenter(self):
        return Vector2(self.pos.x + self.getRect().w / 2, self.pos.y + self.getRect().h / 2)
