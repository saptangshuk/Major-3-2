import pygame

from utils.sounds import mSounds
from utils.utils import utils


class Button:
    def __init__(self,id, pos,text, scale,font = utils.font32):
        self.id = id
        self.text = text

        self.img = pygame.image.load("assets/btn.png")
        self.clickImg = pygame.image.load("assets/clickBtn.png")
        self.drawImg = self.img
        self.pos = pos

        width = self.img.get_width()
        height = self.img.get_height()

        self.img = pygame.transform.scale(self.img, (int(width * scale.x), int(height * scale.y)))
        self.clickImg = pygame.transform.scale(self.clickImg, (int(width * scale.x), int(height * scale.y)))

        self.drawImg = self.img
        self.rect = self.drawImg.get_rect()
        self.rect.topleft = (pos.x,pos.y)
        self.clicked = False

    def onMouseDown(self,clickPos):
        if self.rect.collidepoint(clickPos):
            self.clicked = True
            self.drawImg = self.clickImg
            mSounds.play("click")

    def onMouseUp(self):
        self.clicked = False
        self.drawImg = self.img

    def draw(self):
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        # if self.rect.collidepoint(pos):
        #     if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        #         self.clicked = True
        #         self.drawImg = self.clickImg
        #         action = True
        #         mSounds.play("click")

        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False
        #     self.drawImg = self.img

        # draw button on screen
        utils.screen.blit(self.drawImg, self.rect)

        if self.text != "":
            textT = utils.font16.render(self.text, True, (10,77,104))
            text_rect = textT.get_rect(center=(self.pos.x + self.drawImg.get_width() / 2, self.pos.y + self.drawImg.get_height() / 2))
            if self.clicked:
                text_rect.y += 4
            utils.screen.blit(textT, text_rect)

        return
