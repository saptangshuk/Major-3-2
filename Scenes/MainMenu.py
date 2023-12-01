import pygame
from pygame import Vector2

from Game.Graph import Graph
from Scenes.Game import Game
from Scenes.Scene import Scene
from utils.Button import Button
from utils.Textfield import TextField
from utils.utils import utils


class MainMenu(Scene):
    def __init__(self):
        self.buttons = []

        self.buttons.append(Button(0, Vector2(20, 600),"Start",Vector2(1,0.8)))
        self.buttons.append(Button(3, Vector2(20, 650), "Quit", Vector2(1, 0.8)))
        self.buttons.append(Button(4, Vector2(0, 300), "New Graph", Vector2(2, 1.3)))

        self.maxNode = 10
        self.nodeDst = 200
        self.minDst = 400
        self.maxDst = 600

        self.maxNodeText = TextField(pygame.rect.Rect(20,20,70,20),self.maxNode)
        self.nodeDst = TextField(pygame.rect.Rect(20, 80, 70, 20), self.nodeDst)
        self.minDstText = TextField(pygame.rect.Rect(20, 160, 70, 20), self.minDst)
        self.maxDstText = TextField(pygame.rect.Rect(20, 220, 70, 20), self.maxDst)

        self.textfields = [
            self.maxNodeText,
            self.minDstText,
            self.maxDstText,
            self.nodeDst
        ]

        self.graph = Graph()
        self.selectNode = None

    def update(self):
        try:
            if int(self.nodeDst.text) >= 200 :
                self.nodeDst.text = "200"
        except:
            pass

        mousex, mousey = pygame.mouse.get_pos()
        if self.selectNode is not None:
            self.selectNode.pos = Vector2(mousex - self.selectNode.radius,mousey - self.selectNode.radius)

    def draw(self):
        self.graph.draw()
        self.maxNodeText.draw()
        utils.drawText(Vector2(20, self.maxNodeText.rect.y - 20), "max nodes", (233, 233, 233), font=utils.font12)

        self.nodeDst.draw()
        utils.drawText(Vector2(20, self.nodeDst.rect.y - 20), "node distance", (233, 233, 233), font=utils.font12)


        self.minDstText.draw()
        utils.drawText(Vector2(20, self.minDstText.rect.y - 20), "cmin distance", (233, 233, 233), font=utils.font12)

        self.maxDstText.draw()
        utils.drawText(Vector2(20, self.maxDstText.rect.y - 20), "cmax distance", (233, 233, 233), font=utils.font12)


        for button in self.buttons:
            button.draw()

    def onKeyDown(self, key):
        for text in self.textfields:
            if text.focus:
                text.onKeyDown(key)

    def onMouseDown(self, clickPos):
        for text in self.textfields:
            text.focus = False
            if text.rect.x < clickPos.x < text.rect.x + text.rect.w \
                and text.rect.y < clickPos.y < text.rect.y + text.rect.h:
                    text.focus = True

        for button in self.buttons:
            button.onMouseDown(clickPos)
            if button.clicked:
                if button.id == 0:
                    utils.currentScreen = Game(self.graph)
                    break
                if button.id == 3:
                    exit(1)
                    break
                if button.id == 4:
                    self.graph = Graph(int(self.maxNodeText.text),int(self.nodeDst.text),int(self.minDstText.text),int(self.maxDstText.text))

        # select nodes
        if self.selectNode is None:
            for node in self.graph.nodes:
                if utils.distance(node.getCenter().x,node.getCenter().y,clickPos.x,clickPos.y) < 20:
                    self.selectNode = node

    def onMouseUp(self, clickPos):
        for button in self.buttons:
            button.onMouseUp()

        if self.selectNode is not None:
            self.selectNode = None


