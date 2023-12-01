import pygame
from pygame import Vector2

from Game.GameObject import GameObject
from utils.SpriteSheet import SpriteSheet
from utils.utils import utils


class Cat(GameObject):
    def __init__(self,node):
        super().__init__(Vector2(0,0),None)

        self.node = node
        self.mouseNode = None

        self.runSheet = SpriteSheet(pygame.image.load("assets/cat.png"), 1, 6)

        self.runSheet.setPlay(0, 5, 0.1, loop=True)
        self.sheet = self.runSheet
        self.img = self.sheet.getCurrentFrame()

        self.pos = Vector2(self.node.pos.x - self.getRect().w/2,self.node.pos.y - self.getRect().h/2)
        self.currentNodeIndex = 0
        self.target = Vector2(self.pos.x,self.pos.y)
        self.path = []

        self.speed = 2.15
        self.freezeTime = 0

    def chase(self,mouse,graph):
        if utils.distance(self.target.x,self.target.y,self.getCenter().x,self.getCenter().y) < 5:
            self.currentNodeIndex += 1
            if self.currentNodeIndex > len(self.path) - 1:
                self.mouseNode = mouse.node
                self.path = graph.getPath(self.node, self.mouseNode)
                self.currentNodeIndex = 0
                if self.path == []:
                    return

            self.node = self.path[self.currentNodeIndex]
            self.target = self.path[self.currentNodeIndex].getCenter()
        vDir = self.target - self.getCenter()
        if vDir.length() > 0:
            vDir = vDir.normalize()
        self.vel = vDir * self.speed
        self.pos = self.pos + self.vel

        if self.freezeTime > 0:
            self.freezeTime -= utils.deltaTime()
            self.speed = 0
        else:
            self.speed = 2.15

    def update(self):
        pass

    def draw(self):
        self.sheet.play()
        self.img = self.sheet.getCurrentFrame()
        super().draw()
