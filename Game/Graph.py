import random

import pygame.draw
from pygame import Vector2

from Game.Node import Node
from utils.utils import utils


class Graph:
    def __init__(self,count = 10, nodeDst = 200,  nearDst = 400, farDst = 600):
        self.nodes = []
        self.count = count
        self.nodeDst = nodeDst

        for i in range(0,count):
            self.nodes.append(self.spawnNode(i))

        for node in self.nodes:
            for otherNode in self.nodes:
                if node == otherNode:
                    continue
                if utils.distance(otherNode.pos.x,otherNode.pos.y,node.pos.x,node.pos.y) < nearDst:
                    node.addNeighbour(otherNode)
            if len(node.neighbours) <= 1:
                for otherNode in self.nodes:
                    if node == otherNode:
                        continue
                    if utils.distance(otherNode.pos.x, otherNode.pos.y, node.pos.x, node.pos.y) < farDst:
                        node.addNeighbour(otherNode)

        for node in self.nodes:
            print(node.id,end=": ")
            for nb in node.neighbours:
                print(nb.id,end=", ")
            print()

    def spawnNode(self,id):
        while True:
            newNode = Node(Vector2(random.randint(100, utils.width - 100), random.randint(50, utils.height - 50)),id)
            dstCheck = True
            for node in self.nodes:
                if utils.distance(newNode.pos.x,newNode.pos.y,node.pos.x,node.pos.y) < self.nodeDst:
                    dstCheck = False
                    newNode = Node(Vector2(random.randint(100, utils.width - 100), random.randint(50, utils.height - 50)),id)
                    break
            if dstCheck:
                return newNode

    def getPath(self,start,end):
        if start == end:
            return []

        for node in self.nodes:
            node.parent = None

        self.BFS(start,end)
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = node.parent

        path.reverse()
        return path


    def BFS(self, startNode, destNode):
        visited = [False] * len(self.nodes)
        queue = [startNode]
        visited[startNode.id] = True

        while queue:
            node = queue.pop(0)
            #print(node.id, end=" ")
            for nb in node.neighbours:
                if not visited[nb.id]:
                    queue.append(nb)
                    visited[nb.id] = True
                    nb.parent = node
                    if nb == destNode:
                        return

    def draw(self):
        for node in self.nodes:
            node.draw()
            for nb in node.neighbours:
                pygame.draw.line(utils.screen,(123,123,123),(node.pos.x,node.pos.y),(nb.pos.x,nb.pos.y))

