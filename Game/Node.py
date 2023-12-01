import pygame as pygame
from pygame import Vector2

from Game.GameObject import GameObject
from utils.utils import utils


class Node(GameObject):
    def __init__(self, pos, id):
        super().__init__(pos, None)
        self.radius = 10
        self.neighbours = []
        self.id = id
        self.parent = None

    def getCenter(self):
        return Vector2(self.pos.x + self.radius/2,self.pos.y + self.radius/2)

    def addNeighbour(self,nb):
        for node in self.neighbours:
            if node == nb:
                return
        self.neighbours.append(nb)
        nb.addNeighbour(self)

    def getRect(self):
        return pygame.rect.Rect(self.pos.x,self.pos.y,self.radius*2,self.radius*2)

    def draw(self):
        pygame.draw.circle(utils.screen,(93,93,23),(self.pos.x,self.pos.y),self.radius)
        utils.drawText(Vector2(self.pos.x - 4,self.pos.y  - 8),
                       str(self.id),(233,233,233),utils.font12)