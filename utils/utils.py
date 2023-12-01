import pygame
import math
from pygame.locals import *

from pygame import Vector2


class Utils():

    def __init__(self):
        pygame.init()

        self.width = 1280
        self.height = 720

        self.gameOver = False

        self.screen = pygame.display.set_mode((self.width, self.height), DOUBLEBUF, 16)
        self.dt = 0
        self.clock = pygame.time.Clock()

        self.currentScreen = None

        self.font8 = pygame.font.Font('assets/Unicorn.ttf', 8)
        self.font12 = pygame.font.Font('assets/Unicorn.ttf', 12)
        self.font16 = pygame.font.Font('assets/Unicorn.ttf', 16)
        self.font24 = pygame.font.Font('assets/Unicorn.ttf', 24)
        self.font32 = pygame.font.Font('assets/Unicorn.ttf', 32)
        self.font48 = pygame.font.Font('assets/Unicorn.ttf', 48)

    def initDeltaTime(self):  # calculate deltaTime
        t = self.clock.tick(60)
        self.dt = t / 1000

    def deltaTime(self):
        return self.dt

    def drawText(self, pos, text, color, font):  # draw text
        text = font.render(text, True, color)
        self.screen.blit(text, (pos.x, pos.y))

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)

    def collide(self, a, b):  # aabb 2 box collide check
        rect = a.getRect()
        r = b.getRect()
        if r.x < rect.x + rect.w and r.x + r.w > rect.x and r.y < rect.y + rect.h and r.h + r.y > rect.y:
            return True
        return False

    def collideRect(self, rect, r):  # aabb 2 box collide check
        if r.x < rect.x + rect.w and r.x + r.w > rect.x and r.y < rect.y + rect.h and r.h + r.y > rect.y:
            return True
        return False

    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect


utils = Utils()  # util is global object
