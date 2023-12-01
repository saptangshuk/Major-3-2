import pygame
from pygame import Vector2

from Game.GameObject import GameObject
from utils.SpriteSheet import SpriteSheet
from utils.utils import utils


class Mouse(GameObject):
    def __init__(self,node):
        super().__init__(Vector2(0,0),None)

        self.node = node
        self.runSheet = SpriteSheet(pygame.image.load("assets/mouse.png"), 1, 4)

        self.runSheet.setPlay(0, 3, 0.1, loop=True)
        self.sheet = self.runSheet
        self.img = self.sheet.getCurrentFrame()

        self.pos = Vector2(self.node.pos.x - self.getRect().w/2,self.node.pos.y - self.getRect().h/2)
        self.target = self.node.getCenter()

        self.speed = 2
        self.speedUpTime = 0

    def moveTo(self,node):
        self.node = node
        self.target = self.node.getCenter()

    def update(self):
        if utils.distance(self.target.x, self.target.y, self.getCenter().x, self.getCenter().y) < 5:
            return

        vDir = self.target - self.getCenter()
        if vDir.length() > 0:
            vDir = vDir.normalize()
        self.vel = vDir * self.speed
        self.pos = self.pos + self.vel

        # speedup
        if self.speedUpTime > 0:
            self.speedUpTime -= utils.deltaTime()
            self.speed = 4
        else:
            self.speed = 2

    def draw(self):
        self.sheet.play()
        self.img = self.sheet.getCurrentFrame()
        super().draw()
