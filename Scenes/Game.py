import random

import pygame.image
from pygame import Vector2

from Game.Cat import Cat
from Game.GameObject import GameObject
from Game.Graph import Graph
from Game.Mouse import Mouse
from Scenes.Scene import Scene
from utils.utils import utils


class Game(Scene):
    def __init__(self,graph):
        self.graph = graph
        self.cat = Cat(self.graph.nodes[random.randint(0,len(self.graph.nodes) - 1)])
        while True:
            self.mouse = Mouse(self.graph.nodes[random.randint(0, len(self.graph.nodes) - 1)])
            if self.mouse.node != self.cat.node:
                break

        self.gameOver = False
        self.score = 0
        self.second = 1
        self.spawnItemTime = 0

        self.items = []

    def update(self):
        # check game over
        if utils.distance(self.cat.getCenter().x,self.cat.getCenter().y,self.mouse.getCenter().x,self.mouse.getCenter().y) < 5:
            self.gameOver = True
        if self.gameOver:
            return

        # cat mouse logic
        self.cat.chase(self.mouse,self.graph)
        self.mouse.update()

        # add score
        self.second -= utils.deltaTime()
        if self.second < 0:
            self.second = 1
            self.score += 5

        # spawn item every 20 seconds
        self.spawnItemTime += utils.deltaTime()
        if self.spawnItemTime >= 20:
            self.spawnItemTime = 0
            self.spawnItem()

        # check item collisions with mouse
        for item in self.items:
            if utils.collide(item,self.mouse):
                if item.type == "boost":
                    self.mouse.speedUpTime = 5
                if item.type == "freeze":
                    self.cat.freezeTime = 5
                item.destroyFlag = True
        # remove items
        for item in self.items:
            if item.destroyFlag:
                self.items.remove(item)

    def onMouseDown(self,clickedPos):
        # new game
        if clickedPos.x > utils.width - 70 and clickedPos.y > utils.height - 55:
            from Scenes.MainMenu import MainMenu
            utils.currentScreen = MainMenu()
            return

        if utils.distance(self.mouse.node.getCenter().x,self.mouse.node.getCenter().y,self.mouse.getCenter().x,self.mouse.getCenter().y) > 20:
            return

        for node in self.graph.nodes:
            if node == self.mouse.node:
                continue
            if utils.distance(clickedPos.x,clickedPos.y,node.getCenter().x,node.getCenter().y) < 50:
                if node in self.mouse.node.neighbours:
                    self.mouse.moveTo(node)

    def spawnItem(self):
        if random.randint(0,1) == 0:
            item = GameObject(self.getItemRandomPos(), pygame.image.load("assets/boost.png"), type="boost")
            self.items.append(item)
        else:
            item = GameObject(self.getItemRandomPos(), pygame.image.load("assets/freeze.png"), type="freeze")
            self.items.append(item)

    def getItemRandomPos(self):
        node = self.graph.nodes[random.randint(0, len(self.graph.nodes)-1 )]
        nb = node.neighbours[random.randint(0, len(node.neighbours)-1 )]

        return Vector2((node.pos.x + nb.pos.x)/2,(node.pos.y + nb.pos.y)/2)

    def draw(self):
        self.graph.draw()
        self.mouse.draw()
        self.cat.draw()

        for item in self.items:
            item.draw()

        utils.drawText(Vector2(utils.width - 70,utils.height-55),"Menu",(233,233,23),utils.font24)
        utils.drawText(Vector2(100, utils.height-55), "Score: " + str(self.score), (233, 23, 233), utils.font16)

        if self.gameOver:
            utils.drawText(Vector2(utils.width - 500, utils.height - 55), "Game Over!", (233, 23, 23), utils.font24)